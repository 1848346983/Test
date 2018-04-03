#coding=utf-8 
'''
Created on 2017��6��13��

@author: lovely
'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from lib2to3.tests.support import driver
from logging import thread
from selenium.webdriver.common.action_chains import ActionChains
import csv
import unittest

csvfile=file('d://dd.csv','rb')
reader=csv.reader(csvfile)
for da in reader:
    ueer= da[0]
    password=da[1]
    print ueer
    print password
    


#===============================================================================
# iedriver="C:\Program Files\Internet Explorer\IEDriverServer.exe"
# os.environ["webdriver.ie.driver"] =iedriver
# driver=webdriver.Ie(iedriver)
# url="http://192.168.101.110:8081/YssCISS"
# driver.get(url)
# nowhander=driver.current_window_handle
# handers=driver.window_handles
# chiode=driver.switch_to_window(handers[1])
# loginname=driver.find_element_by_id("username")
# password=driver.find_element_by_id("password")
# submitbut=driver.find_element_by_id("submitBut")
# loginname.clear()
# loginname.send_keys("test")
# password.send_keys("1")
# submitbut.click()
# sleep(5)
#===============================================================================
#===============================================================================
# handers2=driver.window_handles
# driver.switch_to_window(handers2[1])
# jigou=driver.find_element_by_xpath("//*[text()='机构信息']")
# jigou.click()
# sleep(3)
# submitjgadd=driver.find_element_by_id("ext-gen317")
# submitjgadd.click()
# sleep(3)
# orgName=driver.find_element_by_xpath("//input[@name='orgName']")
# orgName.send_keys("test1")
# orgtype=driver.find_element_by_id("ext-comp-1050")
# orgtype.click()
# sleep(3)
# orgtypevalue=driver.find_element_by_xpath("//font[text()='管理人']")
# orgtypevalue.click()
# orgrole=driver.find_element_by_id("ext-comp-1055")
# orgrole.click()
# sleep(3)
# orgrolevalue=driver.find_element_by_xpath("//font[text()='资产管理人']")
# ActionChains(driver).double_click(orgrolevalue).perform()
# btnsave=driver.find_element_by_id("ext-gen525")
# btnsave.click()
#===============================================================================
