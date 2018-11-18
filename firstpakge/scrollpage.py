'''
Created on Oct 4, 2018

@author: Ravinder Singh
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.rogers.com/consumer/home");
target = driver.find_element_by_xpath("//span[contains(.,'Follow')]");
driver.execute_script('arguments[0].scrollIntoView(true);', target)