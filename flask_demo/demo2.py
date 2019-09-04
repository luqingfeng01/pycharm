# 1. 导入Flask request
from flask import Flask,request,jsonify
# 2.从当前模块实例化一个Flask对象
app = Flask(__name__)
# 3. 写个函数
# 4. 挂载接口地址
@app.route('/add')
def add():
    a = request.args.get('a')   # request.args是请求url参数组成的字典
    b = request.args.get('b')   # 从请求中提取a,b两个参数的值
    sum = int(a) + int(b)   # 转换为整形进行相加
    return str(sum)    # 将结果转为字符串返回

# 写个减法函数 /sub
@app.route('/sub',methods=['post'])  # 只支持整形 数字
def sub():
    a = request.json.get('a')   # 1. 提取变量  request.args/form/json
    b = request.json.get('b')
    if a is None or b is None:
        return jsonify({"code":0,"msg":"参数缺失","result":None})

    if not isinstance(a,int) or not isinstance(b,int):
        return jsonify({"code":2,"msg":"参数必须为int类型","result":None})
    c = a - b    #  2. 业务操作
    return jsonify({"code": 1, "msg": "成功", "result": c})  # 组装响应并返回




if __name__ == '__main__':   # 如果是从本模块运行的
    app.run(port=5002)