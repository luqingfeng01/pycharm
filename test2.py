'''题目: 给出一个字符串, 判断其是否是是合法的IP(IPv4)地址
思路

将字符串按"."分割成4段得到一个列表
逐个判断列表中的字符串是否数字格式并且在0~255之间, 是在新列表对应位置保存True, 不是保存False
判断新列表中是否有False'''



def is_ip4(ip:str) ->bool:
    """
       检查ip是否合法
       :param: ip ip地址
       :return: True 合法 False 不合法
       """
    return True if [1] * 4 == [x.isdigit() and 0<= int(x) <=255 for x in  ip.split(".")] else False

print(is_ip4("192.168.1.2"))



# def  is_ipv4(ip: str) -> bool:
#   '''
#     检查ip是否合法
#     :param: ip ip地址
#     :return: True 合法 False 不合法
#     '''
#   return True  if [1] * 4 == [x.isdigit() and 0 <= int(x) <= 255 for x in ip.split(".")] else False
#
# print(is_ipv4("192.168.1.2a0"))

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(7))



'''题目: 给出一个字符串, 判断其是否是是合法的IP(IPv4)地址
思路

将字符串按"."分割成4段得到一个列表
逐个判断列表中的字符串是否数字格式并且在0~255之间, 是在新列表对应位置保存True, 不是保存False
判断新列表中是否有False'''

