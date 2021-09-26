'''
日志：记录系统的一些信息，状态 日志文件中
作用：了解系统的运行状态，通过日志分析和定位错误问题
不需要安装直接引用
debug('调试的级别') 1级别
info('正常级别')  2级别
warning('警告级别') 3级别 程序有问题，但是不影响程序运行
error('错误级别') 4级别
critical('严重级别') 5级别

反应出日之错误信息的严重程度
'''
import logging

# 基础的日志文件：会出现乱码，控制台没有数据，一般不用这个方式，若不想出现乱码，需要修改源文件
def test_log():
    # 设置日志格式：时间、文件名、日志级别判断、调用函数或者方法名、日志的文本内容
    fm = '%(asctime)s  %(filename)s  %(levelname)s  %(funcName)s  %(message)s'
    # 设置日志级别
    logging.basicConfig(level=logging.INFO,format=fm,filename='../log/logs.log')
    return logging
# 用的时候，try:info  except:记录异常状态


    # logging.debug('调试的级别')
    # logging.info('正常级别')
    # logging.warning('警告级别')
    # logging.error('错误级别')
    # logging.critical('严重级别')