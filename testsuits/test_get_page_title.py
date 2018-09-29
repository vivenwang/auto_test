# coding = utf-8

import unittest
from framework.basepage import BasePage
from framework.browser_engine import BrowserEngine

class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser()

    @classmethod
    def tearDownClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.quit_browser()

    def test_get_page_title(self):
        basepage = BasePage(self.driver)
        print basepage.get_page_title()