'''题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]'''

a = [2,23,1,2,3]

b= a[:]
print(b)


import copy

a = [2,23,1,2,3]
b =copy.copy(a)
print(b)