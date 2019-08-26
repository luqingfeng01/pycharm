'''二分查找法
二分查找算法也称折半查找，基本思想就是折半，和平时猜数字游戏一样，比如猜的数字时67，猜测范围是0-100，
则会先猜测中间值50，结果小了，所以就会从50-100猜测，中间值为75，结果大了，
又从50-75猜测中间值，一直到猜中为止。因此，二分查找有一个限制就是原先数组需要是一个有序数组。代码如下：
'''

def binarysearch(a, num):
    length = len(a)
    low = 0
    high = length - 1
    while low <= high:
        mid = high +low // 2 ##使用(low+high)/2会有整数溢出的问题
        if a[mid] < num:
            low = mid + 1
        elif a[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    L = [1, 3, 4, 8, 22, 65, 73, 100]
    print(L)
    a  = binarysearch(L,100)
    print(a)