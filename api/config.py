import yaml

from labelprinterkit.backends.main import Backend
from labelprinterkit.constants import Media
from labelprinterkit.printers.main import Printer
from labelprinterkit.utils.font import get_fonts

CONFIG_FILE = "config.yaml"


def _read_config() -> dict:
    """Read the YAML Config File and Return the Contents as a Dictionary"""
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)


class Config:
    def __init__(self):
        self._config: dict = _read_config()

    @property
    def backend(self) -> Backend | None:
        """Check the Config for a Supplied Default Backend"""
        try:
            return Backend.get(self._config.get("backend", ""))
        except ValueError:
            return None

    @property
    def printer(self) -> Printer | None:
        """Check the Config for a Supplied Default Printer"""
        try:
            return Printer.get(self._config.get("printer", ""))
        except ValueError:
            return None

    @property
    def media(self) -> Media | None:
        """Check the Config for a Supplied Default Media"""
        try:
            return Media.get(self._config.get("media", ""))
        except ValueError:
            return None

    @property
    def font(self) -> str | None:
        """Check the Config for a Supplied Default Font, else use the First Available TrueType Font in Linux"""
        if "font" in self._config:
            return self._config["font"]
        try:
            return list(get_fonts().values())[0][0].as_posix()
        except IndexError:
            return None
