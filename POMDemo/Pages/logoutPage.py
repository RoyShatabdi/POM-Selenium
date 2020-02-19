from POMDemo.locators.locator import *


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_csslocator_id = locator.logout_csslocator_id

    def logout(self):
        self.driver.find_element_by_css_selector(locator.logout_csslocator_id).click()
