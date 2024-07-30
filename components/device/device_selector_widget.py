from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget


class DeviceSelectorWidget(QWidget):
    def __init__(self, devices: list[str]) -> None:
        super().__init__()

        self.device_dropdown = QComboBox()
        self.device_dropdown.addItems(devices)

        dropdown_layout = QHBoxLayout()
        dropdown_layout.addWidget(self.device_dropdown)

        self.setLayout(dropdown_layout)

    @property
    def selected(self) -> str:
        return self.device_dropdown.currentText()
