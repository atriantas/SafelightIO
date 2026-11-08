# Put the SafelightIO Dongle into BOOTSEL mode

> For a simple, step-by-step update guide for end users, open
> [HOW-TO-UPDATE-DONGLE.txt](HOW-TO-UPDATE-DONGLE.txt).

Two small utilities for the SafelightIO Dongle. They find the meter's USB CDC
port, open it at **1200 baud**, and wait for the BOOTSEL drive. The meter
firmware treats the 1200-baud request as a reset into the ROM USB bootloader.
No SDK, picotool or BOOTSEL button is required on the computer.

| Platform | File |
|---|---|
| macOS | `bootsel-mac.command` |
| Windows | `bootsel-windows.bat` (double-click) or `bootsel-windows.ps1` |

## macOS

Double-click `bootsel-mac.command`, or run it from Terminal:

```sh
./bootsel-mac.command
```

If macOS refuses to open it because of the download quarantine, right-click it
and choose **Open**, or run `chmod +x bootsel-mac.command` once.

You can override the port:

```sh
./bootsel-mac.command /dev/cu.usbmodem1234
```

The script only sends the reset when it can identify a SafelightIO Dongle USB device
(VID `0x2E8A`). It prefers the CDC callout device under the device's IOUSB node.
If the tree layout is different, it accepts exactly one `cu.usbmodem*` candidate
and never guesses between several.

## Windows

Double-click `bootsel-windows.bat`. It runs PowerShell with a per-process
`ExecutionPolicy Bypass`; it does not change the machine policy and does not
need Administrator rights.

From PowerShell:

```powershell
.\bootsel-windows.ps1
.\bootsel-windows.ps1 -Port COM7
```

Windows 10/11 include the USB CDC and mass-storage drivers; no driver install is
needed.

## What happens next

When the script reports that the SafelightIO Dongle is in BOOTSEL mode:

1. The BOOTSEL drive is mounted (`/Volumes/RP2350` on macOS, a drive letter on
   Windows). RP2350 hardware normally labels it `RP2350`; the scripts also accept
   the older `RPI-RP2` label.
2. Copy the new `.uf2` file to that drive.
3. Wait for the drive to disappear. Do not unplug during the copy.
4. Reconnect the SafelightIO Dongle to the phone.

The scripts do **not** flash a file themselves. They only request BOOTSEL mode.

## Safety and recovery

- Close the meter app and any serial terminal before running the script;
  only one process can own the CDC port.
- Use a data cable. A charge-only cable will not expose the serial port.
- The 1200-baud touch only works while the current firmware is running. If the
  firmware is hung or an update was interrupted, a sealed unit with no BOOTSEL
  access may need service recovery.
- Do not remove power while the BOOTSEL drive is being written.

## Detection details

The meter uses these USB IDs:

| Device | VID | PID |
|---|---|---|
| SafelightIO Dongle CDC | `0x2E8A` | `0x0009` |
| Compatible CDC | `0x2E8A` | `0x000A` |

If the firmware has custom USB descriptors, pass the port explicitly. The
1200-baud behaviour is controlled by
`PICO_STDIO_USB_ENABLE_RESET_VIA_BAUD_RATE` (default on when the application
does not use TinyUSB directly) and `PICO_STDIO_USB_RESET_MAGIC_BAUD_RATE`
(default `1200`).

## Verification status

The macOS 1200-baud reset was observed on the connected meter: it re-enumerated as
`RP2350 Boot`, and the helper then detected `/Volumes/RP2350`. The Windows script
still needs a Windows hardware run.
