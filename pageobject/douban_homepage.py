# coding = utf-8

from framework.basepage import BasePage

class HomePage(BasePage):
    input_box = "id=>inp-query"
    search_submit_btn = "xpath=>//*[@id='db-nav-book']/div[1]/div/div[2]/form/fieldset/div[2]/input"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)



