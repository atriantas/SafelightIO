<#
.SYNOPSIS
Put the SafelightIO Dongle into BOOTSEL mode.

.DESCRIPTION
Finds the meter's USB CDC port by USB VID/PID, opens it at 1200 baud,
and waits for the BOOTSEL mass-storage drive. The meter firmware handles the
1200-baud touch by resetting into the ROM bootloader. No SDK, picotool or
BOOTSEL button is needed.

.PARAMETER Port
Optional COM port override, for example -Port COM7.

.EXAMPLE
.\bootsel-windows.ps1

.EXAMPLE
.\bootsel-windows.ps1 -Port COM7
#>
[CmdletBinding()]
param(
    [string]$Port
)

$ErrorActionPreference = 'Stop'
$Vid = '2E8A'
$Pids = @('0009', '000A')   # meter CDC, compatible CDC
$VolumeNames = @('RP2350', 'RPI-RP2')

function Write-Step([string]$Text) {
    Write-Host $Text
}

function Get-BootselDrive {
    Get-CimInstance Win32_LogicalDisk -ErrorAction SilentlyContinue |
        Where-Object { $VolumeNames -contains $_.VolumeName } |
        Select-Object -First 1
}

function Get-RpSerialPorts {
    $pattern = "VID_$Vid&PID_($($Pids -join '|'))"
    $ports = @()
    try {
        $entities = Get-CimInstance Win32_PnPEntity -ErrorAction SilentlyContinue |
            Where-Object { $_.PNPDeviceID -match $pattern }
    } catch {
        $entities = @()
    }
    foreach ($entity in $entities) {
        if ($entity.Name -match '\((COM\d+)\)') {
            $com = $Matches[1].ToUpperInvariant()
            if ($ports -notcontains $com) { $ports += $com }
        }
    }
    return $ports
}

function Get-AllComPorts {
    try { return @([System.IO.Ports.SerialPort]::GetPortNames() | Sort-Object -Unique) }
    catch { return @() }
}

function Select-Port([string[]]$Ports) {
    if ($Ports.Count -eq 1) { return $Ports[0] }
    if (-not [Environment]::UserInteractive) {
        throw "More than one SafelightIO Dongle serial port was found: $($Ports -join ', '). Use -Port."
    }
    Write-Step 'Several SafelightIO Dongle serial ports were found:'
    for ($i = 0; $i -lt $Ports.Count; $i++) {
        Write-Step ("  [{0}] {1}" -f ($i + 1), $Ports[$i])
    }
    while ($true) {
        $answer = Read-Host 'Choose the port number'
        $index = 0
        if ([int]::TryParse($answer, [ref]$index) -and $index -ge 1 -and $index -le $Ports.Count) {
            return $Ports[$index - 1]
        }
        Write-Step 'Enter one of the numbers shown.'
    }
}

# Already in BOOTSEL: do not reset again; just tell the user where to copy.
$drive = Get-BootselDrive
if ($drive) {
    Write-Step "Already in BOOTSEL mode at $($drive.DeviceID)."
    Write-Step 'Copy the .uf2 file to that drive; no reset was sent.'
    exit 0
}

if ($Port -and $Port -notmatch '^COM\d+$') {
    throw "Invalid port '$Port'. Use a name such as COM7."
}

if (-not $Port) {
    $rpPorts = @(Get-RpSerialPorts)
    if ($rpPorts.Count -eq 0) {
        $all = @(Get-AllComPorts)
        Write-Step "No SafelightIO Dongle USB CDC port (VID 0x$Vid, PID 0x0009/0x000A) was found."
        if ($all.Count -gt 0) {
            Write-Step "Visible COM ports: $($all -join ', ')."
        }
        Write-Step 'Check the data cable and that the SafelightIO Dongle is running its normal firmware.'
        Write-Step "If it is already in BOOTSEL, the BOOTSEL drive should be visible."
        exit 1
    }
    $Port = Select-Port $rpPorts
}

Write-Step "SafelightIO Dongle serial port: $Port"
Write-Step 'Opening it at 1200 baud to request BOOTSEL mode...'

$serial = $null
try {
    $serial = New-Object System.IO.Ports.SerialPort
    $serial.PortName = $Port
    $serial.BaudRate = 1200
    $serial.Parity = [System.IO.Ports.Parity]::None
    $serial.DataBits = 8
    $serial.StopBits = [System.IO.Ports.StopBits]::One
    $serial.Handshake = [System.IO.Ports.Handshake]::None
    $serial.Open()
    # DTR/RTS are applied after Open so a driver that rejects pre-open line
    # settings cannot stop the 1200-baud request.
    try { $serial.DtrEnable = $true; $serial.RtsEnable = $true } catch { }
    Start-Sleep -Milliseconds 700
}
catch {
    throw "Could not open $Port at 1200 baud. Close the meter app and any serial terminal, then retry. $($_.Exception.Message)"
}
finally {
    if ($serial) {
        try { if ($serial.IsOpen) { $serial.Close() } } catch { }
        $serial.Dispose()
    }
}

Write-Step "Waiting for the BOOTSEL drive..."
$deadline = (Get-Date).AddSeconds(20)
while ((Get-Date) -lt $deadline) {
    $drive = Get-BootselDrive
    if ($drive) {
        Write-Step "Done: the SafelightIO Dongle is in BOOTSEL mode at $($drive.DeviceID)."
        Write-Step 'Copy the .uf2 to that drive, then wait for it to disappear.'
        exit 0
    }
    Start-Sleep -Milliseconds 500
}

Write-Step "The port opened, but the BOOTSEL drive did not appear within 20 seconds."
Write-Step 'The 1200-baud touch only works while the firmware is running.'
exit 3
