
from selenium import webdriver
# from  base.base_log import test_log
# log=test_log()
# 函数封装
from base.my_logging import test_logger
log = test_logger()
# 封装类
class BasePage:
    # driver = webdriver.Chrome()
    # 初始化函数,需要传一个浏览器
    def __init__(self,driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver

    def open(self,url):
        log.info('正在打开{}网站'.format(url))
        self.driver.get(url)

    def loctor(self,loc):
      return self.driver.find_element(*loc)

    # 输入
    # driver.find_element_by_id('kw').sendkeys('百度')
    def input(self,loc,txt):
        log.info('正在定位{}内容，输入{}内容'.format(loc,txt))
        self.loctor(loc).send_keys(txt)

    def click(self,loc):
        log.info('正在定位{}内容，进行点击'.format(loc))
        self.loctor(loc).click()

    # 窗口最大化
    # def max(self):
    #     self.driver.maximize_window()

    # def quit(self):
    #     self.driver.quit()


