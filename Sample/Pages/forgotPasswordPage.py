from Sample.Locators.locators import Locators

class ForgotPasswordPage():

    def __init__(self, driver):
        self.driver = driver

    def clickForgotPassword(self):
        self.driver.find_element_by_css_selector(Locators.forgotPassword_link_css).click()

    def getForgotPasswordHeaderText(self):
        return self.driver.find_element_by_css_selector(Locators.forgotPasswordHeader_label_css).text

    def enterUserNameOnForgotPassword(self, reset_username):
        self.driver.find_element_by_id(Locators.usernameOnForgotPassword_textfield_id).send_keys(reset_username)

    def clickResetButton(self):
        self.driver.find_element_by_id(Locators.reset_button_id).click()

    def clickCancelButton(self):
        self.driver.find_element_by_id(Locators.cancel_button_id).click()