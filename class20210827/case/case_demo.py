import unittest
from time import sleep


from selenium import webdriver

from base.base_page import BasePase
from page_object.login_page import LoginPage
from page_object.payment import Payment
# ddt数据驱动
# from ddt import ddt, file_data
# import yaml

# @ddt
class CaseDemo(unittest.TestCase):
    #测试用例
    # @file_data('../data/user.yml')
    # 作用域
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lg = LoginPage(cls.driver)
        cls.pays = Payment(cls.driver)

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()

    def test_01(self):
        # driver = webdriver.Chrome()
        # username = "ztt1"
        # password = "123456"
        # lg = LoginPage(driver)
        # 读取配置文件->需要单独读取工具类
        username = BasePase.UserPwd(self, 'login','username')
        password = BasePase.UserPwd(self,'login','password')
        self.lg.login(username,password)
        sleep(2)
    # def test_02(self):
    #     # pays = Payment(driver)
    #     self.pays.add_pay()
    #     sleep(2)


if __name__ == '__main__':
    unittest.main()