import time
import unittest
from selenium import webdriver
from Sample.Pages.forgotPasswordPage import ForgotPasswordPage
from Sample.Pages.loginPage import LoginPage

class ForgotPasswordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Professional/Selenium/Driver/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def testForgotPassword(self):
        '''
        #self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_css_selector("div#forgotPasswordLink a").click()
        forgotPasswordHeaderText = self.driver.find_element_by_css_selector("div.head h1").text
        assert forgotPasswordHeaderText == "Forgot Your Password?", "Forgot Password is not opened"
        '''
        forgotPassword = ForgotPasswordPage(self.driver)
        forgotPassword.clickForgotPassword()
        headerText = forgotPassword.getForgotPasswordHeaderText()
        assert headerText == "Forgot Your Password?", "Forgot Password page is not opened"

    def testResetPassword(self):
        '''
        #self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_css_selector("div#forgotPasswordLink a").click()
        self.driver.find_element_by_id("securityAuthentication_userName").send_keys("Admin")
        self.driver.find_element_by_id("btnSearchValues").click()
        '''
        forgotPassword = ForgotPasswordPage(self.driver)
        forgotPassword.clickForgotPassword()
        forgotPassword.enterUserNameOnForgotPassword("Admin")
        forgotPassword.clickResetButton()

    def testCancelOnForgotPassword(self):
        loginPage = LoginPage(self.driver)
        forgotPassword = ForgotPasswordPage(self.driver)
        forgotPassword.clickForgotPassword()
        forgotPassword.clickCancelButton()
        loginPanelText = loginPage.getLoginPanelHeaderText()
        assert loginPanelText == "LOGIN Panel", "Clicking on cancel not returning to login page"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        time.sleep(2)
        print("Test Completed for Forgot password page")
