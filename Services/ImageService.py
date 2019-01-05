import urllib

from Services.Service import Service, ServiceContext
from Utils.ChromeDriver import ChromeDriver
from ApplicationContext2 import ApplicationContext
import logging

logger = logging.getLogger("ImageService")


class ImageService(Service):
    __instance = None

    def __init__(self):
        super().__init__(ImageServiceContext())

    @staticmethod
    def get_instance():
        if ImageService.__instance is None:
            ImageService.__instance = ImageService()
        return ImageService.__instance

    def start(self, url):
        driver = ChromeDriver.get_instance().get_driver(url)
        uri = []
        r = driver.find_elements_by_tag_name('img')
        for v in r:
            src = v.get_attribute("src")
            print(src)
            uri.append(src)
            pos = len(src) - src[::-1].index('/')
            if src[pos::] and src[pos::].strip():
                urllib.request.urlretrieve(src, self.context.values['save_path'] + '/' + src[pos::])


class ImageServiceContext(ServiceContext):
    def __init__(self):
        logger.info("ImageServiceContext initialized")
        self.values['save_path'] = ApplicationContext.default_image_save_path
