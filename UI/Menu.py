from PyQt5.QtWidgets import QHBoxLayout, QWidget, QPushButton
from Service.Image import ImageService, ImageContext
from PyQt5.QtCore import pyqtSlot


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        image_context = ImageContext
        image_context.save_path = "/Users/kamilkorzeniewski/imgs"

        self.image_service = ImageService(image_context)

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
        self.image_service.fetch_images("https://www.wp.pl")
