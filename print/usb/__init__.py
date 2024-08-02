from dataclasses import dataclass

import usb.core

@dataclass
class PrinterUSBDevice:
    vendor_id: int  # Hex Vendor ID
    product_id: int  # Hex Product ID

    @property
    def device(self) -> usb.core.Device:
        return usb.core.find(idVendor=hex(self.vendor_id), idProduct=hex(self.product_id))

    def detach_from_kernel(self) -> None:
        """
        Detach the given Device from the Kernel - allowing PyUSB Exclusive Access
        Required for: usb.core.USBError: [Errno 16] Resource busy
        """
        device = self.device
        device.reset()

        interface = device[0].interfaces()[0].bInterfaceNumber
        if device.is_kernel_driver_active(interface):
            try:
                device.detach_kernel_driver(interface)
            except usb.core.USBError:
                pass

        device.set_configuration()

    @staticmethod
    def get() -> "PrinterUSBDevice":
        """Get the USBPrinterID for the Attached Brother Printer
        Assumes only a SINGLE Brother USB Device is Attached"""
        for device in usb.core.find(find_all=True):
            if device.manufacturer == "Brother":
                return PrinterUSBDevice(device.idVendor, device.idProduct)
