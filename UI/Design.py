# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 811, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.settings_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout.addWidget(self.settings_button)
        self.close_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.close_button.setCheckable(False)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 70, 91, 31))
        self.label.setObjectName("label")
        self.word_list = QtWidgets.QTextEdit(self.centralwidget)
        self.word_list.setGeometry(QtCore.QRect(10, 110, 251, 111))
        self.word_list.setObjectName("word_list")
        self.url_list = QtWidgets.QTextEdit(self.centralwidget)
        self.url_list.setGeometry(QtCore.QRect(420, 110, 381, 111))
        self.url_list.setObjectName("url_list")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 80, 60, 16))
        self.label_2.setObjectName("label_2")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(5, 291, 801, 301))
        self.result.setObjectName("result")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 260, 60, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.close_button.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "Word list"))
        self.label_2.setText(_translate("MainWindow", "URL list"))
        self.label_3.setText(_translate("MainWindow", "OUTPUT"))

