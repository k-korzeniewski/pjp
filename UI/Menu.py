from PyQt5.QtWidgets import QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from ApplicationContext import ApplicationContext


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        start_button = QPushButton('Start', self)
        start_button.clicked.connect(self.start_button_handler)
        layout.addWidget(start_button)

        stop_button = QPushButton('Stop', self)
        layout.addWidget(stop_button)

        configuration_button = QPushButton('Configuration', self)
        layout.addWidget(configuration_button)

        self.setLayout(layout)

    @pyqtSlot()
    def start_button_handler(self):
        print("Feching data from ...")
        ApplicationContext.image_service.fetch_images("https://www.wp.pl")
