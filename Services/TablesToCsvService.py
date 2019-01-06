import os

from selenium.webdriver.common.by import By

from Services.Service import Service, ServiceContext
from ApplicationContext2 import ApplicationContext
from Utils.ChromeDriver import ChromeDriver
import csv
import datetime


class TablesToCsvService(Service):
    __instance = None

    def __init__(self):
        super().__init__(TablesToCsvServiceContext())

    @staticmethod
    def get_instance():
        if TablesToCsvService.__instance is None:
            TablesToCsvService.__instance = TablesToCsvService()
        return TablesToCsvService.__instance

    def start(self, url):
        result_tables = list()
        driver = ChromeDriver.get_instance().get_driver(url)
        tables = driver.find_elements_by_xpath("//table")
        for table in tables:
            if table.text:
                result_tables.append(table)
                print("TABLES ----------------")
        if not os.path.exists(self.context.values['save_path']):
            os.makedirs(ApplicationContext.default_csv_output_path)

        now = datetime.datetime.now()
        file_name = '{}-{}-{}.csv'.format(now.year, now.month, now.day)
        path = '{}/{}'.format(self.context.values['save_path'], file_name)
        print("Try to write to file: " + file_name)

        with open(path, 'w+',newline='') as f:
            wr = csv.writer(f)
            for table in result_tables:
                for row in table.find_elements_by_css_selector('tr'):
                    wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])


class TablesToCsvServiceContext(ServiceContext):
    def __init__(self) -> None:
        super().__init__()
        self.values['save_path'] = ApplicationContext.default_csv_output_path
