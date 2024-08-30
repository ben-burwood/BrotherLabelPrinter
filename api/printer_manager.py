from labelprinterkit.backends.main import Backend
from labelprinterkit.backends.usb import PyUSBBackend
from labelprinterkit.printers import GenericPrinter
from labelprinterkit.printers.main import Printer

from motor.constants import MotorPosition
from motor.motor import Motor


class PrinterManager:
    _instance = None

    def __init__(self, backend_type: Backend, printer_type: Printer) -> None:
        self._backend_type = backend_type
        self._printer_type = printer_type

    def __new__(cls, backend_type: Backend, printer_type: Printer) -> "PrinterManager":
        if cls._instance is None:
            cls._instance = super(PrinterManager, cls).__new__(cls)
            cls._instance.__init__(backend_type, printer_type)
            cls._instance._initialize_printer()
        return cls._instance

    def _initialize_printer(self) -> None:
        backend = self._backend_type.backend()
        if isinstance(backend, PyUSBBackend):
            backend.detach_from_kernel()

        self._printer = self._printer_type.printer(backend)

    @property
    def printer(self) -> GenericPrinter:
        return self._printer

    @staticmethod
    def toggle_power_button() -> None:
        motor = Motor()
        motor.set_position(MotorPosition.LEFT)
        motor.enable_pwm()
        motor.set_position(MotorPosition.RIGHT)
        motor.set_position(MotorPosition.LEFT)
        motor.disable_pwm()
