from pages.home.login_page import LoginPage
from utilities.teststatus import TStatus
import unittest
import pytest
import allure


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("onetimesetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, onetimesetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TStatus(self.driver)

    @allure.description("Validate let's kode it login with valid credentionals")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clearLoginFields()
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @allure.description("Validate let's kode it login with invalid credentionals")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("uiasnk@yahcos.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Login is not successful")