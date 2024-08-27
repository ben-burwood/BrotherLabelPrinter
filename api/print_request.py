from typing import Any

from pydantic import BaseModel, Field, model_validator

from api.config import Config
from labelprinterkit.constants import Media
from labelprinterkit.labels.box import Box
from labelprinterkit.labels.label import Label
from labelprinterkit.labels.text import Padding, Text

class PrintRequest(BaseModel):
    text: str
    height: int
    padding: Padding = Field(default_factory=lambda: Padding(top=0, right=0, bottom=0, left=0))
    font: str = Field(default_factory=lambda: Config().font)
    media: Media = Field(default_factory=lambda: Config().media)

    @model_validator(mode="before")
    def set_padding(cls, values: dict[str, Any]) -> dict[str, Any]:
        padding = values.get("padding")
        if isinstance(padding, dict):
            values["padding"] = Padding.from_dict(padding)
        return values

    @model_validator(mode="before")
    def set_media(cls, values: dict[str, Any]) -> dict[str, Any]:
        media = values.get("media")
        if isinstance(media, str):
            values["media"] = Media.get(media)
        return values

    def generate_label(self, media: Media) -> Label:
        height = min(media.value.printarea, self.height)  # Cap the Height to the media's printarea

        text = Text(height, self.text, font_path=self.font, padding=self.padding)

        box = Box(media.value.printarea, text)

        return Label(box)
