'''编写一个通讯录程序，实现增删改查功能
#### 1.设计数据结构
一条记录： 姓名，电话， id
一个通讯录：列表，里面元素为记录

#### 2. 函数设计
* 增加 add_record
* 查询 query_record
* 修改 change_record
* 删除 delete_record

#### 3. 菜单设计
* main函数
* while 循环
* 选择相应功能
示例
````

        通讯录
        1. 添加
        2. 查找
        3. 删除
        4. 修改
        5. 退出

请选择操作:1
请输入姓名:jia
请输入电话:123
添加成功

        通讯录
        1. 添加
        2. 查找
        3. 删除
        4. 修改
        5. 退出

请选择操作:
````
'''
record_dict = {}
recordid = 0


def add_record():
    name = input("请输入要添加的联系人姓名")
    if name in record_dict:
        print("用户已经存在")
    else:
        phone = input("请输入联系人电话")
        global recordid
        recordid += 1

        l = {"id": recordid, "电话": phone}
        record_dict[name] = l
        print("添加成功")


def query_record():
    name = input("请输入要查询的联系人姓名")
    if name in record_dict:
        print('id:%s\n联系人:%s \n电话号码是:%s ' %
              (record_dict[name]["id"], name, record_dict[name]['电话']))
    else:
        print("输入的名字不存在")


def change_record():
    name = input("请输入要修改的联系人名字")
    print(record_dict)
    if name in record_dict:
        phone = input("请输入要修改的电话")
        record_dict[name]["id"] = recordid

        record_dict[name]["电话"] = phone
        print("修改成功")
    else:

        print("联系人%s不存在" % name)


def delete_record():
    name = input("请输入要删除的联系人名字")
    if name in record_dict:
        del record_dict[name]
        print("删除成功")
    else:
        print('联系人 %s 不存在' % name)


if __name__ == '__main__':
    while True:

        meau = '''
            通讯录
            1. 添加
            2. 查找
            3. 删除
            4. 修改
            5. 退出
            '''
        print(meau)
        try:
            s = input("请输入对应数字")
            if s == "1":
                add_record()

            elif s == "2":
                query_record()
            elif s == "3":
                delete_record()
            elif s == "4":
                change_record()
            elif s == "5":
                break
        except Exception as f:
            print("输入有误:%s" % f)
