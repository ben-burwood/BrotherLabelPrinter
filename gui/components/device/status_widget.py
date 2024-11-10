from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from BrotherLabelPrinterControl.printers import GenericPrinter


class StatusWidget(QWidget):
    def __init__(self, printer: GenericPrinter = None) -> None:
        super().__init__()

        self.printer = printer

        self.refresh_button = QPushButton("Status")
        self.refresh_button.clicked.connect(self.refresh_status)

        self.status_label = QLabel()
        self.status_label.setFixedSize(20, 20)

        self.status_table = QTableWidget()
        self.status_table.setColumnCount(2)
        self.status_table.setHorizontalHeaderLabels(["Key", "Value"])

        layout = QVBoxLayout()
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.status_table)
        self.setLayout(layout)

    def refresh_status(self) -> None:
        """Trigger the get_status Method for the Printer and Display the Result"""
        if not self.printer:
            return

        status = self.printer.get_status()

        self.status_table.setRowCount(len(status._data))
        for row, (key, value) in enumerate(status._data.items()):
            self.status_table.setItem(row, 0, QTableWidgetItem(key))
            self.status_table.setItem(row, 1, QTableWidgetItem(value))

        if status.ready():
            self.status_label.setText("Ready")
            self.status_label.setStyleSheet("background-color: green;")
        else:
            self.status_label.setText("Error")
            self.status_label.setStyleSheet("background-color: red;")

    def update_printer(self, printer: GenericPrinter) -> None:
        self.printer = printer
        self.refresh_status()
