'''
1. a=30, b=26   4  PASS
2. a=10   参数缺失  PASS
3. a='abc' b=2  参数必须为int PASS
4. a=2 b 5
5. a=2 b 2
....

'''
import requests
import pytest
from datetime import datetime


def test_sub_01():
    url = 'http://127.0.0.1:5002/sub'
    data = {"a": 30, "b":2}  # 转成字典
    res = requests.post(url, json=data)
    res_dict = res.json()  # 将响应数据转为字典，只有json格式的响应数据可以转字典
    # 断言
    print(res_dict)
    assert 1 == res_dict.get('code'), '响应信息code应为1'   # 期望值 1   实际值res_dict.get('code')
    assert "成功" == res_dict.get("msg")
    assert 28 == res_dict.get('result')


def test_sub_02():
    url = 'http://127.0.0.1:5002/sub'
    data = {"a": 30}  # 转成字典
    res = requests.post(url, json=data)
    res_dict = res.json()  # 将响应数据转为字典，只有json格式的响应数据可以转字典
    # 断言
    print(res_dict)
    assert 0 == res_dict.get('code')   # 期望值 1   实际值res_dict.get('code')
    assert "参数缺失" == res_dict.get("msg")
    assert res_dict.get('result') is None


def test_sub_03():
    url = 'http://127.0.0.1:5002/sub'
    data = {"a": 'abc', "b": 2}  # 转成字典
    res = requests.post(url, json=data)
    res_dict = res.json()  # 将响应数据转为字典，只有json格式的响应数据可以转字典
    # 断言
    print(res_dict)
    assert 2 == res_dict.get('code')   # 期望值 1   实际值res_dict.get('code')
    assert "参数必须为int类型" == res_dict.get("msg")
    assert res_dict.get('result') is None

if __name__ == '__main__':
    name = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    pytest.main(['test_sub.py', '-v', '--html={}.html'.format(name)])
