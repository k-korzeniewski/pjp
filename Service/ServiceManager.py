from ApplicationContext import ApplicationContext


class SerivceManager:

    @classmethod
    def start_services(cls):
        serivces_settings = ApplicationContext.service_settings
        link_list = ApplicationContext.link_list
        sentences = []
        if serivces_settings['images']:
            for url in link_list:
                print("Start fetching images from : %s", url)
                ApplicationContext.image_service.fetch_images(url)
        if serivces_settings['sentences']:
            for url in link_list:
                print("Start fetching sentences from : %s", url)
                sentences.append(ApplicationContext.find_sentence_service.find_sentce_with_word(url))
        print(sentences)
