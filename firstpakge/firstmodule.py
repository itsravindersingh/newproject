'''
Created on Oct 2, 2018

@author: Ravinder Singh
'''
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from warnings import catch_warnings
from select import select
user = "ravindersingh366@gmail.com"
pwd = "9811075137"
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")

elem1 = driver.find_element_by_id("email")
elem1.send_keys(user)
elem2 = driver.find_element_by_id("pass")
elem2.send_keys(pwd)
s1=Select(driver.find_element_by_id("month"))
s1.select_by_visible_text("Nov")

time.sleep(10)
elem1.send_keys(Keys.RETURN)
elem1.clear()
time.sleep(4)

driver.close()
