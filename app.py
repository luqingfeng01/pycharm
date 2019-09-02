#1.导入Flask request
from flask import Flask,request

#2从当前模块实例化一个Flask对象
app = Flask(__name__)


#3.写个函数
#4.挂载接口地址
@app.route("/add")
def add():
    a = request.args["a"]   #是请求url参数组成的字典
    b = request.args["b"]   #从请求中提取a,b两个参数的值
    print(a,type(a),type(b))

    sum = int(a) +int(b)  #转换为整形进行相加
    print(sum,type(sum))
    return str(sum)   #将结果转为字符串返回
#减法函数
@app.route("/sub")
def minus():
    a = request.args["a"]
    b = request.args["b"]
    return str(float(a)-float(b))




if __name__ == '__main__':    #如果是从本模块运行
    app.run(port=5002)

