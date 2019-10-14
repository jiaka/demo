# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zouyo\Desktop\PyQt5源码\myproject\mianwindown.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1071, 778)
        self.stackedWidget_main = QtWidgets.QStackedWidget(Form)
        self.stackedWidget_main.setGeometry(QtCore.QRect(10, 10, 1061, 741))
        self.stackedWidget_main.setStyleSheet("background-color:rgb(246, 244, 236);")
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.stackedWidget_mainPage1 = QtWidgets.QWidget()
        self.stackedWidget_mainPage1.setObjectName("stackedWidget_mainPage1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.stackedWidget_mainPage1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 141, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet(" QPushButton {\n"
"border-color: rgb(170, 170, 255);\n"
"}\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_music = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 244, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_music.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_music.setFont(font)
        self.pushButton_music.setStyleSheet(" QPushButton {\n"
"border:None;\n"
"}")
        self.pushButton_music.setObjectName("pushButton_music")
        self.verticalLayout.addWidget(self.pushButton_music)
        self.pushButton_tools = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_tools.setFont(font)
        self.pushButton_tools.setStyleSheet(" QPushButton {\n"
"border:None;\n"
"}")
        self.pushButton_tools.setObjectName("pushButton_tools")
        self.verticalLayout.addWidget(self.pushButton_tools)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.stackedWidget_mainPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 50, 921, 691))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.gridLayoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 921, 51))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_9.addWidget(self.pushButton_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_9.addWidget(self.lineEdit_5)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_9.addWidget(self.pushButton_5)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tabWidget1 = QtWidgets.QTabWidget(self.page_2)
        self.tabWidget1.setGeometry(QtCore.QRect(0, 0, 921, 691))
        font = QtGui.QFont()
        font.setFamily("汉仪曹隶繁")
        font.setPointSize(11)
        self.tabWidget1.setFont(font)
        self.tabWidget1.setStyleSheet("QTabWidget::pane{\n"
"    border:none;\n"
"}\n"
"QTabWidget::tab-bar{\n"
"   alignment:left;\n"
"}\n"
"QTabBar::tab{\n"
"    background:transparent;\n"
"    \n"
"    color: rgb(255, 119, 121);\n"
"    min-width:30ex;\n"
"    min-height:10ex;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    background:rgb(255, 255, 255, 100);\n"
"}\n"
"QTabBar::tab:selected{\n"
"    border-color: white;\n"
"    background:white;\n"
"    color:green;\n"
"}\n"
"")
        self.tabWidget1.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget1.setObjectName("tabWidget1")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.tab_4.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.tab_4.setObjectName("tab_4")
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("\n"
" \n"
"QComboBox::down-arrow {\n"
"    border-image: url(:/combox1/1225446.png);\n"
"     \n"
"}\n"
"QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"        color: rgb(170, 170, 127);\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(84, 84, 84);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QComboBox:enabled:hover, QComboBox:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QComboBox::drop-down {\n"
"        width: 20px;\n"
"        border: none;\n"
"        background: transparent;\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"        /**top: 1px;**/\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"        outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"        height: 25px;\n"
"        color: rgb(73, 73, 73);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"        background: rgb(232, 241, 250);\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 0, 88, 41))
        self.pushButton_3.setMinimumSize(QtCore.QSize(88, 41))
        self.pushButton_3.setMaximumSize(QtCore.QSize(88, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(" QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(170, 170, 127);\n"
"  border-radius:5px;\n"
"}\n"
" QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 234, 171);\n"
"    color: rgb(0, 170, 0);\n"
"  }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 50, 461, 571))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_3.setGeometry(QtCore.QRect(470, 50, 451, 571))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget1.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 921, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_8 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout_2.addWidget(self.radioButton_8)
        self.radioButton_10 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout_2.addWidget(self.radioButton_10)
        self.radioButton_16 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setObjectName("radioButton_16")
        self.horizontalLayout_2.addWidget(self.radioButton_16)
        self.radioButton_32 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton_32.setFont(font)
        self.radioButton_32.setObjectName("radioButton_32")
        self.horizontalLayout_2.addWidget(self.radioButton_32)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 80, 921, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(26, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 500, 31))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(126, 255, 141);\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 130, 921, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout_4.addWidget(self.radioButton2)
        self.radioButton4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton4.setFont(font)
        self.radioButton4.setObjectName("radioButton4")
        self.horizontalLayout_4.addWidget(self.radioButton4)
        self.radioButton8 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton8.setFont(font)
        self.radioButton8.setObjectName("radioButton8")
        self.horizontalLayout_4.addWidget(self.radioButton8)
        self.radioButton10 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton10.setFont(font)
        self.radioButton10.setObjectName("radioButton10")
        self.horizontalLayout_4.addWidget(self.radioButton10)
        self.radioButton16 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton16.setFont(font)
        self.radioButton16.setObjectName("radioButton16")
        self.horizontalLayout_4.addWidget(self.radioButton16)
        self.radioButton32 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(10)
        self.radioButton32.setFont(font)
        self.radioButton32.setObjectName("radioButton32")
        self.horizontalLayout_4.addWidget(self.radioButton32)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(" QPushButton {\n"
"  border:none;\n"
"  border-radius:5px;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 170, 921, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(26, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 220, 211, 41))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 260, 921, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_baidu = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_baidu.setMinimumSize(QtCore.QSize(26, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.lineEdit_baidu.setFont(font)
        self.lineEdit_baidu.setObjectName("lineEdit_baidu")
        self.horizontalLayout_6.addWidget(self.lineEdit_baidu)
        self.pushButton_baidu = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_baidu.setMinimumSize(QtCore.QSize(96, 42))
        self.pushButton_baidu.setMaximumSize(QtCore.QSize(105, 42))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_baidu.setFont(font)
        self.pushButton_baidu.setStyleSheet(" QPushButton {\n"
"  border:none;\n"
"  border-radius:5px;\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(255, 244, 158);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 234, 171);\n"
"    color: rgb(0, 170, 0);\n"
"  }")
        self.pushButton_baidu.setObjectName("pushButton_baidu")
        self.horizontalLayout_6.addWidget(self.pushButton_baidu)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 310, 921, 171))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-color:rgb(246, 244, 236);")
        self.textEdit.setObjectName("textEdit")
        self.tabWidget1.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 921, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 163, 151);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 50, 921, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_8.setMinimumSize(QtCore.QSize(70, 0))
        self.label_8.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 163, 151);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(26, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.pushButton_downmd = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_downmd.setMinimumSize(QtCore.QSize(96, 42))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.pushButton_downmd.setFont(font)
        self.pushButton_downmd.setStyleSheet(" QPushButton {\n"
"color: rgb(255, 163, 151);\n"
"  border:none;\n"
"  border-radius:5px;\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(255, 244, 158);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 234, 171);\n"
"    color: rgb(0, 170, 0);\n"
"  }")
        self.pushButton_downmd.setObjectName("pushButton_downmd")
        self.horizontalLayout_7.addWidget(self.pushButton_downmd)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(0, 100, 921, 41))
        self.label_9.setObjectName("label_9")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 150, 921, 81))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_8.addWidget(self.lineEdit_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_8.addWidget(self.pushButton_7)
        self.tabWidget1.addTab(self.widget, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(0, 30, 921, 46))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 163, 151);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.lineEdit_quanmin = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_quanmin.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_quanmin.setFont(font)
        self.lineEdit_quanmin.setObjectName("lineEdit_quanmin")
        self.horizontalLayout_10.addWidget(self.lineEdit_quanmin)
        self.pushButton_quanmin = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.pushButton_quanmin.setMinimumSize(QtCore.QSize(96, 42))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pushButton_quanmin.setFont(font)
        self.pushButton_quanmin.setStyleSheet(" QPushButton {\n"
"color: rgb(255, 163, 151);\n"
"  border:none;\n"
"  border-radius:5px;\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(255, 244, 158);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 234, 171);\n"
"    color: rgb(0, 170, 0);\n"
"  }")
        self.pushButton_quanmin.setObjectName("pushButton_quanmin")
        self.horizontalLayout_10.addWidget(self.pushButton_quanmin)
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(0, -6, 291, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 163, 151);")
        self.label_12.setObjectName("label_12")
        self.tabWidget1.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget1.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.stackedWidget_mainPage1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 0, 921, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("汉仪唐隶繁")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("\n"
"color:green;")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.pushButton_max = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_max.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButton_max.setMaximumSize(QtCore.QSize(42, 42))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.pushButton_max.setFont(font)
        self.pushButton_max.setMouseTracking(False)
        self.pushButton_max.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"  border-radius:5px;\n"
