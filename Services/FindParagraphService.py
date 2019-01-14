import os
from datetime import datetime

from ApplicationContext import ApplicationContext
from Services.Service import Service, ServiceContext
from Utils.ChromeDriver import ChromeDriver


class FindParagraphService(Service):
    __instance = None

    def __init__(self):
        super().__init__(FindParagraphServiceContext())

    @staticmethod
    def get_instance():
        if FindParagraphService.__instance is None:
            FindParagraphService.__instance = FindParagraphService()
        return FindParagraphService.__instance

    def start(self, url):
        driver = ChromeDriver.get_instance().get_driver(url)
        elements = []
        result = []

        for word in self.context.get_values('word_list'):
            for i in range(1, 6):
                try:
                    print(i)
                    xpath = "//h{1}[contains(text(),'{0}')]/parent::*".format(word, i)
                    body = driver.find_element_by_xpath(xpath).text
                    elements.append(body)
                except Exception:
                    pass
        for e in elements:
            r = e.split("\n")
            for x in r:
                result.append(x)

        self.save_to_file(str(result))
        self.output.setText(self.output.toPlainText() + str(result).strip('[]') + '\n')
        return result

    def save_to_file(self, lines):
        if ApplicationContext.save_text:
            if not os.path.exists(self.context.get_values('save_path')):
                os.makedirs(self.context.get_values('save_path'))
            now = datetime.now()
            file_name = '{}-{}-{}-paragraphs.txt'.format(now.year, now.month, now.day)
            path = '{}/{}'.format(self.context.get_values('save_path'), file_name)
            with open(path, "a+") as file:
                file.writelines(lines)


class FindParagraphServiceContext(ServiceContext):
    def __init__(self) -> None:
        super().__init__()
        self.set_values('word_list', list())
        self.set_values('save_path', ApplicationContext.text_output_path)
