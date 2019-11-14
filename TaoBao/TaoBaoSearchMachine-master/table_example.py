# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_example.ui'
#
# Created: Tue Aug 08 17:25:48 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(634, 857)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.itemInput = QtGui.QLineEdit(Dialog)
        self.itemInput.setObjectName(_fromUtf8("itemInput"))
        self.horizontalLayout_2.addWidget(self.itemInput)
        self.confirm = QtGui.QPushButton(Dialog)
        self.confirm.setObjectName(_fromUtf8("confirm"))
        self.horizontalLayout_2.addWidget(self.confirm)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.getData = QtGui.QPushButton(Dialog)
        self.getData.setObjectName(_fromUtf8("getData"))
        self.horizontalLayout.addWidget(self.getData)
        self.Plot = QtGui.QPushButton(Dialog)
        self.Plot.setObjectName(_fromUtf8("Plot"))
        self.horizontalLayout.addWidget(self.Plot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Item", None))
        self.confirm.setText(_translate("Dialog", "Confirm", None))
        self.getData.setText(_translate("Dialog", "Get Data", None))
        self.Plot.setText(_translate("Dialog", "Plot", None))

