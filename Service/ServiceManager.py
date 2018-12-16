from PyQt5.QtWidgets import QMessageBox

from ApplicationContext import ApplicationContext
import datetime


class SerivceManager:

    @classmethod
    def start_services(cls):
        serivces_settings = ApplicationContext.service_settings
        link_list = ApplicationContext.link_list
        if serivces_settings['images']:
            for url in link_list:
                print("Start fetching images from : %s", url)
                ApplicationContext.image_service.fetch_images(url)
        if serivces_settings['sentences']:
            sentences = []
            for url in link_list:
                print("Start fetching sentences from : %s", url)
                sentences.append(ApplicationContext.find_sentence_service.find_sentce_with_word(url))
            if ApplicationContext.service_settings["save_to_file"]:
                cls.save_to_file(sentences, "sentences {0}".format(datetime.datetime.now()))
        if serivces_settings['paragraphs']:
            elements = []
            for url in link_list:
                print("Start fetching paragraphs from : %s", url)
                result = ApplicationContext.find_sentence_service.find_paragraph_with_word(url)
                for e in result:
                    elements.append(e)
            if ApplicationContext.service_settings["save_to_file"]:
                cls.save_to_file(sentences, "paragraphs {0}".format(datetime.datetime.now()))

    @classmethod
    def save_to_file(cls, data, prefix):
        file = open(ApplicationContext.result_file, "a+")
        prefix = '#-------------------------------' + prefix + '-------------------------------#'
        surfix = '#----------------------------------------------------------------------------#'
        data = prefix + data + surfix
        file.write(data)
