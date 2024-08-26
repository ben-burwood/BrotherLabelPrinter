from pydantic import BaseModel, Field

from api.config import Config
from labelprinterkit.constants import Media
from labelprinterkit.labels.box import Box
from labelprinterkit.labels.label import Label
from labelprinterkit.labels.text import Padding, Text

class PrintRequest(BaseModel):
    text: str
    height: int
    _padding: dict[str, int] = Field(default_factory=lambda: {"top": 0, "right": 10, "bottom": 0, "left": 0})
    font: str = Config().font
    _media: str = Config().media

    @property
    def padding(self) -> Padding:
        return Padding.from_dict(self._padding)

    @property
    def media(self) -> Media:
        return Media.get(self._media)

    @property
    def label(self) -> Label:
        text = Text(self.height, self.text, font_path=self.font, padding=self.padding)
        box = Box(70, text)
        return Label(box)
