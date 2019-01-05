class ApplicationContext:
    default_driver_path = "/usr/local/chromedriver/chromedriver-Darwin"
    default_image_save_path = "/Users/kamilkorzeniewski/imgs"
    link_list = []

    @classmethod
    def update_links(cls, links):
        cls.link_list.clear()
        cls.link_list = links
