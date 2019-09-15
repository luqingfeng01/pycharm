import pickle as p

class person:
    notes={}
    def add(self):
        name = input('请输入要添加的联系人姓名')
        if name in person.notes:
            print('该联系人已经存在')
        else:
          telephone =  (input('请输入联系人电话号码'))
          addr =  (input('请输入联系人地址'))
          label={'电话':telephone,'地址':addr}
          person.notes[name]=label

    def dele(self):
      name = (input('请输入要删除的联系人姓名'))
      if name in person.notes:
        del person.notes[name]
        print ("%s" %  person.notes.items())
      else:
        print('联系人 %s 不存在'%name)

    def search(self):
      name = (input('请输入要搜索的联系人姓名'))
      if name in person.notes:
         print('联系人 %s 的电话号码是 %s , 地址是 %s'%(name,person.notes[name]['电话'],person.notes[name]['地址']))
      else:
         print('联系人 %s 不存在'%name)

    def modify(self):
      name = (input('请输入要编辑的联系人姓名'))
      if name in person.notes:
        telephone =  (input('请输入联系人电话号码'))
        addr =  (input('请输入联系人地址'))
        person.notes[name]['电话']=telephone
        person.notes[name]['地址']=addr
      else:
         print('联系人 %s 不存在，若要编辑请选择添加选项'%name)
    def write(self):
      f = open('联系人.txt','wb+')
      p.dump(person.notes,f)
      f.close()
    def read(self):
      file = '联系人.txt'
      try:
        f = open(file ,'rb+')
        person.notes = p.load(f)
        f.close()
      except:
        f = open(file ,'w')
        f.close()
    def show(self):
      print(person.notes)

def menu():
    print('''系统提供以下功能
    1：添加
    2：删除
    3：修改
    4：搜索
    5：退出
    6: 显示全部联系人信息''')

people = person()
people.read()
while True:
  try:
    menu()
    choice = int(input('请输入相应数字操作'))
    if choice==1:
        people.add()
    elif choice ==2:
        people.dele()
    elif choice ==3:
        people.modify()
    elif choice ==4:
        people.search()
    elif choice ==5:
        people.write()
        break
    elif choice==6:
        people.show()
    else:
        print('输入不合法，请输入合法数字')
  except ValueError:
      print('请输入数字选项')
