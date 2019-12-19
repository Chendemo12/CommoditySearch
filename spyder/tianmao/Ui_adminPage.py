# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lichenguang/Documents/GitHub/CommoditySearch/spyder/tianmao/adminPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1250, 950)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.updatedatabaseButon = QtWidgets.QPushButton(self.centralwidget)
        self.updatedatabaseButon.setGeometry(QtCore.QRect(330, 780, 176, 59))
        self.updatedatabaseButon.setObjectName("updatedatabaseButon")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(720, 780, 176, 59))
        self.exitButton.setObjectName("exitButton")
        self.employee_table_label = QtWidgets.QLabel(self.centralwidget)
        self.employee_table_label.setGeometry(QtCore.QRect(60, 40, 130, 43))
        self.employee_table_label.setObjectName("employee_table_label")
        self.work_table_label = QtWidgets.QLabel(self.centralwidget)
        self.work_table_label.setGeometry(QtCore.QRect(60, 350, 130, 43))
        self.work_table_label.setObjectName("work_table_label")
        self.employee_info_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.employee_info_textBrowser.setGeometry(QtCore.QRect(40, 90, 1170, 192))
        self.employee_info_textBrowser.setObjectName("employee_info_textBrowser")
        self.work_info_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.work_info_textBrowser.setGeometry(QtCore.QRect(40, 420, 1170, 301))
        self.work_info_textBrowser.setObjectName("work_info_textBrowser")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 51))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "系统管理界面"))
        self.updatedatabaseButon.setText(_translate("mainWindow", "更新数据库"))
        self.exitButton.setText(_translate("mainWindow", "退出应用"))
        self.employee_table_label.setText(_translate("mainWindow", "员工表"))
        self.work_table_label.setText(_translate("mainWindow", "工作表"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
