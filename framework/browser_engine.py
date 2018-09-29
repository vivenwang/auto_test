#coding=utf-8

import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger


logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):

        driver = webdriver.Chrome()

        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)

        url = config.get("testServer", "URL")
        logger.info("The testServer URL is: %s." % url)

        driver.get(url)
        logger.info("open url:%s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("等待10秒.")
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器.")
        driver = webdriver.Chrome()
        driver.quit()





