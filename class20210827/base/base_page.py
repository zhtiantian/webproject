# 工具类：又称作基类，用于提供所有常用的函数，便于页面对象类进行页面中的元素操作
#     selenium类是一个大型超市，我们获取需要的内容，放在自己家，在需要用到这些东西师，直接从家里面操作
#     封装selenium常用的基本内容
#     访问URL
#     输入
#     点击
#     元素定位

from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
# import sys

#创建构造函数
#创建一个基类

# 定义关键字类，关键字封装形态
def browser(type_):
    # 定义driver的值：判断type是什么内容。则生成对应的浏览器对象即可
    try:
        driver = getattr(webdriver,type_)
    except:
        driver = webdriver.Chrome()
    return driver

class BasePase:
    # driver = webdriver.chrome
    #初始函数
    # def __init__(self,driver):
    #     self.driver = driver
    def __init__(self,type_):
        self.driver = browser(type_)

    #访问URL
    def open(self):
     return self.driver.get(self.url)


    # 元素定位:能够满足各种方法的定位元素的操作，利用元组代替(name,value)
    def locator(self,loc):
       return self.driver.find_element(*loc)


    # 输入
    def input_(self,loc, txt):
        return self.locator(loc).send_keys(txt)

    # 点击
    def click(self,loc):
        return self.locator(loc).click()
    # 窗口最大化
    def max(self):
        self.driver.maximize_window()

    # 关闭
    def quit(self):
        self.driver.quit()


    ## 读取配置文件，键值对，传值，登录用户密码
    def UserPwd(self,value1,value2):
        fg = configparser.ConfigParser()
        fg.read('../data/config.ini',encoding='utf-8-sig')
        return fg.get(value1,value2)

    #读取配置文件,读取添加银行卡信息,用数列的形式读取数据
    # items = conf.items('mysql')
    # print('获取指定section下所有的键值对', items)
    def Bankcard(self,value1):
        fg = configparser.ConfigParser()
        fg.read('../data/config.ini',encoding='utf-8-sig')
        return fg.items(value1)



