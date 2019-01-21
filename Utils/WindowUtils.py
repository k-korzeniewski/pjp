from UI.Window import Window


class Utils:
    # Method that print text in output on main window
    @staticmethod
    def print_output(text):
        Window.__output.setText(Window.__output.text() + text)
