# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 284)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtWidgets.QTabWidget(Dialog)
        self.tabs.setObjectName("tabs")
        self.driver_tab = QtWidgets.QWidget()
        self.driver_tab.setObjectName("driver_tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.driver_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.driver_tab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.driver_path = QtWidgets.QLineEdit(self.driver_tab)
        self.driver_path.setObjectName("driver_path")
        self.horizontalLayout_2.addWidget(self.driver_path)
        self.tabs.addTab(self.driver_tab, "")
        self.files_tab = QtWidgets.QWidget()
        self.files_tab.setObjectName("files_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.files_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.files_tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.image_output_path = QtWidgets.QLineEdit(self.files_tab)
        self.image_output_path.setObjectName("image_output_path")
        self.horizontalLayout_4.addWidget(self.image_output_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.files_tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.text_output_path = QtWidgets.QLineEdit(self.files_tab)
        self.text_output_path.setObjectName("text_output_path")
        self.horizontalLayout_3.addWidget(self.text_output_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabs.addTab(self.files_tab, "")
        self.verticalLayout.addWidget(self.tabs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_button = QtWidgets.QPushButton(Dialog)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Driver path"))
        self.tabs.setTabText(self.tabs.indexOf(self.driver_tab), _translate("Dialog", "Drver"))
        self.label_2.setText(_translate("Dialog", "Images output"))
        self.label_3.setText(_translate("Dialog", "Text output"))
        self.tabs.setTabText(self.tabs.indexOf(self.files_tab), _translate("Dialog", "Files"))
        self.save_button.setText(_translate("Dialog", "Save"))
        self.close_button.setText(_translate("Dialog", "Close"))

