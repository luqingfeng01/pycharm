'''题目：暂停一秒输出，并格式化当前时间。

程序分析：无。'''

import time

import time,datetime

TIME = datetime.datetime.now()
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))
time.sleep(1)
TIME = datetime.datetime.now()
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))