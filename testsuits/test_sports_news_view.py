# coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobject.baidu_homepage import HomePage
from pageobject.baidu_news_homepage import NewsHomePage

class ViewNBANews(unittest.TestCase):


    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser()


    def tearDown(self):
        browse = BrowserEngine(self)
        self.driver = browse.quit_browser()

    def test_view_nba_news(self):

        homepage = HomePage(self.driver)
        homepage.click_news()

        news_homepage = NewsHomePage(self.driver)
        news_homepage.click_sports_news()
        time.sleep(2)

        news_homepage.get_windows_img()

if __name__ == '__main__':
    unittest.main()