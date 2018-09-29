# coding=utf-8

import unittest
import HTMLTestRunner
import os
import time

report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
HtmlFile = report_path + now + '.html'
fp = file(HtmlFile, "wb")

suite = unittest.TestLoader().discover("testsuits")

#suite.addTest(BaiduSearch('test_baidu_search'))
#suite.addTest(BaiduSearch('test_baidu_search2'))
#suite.addTest(GetPageTitle('test_get_page_title'))

if __name__ == '__main__':
    # 执行用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试报告", description=u"百度测试情况")
    runner.run(suite)