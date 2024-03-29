# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day15.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 941, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 937, 527))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_img = QtWidgets.QLabel()
        self.label_img.setGeometry(QtCore.QRect(0, 0, 941, 521))
        self.label_img.setObjectName("label_img")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.label_img)
        self.verticalLayout.addWidget(self.scrollArea)
        self.btn_zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_in.setGeometry(QtCore.QRect(190, 600, 89, 25))
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.label_img_shape = QtWidgets.QLabel(self.centralwidget)
        self.label_img_shape.setGeometry(QtCore.QRect(650, 660, 641, 21))
        self.label_img_shape.setObjectName("label_img_shape")
        self.btn_open_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_file.setGeometry(QtCore.QRect(60, 600, 89, 25))
        self.btn_open_file.setObjectName("btn_open_file")
        self.label_file_name = QtWidgets.QLabel(self.centralwidget)
        self.label_file_name.setGeometry(QtCore.QRect(40, 910, 941, 31))
        self.label_file_name.setObjectName("label_file_name")
        self.slider_zoom = QtWidgets.QSlider(self.centralwidget)
        self.slider_zoom.setGeometry(QtCore.QRect(290, 600, 231, 21))
        self.slider_zoom.setProperty("value", 50)
        self.slider_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.slider_zoom.setObjectName("slider_zoom")
        self.label_ratio = QtWidgets.QLabel(self.centralwidget)
        self.label_ratio.setGeometry(QtCore.QRect(650, 600, 641, 21))
        self.label_ratio.setObjectName("label_ratio")
        self.btn_zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_out.setGeometry(QtCore.QRect(540, 600, 89, 25))
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_img.setText(_translate("MainWindow", "label_img"))
        self.btn_zoom_in.setText(_translate("MainWindow", "zoom in"))
        self.label_img_shape.setText(_translate("MainWindow", "Current image shape: (0,0), Origin image shape: (0,0)"))
        self.btn_open_file.setText(_translate("MainWindow", "Open file"))
        self.label_file_name.setText(_translate("MainWindow", "file name:"))
        self.label_ratio.setText(_translate("MainWindow", "ratio: 100%"))
        self.btn_zoom_out.setText(_translate("MainWindow", "zoom out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
