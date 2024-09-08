from dataclasses import dataclass

import yaml
from labelprinterkit.backends.main import Backend
from labelprinterkit.constants import Media
from labelprinterkit.printers.main import Printer
from labelprinterkit.utils.font import get_fonts

CONFIG_FILE = "config.yaml"


def read_config() -> dict:
    """Read the YAML Config File and Return the Contents as a Dictionary"""
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)


def write_config(config: dict):
    """Write the Dictionary to the YAML Config File"""
    with open(CONFIG_FILE, "w") as file:
        yaml.safe_dump(config, file)


@dataclass
class Config:
    """
    Handles the Configuration of the PrintServer - from the YAML Config File
    """
    backend: Backend | None
    printer: Printer | None
    vendor_id: int | None
    product_id: int | None
    media: Media | None
    font: str | None
    motor_initial: int
    motor_pressed: int

    def to_dict(self) -> dict:
        """Convert the Config Object to a Dictionary"""
        return {
            "backend": self.backend.value if self.backend else None,
            "printer": self.printer.value if self.printer else None,
            "vendor_id": self.vendor_id,
            "product_id": self.product_id,
            "media": self.media.value if self.media else None,
            "font": self.font,
            "motor_initial": self.motor_initial,
            "motor_pressed": self.motor_pressed,
        }

    @staticmethod
    def _from_dict(config: dict) -> "Config":
        """Create a Config Object from a Dictionary"""
        return Config(
            backend=Backend.get(config.get("backend", "")),
            printer=Printer.get(config.get("printer", "")),
            vendor_id=config.get("vendor_id"),
            product_id=config.get("product_id"),
            media=Media.get(config.get("media", "")),
            font=config.get("font") or Config._get_default_font(),
            motor_initial=config.get("motor_initial", 50),
            motor_pressed=config.get("motor_pressed", 25),
        )

    @staticmethod
    def get() -> "Config":
        """Get the Config from the Config File"""
        return Config._from_dict(read_config())

    @staticmethod
    def _get_default_font() -> str | None:
        """Get the First Available TrueType Font in Linux as Default"""
        try:
            return list(get_fonts().values())[0][0].as_posix()
        except IndexError:
            return None
