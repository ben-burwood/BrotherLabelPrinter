from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget

from BrotherLabelPrinterControl.constants import Media


class MediaWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.media_select = QComboBox()
        self.media_select.addItems([media.name for media in Media])

        layout = QHBoxLayout()

        self.setLayout(layout)

    def media(self) -> Media:
        return Media[self.media_select.currentText()]
