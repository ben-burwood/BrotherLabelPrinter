from pydantic import BaseModel, Field, field_validator

from BrotherLabelPrinterControl.constants import Media
from BrotherLabelPrinterControl.labels.box import Box
from BrotherLabelPrinterControl.labels.label import Label
from BrotherLabelPrinterControl.labels.text import Padding, Text

from .config import Config


class PrintRequest(BaseModel):
    text: str
    height: int
    padding: Padding = Field(default_factory=lambda: Padding(top=0, right=0, bottom=0, left=0))
    font: str = Field(default_factory=lambda: Config.get().font)
    media: Media = Field(default_factory=lambda: Config.get().media)

    @field_validator("padding")
    def set_padding(cls, padding: dict[str, int] | Padding) -> Padding:
        if isinstance(padding, dict):
            return Padding.from_dict(padding)
        return padding

    @field_validator("media")
    def set_media(cls, media: str | Media) -> Media:
        if isinstance(media, str):
            return Media.get(media)
        return media

    def generate_label(self, media: Media) -> Label:
        height = min(media.value.printarea, self.height)  # Cap the Height to the media's printarea

        text = Text(height, self.text, font_path=self.font, padding=self.padding)

        box = Box(media.value.printarea, text)

        return Label(box)
