from time import sleep

from selenium import webdriver

'''
写一个简单实现的自动化测试脚本
这是一个hellWord，但是这个代码涵盖70%的操作行为
'''
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('selenium')
'''
webdriver.Chrome().find_element().send_keys('selenium')
首先获取浏览器对象，在基于查找元素行为获取到页面中对应的
webelement对象，在基于对象执行一次TXT输入操作对象
'''

driver.find_element_by_id('su').click()
sleep(2)
driver.quit()


