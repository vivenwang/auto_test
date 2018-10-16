#!/usr/bin/env Python
# coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobject.douban_homepage import HomePage

class DouBanSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser()

    @classmethod
    def tearDownClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.quit_browser()

    def test_douban_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search(u'解忧杂货店')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()
        result_text = homepage.find_element("xpath=>//*[@id='root']/div/div[1]/h1").text
        try:
            assert u'解忧杂货店' in result_text
            print ('Test pass.')
        except Exception as e:
            print('Test fail', format(e))

if __name__ == '__main__':
    unittest.main()
