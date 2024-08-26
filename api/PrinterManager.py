from labelprinterkit.backends.usb import PyUSBBackend
from labelprinterkit.printers import GenericPrinter
from labelprinterkit.printers.main import Printer


class PrinterManager:
    _instance = None

    def __init__(self, printer_type: Printer) -> None:
        self.printer_type = printer_type

    def __new__(cls, printer_type: Printer) -> "PrinterManager":
        if cls._instance is None:
            cls._instance = super(PrinterManager, cls).__new__(cls)
            cls._instance.__init__(printer_type)
            cls._instance._initialize_printer()
        return cls._instance

    def _initialize_printer(self) -> None:
        self.backend = PyUSBBackend()
        self.backend.detach_from_kernel()
        self._printer = self.printer_type.printer(self.backend)

    @property
    def printer(self) -> GenericPrinter:
        return self._printer
