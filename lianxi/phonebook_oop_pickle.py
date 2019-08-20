'''通讯录（面向对象）'''


"""
龙腾测试dev课程，通讯录程序
实现一个简单的通讯录，包含增删改查


编写一个通讯录程序，实现增删改查功能
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


## 四、使用面向对象实现该通讯录
#### 1.设计数据结构
* 记录类 Record
* 通讯录类 PhoneBook

#### 2. 类方法设计
* Record __init__、 set_number
* PhoneBook __init__、add_record、query_record、change_record、delete_record
#### 3. 菜单设计不变
"""


import pickle

class Record():

    global_id = 0
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        Record.global_id += 1
        self.record_id = Record.global_id

    def set_number(self,phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return "{}\t{}\t{}".format(self.record_id, self.name, self.phone_number)

class PhoneBook:

    def __init__(self):
        self.data = []

    def input_record(self):
        name = input("请输入姓名:")
        phone_number = input("请输入电话:")
        record = {"name": name, "phone_number": phone_number}
        return record


    def add_record(self,record):
        self.data.append(record)



    def query_record(self,name):
        query_result = []
        query_ids = []
        for record in self.data:
            if record.name == name:
                query_ids.append(record.record_id)
                query_result.append(record)
        return query_ids, query_result


    def delete_record(self,name):
        query_ids, query_result = self.query_record(name)
        if len(query_ids) == 0:
            print("不存在")
        else:
            if len(query_result) > 1:
                for record in query_result:
                    print(record)
                record_id = input("请选择要删除的id:")
                if int(record_id) in query_ids:
                    for record in self.data:
                        if int(record_id) == record.record_id:
                            self.data.remove(record)
                else:
                    print("输入错误!!!")
            else:
                print(query_result[0])
                while True:
                    s = input("是否确认删除(Y/N):")
                    if s in ["Y", "N"]:
                        if s == "Y":
                            self.data.remove(query_result[0])
                        else:
                            pass
                        break
                    else:
                        print("输入错误!!!")


    def change_record(self,name):
        query_ids, query_result = self.query_record(name)
        if len(query_ids) == 0:
            print("不存在!!!")
        else:
            if len(query_result) > 1:
                for record in query_result:
                    print(record)
                record_id = input("请选择要修改的id:")
                if int(record_id) in query_ids:
                    for record in self.data:
                        if int(record_id) == record.record_id:
                            phone_number =input("请输入修改后的电话号码:")

                            record.set_number = phone_number

                            print("修改成功")
                            break
                else:
                    print("输入错误!!!")
            else:
                print(query_result[0])
                phone_number = input("请输入修改后的电话号码:")

                query_result[0].set_number(phone_number)

                print("修改成功")

    def save(self):
        with open("/tmp/data.dat","wb") as  f:
            pickle.dump(self.data,f)

    def load(self):
        with open("/tmp/data.dat","rb") as f:
            self.data = pickle.load(self.data,f)


if __name__ == "__main__":
    phonebook = PhoneBook()


    try:
        phonebook.load()
        Record.global_id = phonebook.data[-1].record_id
    except Exception:
        print("数据不存在")
    while True:
        menu = """
        通讯录
        1. 添加
        2. 查找
        3. 删除
        4. 修改
        5. 退出
        """
        print(menu)
        s = input("请选择操作:")
        if s in ["1", "2", "3", "4", "5"]:

            if s == "1":
                name = input("请输入姓名:")
                phone_number = input("请输入电话:")
                record = Record(name,phone_number)
                phonebook.add_record(record)
                print(record)
            if s == "2":
                name = input("请输入姓名:")
                query_ids, query_result = phonebook.query_record(name)
                if len(query_ids) == 0:
                    print("不存在")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record.record_id, record.name, record.phone_number))
            if s == "3":
                name = input("请输入姓名:")
                phonebook.delete_record(name)
            if s == "4":
                name = input("请输入姓名:")
                phonebook.change_record(name)
            if s == "5":
                break
        else:
            print("输入错误")
            continue

