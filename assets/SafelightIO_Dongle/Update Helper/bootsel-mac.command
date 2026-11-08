#!/bin/bash
#
# Put the SafelightIO Dongle into BOOTSEL mode from macOS.
#
# The meter uses the standard USB serial 1200-baud
# touch. Opening the CDC port at 1200 baud makes the firmware call
# reset_usb_boot(); the ROM then exposes the BOOTSEL drive.
#
# Usage:
#   ./bootsel-mac.command            # find the meter automatically
#   ./bootsel-mac.command /dev/cu.usbmodem1234
#
# No SDK, picotool or BOOTSEL button is required.

set -euo pipefail

VID_DECIMAL=$((0x2E8A))   # 11914; shell arithmetic avoids a decimal typo
PRODUCTS="9 10"             # 0x0009 = meter CDC, 0x000A = compatible CDC
BOOTSEL_VOLUMES=(/Volumes/RP2350 /Volumes/RPI-RP2)
RP_VOLUME=""

say()  { printf '%s\n' "$*"; }
fail() { printf 'Error: %s\n' "$*" >&2; pause_if_terminal; exit 1; }

pause_if_terminal() {
    # Keep a double-clicked Terminal window readable. A command-line run is
    # not paused.
    if [[ -t 0 ]]; then
        printf '\nPress Return to close...'
        read -r _ || true
    fi
}

find_bootsel_volume() {
    local candidate
    for candidate in "${BOOTSEL_VOLUMES[@]}"; do
        if [[ -d "$candidate" ]]; then
            RP_VOLUME="$candidate"
            return 0
        fi
    done
    RP_VOLUME=""
    return 1
}

already_bootsel() {
    if find_bootsel_volume; then
        say "Already in BOOTSEL mode; the BOOTSEL drive is mounted at $RP_VOLUME."
        say "Copy the .uf2 file to that drive; no reset was sent."
        return 0
    fi
    return 1
}

# Find a callout device under the meter USB device. The USB tree places
# the IOSerialBSDClient (with IOCalloutDevice) below the IOUSBHostDevice that
# carries idVendor/idProduct. This awk pass follows that subtree.
find_port_from_ioreg() {
    command -v ioreg >/dev/null 2>&1 || return 1
    ioreg -p IOUSB -l -w 0 2>/dev/null | awk -v vid="$VID_DECIMAL" -v products="$PRODUCTS" '
        function wanted_product(value) {
            n = split(products, p, " ")
            for (i = 1; i <= n; i++) if (value == p[i]) return 1
            return 0
        }
        /<class IOUSBHostDevice/ {
            # A new USB device starts. If the previous one had no callout,
            # drop its state rather than borrowing its child.
            if (in_rp && !found_callout) { in_rp = 0; product_ok = 0 }
            found_callout = 0
        }
        /"idVendor"[[:space:]]*=[[:space:]]*[0-9]+/ {
            line = $0
            sub(/.*"idVendor"[[:space:]]*=[[:space:]]*/, "", line)
            sub(/[^0-9].*/, "", line)
            if (line == vid) { in_rp = 1; product_ok = 0; found_callout = 0 }
            next
        }
        in_rp && /"idProduct"[[:space:]]*=[[:space:]]*[0-9]+/ {
            line = $0
            sub(/.*"idProduct"[[:space:]]*=[[:space:]]*/, "", line)
            sub(/[^0-9].*/, "", line)
            if (wanted_product(line)) product_ok = 1
            next
        }
        in_rp && product_ok && /"IOCalloutDevice"[[:space:]]*=/ {
            line = $0
            sub(/.*"IOCalloutDevice"[[:space:]]*=[[:space:]]*"/, "", line)
            sub(/".*/, "", line)
            if (line ~ /^\/dev\/cu\./) { print line; found_callout = 1; exit }
        }
    '
}

find_port() {
    local override="${1:-}"
    if [[ -n "$override" ]]; then
        [[ -c "$override" ]] || fail "not a character device: $override"
        printf '%s\n' "$override"
        return 0
    fi

    local port
    if port="$(find_port_from_ioreg)" && [[ -n "$port" ]]; then
        printf '%s\n' "$port"
        return 0
    fi

    # Fallback for macOS versions where the IOUSB tree layout differs. Only
    # accept a single usbmodem candidate; never guess between several.
    local -a candidates=()
    shopt -s nullglob
    for port in /dev/cu.usbmodem*; do
        [[ "$port" == *debug-console* ]] && continue
        candidates+=("$port")
    done
    shopt -u nullglob

    if (( ${#candidates[@]} == 1 )); then
        printf '%s\n' "${candidates[0]}"
        return 0
    fi

    if (( ${#candidates[@]} > 1 )); then
        say "Several USB modem ports were found; choose the SafelightIO Dongle one:" >&2
        printf '  %s\n' "${candidates[@]}" >&2
        fail "pass the port explicitly, e.g. $0 ${candidates[0]}"
    fi
    return 1
}

main() {
    if already_bootsel; then
        pause_if_terminal
        return 0
    fi

    # An explicit port is the escape hatch for a custom VID/PID; do not apply
    # the USB vendor-ID precheck to it.
    if [[ -z "${1:-}" ]]; then
        if ! ioreg -p IOUSB -l -w 0 2>/dev/null | grep -q "\"idVendor\" = $VID_DECIMAL"; then
            say "No SafelightIO Dongle USB device (VID 0x2E8A) is attached." >&2
            say "Check the data cable and that the SafelightIO Dongle is in its normal firmware." >&2
            say "If it is already in BOOTSEL, the BOOTSEL drive should be mounted." >&2
            pause_if_terminal
            return 1
        fi
    fi

    local port
    if ! port="$(find_port "${1:-}")"; then
        say "No SafelightIO Dongle CDC serial port was found." >&2
        say "If the meter is already in BOOTSEL, copy the .uf2 to the BOOTSEL drive." >&2
        pause_if_terminal
        return 1
    fi

    say "SafelightIO Dongle serial port: $port"
    say "Opening it at 1200 baud to request BOOTSEL mode..."

    # stty opens the cu.* device and sets the line coding. The meter sees
    # the 1200 baud SET_LINE_CODING request and resets into the ROM bootloader.
    if ! stty -f "$port" 1200 cs8 -cstopb -parenb; then
        fail "could not open $port at 1200 baud. Close the meter app and any serial terminal, then retry."
    fi

    say "Waiting for the BOOTSEL drive..."
    for _ in $(seq 1 40); do
        if find_bootsel_volume; then
            say "Done: the SafelightIO Dongle is in BOOTSEL mode."
            say "The BOOTSEL drive is mounted at $RP_VOLUME."
            say "Copy the .uf2 to it, then wait for it to disappear."
            pause_if_terminal
            return 0
        fi
        sleep 0.5
    done

    say "The port opened, but $RP_VOLUME did not appear within 20 seconds." >&2
    say "The 1200-baud touch only works while the firmware is running." >&2
    pause_if_terminal
    return 3
}

main "$@"
