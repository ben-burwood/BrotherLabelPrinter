from PySide6.QtWidgets import QButtonGroup, QHBoxLayout, QRadioButton, QWidget

from print.connection import ConnectionType

class ConnectionWidget(QWidget):

    def __init__(self) -> None:
        super().__init__()

        radio_buttons = [QRadioButton(connection_type.value) for connection_type in ConnectionType]
        radio_buttons[0].setChecked(True)

        self.radio_group = QButtonGroup()
        for radio_button in radio_buttons:
            self.radio_group.addButton(radio_button)

        radio_layout = QHBoxLayout()
        for radio_button in radio_buttons:
            radio_layout.addWidget(radio_button)

        self.setLayout(radio_layout)

    @property
    def connection(self) -> ConnectionType:
        selected_button_text = self.radio_group.checkedButton().text()
        return ConnectionType.get_by_value(selected_button_text)
