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

        def get_backend_from_str(backend: str) -> Backend | None:
            return next((b for b in Backend if b.name.lower() == backend.lower()), None)

        return get_backend_from_str(self._config.get("backend", ""))

    @property
    def printer(self) -> Printer | None:
        """Check the Config for a Supplied Default Printer"""

        def get_printer_from_str(printer: str) -> Printer | None:
            return next((p for p in Printer if p.name.lower() == printer.lower()), None)

        return get_printer_from_str(self._config.get("printer", ""))

    @property
    def media(self) -> Media | None:
        """Check the Config for a Supplied Default Media"""

        def get_media_from_str(media: str) -> Media | None:
            return next((m for m in Media if m.name.lower() == media.lower()), None)

        return get_media_from_str(self._config.get("media", ""))

    @property
    def font(self) -> str | None:
        """Check the Config for a Supplied Default Font, else use the First Available TrueType Font in Linux"""
        if "font" in self._config:
            return self._config["font"]
        try:
            return list(get_fonts().values())[0][0].as_posix()
        except IndexError:
            return None
