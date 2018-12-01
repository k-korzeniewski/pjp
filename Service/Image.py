from Service.Exceptions import NoneContextException
import urllib.request


class ImageService:
    def __init__(self, image_context, driver):
        if image_context is None:
            raise NoneContextException("Image Context must be provided")  # if context is null then raise error
        self.context = image_context
        self.driver = driver

    def fetch_images(self, url):
        driver = self.driver.get_driver(url=url)
        uri = []
        r = driver.find_elements_by_tag_name('img')
        for v in r:
            src = v.get_attribute("src")
            uri.append(src)
            pos = len(src) - src[::-1].index('/')
            urllib.request.urlretrieve(src, "/".join([self.context.save_path, src[pos:]]))


class ImageContext:

    def __init__(self):
        self.save_path = ""
