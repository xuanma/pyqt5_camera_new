# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(266, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 101))
        self.groupBox.setObjectName("groupBox")
        
        self.open_cameras = QtWidgets.QPushButton(self.groupBox)
        self.open_cameras.setGeometry(QtCore.QRect(10, 20, 110, 31))
        self.open_cameras.setObjectName("open_cameras")
        
        self.release_cameras = QtWidgets.QPushButton(self.groupBox)
        self.release_cameras.setGeometry(QtCore.QRect(124, 20, 110, 31))
        self.release_cameras.setObjectName("release_cameras")
        
        self.close_preview = QtWidgets.QPushButton(self.groupBox)
        self.close_preview.setGeometry(QtCore.QRect(10, 60, 110, 31))
        self.close_preview.setObjectName("close_preview")
        
        self.open_preview = QtWidgets.QPushButton(self.groupBox)
        self.open_preview.setGeometry(QtCore.QRect(124, 60, 110, 31))
        self.open_preview.setObjectName("open_preview")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 241, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Label_savepath = QtWidgets.QLabel(self.groupBox_2)
        self.Label_savepath.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.Label_savepath.setText("")
        self.Label_savepath.setObjectName("Label_savepath")
        self.Edit_filename = QtWidgets.QLineEdit(self.groupBox_2)
        self.Edit_filename.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.Edit_filename.setText("")
        self.Edit_filename.setObjectName("Edit_filename")
        self.Button_filename = QtWidgets.QPushButton(self.groupBox_2)
        self.Button_filename.setGeometry(QtCore.QRect(160, 30, 71, 31))
        self.Button_filename.setObjectName("Button_filename")
        self.Button_savepath = QtWidgets.QPushButton(self.groupBox_2)
        self.Button_savepath.setGeometry(QtCore.QRect(160, 70, 71, 28))
        self.Button_savepath.setObjectName("Button_savepath")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 240, 231, 121))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Button_recording = QtWidgets.QPushButton(self.tab)
        self.Button_recording.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.Button_recording.setText("")
        self.Button_recording.setIcon(QtGui.QIcon("start.png"))
        self.Button_recording.setObjectName("Button_recording")
        self.Button_endrecording = QtWidgets.QPushButton(self.tab)
        self.Button_endrecording.setGeometry(QtCore.QRect(120, 10, 101, 31))
        self.Button_endrecording.setText("")
        self.Button_endrecording.setIcon(QtGui.QIcon("stop.png"))
        self.Button_endrecording.setObjectName("Button_endrecording")
        self.Label_mrecordingtime = QtWidgets.QLabel(self.tab)
        self.Label_mrecordingtime.setGeometry(QtCore.QRect(10, 50, 211, 21))
        self.Label_mrecordingtime.setText("")
        self.Label_mrecordingtime.setObjectName("Label_mrecordingtime")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Button_trigger = QtWidgets.QPushButton(self.tab_2)
        self.Button_trigger.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.Button_trigger.setObjectName("Button_trigger")
        self.Button_canceltrigger = QtWidgets.QPushButton(self.tab_2)
        self.Button_canceltrigger.setGeometry(QtCore.QRect(120, 10, 101, 31))
        self.Button_canceltrigger.setObjectName("Button_canceltrigger")
        self.Label_trecordingtime = QtWidgets.QLabel(self.tab_2)
        self.Label_trecordingtime.setGeometry(QtCore.QRect(10, 50, 211, 21))
        self.Label_trecordingtime.setText("")
        self.Label_trecordingtime.setObjectName("Label_trecordingtime")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 266, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LimbLab"))
        MainWindow.setWindowIcon(QtGui.QIcon("main_program.ico"))
        self.groupBox.setTitle(_translate("MainWindow", "Cameras"))
        self.open_cameras.setText(_translate("MainWindow", "Open cameras"))
        self.release_cameras.setText(_translate("MainWindow", "Release cameras"))
        self.close_preview.setText(_translate("MainWindow", "Close preview"))
        self.open_preview.setText(_translate("MainWindow", "Open preview"))
        self.groupBox_2.setTitle(_translate("MainWindow", "File recordings"))
        self.Button_filename.setText(_translate("MainWindow", "Set name"))
        self.Button_savepath.setText(_translate("MainWindow", "Set path"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Manual"))
        self.Button_trigger.setText(_translate("MainWindow", "Trigger"))
        self.Button_canceltrigger.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Trigger"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
