# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNew.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(110, 280, 180, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_save.setIcon(icon1)
        self.btn_save.setObjectName("btn_save")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 291, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_version = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_version.setObjectName("line_version")
        self.gridLayout.addWidget(self.line_version, 4, 2, 1, 2)
        self.line_suffix = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_suffix.setObjectName("line_suffix")
        self.gridLayout.addWidget(self.line_suffix, 5, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.line_keyword = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_keyword.setObjectName("line_keyword")
        self.gridLayout.addWidget(self.line_keyword, 0, 2, 1, 2)
        self.line_region = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_region.setObjectName("line_region")
        self.gridLayout.addWidget(self.line_region, 1, 2, 1, 2)
        self.line_standard = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_standard.setObjectName("line_standard")
        self.gridLayout.addWidget(self.line_standard, 3, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 2)
        self.line_type = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_type.setObjectName("line_type")
        self.gridLayout.addWidget(self.line_type, 2, 2, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 3)
        self.gridLayout.setColumnStretch(3, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.line_keyword, self.line_region)
        Dialog.setTabOrder(self.line_region, self.line_type)
        Dialog.setTabOrder(self.line_type, self.line_standard)
        Dialog.setTabOrder(self.line_standard, self.line_version)
        Dialog.setTabOrder(self.line_version, self.line_suffix)
        Dialog.setTabOrder(self.line_suffix, self.btn_save)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add  keywords"))
        self.btn_save.setText(_translate("Dialog", "Save"))
        self.label_5.setText(_translate("Dialog", "Version"))
        self.label.setText(_translate("Dialog", "Keyword"))
        self.label_3.setText(_translate("Dialog", "Type"))
        self.label_4.setText(_translate("Dialog", "Standard"))
        self.label_2.setText(_translate("Dialog", "Region"))
        self.label_6.setText(_translate("Dialog", "Suffix"))