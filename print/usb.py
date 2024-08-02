import usb.core


def detach_device_from_kernel(vendor_id: int, product_id: int) -> None:
    """
    Detach the given Device from the Kernel - allowing PyUSB Exclusive Access
    :param vendor_id: Hex Vendor ID
    :param product_id: Hex Product ID
    """
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    device.reset()

    interface = device[0].interfaces()[0].bInterfaceNumber
    if device.is_kernel_driver_active(interface):
        try:
            device.detach_kernel_driver(interface)
        except usb.core.USBError:
            pass

    device.set_configuration()
