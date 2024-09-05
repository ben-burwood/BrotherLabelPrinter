import time

from labelprinterkit.backends.main import Backend
from labelprinterkit.backends.usb import PyUSBBackend
from labelprinterkit.printers import GenericPrinter
from labelprinterkit.printers.main import Printer

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
    def toggle_power_button(initial_position: int = 50, pressed_position: int = 25) -> None:
        """Toggles the Power Button of the Printer by moving the Motor to the Pressed Position and then back to the Initial"""
        if not Motor.is_supported():
            return

        motor = Motor()
        motor.set_position_percentage(initial_position)
        motor.enable_pwm()
        time.sleep(2)
        motor.set_position_percentage(pressed_position)
        time.sleep(2)
        motor.set_position_percentage(initial_position)
        time.sleep(2)
        motor.disable_pwm()
