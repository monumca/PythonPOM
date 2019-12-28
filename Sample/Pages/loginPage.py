from Sample.Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, username):
        self.driver.find_element_by_id(Locators.userName_textfield_id).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element_by_id(Locators.password_textfield_id).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element_by_id(Locators.login_button_id).click()

    def getUseramePasswordValidationText(self):
        return self.driver.find_element_by_id(Locators.userName_password_validation_label_css).text

    def getLoginPanelHeaderText(self):
        return self.driver.find_element_by_id(Locators.loginPanelHeader_label_id).text