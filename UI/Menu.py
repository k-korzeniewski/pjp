from PyQt5.QtWidgets import QHBoxLayout, QWidget, QPushButton


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        start_button = QPushButton('Start', self)
        layout.addWidget(start_button)

        stop_button = QPushButton('Stop', self)
        layout.addWidget(stop_button)

        configuration_button = QPushButton('Configuration', self)
        layout.addWidget(configuration_button)

        self.setLayout(layout)
