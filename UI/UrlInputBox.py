from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QHBoxLayout


class UrlInputBox(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        text_edit = QPlainTextEdit()
        text_edit.resize(400, 200)
        text_edit.insertPlainText("Here you can paste links.")

        layout = QHBoxLayout()
        layout.addWidget(text_edit)

        self.setLayout(layout)
