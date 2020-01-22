#coding:utf-8
from selenium import  webdriver
from common import public
import unittest
import time

class MyTest(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://zjqz-registration.test.mararun.com/login.html")
        self.driver.maximize_window()

        alert=self.driver.switch_to.alert
        alert.send_keys("malamala")
        alert.accept()
        time.sleep(2)


    def test_login01_Success(self):

        '''正确的用户名密码成功登录'''
        username="13011122158"
        password="889988"
        login=public.Login(self.driver,username,password)
        login.user_login()
        time.sleep(1)

        result=self.driver.find_element_by_xpath("//span[contains(text(),'13011122158')]").text

        hope="13011122158"

        self.assertEqual(result,hope)


    def test_login02_Failed(self):

        '''错误的密码'''
        username = "13000000000"
        password = "889966"
        login = public.Login(self.driver, username, password)
        login.user_login()
        time.sleep(1)

        result=self.driver.find_element_by_xpath("//div[@class='error-text']").text
        print(result)

        hope="验证码不正确，请重新输入"

        self.assertIn(result,hope)

    def test_login03_Failed(self):
        '''用户名为空'''
        username=""
        password="889988"
        login=public.Login(self.driver,username,password)
        login.user_login()
        time.sleep(1)

        result=self.driver.find_element_by_class_name("input-login-error-update").text

        hope="不能为空"
        self.assertEqual(result,hope)

    def test_login04_failed(self):
        '''密码为空'''
        username="13011122158"
        password=""
        login=public.Login(self.driver,username,password)
        login.user_login()
        time.sleep(1)

        result=self.driver.find_element_by_xpath("//div[@class='login-userCode-update clearfix']/p[@class='input-login-error-update']").text
        hope="不能为空"
        self.assertEqual(result,hope)



    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":

    unittest.main()


