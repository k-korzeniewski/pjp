from PyQt5.QtCore import pyqtSlot

from Services.FindParagraphService import FindParagraphService
from Services.FindSentenceService import FindSentenceService
from Services.ImageService import ImageService
from UI import SettingsDesign
from ApplicationContext2 import ApplicationContext
from Services.ServicesManager import Manager
from Utils.ChromeDriver import ChromeDriver


class SettingsController:

    def __init__(self, settings_design: SettingsDesign) -> None:
        super().__init__()
        self.settings_design = settings_design
        self.driver_tab()
        self.default_values()
        self.check_box_handler()

    def default_values(self):
        self.settings_design.driver_path.setText(ChromeDriver.get_driver_path())
        self.settings_design.image_output_path.setText(ImageService.get_instance().context.values['save_path'])
        self.settings_design.csv_output.setText(ApplicationContext.default_csv_output_path)  # Need to be changed !!!!
        self.settings_design.text_output_path.setText(ApplicationContext.text_output_path)

        self.paragraph_checked = False
        self.sentence_checked = False
        self.image_checked = False

        if FindSentenceService.get_instance() in Manager.get_services_list():
            self.settings_design.sentence_checkbox.setChecked(True)
            self.sentence_checked = True
        if FindParagraphService.get_instance() in Manager.get_services_list():
            self.settings_design.paragraph_checkbox.setChecked(True)
            self.paragraph_checked = True
        if ImageService.get_instance() in Manager.get_services_list():
            self.settings_design.images_checkbox.setChecked(True)
            self.image_checked = True

    def driver_tab(self):
        self.driver_path = self.settings_design.driver_path.text()
        print(self.driver_path)

    def check_box_handler(self):

        self.settings_design.paragraph_checkbox.stateChanged.connect(lambda: self.paragraph_checked())
        self.settings_design.sentence_checkbox.stateChanged.connect(lambda: self.sentence_checked())
        self.settings_design.images_checkbox.stateChanged.connect(lambda: self.image_checked())

    @pyqtSlot()
    def paragraph_checked(self):
        self.paragraph_checked = not self.paragraph_checked

    @pyqtSlot()
    def sentence_checked(self):
        self.sentence_checked = not self.sentence_checked
        # if FindParagraphService.get_instance() in Manager.get_services_list():
        #     Manager.remove_service(FindSentenceService.get_instance())
        # else:
        #     Manager.append_service(FindSentenceService.get_instance())

    @pyqtSlot()
    def image_checked(self):
        self.image_checked = not self.image_checked
        # if ImageService.get_instance() in Manager.get_services_list():
        #     Manager.remove_service(ImageService.get_instance())
        # else:
        #     Manager.append_service(ImageService.get_instance())

    @pyqtSlot()
    def save_hander(self):
        if self.image_checked:
            Manager.append_service(ImageService.get_instance())
        else:
            Manager.remove_service(ImageService.get_instance())

        if self.sentence_checked:
            Manager.append_service(FindSentenceService.get_instance())
        else:
            Manager.remove_service(FindSentenceService.get_instance())

        if self.paragraph_checked:
            Manager.append_service(FindParagraphService.get_instance())
        else:
            Manager.remove_service(FindParagraphService.get_instance())
        # add CSV checkbox when done
        ChromeDriver.set_driver_path(self.settings_design.driver_path.text())
        ImageService.get_instance().context.values['save_path'] = self.settings_design.image_output_path.text()
        # add CSV when done
