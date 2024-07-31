from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget

from print.device import Device


class DeviceSelectorWidget(QWidget):
    def __init__(self, devices: list[str]) -> None:
        super().__init__()

        self.device_dropdown = QComboBox()
        self.device_dropdown.addItems(devices)

        dropdown_layout = QHBoxLayout()
        dropdown_layout.addWidget(self.device_dropdown)

        self.setLayout(dropdown_layout)

    @property
    def selected(self) -> Device:
        selected_device_text = self.device_dropdown.currentText()
        return Device.get_by_name(selected_device_text)
