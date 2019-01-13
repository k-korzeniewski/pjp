import os
from datetime import datetime

from Services.Service import Service, ServiceContext
from Utils.ChromeDriver import ChromeDriver


class FindSentenceService(Service):
    __instance = None

    def __init__(self):
        super().__init__(FindSentenceServiceContext())

    @staticmethod
    def get_instance():
        if FindSentenceService.__instance is None:
            FindSentenceService.__instance = FindSentenceService()
        return FindSentenceService.__instance

    def start(self, url):
        """Returning LIST of sentences"""
        driver = ChromeDriver.get_instance().get_driver(url)
        body = driver.find_element_by_tag_name("p").text.split(".")
        result = []
        for sentence in body:
            for word in self.context.values['word_list']:
                if word in sentence:
                    result.append(sentence)

        print(result)
        self.save_to_file(str(result))
        self.output.setText(self.output.toPlainText() + str(result).strip('[]') + '\n')
        return result

    def save_to_file(self, lines):
        if not os.path.exists(self.context.values['save_path']):
            os.makedirs(self.context.values['save_path'])
        now = datetime.now()
        file_name = '{}-{}-{}.txt'.format(now.year, now.month, now.day)
        path = '{}/{}'.format(self.context.values['save_path'], file_name)
        with open(path, "a+") as file:
            file.writelines(lines)


class FindSentenceServiceContext(ServiceContext):
    def __init__(self) -> None:
        super().__init__()
        self.values['word_list'] = list()
