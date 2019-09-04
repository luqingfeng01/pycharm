#1.导入Flask request
from flask import Flask,request,jsonify

#2从当前模块实例化一个Flask对象
app = Flask(__name__)


#3.写个函数
#4.挂载接口地址
@app.route("/add",methods=["get","post"])
def add():
    a = request.args.get("a")   #是请求url参数组成的字典
    b = request.args.get("b")  #从请求中提取a,b两个参数的值
    print(a,type(a),type(b))

    if a is None or b is None:
        return jsonify({"code": 1, "msg": "a或者b不能为空", "result": None})
    elif not isinstance(a, int) or not isinstance(b, int):
        return jsonify({"code": 2, "msg": " 返回的不是int类型", "result": None})
    else:
        return jsonify({"code": 0, "msg": "成功", "result": a + b})
#减法函数
@app.route("/sub",methods=["get","post"])
def sub():
    a = request.form.get("a")
    b = request.form.get("b")


    if a is None or b is None:
        return jsonify({"code":1,"msg":"a或者b不能为空","result":None})
    elif not isinstance(a,int) or not isinstance(b,int):
        return jsonify({"code":2,"msg":" 返回的不是int类型","result":None})
    else:
        return jsonify({"code":0,"msg":"成功","result":a-b})




if __name__ == '__main__':    #如果是从本模块运行
    app.run(port=5002)

