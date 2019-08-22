import logging
# #1 logging.basicConfig函数对日志的输出格式及方式做相关配置
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#
# #2.由于日志基本配置中设置为DEBUG，所以一下打印信息将会全部显示在控制台上
#
# logging.info("this is a logging info message")
# logging.debug("this is a logging debug message")
# logging.warning("this is a logging a warnig message")
# logging.error("this is a logging error message")
# logging.critical("this is a logging critical message")


# 五部将日志输入到文件

import  logging,os,time

#1、创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)   #Log等级总开关

#2、创建一个handler,用于写入日志文件
rq = time.strftime("%Y%m%d%H%M")
log_path = os.path.dirname(os.getcwd()+"/Logs/")
log_name = log_path + rq + ".log"
logfile = log_name
fh = logging.FileHandler(logfile,mode="w")
fh.setLevel(logging.DEBUG) #输入到file的log等级的开关

#3、定义handler的输入格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

#4、将logger添加到handler里面
logger.addHandler(fh)

#5、输出日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')

