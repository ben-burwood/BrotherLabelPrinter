from PySide6.QtWidgets import QFormLayout, QSpinBox, QWidget
from labelprinterkit.labels.text import Padding

from gui.components.label.settings.font import FontWidget
from gui.components.label.settings.padding import PaddingWidget


class LabelSettingsWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.text_height_widget = QSpinBox()
        self.padding_widget = PaddingWidget()
        self.font_widget = FontWidget()

        layout = QFormLayout()
        layout.addRow("Text Height:", self.text_height_widget)
        layout.addRow("Padding:", self.padding_widget)
        layout.addRow("Font:", self.font_widget)

        self.setLayout(layout)

    @property
    def text_height(self) -> int:
        return int(self.text_height_widget.value())

    @property
    def font(self):
        return self.font_widget.font

    @property
    def padding(self) -> Padding:
        return self.padding_widget.padding
