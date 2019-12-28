import time
import unittest

from Sample.Pages.loginPage import LoginPage
from selenium import webdriver
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Professional/Selenium/Driver/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    '''
    def testValidLogin(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
    '''

    def testInvalidLogin(self):
        '''
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin")
        self.driver.find_element_by_id("btnLogin").click()
        invalidCredentialsText = self.driver.find_element_by_id("spanMessage").text
        assert invalidCredentialsText == "Invalid credentials", "Invalid credentials text is not displayed"
        '''
        loginPage = LoginPage(self.driver)
        loginPage.enterUserName("Admin")
        loginPage.enterPassword("admin")
        loginPage.clickLoginButton()
        invalidCredentialsText = loginPage.getUseramePasswordValidationText()
        assert invalidCredentialsText == "Invalid credentials", "Invalid credentials text is not displayed"

    def testUsernameCannotBlank(self):
        loginPgae = LoginPage(self.driver)
        loginPgae.enterUserName("")
        loginPgae.enterPassword("admin")
        loginPgae.clickLoginButton()
        userNameValidationText = loginPgae.getUseramePasswordValidationText()
        assert userNameValidationText == "Username cannot be empty", "Username cannot be empty is not displayed"

    def testPasswordCannotBlank(self):
        loginPgae = LoginPage(self.driver)
        loginPgae.enterUserName("Admin")
        loginPgae.enterPassword("")
        loginPgae.clickLoginButton()
        passwordValidationText = loginPgae.getUseramePasswordValidationText()
        assert passwordValidationText == "Password cannot be empty", "Password cannot be empty is not displayed"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        time.sleep(2)
        print("Test Completed for login page")

if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner('D:/Professional/Framework/MyPOM/Sample/Reports'))