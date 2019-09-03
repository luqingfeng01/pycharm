""" 
@author: lileilei
@file: ddd.py 
@time: 2018/1/19 11:43 
"""
import xlrd
from seleniummaster.util import  log
# logs=log.log_message()
def huoqu_test(filepath,index):
    try:
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[index]
        print(me)
        nrows = me.nrows
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {}
            dict_canshu['id']=me.cell(i,0).value
            dict_canshu.update(eval(me.cell(i,2).value))
            dict_canshu.update(eval(me.cell(i,3).value))
            listdata.append(dict_canshu)
        return listdata
    except Exception as e:
        print(e)
        # logs.error_log('获取测试用例数据失败，原因：%s'%e)

if __name__ == '__main__':
    test =huoqu_test("E:\pycharm\seleniummaster\data\case.xlsx",0)

    print(test)
