# coding=utf-8

from framework.basepage import BasePage

class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    # //*[@id="su"]
    news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"
    # //*[@id="u1"]/a[1]

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)