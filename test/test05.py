'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。
'''

x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
num = [x, y, z]
num.sort()          # 对列表进行升序排序
print ('这三个数由小到大的顺序为：',num)
rnum = [x, y, z]                  # 对列表进行降序排序
rnum.sort(reverse=True)
print ('这三个数由大到小的顺序为：',rnum)
