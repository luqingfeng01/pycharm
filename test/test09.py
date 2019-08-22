'''题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。

程序源代码：'''


import time

a = [1,2,3,4]
for i in range(len(a)):
    print(a[i])
    time.sleep(1)