# coding=utf-8
import os
import time
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger

mylog =Logger(logger='BasePage').getlog()

class BasePage(object):

    def __init__(self,driver):

        self.driver = driver

    def back(self):
        self.driver.back()
        mylog.info("回退上一页面")

    def forward(self):
        self.driver.forward()
        mylog.info("前进下一页面")

    def open_url(self,url):
        self.driver.get(url)
        mylog.info("打开URL")

    def max_window(self):
        self.driver.maximize_window()
        mylog.info("最大化窗口")

    def quit_browser(self):
        self.driver.quit()
        mylog.info("关闭浏览器")

    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        mylog.info("等待%d秒" % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            mylog.info("关闭并退出浏览器")
        except NameError as e:
            mylog.error("Failed to quit the browser with %s" % e)

    def get_windows_img(self):

        """
        截图并保存在根目录下的Screenshots文件夹下

        """
        file_path=os.path.dirname(os.getcwd())+'/screenshot/'
        rq=time.strftime('Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("开始截图并保存")
        except Exception as e:
            mylog.error("出现异常",format(e))
            self.get_windows_img()

    # 定位元素方法
    def find_element(self,selector):
        element= ' '
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by=selector.split('=>')[0]
        selector_value=selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                element=self.driver.find_element_by_id(selector_value)
                mylog.info("Had find the element \'%s \' successful."
                           "by %s via value: %s" % (element.text,selector_by,selector_value))
            except Exception as e:
                mylog.error("NoSuchElementException: %s" % e)

        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)

        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            mylog.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            mylog.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            mylog.info("Clear text in input box before typing.")
        except NameError as e:
            mylog.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            mylog.info("页面元素被点击")
#            mylog.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            mylog.error("Failed to click the element with %s" % e)

    # 获取网页标题
    def get_page_title(self):
        mylog.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        mylog.info("Sleep for %d seconds." % seconds)
