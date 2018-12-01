import sys
from UI.Window import Window
from PyQt5.QtWidgets import QApplication



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
