from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from labelprinterkit.printers import BasePrinter

from components.device.connection_widget import ConnectionWidget
from components.device.device_selector_widget import DeviceSelectorWidget
from print.device import Device


class DeviceWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.printer: BasePrinter | None = None

        self.connection_type_widget = ConnectionWidget()

        self.device_selector_widget = DeviceSelectorWidget(devices=[d.name for d in Device])

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_device)

        device_layout = QVBoxLayout()
        device_layout.addWidget(self.connection_type_widget)
        device_layout.addWidget(self.device_selector_widget)
        device_layout.addWidget(self.connect_button)

        self.setLayout(device_layout)

    def connect_device(self) -> None:
        backend = self.connection_type_widget.connection.backend
        self.printer = self.device_selector_widget.device.printer(backend)

        print(self.printer.get_status())