"    color: rgb(254, 255, 165);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"background-color: rgb(133, 139, 255);\n"
"\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"background-color: rgb(188, 189, 255);\n"
"\n"
"  }\n"
"")
        self.pushButton_max.setText("")
        self.pushButton_max.setObjectName("pushButton_max")
        self.horizontalLayout.addWidget(self.pushButton_max)
        self.pushButton_min = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_min.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButton_min.setMaximumSize(QtCore.QSize(42, 42))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_min.setFont(font)
        self.pushButton_min.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(172, 255, 153);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"\n"
"    background-color: rgb(115, 255, 120);\n"
"    \n"
"\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    background-color: rgb(182, 255, 155);\n"
"    \n"
"  }\n"
"\n"
"")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout.addWidget(self.pushButton_min)
        self.pushButton_quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_quit.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButton_quit.setMaximumSize(QtCore.QSize(42, 42))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(16)
        self.pushButton_quit.setFont(font)
        self.pushButton_quit.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"    color: rgb(0, 170, 0);\n"
"      border-radius:5px;\n"
"    \n"
"    \n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"    background-color: rgb(255, 34, 34);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    background-color: rgb(255, 99, 94);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout.addWidget(self.pushButton_quit)
        self.stackedWidget_main.addWidget(self.stackedWidget_mainPage1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_main.addWidget(self.page_3)

        self.retranslateUi(Form)
        self.stackedWidget_main.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget1.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_music.setText(_translate("Form", "音乐"))
        self.pushButton_tools.setText(_translate("Form", "实用工具"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.tabWidget1.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "英文 » 中文"))
        self.comboBox.setItemText(1, _translate("Form", "中文 » 英文 "))
        self.pushButton_3.setText(_translate("Form", "翻译"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:16pt;\">请输入翻译的文本</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_4), _translate("Form", "英汉翻译"))
        self.radioButton_2.setText(_translate("Form", "2进制"))
        self.radioButton_4.setText(_translate("Form", "4进制"))
        self.radioButton_8.setText(_translate("Form", "8进制"))
        self.radioButton_10.setText(_translate("Form", "10进制"))
        self.radioButton_16.setText(_translate("Form", "16进制"))
        self.radioButton_32.setText(_translate("Form", "32进制"))
        self.label.setText(_translate("Form", "转换数字："))
        self.label_2.setText(_translate("Form", "支持在2~36进制之间进行任意转换，支持浮点型"))
        self.radioButton2.setText(_translate("Form", "2进制"))
        self.radioButton4.setText(_translate("Form", "4进制"))
        self.radioButton8.setText(_translate("Form", "8进制"))
        self.radioButton10.setText(_translate("Form", "10进制"))
        self.radioButton16.setText(_translate("Form", "16进制"))
        self.radioButton32.setText(_translate("Form", "32进制"))
        self.label_4.setText(_translate("Form", "转换结果："))
        self.label_5.setText(_translate("Form", "百度文库免费下载"))
        self.label_6.setText(_translate("Form", "输入链接："))
        self.pushButton_baidu.setText(_translate("Form", "提取"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab), _translate("Form", "进制转换"))
        self.label_7.setText(_translate("Form", "网页转md"))
        self.label_8.setText(_translate("Form", "链接："))
        self.pushButton_downmd.setText(_translate("Form", "下载"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.label_10.setText(_translate("Form", "TextLabel"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.widget), _translate("Form", "网页转换"))
        self.label_11.setText(_translate("Form", "输入链接："))
        self.pushButton_quanmin.setText(_translate("Form", "下载"))
        self.label_12.setText(_translate("Form", "全民K歌音乐外链提取工具"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_5), _translate("Form", "资源下载"))
        self.label_title.setText(_translate("Form", "邹永佳的小工具"))
        self.pushButton_quit.setText(_translate("Form", "X"))
import k1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
