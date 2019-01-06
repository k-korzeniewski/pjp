import logging

from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from ApplicationContext2 import ApplicationContext


class ChromeDriver:
    __instance = None
    __driver_path = ApplicationContext.default_driver_path

    @staticmethod
    def get_instance():
        """Singleton implementation -> only one instance of this class can exist"""
        if ChromeDriver.__instance is None:
            ChromeDriver()
        return ChromeDriver.__instance

    def __init__(self):

        self.options = Options()
        self.options.headless = True
        self.options.add_argument('--no-sandbox --headless --start-maximized --ignore-certificate-errors')

        self.capabilities = DesiredCapabilities.CHROME.copy()
        self.capabilities['acceptSslCerts'] = True
        self.capabilities['acceptInsecureCerts'] = True

        self.driver = webdriver.Chrome(executable_path=ChromeDriver.__driver_path,
                                       chrome_options=self.options, desired_capabilities=self.capabilities)

    def get_driver(self, url) -> WebDriver:
        self.driver.get(url)
        return self.driver

    @staticmethod
    def set_driver_path(path):
        ChromeDriver.__driver_path = path
        ChromeDriver.__instance = ChromeDriver()

    @staticmethod
    def get_driver_path():
        return ChromeDriver.__driver_path
