import logging

# 高级的日志，日志文件和控制台都会输出日志，一般情况下用的是这个日志文件
def test_logger():
    # 创建一个日志器
    logger = logging.getLogger()

    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 日志信息输出到控制台 ，创建一个控制台
    sh = logging.StreamHandler()
    # 把日志信息输出到控制台
    logger.addHandler(sh)
    fmt = '%(asctime)s  %(filename)s  %(levelname)s  %(funcName)s  %(message)s'

    # 创建一个格式器
    formator= logging.Formatter(fmt)
    #给控制台设置格式
    sh.setFormatter(formator)

    # 把日志信息输出到文件 创建一个文件 文件在哪
    fh = logging.FileHandler('../log/logs.log',encoding='utf-8')
    logger.addHandler(fh)
    # 设置文件格式
    fh.setFormatter(formator)
    # logger.info('日志信息')
    return logger
#
# 日志把他写在配置文件中
# 元素定位不到 1、让代码运行慢点 等待 3种等待 2、元素的定位写法有没有问题

