from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Services.FindParagraphService import FindParagraphService
from Services.FindSentenceService import FindSentenceService
from Services.ImageService import ImageService
from Services.TablesToCsvService import TablesToCsvService
from UI import SettingsDesign
from ApplicationContext import ApplicationContext
from Services.ServicesManager import Manager
from Utils.ChromeDriver import ChromeDriver


class SettingsController:

    def __init__(self, settings_design: SettingsDesign, dialog: QDialog) -> None:
        super().__init__()
        self.dialog = dialog
        self.settings_design = settings_design
        self.driver_tab()
        self.default_values()
        self.check_box_handler()

    def default_values(self):
        self.settings_design.driver_path.setText(ChromeDriver.get_driver_path())
        self.settings_design.image_output_path.setText(ImageService.get_instance().context.get_values('save_path'))
        self.settings_design.csv_output.setText(
            TablesToCsvService.get_instance().context.get_values('save_path'))
        self.settings_design.text_output_path.setText(ApplicationContext.text_output_path)
        self.settings_design.links_path.setText(ApplicationContext.link_input_path)

        self.paragraph_checked = False
        self.sentence_checked = False
        self.image_checked = False
        self.csv_checked = False
        self.load_links_from_file_checked = ApplicationContext.load_links_from_file
        self.save_text_checked = ApplicationContext.save_text

        self.settings_design.save_button.clicked.connect(lambda: self.save_hander())

        if FindSentenceService.get_instance() in Manager.get_services_list():
            self.settings_design.sentence_checkbox.setChecked(True)
            self.sentence_checked = True
        if FindParagraphService.get_instance() in Manager.get_services_list():
            self.settings_design.paragraph_checkbox.setChecked(True)
            self.paragraph_checked = True
        if ImageService.get_instance() in Manager.get_services_list():
            self.settings_design.images_checkbox.setChecked(True)
            self.image_checked = True
        if TablesToCsvService.get_instance() in Manager.get_services_list():
            self.settings_design.csv_checkbox.setChecked(True)
            self.csv_checked = True
        if self.load_links_from_file_checked:
            self.settings_design.load_links_checkbox.setChecked(True)
        else:
            self.settings_design.load_links_checkbox.setChecked(False)
        if self.save_text_checked:
            self.settings_design.save_result_checkbox.setChecked(True)
        else:
            self.settings_design.save_result_checkbox.setChecked(False)

    def driver_tab(self):
        self.driver_path = self.settings_design.driver_path.text()
        print(self.driver_path)

    def check_box_handler(self):

        self.settings_design.paragraph_checkbox.stateChanged.connect(lambda: self.paragraph_checked_handler())
        self.settings_design.sentence_checkbox.stateChanged.connect(lambda: self.sentence_checked_handler())
        self.settings_design.images_checkbox.stateChanged.connect(lambda: self.image_checked_handler())
        self.settings_design.csv_checkbox.stateChanged.connect(lambda: self.csv_checked_handler())
        self.settings_design.save_result_checkbox.stateChanged.connect(lambda: self.save_text_handler())
        self.settings_design.load_links_checkbox.stateChanged.connect(lambda: self.load_links_from_file_handler())

    @pyqtSlot()
    def paragraph_checked_handler(self):
        self.paragraph_checked = not self.paragraph_checked

    @pyqtSlot()
    def sentence_checked_handler(self):
        self.sentence_checked = not self.sentence_checked

    @pyqtSlot()
    def image_checked_handler(self):
        self.image_checked = not self.image_checked

    @pyqtSlot()
    def csv_checked_handler(self):
        self.csv_checked = not self.csv_checked

    @pyqtSlot()
    def load_links_from_file_handler(self):
        self.load_links_from_file_checked = not self.load_links_from_file_checked

    @pyqtSlot()
    def save_text_handler(self):
        self.save_text_checked = not self.save_text_checked

    @pyqtSlot()
    def save_hander(self):

        if self.image_checked:
            if ImageService.get_instance() not in Manager.get_services_list():
                Manager.append_service(ImageService.get_instance())
        else:
            if ImageService.get_instance() in Manager.get_services_list():
                Manager.remove_service(ImageService.get_instance())

        if self.sentence_checked:
            if FindSentenceService.get_instance() not in Manager.get_services_list():
                Manager.append_service(FindSentenceService.get_instance())
        else:
            if FindSentenceService.get_instance() in Manager.get_services_list():
                Manager.remove_service(FindSentenceService.get_instance())

        if self.paragraph_checked:
            if FindParagraphService.get_instance() not in Manager.get_services_list():
                Manager.append_service(FindParagraphService.get_instance())
        else:
            if FindParagraphService.get_instance() in Manager.get_services_list():
                Manager.remove_service(FindParagraphService.get_instance())

        if self.csv_checked:
            if TablesToCsvService.get_instance() not in Manager.get_services_list():
                Manager.append_service(TablesToCsvService.get_instance())
            else:
                if TablesToCsvService.get_instance() in Manager.get_services_list():
                    Manager.remove_service(TablesToCsvService.get_instance())
        if self.load_links_from_file_checked:
            ApplicationContext.load_links_from_file = True
        else:
            ApplicationContext.load_links_from_file = False
        if self.save_text_checked:
            ApplicationContext.save_text = True
        else:
            ApplicationContext.save_text = False

        ChromeDriver.set_driver_path(self.settings_design.driver_path.text())

        TablesToCsvService.get_instance().context.set_values(key='save_path',
                                                             value=self.settings_design.csv_output.text())
        FindParagraphService.get_instance().context.set_values(key='save_path',
                                                               value=self.settings_design.text_output_path.text())
        FindSentenceService.get_instance().context.set_values(key='save_path',
                                                              value=self.settings_design.text_output_path.text())
        ImageService.get_instance().context.set_values(key='save_path',
                                                       value=self.settings_design.image_output_path.text())
        ApplicationContext.text_output_path = self.settings_design.text_output_path.text()
        ApplicationContext.link_input_path = self.settings_design.links_path.text()

        self.dialog.close()
