from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QDialog, QVBoxLayout, QPlainTextEdit, QTabWidget,
                             QGridLayout,QLabel,QLineEdit)

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
        links = self.text_edit.toPlainText()
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

        tabs.addTab(driver_tab, "Driver")
        tabs.addTab(image_tab, "Image")

        # Driver tab:
        driver_tab_layout = QGridLayout()
        driver_tab_layout.addWidget(QLabel("Driver path: "),0,0)
        driver_path_input = QLineEdit(ApplicationContext.driver_context.driver_path)
        driver_tab_layout.addWidget(driver_path_input,0,1)
        driver_tab.setLayout(driver_tab_layout)

        # Image Tab:

        # Main Layout

        main_layout = QVBoxLayout()

        # Buttons:

        button_layout = QHBoxLayout()

        close_button = QPushButton('Close', self)
        button_layout.addWidget(close_button)

        save_button = QPushButton('Save', self)
        button_layout.addWidget(save_button)

        # Add components do layout ( order -> first add on top )
        main_layout.addWidget(tabs)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

# -----------------------------------------------------------------------------------
