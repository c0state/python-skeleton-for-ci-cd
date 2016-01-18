import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AppSeleniumTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = None

    def tearDown(self):
        self.driver.close()

    def _test_selenium_actions(self):
        self.driver.get("http://localhost:5000")
        self.assertEquals(self.driver.title, "Clean Blog")

    # def test_selenium_chrome(self):
    #     self.driver = webdriver.Chrome("/vagrant/bin/chromedriver")
    #     self._test_selenium_actions()
    #
    # def test_selenium_firefox(self):
    #     self.driver = webdriver.Firefox()
    #     self._test_selenium_actions()

    def test_selenium_phantomjs(self):
        self.driver = webdriver.PhantomJS()
        self._test_selenium_actions()
