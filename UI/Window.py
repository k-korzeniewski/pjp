from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QVBoxLayout, QWidget
from UI.Components import Menu, UrlInputBox


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Some title")
        self.center()

        window_layout = QVBoxLayout() # Here can be added new QWidgets to main window
        window_layout.addWidget(Menu())
        window_layout.addWidget(UrlInputBox())

        central_widget = QWidget() # Helper object to parse window_layout to QWidget
        central_widget.setLayout(window_layout)

        self.setCentralWidget(central_widget)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
