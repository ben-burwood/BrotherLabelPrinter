from PIL import ImageFont
from PySide6.QtWidgets import QComboBox, QFormLayout, QSpinBox, QWidget

from BrotherP700USBControl.labelprinterkit.utils.font import FontPath, get_linux_fonts

class FontWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self._fonts = get_linux_fonts()

        self._font_path_edit = QComboBox()
        self._font_path_edit.addItems([font for font in self._fonts.keys()])

        self._font_size_edit = QSpinBox()
        self._font_index_edit = QSpinBox()

        self._font_size_edit.setRange(1, 1000)
        self._font_index_edit.setRange(0, 100)

        layout = QFormLayout()
        layout.addRow("Font Path:", self._font_path_edit)
        layout.addRow("Font Size:", self._font_size_edit)
        layout.addRow("Font Index:", self._font_index_edit)

        self.setLayout(layout)

    @property
    def font_path(self) -> FontPath:
        """Truetype Font File (.ttf) - Under Windows, if the file is not found in this filename, the loader also looks in Windows fonts/ directory."""
        return self._fonts[self._font_path_edit.currentText()][0]

    @property
    def font_size(self) -> int:
        """Font Size - in Points"""
        return self._font_size_edit.value()

    @property
    def font_index(self) -> int:
        """Font Face to load (default is first available face)"""
        return self._font_index_edit.value()

    @property
    def font(self) -> ImageFont.FreeTypeFont:
        return ImageFont.truetype(self.font_path, self.font_size, self.font_index)
