'''2、M与N的数学运算：用户输入两个数 M 和 N，其中 N 是整数，计算M 和 N 的5种数学运算结果，并依次输出，结果间用空格分隔。

5种数学运算分别是：M 与 N 的和、M 与 N 的乘积、M 的 N 次幂、M除 N 的余数、M 和 N 中较大的值。'''

M = int(input())
N =int(float(input()))

list =[]
list.append(str(M+N))
list.append(str(M*N))
list.append(str(M**N))
list.append(str(M/N))
if M >N:
    list.append(str(M))
else:
    list.append(str(N))
print(" ".join(tuple(list)))