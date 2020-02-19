from POMDemo.locators.locator import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id =  locator.username_textbox_id
        self.userpwd_textbox_id = locator.userpwd_textbox_id
        self.login_button = locator.login_button

    def enter_username(self, username):
        self.driver.find_element_by_id(locator.username_textbox_id).clear()
        self.driver.find_element_by_id(locator.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(locator.userpwd_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_class_name(locator.login_button).click()


