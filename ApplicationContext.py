from Service.Drivers import DriverContext, ChromeDriver


class ApplicationContext:

    # Default settings:
    driver_context = DriverContext()
    driver_context.driver_path = "/usr/local/chromedriver/chromedriver-Darwin"
    driver = ChromeDriver(driver_context=driver_context)

    # Change context and re-init driver
    @classmethod
    def set_driver_context(cls,context):
        ApplicationContext.driver_context = context
        ApplicationContext.driver = ChromeDriver(driver_context=ApplicationContext.driver_context)
