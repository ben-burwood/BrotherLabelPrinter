from PySide6.QtWidgets import QGridLayout, QSpinBox, QWidget

from BrotherLabelPrinterControl.labelprinterkit.labels.text import Padding

class PaddingWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self._top_edit = QSpinBox()
        self._right_edit = QSpinBox()
        self._bottom_edit = QSpinBox()
        self._left_edit = QSpinBox()

        for spin_box in [self._top_edit, self._right_edit, self._bottom_edit, self._left_edit]:
            spin_box.setRange(0, 10)

        layout = QGridLayout()
        layout.addWidget(self._top_edit, 0, 1)
        layout.addWidget(self._left_edit, 1, 0)
        layout.addWidget(self._right_edit, 1, 2)
        layout.addWidget(self._bottom_edit, 2, 1)

        self.setLayout(layout)

    @property
    def padding(self) -> Padding:
        return Padding(
            left=int(self._left_edit.text()),
            top=int(self._top_edit.text()),
            bottom=int(self._bottom_edit.text()),
            right=int(self._right_edit.text()),
        )
