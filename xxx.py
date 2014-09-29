# -*- coding:utf-8 -*-
import sys

# Import Qt GUI component
from PyQt4 import QtGui 
from PyQt4 import QtCore
from Sweibo import webDrive
from Sweibo import del_repeat
import time
# Import GUI File
from ui_test import Ui_MainWindow

# Self Function
import threading
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class threadComment(threading.Thread):
    def __init__(self,name,passwd,co):
        threading.thread.__init__(self)
        self.thread_stop = False    
        self.name= name
        self.passwd = passwd
        self.co = co
    def run(self):
        login=webDrive(self.name,self.passwd,self.co)
        time.sleep(2)
        login.comment()
    def stop(self):
        self.thread_stop = True
class threadAddFans(threading.Thread):
    def __init__(self,name,passwd):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.name = name
        self.passwd = passwd
    def run(self):
    	self.login=webDrive(self.name,self.passwd)
        self.login.search()
    def stop(self):
    	print "stip"
    	self.login.quitChrome()
    	self.thread_stop = True     

def del_name():
    del_repeat()

# Make main window class
class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        #self.pushButton.clicked.connect(PrintInput())
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'),self.addFans)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'),self.login)
        self.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'),self.delName)
        self.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'),self.addFans)
        self.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'),self.login)
    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.textEdit_2.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit_2.setTextCursor(cursor)
        self.textEdit_2.ensureCursorVisible()
    def addFans(self):
        thread1= threadAddFans(self.lineEdit.text(),self.lineEdit_2.text())
        sender = self.sender()
        if sender.objectName() == "pushButton":
           thread1.start()
        if sender.objectName() == "pushButton_4":
           print "pu"
           thread1.stop()
    def login(self):
        thread2 = threadComment(self.lineEdit.text(),self.lineEdit_2.text(),self.textEdit.toPlainText())
        sender = self.sender()
        if sender.objectName() == "pushButton_2":
           thread2.start()
        if sender.objectName() == "pushButton_5":
           thread2.stop()
    def delName(self):
        del_name()
class EmittingStream(QtCore.QObject):     
        textWritten = QtCore.pyqtSignal(str)
        def write(self, text):
            self.textWritten.emit(str(text))
if __name__=='__main__':
    Program = QtGui.QApplication(sys.argv)
    Window=MainWindow()
    Window.show()
    Program.exec_()
    main()
