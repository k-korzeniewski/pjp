from Service.Drivers import DriverContext, ChromeDriver
from Service.Image import ImageContext, ImageService
from Service.FindSentence import FindSentenceService, FindSentenceContext
from Service.TableToCsv import TableToCsvService, TableToCsvContext

"""
    This class is holding all settings and service instances.
    Services are instances only ones - and re-instance when context are changed
"""


class ApplicationContext:
    # Application:
    link_list = []
    service_settings = {'images': False, 'sentences': False, 'paragraphs': True,
                        "url_from_file": False, "save_to_file": True}
    urls_file = "/Users/kamilkorzeniewski/urls.txt"  # Loading urls from that file
    result_file = "/Users/kamilkorzeniewski/results.txt"  # Saving result in this file

    # UI
    url_inputbox_default_text = "Paste here links -> each in own line "
    # Driver:
    driver_context = DriverContext()
    driver_context.driver_path = "/usr/local/chromedriver/chromedriver-Darwin"
    driver = ChromeDriver(driver_context=driver_context)

    # Change context and re-init driver

    # Image:
    image_context = ImageContext()
    image_context.save_path = "/Users/kamilkorzeniewski/imgs"  # Default path to save images
    image_service = ImageService(image_context=image_context, driver=driver)

    # FindSentence Service
    find_sentence_context = FindSentenceContext()
    find_sentence_context.word_list = ['Java']
    find_sentence_service = FindSentenceService(find_sentece_context=find_sentence_context, driver=driver)

    # table to csv service
    table_to_csv_context = TableToCsvContext()
    table_to_csv_service = TableToCsvService(table_to_csv_context, driver)

    @classmethod
    def set_find_sentence_context(cls, context):
        ApplicationContext.find_sentence_context = context
        ApplicationContext.find_sentence_service = FindSentenceService(find_sentece_context=cls.find_sentence_context,
                                                                       driver=cls.driver)

    @classmethod
    def set_driver_context(cls, context):
        ApplicationContext.driver_context = context
        ApplicationContext.driver = ChromeDriver(driver_context=cls.driver_context)

    @classmethod
    def set_image_context(cls, context):
        ApplicationContext.image_context = context
        ApplicationContext.image_service = ImageService(image_context=cls.image_context,
                                                        driver=cls.driver)
    @classmethod
    def set_table_to_csv_context(cls, context):
        ApplicationContext.table_to_csv_context = context
        ApplicationContext.table_to_csv_service = TableToCsvService(table_to_csv_context=cls.table_to_csv_context,
                                                                    driver=cls.driver)

    @classmethod
    def update_links(cls, links):
        cls.link_list.clear()
        cls.link_list = links
