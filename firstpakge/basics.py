'''
Created on Oct 3, 2018

@author: Ravinder Singh
'''
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.facebook.com")
e1=driver.find_element_by_xpath("//input[@value='1']").is_displayed()
try:
    if(e1):
           print "test passes"
except :
    print "failed" 
    
user = "ravindersingh366@gmail.com"
pwd = "9811075137"
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
    
 

