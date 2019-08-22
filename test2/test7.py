'''7、完美立方：找到大于1的4个整数满足完美立方等式：a3=b3+c3+d3（例如123=63+83+103）。
编写一个程序，对于任意给定的正整数N（N ≤100），
寻找所有的四元组（a,b,c,d），满足a3=b3+c3+d3，其中1<a，b，c，d≤N'''

n = int(input())  # n范围内的立方数

list_cube = [0]  # 用于存储立方数的列表
for i in range(1, n + 1):
    list_cube.append(i * i * i)

for a in range(6, n + 1):
    for b in range(2, a - 1):
        if list_cube[a] < (list_cube[b] + list_cube[b + 1] + list_cube[b + 2]):
            break
        for c in range(b + 1, a):
            if list_cube[a] < (list_cube[b] + list_cube[c] + list_cube[c + 1]):
                break
            for d in range(c + 1, a):
                if list_cube[a] == (list_cube[b] + list_cube[c] + list_cube[d]):
                    print("Cube=%d,Tripe=(%d,%d,%d)" % (a, b, c, d))

