from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QWidget


class LabelWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.text_box = QLineEdit()
        self.print_button = QPushButton("Print")
        self.print_button.clicked.connect(self.print_text)

        layout = QHBoxLayout()
        layout.addWidget(self.text_box)
        layout.addWidget(self.print_button)

        self.setLayout(layout)

    def print_text(self) -> None:
        print(self.text_box.text())
