import logging

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QPlainTextEdit)

from ApplicationContext import ApplicationContext
from Service.ServiceManager import SerivceManager
from UI.Settings import SettingsDialog

"""
    All UI components 
"""

logger = logging.getLogger('Components')


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
        SerivceManager.start_services()

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

        self.text_edit = QPlainTextEdit()
        self.init_ui()

    def init_ui(self):
        self.text_edit.resize(400, 200)
        self.text_edit.insertPlainText("Here you can paste links.")
        self.text_edit.textChanged.connect(self.text_change_handle)
        layout = QHBoxLayout()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    @pyqtSlot()
    def text_change_handle(self):
        links = self.text_edit.toPlainText().split('\n')
        ApplicationContext.update_links(links=links)


# -----------------------------------------------------------------------------------


# Dialog that shows when Settings button clicked

# ----------------------------------------------------------------------------------
