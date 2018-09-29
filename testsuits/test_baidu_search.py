# coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobject.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser()

    @classmethod
    def tearDownClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.quit_browser()

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()
        try:
            assert 'selenium' in homepage.get_page_title()
            print ('Test pass.')
        except Exception as e:
            print('Test fail', format(e))

    def test_baidu_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()
        try:
            assert 'python' in homepage.get_page_title()
            print ('Test pass.')
        except Exception as e:
            print('Test fail', format(e))


if __name__ == '__main__':
    unittest.main()


