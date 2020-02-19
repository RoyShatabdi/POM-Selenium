from selenium import webdriver
import time
import unittest
import os
import sys
from POMDemo.Pages.loginPage import *
from POMDemo.Pages.logoutPage import *
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # for test function always use test in front of the name
    def test_login_valid(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

        login = LoginPage(self.driver)

        login.enter_username("tomsmith")
        login.enter_password("SuperSecretPassword!")
        login.login_button()

        logout = LogoutPage()
        logout.logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print("Test passed")

    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="POMDemo/testReports"))
