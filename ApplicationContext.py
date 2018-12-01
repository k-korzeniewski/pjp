from Service.Drivers import DriverContext, ChromeDriver
from Service.Image import ImageContext, ImageService

"""
    This class is holding all settings and service instances.
"""


class ApplicationContext:
    # Driver:
    driver_context = DriverContext()
    driver_context.driver_path = "/usr/local/chromedriver/chromedriver-Darwin"
    driver = ChromeDriver(driver_context=driver_context)

    # Change context and re-init driver
    @classmethod
    def set_driver_context(cls, context):
        ApplicationContext.driver_context = context
        ApplicationContext.driver = ChromeDriver(driver_context=cls.driver_context)

    # Image:
    image_context = ImageContext()
    image_context.save_path = "/Users/kamilkorzeniewski/imgs"  # Default path to save images
    image_service = ImageService(image_context=image_context, driver=driver)

    @classmethod
    def set_image_context(cls, context):
        ApplicationContext.image_context = context
        ApplicationContext.image_service = ImageService(image_context=cls.image_context,
                                                        driver=cls.driver)
