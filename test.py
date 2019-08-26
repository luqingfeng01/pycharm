'''题目
判断一个文本中的括号是否闭合,
如: text = "({[({{abc}})][{1}]})2([]){({[]})}[]", 判断所有括号是否闭合'''


test = '({[({{abc}})][{1}]})2([]){({[]})}[]'

def is_closed(test:str) ->bool:
    """
       判断文本中括号是否封闭
       :param:text 包含括号的文本字符串
       :returns: True无括号或所有括号全部封闭
                      False 存在括号不封闭
       """

    stack = []  # 创建一个栈   # 使用list模拟栈, stack.append()入栈, stack.pop()出栈并获取栈顶元素
    brackets = {")":"(","]":"[","}":"{"}  # 使用字典存储括号的对应关系, 使用反括号作key方便查询对应的括号
    for char in test:
        if char in brackets.values(): # 如果是正括号,入栈
            stack.append(char)
        elif char in brackets.keys():   # 如果是反括号
            if brackets[char] != stack.pop():  # 如果不匹配弹出的栈顶元素
                return False
    return True

print(is_closed(test))


