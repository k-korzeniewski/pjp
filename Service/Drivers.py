from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import DesiredCapabilities
from Service.Exceptions import NoneContextException
import logging
"""
    Selenium chrome driver implementation
"""


class ChromeDriver:
    def __init__(self, driver_context):
        logger = logging.getLogger('Driver')

        if driver_context is None:
            raise NoneContextException("DriverContext class must be provided")

        self.options = Options()
        self.options.headless = True
        self.options.add_argument('--no-sandbox --headless --start-maximized --ignore-certificate-errors')

        self.capabilities = DesiredCapabilities.CHROME.copy()
        self.capabilities['acceptSslCerts'] = True
        self.capabilities['acceptInsecureCerts'] = True

        self.driver = webdriver.Chrome(executable_path=driver_context.driver_path,
                                       chrome_options=self.options, desired_capabilities=self.capabilities)
        logger.info('Driver initialized ')

    def get_driver(self, url) -> WebDriver:
        self.driver.get(url)
        return self.driver


"""
    Chrome driver settings
"""


class DriverContext:
    def __init__(self) -> None:
        super().__init__()
        self.driver_path = ""
