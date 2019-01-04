import os

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QGridLayout, QCheckBox, QPlainTextEdit, QLineEdit, \
    QMessageBox, QDialog, QHBoxLayout, QPushButton, QLabel

from ApplicationContext import ApplicationContext
from Service.Drivers import DriverContext
from Service.Image import ImageContext


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.init_ui()

    def init_ui(self):
        # Tab init:

        general = QTabWidget()
        tabs = QTabWidget()
        driver_tab = QWidget()
        image_tab = QWidget()
        files = QWidget()

        general.setLayout(self.general_tab_init())
        files.setLayout(self.files_tab_init())
        # Set tabs layout:
        driver_tab.setLayout(self.driver_tab_init())
        image_tab.setLayout(self.image_tab_init())

        # Add all tabs to one widget:
        tabs.addTab(driver_tab, "Driver")
        tabs.addTab(image_tab, "Image")
        tabs.addTab(general, "General")
        tabs.addTab(files, "Files")
        main_layout = QVBoxLayout()

        # Add components do layout ( order -> first add on top )
        main_layout.addWidget(tabs)
        main_layout.addLayout(self.buttons_init())

        self.setLayout(main_layout)

    def general_tab_init(self) -> QGridLayout:
        general_tab_layout = QGridLayout()

        self.images_checkbox = QCheckBox('Images')
        self.sentences_checkbox = QCheckBox('Sentences')
        self.paragraphs_checkbox = QCheckBox('Paragraphs')
        self.load_url_from_file = QCheckBox('Load url from file:')
        self.images_checkbox.stateChanged.connect(lambda val: self.checkbox_handler('images', val))
        self.sentences_checkbox.stateChanged.connect(lambda val: self.checkbox_handler('sentences', val))
        self.paragraphs_checkbox.stateChanged.connect(lambda val: self.checkbox_handler('paragraphs', val))
        self.load_url_from_file.stateChanged.connect(lambda val: self.checkbox_handler('url_from_file', val))

        general_tab_layout.addWidget(self.images_checkbox, 0, 1)
        general_tab_layout.addWidget(self.sentences_checkbox, 0, 2)
        general_tab_layout.addWidget(self.images_checkbox, 0, 3)
        general_tab_layout.addWidget(self.load_url_from_file, 0, 4)
        return general_tab_layout

    def files_tab_init(self) -> QGridLayout:
        files_tab_layout = QGridLayout()

        self.urls_file = QLineEdit()
        self.urls_file.setText(ApplicationContext.urls_file)

        self.save_result_file_path = QLineEdit()
        self.save_result_file_path.setText(ApplicationContext.result_file)

        files_tab_layout.addWidget(QLabel("Urls file : "), 0, 0)
        files_tab_layout.addWidget(self.urls_file, 0, 1)
        files_tab_layout.addWidget(QLabel("Save file: "), 1, 0)
        files_tab_layout.addWidget(self.save_result_file_path, 1, 1)
        return files_tab_layout

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

    @pyqtSlot()
    def save_button_handler(self):
        self.save_settings()

    @pyqtSlot()
    def checkbox_handler(self, service, state):
        if state == Qt.Checked:
            ApplicationContext.service_settings[service] = True
        else:
            ApplicationContext.service_settings[service] = False

    def save_settings(self):
        try:
            driver_context = DriverContext()
            driver_context.driver_path = self.driver_path_input.text()
            ApplicationContext.set_driver_context(driver_context)
            print("Settings saved ;)")
        except Exception:
            QMessageBox.critical(self, "Driver", "Driver path is wrong")
        try:
            if os.path.isdir(self.image_path_input.text()):
                image_context = ImageContext()
                image_context.save_path = self.image_path_input.text()
                ApplicationContext.set_image_context(image_context)
                print("Settings saved ;)")
            else:
                QMessageBox.critical(self, "Image", "Image path is wrong !")
        except Exception as detail:
            QMessageBox.critical(self, "Image", "Image path is wrong !")
            print(detail)

        try:
            if os.path.isfile(self.urls_file.text()):
                ApplicationContext.urls_file = self.urls_file.text()
            else:
                QMessageBox.critical(self, "Files", "Urls file path is wrong!")
        except Exception:
            QMessageBox.critical(self, "Files", "Urls file path is wrong!")

        try:
            if os.path.isfile(self.save_result_file_path.text()):
                ApplicationContext.result_file = self.save_result_file_path.text()
            else:
                QMessageBox.critical(self, "Files", "Save file path is wrong!")
        except Exception:
            QMessageBox.critical(self, "Files", "Save file path is wrong!")


