#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic

class MyDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        uic.loadUi("res.ui",self)

class MyWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('PyQt')
        self.resize(300,200)
        gridlayout = QtGui.QGridLayout()
        self.button = QtGui.QPushButton('CreateDialog')
        gridlayout.addWidget(self.button,1 ,1)
        self.setLayout(gridlayout)
        self.connect(self.button, QtCore.SIGNAL('clicked()'),
                     self.OnButton)

    def OnButton(self):
        dialog = MyDialog()
        r = dialog.exec_()
        if r:
            self.button.setText(dialog.lineEdit.text())

app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
