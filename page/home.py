from selenium.webdriver.common.by import By

phone_number = (By.XPATH, '//*[@id="login-form"]/fieldset/label[1]/span/input')
password = (By.XPATH, '//*[@id="login-form"]/fieldset/label[2]/span/input')
login_btn = (By.XPATH, '//*[@id="login-form"]/fieldset/button')
remember_password = (By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/label/span')
register = (By.XPATH, '//*[@id="login-form"]/fieldset/div[3]/a[1]')
forget_password = (By.XPATH, '//*[@id="login-form"]/fieldset/div[3]/a[2]')
login_success_flag = (By.XPATH, '//h3[contains(text(),"进行中任务分工")]')
Workbill_Config = (By.LINK_TEXT, '作业票配置')
Workbill_Guanli = (By.LINK_TEXT, '作业票管理')
ByCondition = (By.LINK_TEXT, '按条件')
searchButton = (By.XPATH, '//button[@class="btn btn-primary btn-block"]')