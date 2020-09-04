from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __int__(self, driver):
        # """
        # :Inits BasePage class
        # :return
        #     None
        # """

        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        # """
        # Verify the page title
        # :parameter
        #     titleToVerify: Title on the page that needs to be verified
        # """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
