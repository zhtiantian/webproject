'''
关键字驱动：将selenium中常用的操作行为，封装成自定义的函数，以便于直接调用
selenium本身是一个大型的超市，这里面什么都有，我们将需要的东西先买回来，放在家里面
当买回来的东西不够用了，再去超市买点回来
selenium中常用的所有关键字，结合自身需要，将其提取并二次封装，保存至自定义类中
往后在调用selenium执行自动化时，直接调用自定义类即可
'''
from time import sleep

from selenium import webdriver
# 自己家。关键字驱动类,
# 判断用什么浏览器
def open_browser(type_):
    try:
        driver = getattr(webdriver,type_)
    except:
        driver =webdriver.Chrome()
    return driver


class Webkey:
    # 构造函数，实例化Webkey对象
    def __init__(self,type_):
        self.driver=open_browser(type_)
    # 访问URL
    def open(self,url):
        self.driver.get(url)
    # 定位元素
    def locator(self,loc):
     return self.driver.find_element(*loc)
    # 输入
    def input(self,loc,txt):
        self.loactor(loc).send_keys(txt)
    # 点击
    def click(self,loc):
        self.loactor(loc).click()
    # 等待
    def wait(self,time):
        sleep(time)
    # 退出
    def quit(self):
        self.driver.quit()





