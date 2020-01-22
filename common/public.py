#coding:utf-8
import time

class Login:
    def __init__(self,driver,username,password):
        self.driver = driver
        self.username = username
        self.password = password

    def user_login(self):


        self.driver.find_element_by_xpath("//span[contains(text(),'动态登录')]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号/邮箱']").send_keys(self.username)
        time.sleep(1)

        self.driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys(self.password)
        time.sleep(2)

        self.driver.find_element_by_class_name("login-button-update").click()
        time.sleep(1)



