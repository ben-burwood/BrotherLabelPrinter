from brother_label_printer_control.backends.main import Backend
from brother_label_printer_control.constants import Media
from brother_label_printer_control.printers.main import Printer
from brother_label_printer_control.utils.font import get_fonts
from pydantic import model_validator
from pydantic_settings import BaseSettings

from . import BrotherPrinterApiError

class Settings(BaseSettings):
    """Get the Settings from the Environment"""

    backend: Backend | None
    printer: Printer | None
    vendor_id: int | None
    product_id: int | None
    motor_initial: int | None
    motor_final: int | None
    media: Media | None
    font: str | None

    @classmethod
    @model_validator(mode="before")
    def convert_fields(cls, values):
        backend_value = values.get("backend")
        if not backend_value:
            raise BrotherPrinterApiError("Must Provide a Valid Backend")
        values["backend"] = Backend.get(backend_value)

        printer_value = values.get("printer")
        if not printer_value:
            raise BrotherPrinterApiError("Must Provide a Valid Printer")
        values["printer"] = Printer.get(printer_value)

        media_value = values.get("media")
        if media_value:
            values["media"] = Media.get(media_value)

        if not values.get("font"):
            values["font"] = cls._get_default_font()

        return values

    @staticmethod
    def _get_default_font() -> str | None:
        """Get the First Available TrueType Font in Linux as Default"""
        try:
            return list(get_fonts().values())[0][0].as_posix()
        except IndexError:
            return None
