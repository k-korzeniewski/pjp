from PyQt5.QtWidgets import QWidget


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Some title")

        self.show()

