from enum import Enum


class Font(Enum):
    ARIAL = "arial.ttf"
    TIMES_NEW_ROMAN = "times.ttf"
    COURIER = "cour.ttf"
    COMIC_SANS = "comic.ttf"
    VERDANA = "verdana.ttf"

    @staticmethod
    def get_by_name(name: str) -> "Font":
        for font in Font:
            if font.name == name:
                return font
        raise ValueError(f"Font with name '{name}' not found.")
