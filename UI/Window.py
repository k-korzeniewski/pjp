from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QDialog
from UI.Design import Ui_MainWindow
from Services.ServicesManager import Manager
from UI.Settings_design import Ui_Dialog


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.button_handlers_setup()

    def button_handlers_setup(self):
        self.start_button.clicked.connect(self.start_button_handler)
        self.close_button.clicked.connect(self.close_button_handler)
        self.settings_button.clicked.connect(self.settings_button_handler)

    @pyqtSlot()
    def start_button_handler(self):
        Manager.start_services()
        print("Start button clicked")

    @pyqtSlot()
    def close_button_handler(self):
        QMainWindow.close(self)
        print("Close button clicked")

    @pyqtSlot()
    def settings_button_handler(self):
        dialog_ui = Ui_Dialog()
        dialog = QDialog()
        dialog_ui.setupUi(dialog)
        dialog.exec_()
        print("Settings button clicked")
