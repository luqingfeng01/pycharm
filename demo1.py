from flask import Flask,request,jsonify,render_template
#render_template渲染模板


app = Flask(__name__)

data = [
    {"case":"test_sub_01","result":"PASS"},
    {"case":"test_sub_02","result":"FAIL"},
    {"case":"test_sub_03","result":"PASS"},
    {"case":"test_sub_04","result":"PASS"},
]

@app.route("/login")
def login():
    return render_template("login.html",
                           tester="tim",
                           pass_num=3,
                           fail_num=0,
                           data=data
                           )

if __name__ == '__main__':
    app.run()