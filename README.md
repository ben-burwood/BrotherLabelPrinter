# Brother Printer

CLI and GUI for Brother PTP-700 Label Printer

This Repo is a Wrapper for and uses labelprinterkit (https://github.com/ogelpre/labelprinterkit) for Interfacing the Printer.

# Print Settings

Labels MUST use the full pixel/points PrintArea for the given Media.
e.g. the 12mm has 70 pixel/points so the content (Text) MUST fill the 70 pixel/points.

## Installation

- Python
- pip
- libusb - Check Linux/Windows install Guides for this
    - On Ubuntu this is likely already installed.

Install all Dependencies from the requirements.txt file

### Device

Get VendorID : `lsusb | grep -i Brother | awk '{print $6}' | cut -d':' -f1`

Get ProductID: `lsusb | grep -i Brother | awk '{print $6}' | cut -d':' -f2`

### Permissions

If you are on Linux, you may need to add a UDEV Rule to allow the Printer to be accessed by your User.

Rule: `/etc/udev/rules.d/99-brother-ptp700.rules`

```bash
SUBSYSTEMS=="usb", GROUP="plugdev", ACTION=="add", ATTRS{idVendor}==<VENDOR_ID>, ATTRS{idProduct}==<PRODUCT_ID>, MODE="0660"
```

This sets the owner of the device node to root:usbusers rather than root:root

Ensure that the User is in the `plugdev` group : `sudo usermod -aG plugdev <USER>`
