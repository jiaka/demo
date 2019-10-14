# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zouyo\Desktop\PyQt5源码\word\mian.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 534)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 431, 531))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.widget.setObjectName("widget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 70, 431, 461))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 60, 431, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setStyleSheet("background-color: rgb(83, 145, 168);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(110, 120, 321, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(202, 214, 226);\n"
"\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_10 = QtWidgets.QPushButton(self.page)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.pushButton_10.setMinimumSize(QtCore.QSize(64, 0))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 30, 111, 31))
        self.pushButton_11.setMinimumSize(QtCore.QSize(86, 0))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(0, 180, 431, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(83, 145, 168);")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.page)
        self.pushButton_12.setGeometry(QtCore.QRect(110, 0, 61, 31))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.page)
        self.pushButton_13.setGeometry(QtCore.QRect(110, 30, 61, 31))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setGeometry(QtCore.QRect(0, 220, 431, 241))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QTextBrowser{border-width:0;border-style:outset;background-color: rgb(202, 214, 226);}\n"
"\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 120, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("\n"
"QTextBrowser{border-width:0;border-style:outset;background-color: rgb(150, 141, 125);\n"
"color: rgb(255, 255, 255);}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.page)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_15 = QtWidgets.QPushButton(self.page)
        self.pushButton_15.setGeometry(QtCore.QRect(170, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.page)
        self.pushButton_16.setGeometry(QtCore.QRect(240, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.page)
        self.pushButton_17.setGeometry(QtCore.QRect(240, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.page)
        self.pushButton_18.setGeometry(QtCore.QRect(170, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.page)
        self.pushButton_19.setGeometry(QtCore.QRect(370, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.page)
        self.pushButton_20.setGeometry(QtCore.QRect(300, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.page)
        self.pushButton_21.setGeometry(QtCore.QRect(300, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"background-color: rgb(83, 145, 168);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(171, 154, 156);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(171, 154, 156);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_21.setObjectName("pushButton_21")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setMinimumSize(QtCore.QSize(32, 55))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.comboBox = QtWidgets.QComboBox(self.page_4)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 111, 31))
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 0, 75, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 0, 71, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(0, 30, 61, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 30, 91, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_25.setGeometry(QtCore.QRect(390, 30, 41, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(220, 30, 91, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 30, 71, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 30, 51, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(0, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" \n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color:rgb(150, 141, 125);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(83, 145, 168);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(83, 145, 168);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 40, 75, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(" \n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color:rgb(150, 141, 125);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(83, 145, 168);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(83, 145, 168);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 40, 81, 31))
        self.pushButton_3.setStyleSheet(" \n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color:rgb(150, 141, 125);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(83, 145, 168);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(83, 145, 168);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 40, 81, 31))
        self.pushButton_4.setStyleSheet(" \n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color:rgb(150, 141, 125);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(83, 145, 168);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(83, 145, 168);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(" \n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color:rgb(150, 141, 125);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(83, 145, 168);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(83, 145, 168);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 351, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:  rgb(150, 141, 125);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_22 = QtWidgets.QPushButton(self.widget)
        self.pushButton_22.setGeometry(QtCore.QRect(350, 0, 41, 41))
        self.pushButton_22.setStyleSheet(" \n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color:rgb(150, 141, 125);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(83, 145, 168);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(83, 145, 168);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget)
        self.pushButton_23.setGeometry(QtCore.QRect(390, 0, 41, 41))
        self.pushButton_23.setStyleSheet("QPushButton {\n"
"      border:none;\n"
"      background-color: rgb(255, 99, 94);\n"
"\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"    background-color: rgb(255, 34, 34);\n"
"\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"      background-color: rgb(255, 165, 158);\n"
"\n"
"  }\n"
"")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.widget)
        self.pushButton_24.setGeometry(QtCore.QRect(380, 40, 51, 31))
        self.pushButton_24.setStyleSheet(" \n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"  border:none;\n"
"\n"
"background-color:rgb(150, 141, 125);\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: rgb(83, 145, 168);\n"
"    color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(83, 145, 168);\n"
"\n"
"    color:  rgb(202, 214, 226);\n"
"  }")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_23.clicked.connect(self.pushButton_23.close)
        self.pushButton_22.clicked.connect(Form.showMinimized)
        self.pushButton_23.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton_10.setText(_translate("Form", "顺序检查"))
        self.pushButton_11.setText(_translate("Form", "随机检查"))
        self.pushButton_8.setText(_translate("Form", "上一个"))
        self.pushButton_15.setText(_translate("Form", "同近义词"))
        self.pushButton_16.setText(_translate("Form", "例句"))
        self.pushButton_17.setText(_translate("Form", "同根词"))
        self.pushButton_18.setText(_translate("Form", "词语辨析"))
        self.pushButton_19.setText(_translate("Form", "跳过"))
        self.pushButton_20.setText(_translate("Form", "英英释义"))
        self.pushButton_21.setText(_translate("Form", "标准释义"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.radioButton_3.setText(_translate("Form", "RadioButton"))
        self.radioButton_4.setText(_translate("Form", "RadioButton"))
        self.pushButton_14.setText(_translate("Form", "下一个"))
        self.comboBox.setItemText(0, _translate("Form", "考研词汇"))
        self.comboBox.setItemText(1, _translate("Form", "复习词汇"))
        self.comboBox.setItemText(2, _translate("Form", "四级词汇"))
        self.comboBox.setItemText(3, _translate("Form", "六级词汇"))
        self.pushButton_6.setText(_translate("Form", "选择文件夹"))
        self.label_2.setText(_translate("Form", "导入资源"))
        self.pushButton_7.setText(_translate("Form", "导入"))
        self.label_6.setText(_translate("Form", "选择进度"))
        self.pushButton_25.setText(_translate("Form", "确定"))
        self.label_7.setText(_translate("Form", "单词开始位置"))
        self.pushButton_9.setText(_translate("Form", "确定"))
        self.pushButton.setText(_translate("Form", "拼写检查"))
        self.pushButton_2.setText(_translate("Form", "英文选意"))
        self.pushButton_5.setText(_translate("Form", "设置"))
        self.label_5.setText(_translate("Form", "可爱背单词"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
