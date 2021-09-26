from selenium.webdriver.common.by import By
from selenium import webdriver

from base.base_page1 import BasePage

# 登录文件
class LoginPage(BasePage):
    search = (By.ID, 'kw')
    sear_btn = (By.ID, 'su')
    url = 'https://www.baidu.com/'

    def login(self, name):
        self.open(self.url)
        self.input(self.search, name)
        self.click(self.sear_btn)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    name = '秋水'
    lp = LoginPage(driver)
    lp.login(name)

# 继续封装日志，把日志信息又要输出到控制台又要输出到日志里面
