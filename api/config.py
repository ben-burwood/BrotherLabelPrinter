import yaml

from labelprinterkit.constants import Media
from labelprinterkit.utils.font import get_fonts

CONFIG_FILE = "config.yaml"


def _read_config() -> dict:
    """Read the YAML Config File and Return the Contents as a Dictionary"""
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)


def get_font() -> str | None:
    """Check the Config for a Supplied Default Font, else use the First Available TrueType Font in Linux"""
    config = _read_config()
    if "font" in config:
        return config["font"]
    try:
        return list(get_fonts().values())[0][0].as_posix()
    except IndexError:
        return None


def get_media() -> Media | None:
    """Check the Config for a Supplied Default Media"""

    def get_media_from_str(media: str) -> Media:
        return next((m for m in Media if m.name.lower() == media.lower()))

    config = _read_config()
    if "media" in config:
        return get_media_from_str(config["media"])
    return None
