from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QDialog, QVBoxLayout, QPlainTextEdit
from ApplicationContext import ApplicationContext

"""
    All UI components 
"""


## Menu on main window

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

        settings_button = QPushButton('Settings', self)
        settings_button.clicked.connect(self.show_settings_dialog)
        layout.addWidget(settings_button)

        self.setLayout(layout)

    @pyqtSlot()
    def start_button_handler(self):
        print("Feching data from ...")
        ApplicationContext.image_service.fetch_images("https://www.wp.pl")

    @pyqtSlot()
    def show_settings_dialog(self):
        print("Open settings dialog")
        dialog = SettingsDialog()
        dialog.exec_()


# -----------------------------------------------------------------------------------


##Input box for urls in main window

class UrlInputBox(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        text_edit = QPlainTextEdit()
        text_edit.resize(400, 200)
        text_edit.insertPlainText("Here you can paste links.")

        layout = QHBoxLayout()
        layout.addWidget(text_edit)

        self.setLayout(layout)


# -----------------------------------------------------------------------------------


# Dialog that shows when Settings button clicked

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        close_button = QPushButton('Close', self)
        button_layout.addWidget(close_button)

        save_button = QPushButton('Save', self)
        button_layout.addWidget(save_button)

        main_layout.addChildLayout(button_layout)
        self.setLayout(main_layout)

# -----------------------------------------------------------------------------------
