# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_wlq.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 469)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("素材/伍六七.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(150, 20, 300, 420))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("素材/伍六七.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 211, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(0)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setPixmap(QtGui.QPixmap("素材/星球.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(50, 120, 161, 101))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setMouseTracking(False)
        self.textEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.textEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.closeui = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("关  闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeui.setIcon(icon1)
        self.closeui.setObjectName("closeui")
        self.ontop = QtWidgets.QAction(MainWindow)
        self.ontop.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("固定.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ontop.setIcon(icon2)
        self.ontop.setObjectName("ontop")
        self.set = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set.setIcon(icon3)
        self.set.setObjectName("set")

        self.retranslateUi(MainWindow)
        self.closeui.triggered['bool'].connect(MainWindow.close)
        self.ontop.triggered['bool'].connect(MainWindow.WinOnTop)
        self.set.triggered.connect(MainWindow.SetPattern)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "刺客伍六七"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文新魏\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   此后如竟没有炬火，我便是唯一的光。</p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "这里可以填写备忘的哦"))
        self.closeui.setText(_translate("MainWindow", "关闭"))
        self.closeui.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.ontop.setText(_translate("MainWindow", "置顶"))
        self.set.setText(_translate("MainWindow", "设置"))
        self.set.setShortcut(_translate("MainWindow", "Ctrl+2"))
