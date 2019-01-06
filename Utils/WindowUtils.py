from UI.Window import Window


class Utils:
    @staticmethod
    def print_output(text):
        Window.__output.setText(Window.__output.text() + text)