
from PyQt5.QtCore import pyqtSlot, QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from os import listdir, remove
from os.path import exists
from Ui_mian import Ui_Form
from requests import get
from random import sample, randint
import requests
import re
from lxml import html
from html.parser import HTMLParser
from html import unescape
from playsound import playsound
from PyQt5.QtGui import QCursor,QColor, QIntValidator

class Form(QWidget, Ui_Form):
    """
        程序开始运行，初始化参数
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_3.setValidator(QIntValidator())
        self.lineEdit_2.setValidator(QIntValidator())
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.file = "C:\\Users\\zouyo\\Desktop\\word"
        self.dict = {}
        self.initi()
        with open("./words.txt", "r") as fp:
            self.words = eval(fp.read())
        
    
    def initi(self):
        """
            打开保存在本地的配置信息，并将这些配置信息加载到程序中
            
        """
        # 如果存在配置文件则加载配置文件，否则重置配置
        if exists("./dicts.txt"):
            with open(r"C:\Users\zouyo\Desktop\Data\dicts.txt",  "r") as fp:
                self.dict = eval(fp.read())
        else:
            self.dict = {
                "num": 0,               # 英文选意的单词位置
                "days": 1,                 # 英文选意的天数
                "w2": 0,                 # 英文选意单词位置
                "days_1": 1,            # 拼写检查天数
                "w2_1": 0,              # 拼写检查单词位置
                "net": 1,              # 检查网络的标志，设置是否打开网络模式
                "net_is_ok": 0,     # 检查是否已经下载好了数据
                "word": ""            # 记录单词，避免不必要的重复读取，此处需要改进
            }
        self.word , self.len= self.get_words(self.dict["days_1"])
        self.dict["word"] = self.word[self.dict["w2_1"]][0]
        self.dict["net_is_ok"] = 0
    
    def collect(self,  word=0,  day = -1):
        """
        word ：不为0时则获取每一个文件的单词数
        day : 获取具体一天的单词数量
        返回文件个数和每个文件包含的单词个数 
        word和daybu
        """
        dirs = listdir(self.file)
        counts = []
        if word != 0:
            for dir in dirs:
                file_dir = self.file + "\\" + dir
                with open(file_dir, "r") as fp:
                    count = 0
                    for line in fp.readlines():
                        count = count + 1
                counts.append(count)
        elif day != -1:
            file_dir = self.file + "\\" + dirs[day]
            with open(file_dir, "r") as fp:
                count = 0
                for line in fp.readlines():
                    count = count + 1
                counts.append(count)
        return len(dirs), counts
        
    # 每答对一个单词调用此函数，单词位置加一，每加一需要更新资料，这里获取总的资料
    def get_word_info(self, word):
        if self.dict["net"] == 1:
            url1 = "http://dict.youdao.com/search?q={}&keyfrom=new-fanyi.smartResult".format(word)
            try:
                response = requests.get(url1)
                # print(repose.text)
                with open(r"C:\Users\zouyo\Desktop\Data\data.txt", "w", encoding='utf-8') as fp:
                    fp.write(response.text)
                self.dict["net_is_ok"] = 1
            except:
                self.dict["net_is_ok"] = 0
                # 这里调用一个弹窗函数，显示是哪里出错了#############################
                
        else:
            self.dict["net_is_ok"] = 0
            
    
    def refer(self, n):
        #try:
        with open(r"C:\Users\zouyo\Desktop\Data\data.txt", "r", encoding='utf-8') as fp:
            a = fp.read()
        tree = html.fromstring(a)
        if n == 1:
            # 同近义词
            try:
                self.textBrowser.document().clear()
                name = tree.xpath(r"//div[@id='synonyms']")
                name = html.tostring(name[0])
                name = unescape(name.decode())
                self.textBrowser.append(name)
            except:
                self.textBrowser.append("没有找到同近义词！！！")
        elif n == 2:
            # 词语辨析
            try:
                self.textBrowser.document().clear()
                name = tree.xpath(r"//div[@id='discriminate']")
                name = html.tostring(name[0])
                name = unescape(name.decode())
                self.textBrowser.append(name)
            except:
                self.textBrowser.append("没有找到词语辨析！！！")
        elif n == 3:
            # 例句
            try:
                self.textBrowser.document().clear()
                word_liju,  l = self.get_words(self.dict["days"])
                if self.dict["net"] == 1:
                    url1 = "http://dict.youdao.com/example/blng/eng/{}/".format(word_liju[self.dict["w2_1"]][0])
                    try:
                        response = requests.get(url1)
                    except:
                        # 这里调用一个弹窗函数，显示是哪里出错了#############################
                        pass
                else:
                    return
                tree = html.fromstring(response.text)
                name = tree.xpath(r"//ul[@class='ol']")
                name = html.tostring(name[0])
                name = unescape(name.decode())
                self.textBrowser.append(name)
            except:
                self.textBrowser.append("没有找到例句或者检查网络！！！")
        elif n == 4:
            # 同根词
            try:
                self.textBrowser.document().clear()
                name = tree.xpath(r"//div[@id='relWordTab']")
                name = html.tostring(name[0])
                name = unescape(name.decode())
                self.textBrowser.append(name)
            except:
                self.textBrowser.append("没有找到同根词！！！")
        elif n == 5:
            # 英英
            try:
                self.textBrowser.document().clear()
                name = tree.xpath(r"//div[@id='tEETrans']/div[@class='trans-container']")
                name = html.tostring(name[0])
                name = unescape(name.decode())
                self.textBrowser.append(name)
            except:
                self.textBrowser.append("没有找到英英释义！！！")
        elif n == 6:
            # 标准释义
            try:
                self.textBrowser.document().clear()
                name = tree.xpath(r"//div[@id='phrsListTab']/div[@class='trans-container']")
                name = html.tostring(name[0])
                name = unescape(name.decode())
                self.textBrowser.append(name)
            except:
                self.textBrowser.append("标准释义都没有那就是哪里出错了！！！")
        #except:
            # 这里调用一个弹窗函数，显示是哪里出错了#############################
          #  pass
        
    def box(self, e): # 消息：警告
        reply = QMessageBox.warning(self,
                                    "警告",  
                                    e,  
                                    QMessageBox.Yes)
                        
    def get_words(self,  n):
        word=[]
        self.word = []
        with open(self.file + '\\' + str(n) + ".txt",  "r") as fp:
            x = fp.readlines()
            for k in range(len(x)):
                x1 = x[k][:-1]
                y = x1.split("-")
                word.append(y)
        self.word=word
        self.len = len(word)
        return word,  len(word)
    
    def textborwer(self, word, word_mean):  
        self.textBrowser_2.document().clear()
        self.textBrowser_2.append(word)
        self.textBrowser_2.append(word_mean)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.stackedWidget.setCurrentWidget(self.page)
#        word_days_1,  l = self.get_words(self.dict["days"])
        self.label.setText(self.word[self.dict["w2_1"]][1])
        if self.dict["w2_1"] - 1 >= 0 : 
            self.textborwer(self.word[self.dict["w2_1"]-1][0], self.word[self.dict["w2_1"]-1][1])
        
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        day_len, _ = self.collect()
        self.lineEdit_2.setPlaceholderText("0~{}".format(day_len-1))
        
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.set_radio()
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        self.file = QFileDialog.getExistingDirectory()
    
    # 导入
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        words = []
        for file1 in listdir(self.file):
            file1 = self.file +  "\\" + file1
            with open(file1, "r") as fp:
                x = fp.readlines()
                for k in range(len(x)):
                    x1 = x[k][:-1]
                    y = x1.split("-")
                    words.append(y)
        with open("./words.txt", "w") as fp:
            fp.write(str(words))
 
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
 
 
    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        self.lineEdit.returnPressed.connect(self.lineEdit_function)
        self.label.setText(self.words[self.dict["num"]][1])
    
    # 程序完成时记得将路劲改好##################################
    @pyqtSlot()    
    def closeEvent(self, event):
        with open(r"C:\Users\zouyo\Desktop\Data\dicts.txt", "w") as fp:
            fp.write(str(self.dict))
        event.accept()

    @pyqtSlot()
    def on_pushButton_11_clicked(self):
        self.lineEdit.returnPressed.connect(self.lineEdit_function1)
    
    def set_radio(self):
        word_day,  l = self.get_words(self.dict["days"])
        # 在单词所在位置的一定范围内选择单词中文意思
        if self.dict["w2"] < 5:
            A,  B = 0, 10
        elif self.dict["w2"]  < l - 5:
            A = self.dict["w2"] - 5
            B = self.dict["w2"] + 5
        elif self.dict["w2"]  >= l - 5 and self.dict["w2"]  < l:
            A = l -8
            B = l- 1
        elif self.dict["w2"] == l:
            self.dict["w2"] = 0
            self.dict["days"]  = self.dict["days"]  + 1
            word_day,  l = self.get_words(self.dict["days"])
            A,  B = 0, 10
        resultList=sample(range(A,B),3)
        if self.dict["w2"] in resultList:
            resultList[resultList.index(self.dict["w2"])] -= 1 
        x = randint(0, 3)
        resultList.insert(x,  self.dict["w2"])
        # print(resultList, l)
        self.label_4.setText(word_day[self.dict["w2"]][0])
        self.radioButton.setText(word_day[resultList[0]][1])
        self.radioButton_2.setText(word_day[resultList[1]][1])
        self.radioButton_3.setText(word_day[resultList[2]][1])
        self.radioButton_4.setText(word_day[resultList[3]][1])

    @pyqtSlot()
    def on_pushButton_14_clicked(self):
        word_day,  l = self.get_words(self.dict["days"])
        if self.radioButton.isChecked() == True:
            if self.radioButton.text() == word_day[self.dict["w2"]][1]:
               self.dict["w2"] = self.dict["w2"] + 1
               self.set_radio()
        elif self.radioButton_2.isChecked() == True:
            if self.radioButton_2.text() == word_day[self.dict["w2"]][1]:
               self.dict["w2"] = self.dict["w2"] + 1
               self.set_radio()
        elif self.radioButton_3.isChecked() == True:
            if self.radioButton_3.text() == word_day[self.dict["w2"]][1]:
               self.dict["w2"] = self.dict["w2"] + 1
               self.set_radio()
        else:
            if self.radioButton_4.text() == word_day[self.dict["w2"]][1]:
               self.dict["w2"] = self.dict["w2"] + 1
               self.set_radio()
        self.radioButton.setChecked(True)
    
    @pyqtSlot()
    def on_lineEdit_returnPressed(self):
        self.dict["word"] = self.word[self.dict["w2_1"]][0]
        if self.lineEdit.text() == self.word[self.dict["w2_1"]][0]:
            self.dict["w2_1"] += 1
            if self.dict["w2_1"] >= self.len:
                self.dict["w2_1"] = 0
                self.dict["days_1"] += 1
                self.get_words(self.dict["days_1"])
            self.dict["word"] = self.word[self.dict["w2_1"]][0]
            if self.dict["net"] == 1:
                self.get_word_info(self.word[self.dict["w2_1"]][0])
            if self.dict["w2_1"] - 1 >= 0 : 
                self.textborwer(self.word[self.dict["w2_1"]-1][0], self.word[self.dict["w2_1"]-1][1])
            self.lineEdit.setText("")
            self.label.setText(self.word[self.dict["w2_1"]][1])
            self.label_3.setText(" ")
            self.textBrowser.document().clear()
            print(self.dict["net_is_ok"])
        else:
            x = list(self.lineEdit.text())
            words = self.word[self.dict["w2_1"]][0]
            if len(x) <= len(words):
                for i in range(len(words)):
                    if i < len(x):
                        if words[i] != x[i]:
                            x[i] = '_'
                    else:
                        x.append('_')
            else:
                for i in range(len(words)):
                    if words[i] != x[i]:
                        x[i] = '_'
                for i in range(len(words), len(x)):
                    x[i]='x'
            self.label_3.setText("".join(x))
      
    # 英语单词播放
    @pyqtSlot()
    def on_pushButton_12_clicked(self):
        try:
            url = "http://dict.youdao.com/dictvoice?audio={}&type=2".format(self.dict["word"])
            repose = get(url)
            with open(r"C:\Users\zouyo\Desktop\Data\{}.mp3".format(self.dict["word"]),"wb") as fp:
                fp.write(repose.content)
            playsound(r"C:\Users\zouyo\Desktop\Data\{}.mp3".format(self.dict["word"]))
            remove(r"C:\Users\zouyo\Desktop\Data\{}.mp3".format(self.dict["word"]))
        except:
            self.box("单词音源链接错误！")

    @pyqtSlot()
    def on_pushButton_15_clicked(self):
        if self.dict["net_is_ok"] == 0:
            self.get_word_info(self.dict["word"])
            self.dict["net_is_ok"] = 1
        self.refer(1)
    
    @pyqtSlot()
    def on_pushButton_16_clicked(self):
        if self.dict["net_is_ok"] == 0:
            self.get_word_info(self.dict["word"])
            self.dict["net_is_ok"] = 1
        self.refer(3)
    
    @pyqtSlot()
    def on_pushButton_17_clicked(self):
        if self.dict["net_is_ok"] == 0:
            self.get_word_info(self.dict["word"])
            self.dict["net_is_ok"] = 1
        self.refer(4)
    
    @pyqtSlot()
    def on_pushButton_18_clicked(self):
        if self.dict["net_is_ok"] == 0:
            self.get_word_info(self.dict["word"])
            self.dict["net_is_ok"] = 1
        self.refer(2)
    
    @pyqtSlot()
    def on_pushButton_19_clicked(self):
        self.dict["w2_1"] += 1
#        word_day,  l = self.get_words(self.dict["days"])
        if self.dict["w2_1"] - 1 >= 0 : 
            self.textborwer(self.word[self.dict["w2_1"]-1][0], self.word[self.dict["w2_1"]-1][1])
        if self.dict["w2_1"] >= self.len:
            self.dict["days_1"] += 1
            self.dict["w2_1"] = 0
            self.get_words(self.dict["days_1"])
        self.dict["word"] = self.word[self.dict["w2_1"]][0]
        if self.dict["net"] == 1:
            self.get_word_info(self.word[self.dict["w2_1"]][0])
            self.refer(6)
        self.label.setText(self.word[self.dict["w2_1"]][1])
        self.lineEdit.setText("")
        self.label_3.setText("")
    
    @pyqtSlot()
    def on_pushButton_20_clicked(self):
        if self.dict["net_is_ok"] == 0:
            self.get_word_info(self.dict["word"])
            self.dict["net_is_ok"] = 1
        self.refer(5)
        
    @pyqtSlot()
    def on_pushButton_21_clicked(self):
        if self.dict["net_is_ok"] == 0:
            self.get_word_info(self.dict["word"])
            self.dict["net_is_ok"] = 1
        self.refer(6)
    
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        self.dict["w2_1"] -= 1
#        word_day,  l = self.get_words(self.dict["days"])
        if self.dict["w2_1"] - 1 >= 0 : 
            self.textborwer(self.word[self.dict["w2_1"]-1][0], self.word[self.dict["w2_1"]-1][1])
        else:
            self.dict["w2_1"] = 0
        self.dict["word"] = self.word[self.dict["w2_1"]][0]
        if self.dict["net"] == 1:
            self.get_word_info(self.word[self.dict["w2_1"]][0])
            self.refer(6)
        self.label.setText(self.word[self.dict["w2_1"]][1])
    
    # 设置中第二个确定键
    @pyqtSlot()
    def on_pushButton_25_clicked(self):
        
        if self.lineEdit_3.text() == "":
            self.box("请先输入进度！")
        else:
            str = int(self.lineEdit_3.text())
            day = int(self.lineEdit_2.text())
            _, count = self.collect(day=day)
            if str < count[0]:
                self.dict["w2_1"] = str
                self.box("设置成功！")
            else:
                self.box("您输入的不在范围内！")
        # 这里写上每一天的单词数是否符合，并设置单词数，函数self.collect()
        # 当没有选天数就选单词数，报错
    
    # 设置中第一个确定按键
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        day_len = int(self.lineEdit_2.text())
        n, _ = self.collect()
        if day_len <  n and day_len >= 0:
            self.dict["days_1"] = day_len+1
            _, count = self.collect(day=day_len)
            self.lineEdit_3.setPlaceholderText("0~{}".format(count[0]-1))
        else:
            self.box("您输入的不在范围内！")
    
if __name__ == "__main__":
    import sys
    app =QApplication(sys.argv)
    st = Form()
    st.show()
    sys.exit(app.exec_())
    
    
