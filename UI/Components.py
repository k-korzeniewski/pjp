from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QDialog, QVBoxLayout, QPlainTextEdit, QTabWidget,
                             QGridLayout, QLabel, QLineEdit)

from ApplicationContext import ApplicationContext
from Service.Drivers import DriverContext
from Service.Image import ImageContext
from PyQt5.QtWidgets import QMessageBox
from Service.ServiceManager import SerivceManager
import logging
import os

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

    def text_change_handle(self):
        links = self.text_edit.toPlainText().split('\n')
        ApplicationContext.update_links(links=links)


# -----------------------------------------------------------------------------------


# Dialog that shows when Settings button clicked

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.init_ui()

    def init_ui(self):
        # Tab init:
        tabs = QTabWidget()
        driver_tab = QWidget()
        image_tab = QWidget()

        # Set tabs layout:
        driver_tab.setLayout(self.driver_tab_init())
        image_tab.setLayout(self.image_tab_init())

        # Add all tabs to one widget:
        tabs.addTab(driver_tab, "Driver")
        tabs.addTab(image_tab, "Image")

        main_layout = QVBoxLayout()

        # Add components do layout ( order -> first add on top )
        main_layout.addWidget(tabs)
        main_layout.addLayout(self.buttons_init())

        self.setLayout(main_layout)

    def driver_tab_init(self) -> QGridLayout:

        driver_tab_layout = QGridLayout()
        driver_tab_layout.addWidget(QLabel("Driver path: "), 0, 0)

        self.driver_path_input = QLineEdit()
        self.driver_path_input.setText(ApplicationContext.driver_context.driver_path)
        driver_tab_layout.addWidget(self.driver_path_input, 0, 1)

        return driver_tab_layout

    def image_tab_init(self) -> QGridLayout:
        image_tab_layout = QGridLayout()
        image_tab_layout.addWidget(QLabel("Images save path: "), 0, 0)

        self.image_path_input = QLineEdit()
        self.image_path_input.setText(ApplicationContext.image_context.save_path)
        image_tab_layout.addWidget(self.image_path_input, 0, 1)

        return image_tab_layout

    def buttons_init(self) -> QHBoxLayout:
        button_layout = QHBoxLayout()  # Layout for buttons

        close_button = QPushButton('Close', self)  # Close button
        button_layout.addWidget(close_button)

        save_button = QPushButton('Save', self)  # Save button
        save_button.clicked.connect(self.save_button_handler)
        button_layout.addWidget(save_button)
        return button_layout

    def save_button_handler(self):
        try:
            driver_context = DriverContext()
            driver_context.driver_path = self.driver_path_input.text()
            ApplicationContext.set_driver_context(driver_context)
            print("Settings saved ;)")
        except Exception:
            QMessageBox.critical(self, "Driver", "Driver path is wrong")
        try:
            if (os.path.isdir(self.image_path_input)):
                image_context = ImageContext()
                image_context.save_path = self.image_path_input.text()
                ApplicationContext.set_image_context(image_context)
                print("Settings saved ;)")
            else:
                QMessageBox.critical(self, "Image", "Image path is wrong !")
        except Exception:
            QMessageBox.critical(self, "Image", "Image path is wrong !")
# -----------------------------------------------------------------------------------
