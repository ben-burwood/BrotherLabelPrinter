import time
from dataclasses import dataclass

from brother_label_printer_control.backends.main import Backend
from brother_label_printer_control.backends.usb import PyUSBBackend
from brother_label_printer_control.printers import GenericPrinter
from brother_label_printer_control.printers.main import Printer
from fastapi import Depends
from servo_motor_control.motor import Motor

from .settings import Settings

@dataclass(frozen=True)
class MotorPowerButtonControl:
    initial_position: int = 50
    final_position: int = 25

    @classmethod
    def get(
            cls, initial_position: int | None, final_position: int | None
    ) -> "MotorPowerButtonControl" | None:
        if initial_position is None or final_position is None:
            return None
        return cls(initial_position, final_position)

class PrinterManager:
    _instance = None

    def __init__(
            self,
            backend_type: Backend,
            printer_type: Printer,
            motor_control: MotorPowerButtonControl | None = None,
            vendor_id: int | None = None,
            product_id: int | None = None,
    ) -> None:
        self._backend_type = backend_type
        self._printer_type = printer_type

        self._motor_control = motor_control

        self._vendor_id = vendor_id
        self._product_id = product_id

    def __new__(
            cls,
            backend_type: Backend,
            printer_type: Printer,
            motor_control: MotorPowerButtonControl | None = None,
            vendor_id: int | None = None,
            product_id: int | None = None,
    ) -> "PrinterManager":
        if cls._instance is None:
            cls._instance = super(PrinterManager, cls).__new__(cls)
            cls._instance.__init__(
                backend_type, printer_type, motor_control, vendor_id, product_id
            )
            cls._instance._initialize_printer()
        return cls._instance

    def _initialize_printer(self) -> None:
        if self._motor_control is not None:
            PrinterManager.toggle_power_button(self._motor_control)
            time.sleep(5)

        backend = self._backend_type.backend(self._vendor_id, self._product_id)
        if isinstance(backend, PyUSBBackend):
            backend.detach_from_kernel()

        self._printer = self._printer_type.printer(backend)

    @property
    def printer(self) -> GenericPrinter:
        return self._printer

    @staticmethod
    def toggle_power_button(
            motor_control: MotorPowerButtonControl,
    ) -> None:
        """Toggles the Power Button of the Printer by moving the Motor to the Pressed Position and then back to the Initial"""
        if not Motor.is_supported():
            return

        motor = Motor()
        motor.set_position_percentage(motor_control.initial_position)
        motor.enable_pwm()
        time.sleep(2)
        motor.set_position_percentage(motor_control.final_position)
        time.sleep(2)
        motor.set_position_percentage(motor_control.initial_position)
        time.sleep(2)
        motor.disable_pwm()

    @classmethod
    def get(cls, settings: Settings = Depends(Settings)) -> "PrinterManager":
        return cls(
            settings.backend,
            settings.printer,
            MotorPowerButtonControl.get(settings.motor_initial, settings.motor_final),
        )
