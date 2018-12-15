from Service.Exceptions import NoneContextException


class FindSentenceService:
    def __init__(self, find_sentece_context, driver):
        if find_sentece_context is None:
            raise NoneContextException("Find Sentence must be provided")
        self.context = find_sentece_context
        self.driver = driver

    def find_sentce_with_word(self, url) -> list:
        driver = self.driver.get_driver(url=url)
        body = driver.find_element_by_tag_name("p").text.split(".")
        result = []
        for sentence in body:
            for word in self.context.word_list:
                if word in sentence:
                    result.append(sentence)
        # Filter once again
        for sentence in result:
            for word in self.context.word_list:
                if word not in sentence:
                    result.remove(sentence)
        return result

    def find_paragraph_with_word(self, url) -> list:
        driver = self.driver.get_driver(url=url)
        elements = []
        result = []

        for word in self.context.word_list:
            for i in range(1, 6):
                try:
                    print(i)
                    xpath = "//h{1}[contains(text(),'{0}')]/parent::*".format(word, i)
                    body = driver.find_element_by_xpath(xpath).text
                    elements.append(body)
                except Exception:
                    print("Cant get some header.")

        for e in elements:
            result.append(e)
        return result


class FindSentenceContext:

    def __init__(self):
        self.word_list = []
