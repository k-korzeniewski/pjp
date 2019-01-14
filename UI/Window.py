from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QDialog

from Services.FindParagraphService import FindParagraphService
from Services.FindSentenceService import FindSentenceService
from UI.Design import Ui_MainWindow
from Services.ServicesManager import Manager
from UI.SettingsDesign import Ui_Dialog
from UI.SettingsController import SettingsController
from ApplicationContext import ApplicationContext


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.button_handlers_setup()
        Manager.change_output(self.result)

    def button_handlers_setup(self):
        self.start_button.clicked.connect(self.start_button_handler)
        self.close_button.clicked.connect(self.close_button_handler)
        self.settings_button.clicked.connect(self.settings_button_handler)
        self.url_list.textChanged.connect(self.urls_changed)
        self.word_list.textChanged.connect(self.word_list_changed)

    @pyqtSlot()
    def urls_changed(self):
        ApplicationContext.update_links(self.url_list.toPlainText().splitlines())

    @pyqtSlot()
    def word_list_changed(self):
        FindParagraphService.get_instance().context.set_values('word_list',self.word_list.toPlainText().splitlines())
        FindSentenceService.get_instance().context.set_values('word_list',self.word_list.toPlainText().splitlines())
        print(self.word_list.toPlainText().splitlines())

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
        SettingsController(dialog_ui, dialog)
        dialog.exec_()
        print("Settings button clicked")
