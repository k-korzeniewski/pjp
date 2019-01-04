from PyQt5.QtWidgets import QMessageBox

from ApplicationContext import ApplicationContext
import datetime


class SerivceManager:

    @classmethod
    def start_services(cls):
        serivces_settings = ApplicationContext.service_settings
        link_list = ApplicationContext.link_list
        if ApplicationContext.service_settings['url_from_file']:
            result = cls.load_urls_from_file()
            for link in result:
                if link not in link_list:
                    link_list.append(link)
        print("Links loaded from file")
        link_list = list(filter(None, link_list))
        print(link_list)

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
                cls.save_to_file(elements, "paragraphs {0}".format(datetime.datetime.now()))

    @classmethod
    def save_to_file(cls, data, prefix):
        with open(ApplicationContext.result_file, "a+") as f:
            prefix = '#-------------------------------' + prefix + '-------------------------------#'
            surfix = '#----------------------------------------------------------------------------#'
            f.write(prefix)
            for line in data:
                f.writelines(line)
            f.write(surfix)

    @classmethod
    def load_urls_from_file(cls) -> list:
        path = ApplicationContext.urls_file;
        file = open(path, "r")
        result = []
        for line in file.readlines():
            result.append(line)
        return result
