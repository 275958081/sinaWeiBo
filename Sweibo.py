#coding:utf-8
from selenium import webdriver
import time
import string
import random
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
def del_repeat():
    with open('name.txt') as file:
        with open('temp.txt','w') as f:
            f.writelines(set(file.readlines()))
    if os.path.isfile('name.txt'):
    	os.remove('name.txt')
    shutil.copy('temp.txt','name.txt')
class webDrive:
    def __init__(self,name,passwd,co=None):
        self.driver = webdriver.Chrome()
        #self.driver.set_window_size(600,600)
        self.name=name
        self.passwd=passwd
        self.co=co
        self.login(self.name,self.passwd)
    def write_to_file(self,temp):
        with open("name.txt","a") as f:
             f.write("%s"%temp)
             f.write("\n")
        
    def login(self,name,passwd):
        time.sleep(3)
        self.driver.get('http://weibo.com/login')
        time.sleep(3)
        print self.driver.current_url
        if self.driver.current_url == "http://weibo.com/login":
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='pl_login_form']/div[5]/div[1]/div/input").send_keys("%s"%name)
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='pl_login_form']/div[5]/div[2]/div/input").send_keys("%s"%passwd)
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='pl_login_form']/div[5]/div[6]/div[1]/a/span").click()
            time.sleep(1)
    def comment(self):
        element=self.driver.find_element_by_xpath("//*[@id='pl_content_publisherTop']/div/div[2]/textarea")
        comment=u'%s'%self.co 
        temp=[]
        temp=map(lambda x:x.strip(),open('temp.txt'))
        for i in range(25,1,-1):
            name=random.sample(temp,i)
            t='@'+'@'.join(map(lambda line:u"%s"%line.strip(),name))
            if len(u"%s"%t)<140-len("%s"%comment):
                temp=map(lambda x:"%s\n"%x,filter(lambda x:x not in name,temp))
                open('temp.txt','w').writelines(temp)
                break
        
        element.send_keys(u"%s%s"%(comment,t))
        self.driver.find_element_by_xpath("//*[@id='pl_content_publisherTop']/div/div[3]/div[1]/a/span").click()
        time.sleep(20)
    def search(self):
        num1=self.driver.find_element_by_xpath("//*[@id='pl_rightmod_myinfo']/ul/li[2]/a/strong").text #关注我的人数
        num2=self.driver.find_element_by_xpath("//*[@id='pl_rightmod_myinfo']/ul/li[1]/a/strong").text #我关注的人数
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='pl_rightmod_myinfo']/ul/li[2]/a/span").click()
        time.sleep(1)
        for i in range(1,20):
            try:
                time.sleep(1) 
                temp=self.driver.find_element_by_xpath("//*[@id='pl_relation_fans']/div/div[2]/div[2]/ul/li[%d]/div/div[2]/div[2]/div[1]/strong/a"%i).text
                self.write_to_file(temp)
                print temp
            except Exception,e:
                pass
        self.driver.find_element_by_xpath("//*[@id='pl_relation_fans']/div/div[2]/div[2]/div/div[2]/div/a[1]").click()
        time.sleep(1)
        url=self.driver.current_url
        print url
        print int(url.split("=")[-1])
        
        for i in range(int(url.split("=")[-1]),int(int(num1)/20)+1):
            while(1):
                try:
                    print "i:%s"%i
                    self.driver.get("%s=%d"%("=".join(url.split("=")[:-1]),i))
                except Exception,e:
                    time.sleep(1)
                    pass
                else:
                    break
            for j in range(1,20):
                try:
                    time.sleep(1)
                    temp=self.driver.find_element_by_xpath("//*[@id='pl_relation_fans']/div/div[2]/div[2]/ul/li[%d]/div/div[2]/div[2]/div[1]/strong/a"%j).text
                    self.write_to_file(temp)
                    print temp
                except Exception,e:
                    time.sleep(1)
                    print e
                    pass
    def quitChrome(self):
    	print "stop"
    	self.driver.quit()
if __name__ == "__main__":
    if len(sys.argv)>0 and sys.argv[1] == 'rename':
        del_repeat()
    if len(sys.argv)>0 and sys.argv[1] == 'comment':
        weibo = webDrive()
        for i in range(4):
            print i
            try:
                weibo.comment()
                time.sleep(1)
            except Exception,e:
                print e
                pass
    elif len(sys.argv)>0 and sys.argv[1] == 'so':
        weibo = webDrive()
        weibo.search()
    
