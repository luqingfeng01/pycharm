'''题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

程序源代码：'''
p = [31,28,31,30,31,30,31,31,30,31,30,31] #平年
w = [31,29,31,30,31,30,31,31,30,31,30,31] # 闰年
year = int(input("请输入年份"))
moth= int(input("请输入月份"))
day = int(input("请输入日"))

arr = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = day
for i   in range(0,moth-1):
    sum +=arr[i]

if year%4 ==0:
    if year