import usb.core


class BrotherPrinterError(Exception):
    pass


def handle_error(e: Exception) -> None:
    """Handle the Exception from labelprinterkit or PyUSB"""
    if isinstance(e, usb.core.USBError):
        match e.errno:
            case 16:
                raise BrotherPrinterError("USB Device is Busy - Detach from Kernel") from e
            case 19:
                raise BrotherPrinterError("USB Device is Disconnected - Turn the Device On") from e
    raise e
