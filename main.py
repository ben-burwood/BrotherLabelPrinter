import sys

from PySide6.QtWidgets import QApplication, QFrame, QMainWindow, QVBoxLayout, QWidget

from components.device.device_widget import DeviceWidget
from components.device.status_widget import StatusWidget
from components.label.label_settings_widget import LabelSettingsWidget
from components.label.label_widget import LabelWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.device_widget = DeviceWidget()
        self.status_widget = StatusWidget()

        # Connect the printer_connected signal to the update_printer slot
        self.device_widget.printer_connected.connect(self.status_widget.update_printer)

        self.label_settings_widget = LabelSettingsWidget()
        self.print_widget = LabelWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.device_widget)
        layout.addWidget(self.divider())
        layout.addWidget(self.status_widget)
        layout.addWidget(self.divider())
        layout.addWidget(self.label_settings_widget)
        layout.addWidget(self.divider())
        layout.addWidget(self.print_widget)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setWindowTitle("Main Application")

    @staticmethod
    def divider() -> QFrame:
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        return divider


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
