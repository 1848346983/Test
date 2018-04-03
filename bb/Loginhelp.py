#coding=utf-8
'''
Created on 2017��6��30��

@author: lovely
'''
import os
from selenium import webdriver
from time import sleep



  

class Loginhelp(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    def setup(self):
        self.iedriver="C:\Program Files\Internet Explorer\IEDriverServer.exe"
        self.os.environ["webdriver.ie.driver"] =self.iedriver
        self.driver=webdriver.Ie(self.iedriver)
        self.url="http://192.168.101.110:8081/YssCISS"
        self.driver.get(self.url)
    def Login(self,username,password):    
        nowhander=self.driver.current_window_handle
        handers=self.driver.window_handles
        chiode=self.driver.switch_to_window(handers[1])
        loginname=self.driver.find_element_by_id("username")
        password=self.driver.find_element_by_id("password")
        submitbut=self.driver.find_element_by_id("submitBut")
        loginname.clear()
        loginname.send_keys(username)
        password.send_keys(password)
        submitbut.click()
        sleep(5)
        
    if __name__ == '__main__':
       Loginhelp.setup()
       Loginhelp.Login("test", "1")
       
        
        
        