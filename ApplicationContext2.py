class ApplicationContext:
    default_driver_path = "/usr/local/chromedriver/chromedriver-Darwin"
    default_image_save_path = "/Users/kamilkorzeniewski/imgs"
    default_csv_output_path = "/Users/kamilkorzeniewski/csv"
    default_text_output_path = "/Users/kamilkorzeniewski/text"
    text_output_path = default_text_output_path
    link_list = []

    @classmethod
    def update_links(cls, links):
        cls.link_list.clear()
        cls.link_list = links
        print(ApplicationContext.link_list)


