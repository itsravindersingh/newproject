'''
Created on Oct 4, 2018

@author: Ravinder Singh
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
    
driver = webdriver.Firefox();
driver.get("https://seleniumwithjavapython.wordpress.com/selenium/");
action = ActionChains(driver);
    
firstLevelMenu = driver.find_element_by_xpath("//a[contains(.,'Resources')]");
action.move_to_element(firstLevelMenu).perform();
    
secondLevelMenu = driver.find_element_by_xpath("//a[@href='https://seleniumwithjavapython.wordpress.com/selenium-resources/']");
action.move_to_element(secondLevelMenu).perform();
thirdlevel=driver.find_element_by_xpath("//a[@href='https://seleniumwithjavapython.wordpress.com/selenium-resources/comprehensive-selenium-tutorials/']");
thirdlevel.click();