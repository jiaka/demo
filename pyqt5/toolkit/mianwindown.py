# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading, k1_rc, urllib.parse, http.client, random, hashlib, json, requests
from re import match, compile
import html2text as ht
from lxml import etree
from Ui_mianwindown import Ui_Form
from baidu import  BDWKDOC, BDWKPPT, BDWKTXT, BaiduWK
from PyQt5.QtWebEngineWidgets import *


class Form(QWidget, Ui_Form, BDWKDOC, BDWKPPT, BDWKTXT):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.radioButton10.setChecked(True)
        self.radioButton_2.setChecked(True)
        self.cursor = self.textEdit.textCursor()
        self.textEdit.moveCursor(self.cursor.Start)
        self.textEdit.insertPlainText("请在输入框中输入地址\n");



        
        # self.pushButton_downmd.clicked.connect(self.info)
        
    def info(self, n):
        if n==1:
            str = "    请输入网页链接！\n\n"
        else:
            str = "    请输入正确格式的链接！\n\n"
        reply = QMessageBox.information(self,'提示',str, QMessageBox.Ok )
        if reply == QMessageBox.Ok:
            self.lineEdit_3.setText('https://www.baidu.com/')
        #else:
        #    self.lineEdit_3.setText('你选择了Closee！')
        
    def f(self, n, x):
        # 十进制转2-16进制函数
        # n为待转换的十进制数，x为机制，取值为2-16
        a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
        b=[]
        while True:
            s=n//x#商
            y=n%x#余数
            b=b+[y]
            if s==0:
                break
            n=s
        b.reverse()
        return b

    @pyqtSlot()
    def on_pushButton_music_clicked(self):
        # 设置按钮切换stackedWidget
        self.stackedWidget.setCurrentWidget(self.page)
        
    
    @pyqtSlot()
    def on_pushButton_tools_clicked(self):
        # 设置按钮切换stackedWidget
        self.stackedWidget.setCurrentWidget(self.page_2)
       
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        pass

        
    @pyqtSlot()
    def on_lineEdit_returnPressed(self):
        # 教程lineexit  https://blog.csdn.net/qq_29406323/article/details/81360115
        #  radiobutton  https://blog.csdn.net/jia666666/article/details/81514777
        x = self.lineEdit.text()
        if x=='':
            x="0"
        if self.radioButton_2.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 2), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText(oct(int(x, 2)))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 2)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(hex(int(x, 2)))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
            else:
                pass
        elif self.radioButton_4.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 4), 2))))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 4), 8))))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 4)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 4), 16))))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
        elif self.radioButton_8.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 8), 2))))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 8), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 8)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(hex(int(x, 8)))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
        elif self.radioButton_10.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText(bin(int(x)))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText(oct(int(x)))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(hex(int(x)))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
        elif self.radioButton_16.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 16), 2))))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 16), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 16), 8))))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 16)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton32.isChecked():
                pass
        else:
            pass
            
    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, p0):
        x = self.lineEdit.text()
        if x=='':
            x="0"
        if self.radioButton_2.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 2), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText(oct(int(x, 2)))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 2)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(hex(int(x, 2)))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
            else:
                pass
        elif self.radioButton_4.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 4), 2))))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 4), 8))))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 4)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 4), 16))))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
        elif self.radioButton_8.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 8), 2))))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 8), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 8)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(hex(int(x, 8)))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
        elif self.radioButton_10.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText(bin(int(x)))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText(oct(int(x)))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(hex(int(x)))
            elif self.radioButton32.isChecked():
                self.lineEdit_2.setText()
        elif self.radioButton_16.isChecked():
            if self.radioButton2.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 16), 2))))
            elif self.radioButton4.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 16), 4))))
            elif self.radioButton8.isChecked():
                self.lineEdit_2.setText("".join(map(str, self.f(int(x, 16), 8))))
            elif self.radioButton10.isChecked():
                self.lineEdit_2.setText(str(int(x, 16)))
            elif self.radioButton16.isChecked():
                self.lineEdit_2.setText(x)
            elif self.radioButton32.isChecked():
                pass
        else:
            pass
            
    @pyqtSlot()
    def on_pushButton_baidu_clicked(self):    
        threading1 = threading.Thread(target = self.run)
        threading1.start()
        
    def run(self):    
        try:
            url = self.lineEdit_baidu.text()
            docType = BaiduWK(url).docType
            title1 = BaiduWK(url).title
        except:
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("您输入的url有误请重新输入!\n")
            docType = "xxx"
        if docType != "xxx":
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("文档类型为{}\n".format(docType))
        if docType == "ppt":
            ppt = BDWKPPT(url)
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("您将要获取的演示文稿(ppt)名称为:{}\n".format(title1))
            ppt.get_ppt_json_info()
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("已经保存为:{}\n".format(title1))
        elif docType == "doc":
            word = BDWKDOC(url)
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("您将要获取的文档(word)名称为:{}\n".format(title1))
            pure_addr_list = word.get_pure_addr_list()
            word.get_json_content(pure_addr_list)
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("已经保存为:{}\n".format(title1))
        elif docType == "pdf":
            pdf = BDWKDOC(url)
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("您将要获取的PDF名称为:{}".format(title1))
            pure_addr_list = pdf.get_pure_addr_list()
            pdf.get_json_content(pure_addr_list)
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("已经保存为:".format(title1))
        elif docType == "txt":
            txt = BDWKTXT(url)
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("您将要下载的文本文档(txt)名称为:{}".format(title1))
            txt.get_txt(url)
            self.cursor = self.textEdit.textCursor()
            self.textEdit.moveCursor(self.cursor.Start)
            self.textEdit.insertPlainText("已经保存为:".format(title1))
        else:
            pass
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        q = self.textEdit_2.toPlainText()
        appKey = '24435b07daa2dac6'
        secretKey = 'imDeQUT24yCeGVaw9rvF9Aj8RnspBcld'
        httpClient = None
        myurl = '/api'
        if self.comboBox.currentText() =="英文 » 中文": 
            fromLang = 'EN'
            toLang = 'zh-CHS'
        else:
            fromLang = 'zh-CHS'
            toLang = 'EN'
        salt = random.randint(1, 65536)
        sign = appKey + q + str(salt) + secretKey
        m1 = hashlib.new('md5')
        m1.update(sign.encode("utf-8"))
        sign = m1.hexdigest()
        myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        if q != '':
            s = json.loads(response.read().decode("utf-8"))['translation'][0]
        else:
            s = ''
        self.textEdit_3.setPlainText(s)
        httpClient.close()
        
    def main_page_loaddown(self, url):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        response = requests.get(url,headers)
        print(response)
        if response.status_code == 200:
            return response.text
        return None    
        
    @pyqtSlot()
    def on_pushButton_downmd_clicked(self):
        pattern = compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    # 匹配模式
        str = self.lineEdit_3.text()
        url = match(pattern,str)
        if str == "":
            self.info(1)
        elif url == None:
            self.info(2)
        else:
            download_path = QFileDialog.getExistingDirectory(self)  
            url = self.lineEdit_3.text()
            content = self.main_page_loaddown(url)
            # time.sleep(random.uniform(0, 2))
            x = random.randint(1, 100)
            file = download_path +"/{:}.html".format(x)
            file1 = download_path + "/{:}.md".format(x)
            with open(file, "w", encoding='utf-8') as f:
                f.write(content)
            with open(file, "r", encoding='utf-8') as f:
                htmltxt = f.read()
            text_maker = ht.HTML2Text()
            text = text_maker.handle(htmltxt)
            with open(file1, "w", encoding='utf-8') as f:
                f.write(text)
        # 加弹框
        
    def music_api(self, url):
        text = requests.get(url).text
        json_txt = etree.HTML(text)
        result1 = json_txt.xpath("/html/body/script[1]/text()")
        if json.loads(str(result1[0][18:-2]))["detail"]["playurl"] != "" :
            return 1, json.loads(str(result1[0][18:-2]))["detail"]["playurl"], json.loads(str(result1[0][18:-2]))["detail"]["song_name"], json.loads(str(result1[0][18:-2]))["detail"]["kg_nick"]
        elif json.loads(str(result1[0][18:-2]))["detail"]["playurl_video"] != "":
            return 2, json.loads(str(result1[0][18:-2]))["detail"]["playurl_video"], json.loads(str(result1[0][18:-2]))["detail"]["song_name"], json.loads(str(result1[0][18:-2]))["detail"]["kg_nick"]
        else:
            return 0, None, None, None

    def downmusic(self, url, down_path):
        n,  playurl, name, nick = self.music_api(url)
        repose = requests.get(playurl)
        if n == 1:
            type = ".mp3"
        elif n == 2:
            type = ".mp4"
        else:
            # QMessageBox.information(self,'提示',"   链接错误或者不支持该歌曲下载！", QMessageBox.Ok )
            return None
        with open(down_path + "/" + name + "-" + nick + type , 'wb') as f:
            f.write(repose.content)
           
            
    @pyqtSlot()
    def on_pushButton_quanmin_clicked(self):
        download_path = QFileDialog.getExistingDirectory(self)  
        url = self.lineEdit_quanmin.text()
        t1 = threading.Thread(target=self.downmusic, args=(url,download_path, ))
        t1.start()
        QMessageBox.information(self,'提示',"   开始下载！", QMessageBox.Ok )
        t1.join()
        QMessageBox.information(self,'提示',"   下载成功！", QMessageBox.Ok )
        
if __name__ == "__main__":
    import sys
    app =QApplication(sys.argv)
    st = Form()
    st.show()
    sys.exit(app.exec_())
    

