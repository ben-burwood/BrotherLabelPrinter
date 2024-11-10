from PySide6.QtWidgets import QButtonGroup, QHBoxLayout, QRadioButton, QWidget

from brother_label_printer_control.backends.main import Backend


class ConnectionWidget(QWidget):

    def __init__(self) -> None:
        super().__init__()

        radio_buttons = [QRadioButton(backend.value) for backend in Backend]
        radio_buttons[0].setChecked(True)

        self.radio_group = QButtonGroup()
        for radio_button in radio_buttons:
            self.radio_group.addButton(radio_button)

        radio_layout = QHBoxLayout()
        for radio_button in radio_buttons:
            radio_layout.addWidget(radio_button)

        self.setLayout(radio_layout)

    @property
    def backend(self) -> Backend:
        selected_button_text = self.radio_group.checkedButton().text()
        return Backend.get(selected_button_text)
