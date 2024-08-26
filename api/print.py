from pydantic import BaseModel

from api.config import Config
from labelprinterkit.labels.box import Box
from labelprinterkit.labels.label import Label
from labelprinterkit.labels.text import Padding, Text

class PrintRequest(BaseModel):
    text: str
    height: int
    font: str = Config().font
    padding: Padding = Padding(0, 10, 0, 0)

    @property
    def label(self) -> Label:
        text = Text(self.height, self.text, font_path=self.font, padding=self.padding)
        box = Box(70, text)
        return Label(box)
