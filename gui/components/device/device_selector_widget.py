from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget

from brother_label_printer_control.printers.main import Printer


class DeviceSelectorWidget(QWidget):
    def __init__(self, devices: list[str]) -> None:
        super().__init__()

        self.device_dropdown = QComboBox()
        self.device_dropdown.addItems(devices)

        dropdown_layout = QHBoxLayout()
        dropdown_layout.addWidget(self.device_dropdown)

        self.setLayout(dropdown_layout)

    @property
    def device(self) -> Printer:
        return Printer[self.device_dropdown.currentText()]
