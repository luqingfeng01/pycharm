data = {
    'a': 3,
    'b': 5
}

def add1(a,b):
    return a+b

print(add1(1,2))


# 定义函数
def add2():
    print(data)
    a = data['a']
    b = data['b']
    return a+b


print(add2())