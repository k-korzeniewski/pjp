from Service.Exceptions import NoneContextException


class FindSentenceService:
    def __init__(self, find_sentece_context, driver):
        if find_sentece_context is None:
            raise NoneContextException("Find Sentence must be provided")
        self.context = find_sentece_context
        self.driver = driver

    def find_sentce_with_word(self, url):
        driver = self.driver.get_driver(url=url)
        body = driver.find_elements_by_tag_name("body")
        result = body.text
        print(result)


class FindSentenceContext:

    def __init__(self):
        self.word_list = []
