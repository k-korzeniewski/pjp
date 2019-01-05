from Services.Service import Service, ServiceContext
from Utils import ChromeDriver


class FindSentenceService(Service):
    __instance = None

    def __init__(self):
        super().__init__(FindSentenceServiceContext())

    def get_instance(self):
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
        # Filter once again
        for sentence in result:
            for word in self.context.values["word_list"]:
                if word not in sentence:
                    result.remove(sentence)
        return result


class FindSentenceServiceContext(ServiceContext):
    def __init__(self) -> None:
        super().__init__()
        self.values['word_list'] = list()
