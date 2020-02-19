# from selenium import webdriver
# import time
# import unittest
#
#
# class LoginTest(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.implicitly_wait(10)
#         cls.driver.maximize_window()
#
#     # for test function always use test in front of the name
#     def test_login_valid(self):
#         self.driver.get("https://the-internet.herokuapp.com/login")
#
#         self.driver.find_element_by_id("username").send_keys("tomsmith")
#         self.driver.find_element_by_id('password').send_keys("SuperSecretPassword!")
#         self.driver.find_element_by_class_name("radius").click()
#
#         self.driver.find_element_by_css_selector(".button.secondary")
#         time.sleep(2)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#         cls.driver.quit()
#
#         print("Test passed")
#
#
# if __name__ == '__main__':
#     unittest.main()
