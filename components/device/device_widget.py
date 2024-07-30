import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

from components.device.connection_selector_widget import ConnectionSelectorWidget
from components.device.device_selector_widget import DeviceSelectorWidget
from print.device import Device

class DeviceWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.connection_type_widget = ConnectionSelectorWidget()

        self.device_selector_widget = DeviceSelectorWidget(devices=[d.name for d in Device])

        self.connect_button = QPushButton("Connect")

        device_layout = QVBoxLayout()
        device_layout.addWidget(self.connection_type_widget)
        device_layout.addWidget(self.device_selector_widget)
        device_layout.addWidget(self.connect_button)

        self.setLayout(device_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DeviceWidget()
    widget.show()
    sys.exit(app.exec())
