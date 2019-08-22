import logging
import os


# mysql的数据库配置
host = "115.28.108.130"
user = "test"
password = "123456"
database = "longtengserver"
port =  3306


#邮件配置

sender = '260137162@qq.com' #发送方
receiver = "274832258@qq.com"  #接受方
emailusername = "260137162@qq.com"  # 登录邮箱的用户名
emailpassword = "deynljbeluxqbjhh"             # 登录邮箱的密码,请配置自己的
server = "smtp.qq.com"  # smtp服务器


#项目路径

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#数据路径
datadir = os.path.join(basedir,"Data/")

#报告路径
reportdir = os.path.join(basedir,"Report/")

#日记路径
logdir = os.path.join(basedir,"Log/")
logpath = os.path.join(logdir,".log.txt")



logger = logging.getLogger("AutoProject")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logpath,encoding="utf-8")
datafmt = "%Y-%m-%d-%H:M%:S%"
fm = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt=datafmt)
fh.setFormatter(fm)
logger.addHandler(fh)

logging.getLogger("rquests").setLevel(logging.WARNING)

if __name__ == '__main__':
    logging.info("this is test")