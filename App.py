import sys,os,time
from UI.Window import Window
from PyQt5.QtWidgets import QApplication

import logging


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
