'''题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：
0、1、1、2、3、5、8、13、21、34、……。
(n-1)+(n-2)

在数学上，费波那契数列是以递归的方法来定义：'''


def factorial(n):
    if n == 1 or n ==2:
        return 1
    

    return factorial(n-1) +factorial(n-2)

if __name__ == "__main__":
    print(factorial(0))
