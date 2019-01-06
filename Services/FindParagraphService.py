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

        for word in self.context.values['word_list']:
            for i in range(1, 6):
                try:
                    print(i)
                    xpath = "//h{1}[contains(text(),'{0}')]/parent::*".format(word, i)
                    body = driver.find_element_by_xpath(xpath).text
                    elements.append(body)
                except Exception:
                    print("Cant get some header.")

        for e in elements:
            r = e.split("\n")
            for x in r:
                result.append(x)

        self.output.setText(self.output.toPlainText() + str(result).strip('[]') + '\n')
        return result


class FindParagraphServiceContext(ServiceContext):
    def __init__(self) -> None:
        super().__init__()
        self.values['word_list'] = list()
