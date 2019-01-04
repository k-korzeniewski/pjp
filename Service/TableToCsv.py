from Service.Exceptions import NoneContextException


class TableToCsvService:
    def __init__(self, table_to_csv_context, driver):
        if table_to_csv_context is None:
            raise NoneContextException
        self.context = table_to_csv_context
        self.driver = driver

    def fetch_tables(self, url):
        driver = self.driver.get_driver(url=url)
        tables = driver.find_elements_by_xpath("//table")
        for table in tables:
            print(table.text)


class TableToCsvContext:
    def __init__(self):
        pass
