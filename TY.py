from selenium import webdriver

from page import home

FF1 = webdriver.Firefox(executable_path="/Users/shishuaigang/Desktop/browser_driver/firefoxDriver/geckodriver")
FF1.get("http://119.3.6.176:8000")
FF1.find_element(*home.phone_number).send_keys('15102100358')
FF1.find_element(*home.password).send_keys('123456')
FF1.find_element(*home.login_btn).click()
FF1.find_element(*home.Workbill_Config).click()
FF1.find_element(*home.Workbill_Guanli).click()
FF1.find_element(*home.ByCondition).click()
FF1.find_element(*home.searchButton).click()