import requests,datetime,time,pytest

def test_sub_03():
    url = "http:127.0.0.1:5002/sub"
    data = {"a":"abc","b":2}  #转出字典
    res = requests.post(url,josn=data)
    res_dict = res.json()
    #断言
    print(res_dict)
    assert  2 ==res_dict.get("code")
    assert "参数必须为int型"==res_dict.get("msg")
    assert res_dict.get("result") is None

if __name__ == '__main__':
    name = datetime
    pytest.main(["test_sub.py","-v","--html={}.html".format(name)])