
import os
from locust import HttpLocust, TaskSet, task
import re


def login(l):
    l.head = {  # 头部信息
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    l.loginparameter = {  # 参数信息
        "formhash": "1f3a2bb2",
        "referer": "http://localhost:8090/discuz/",
        "loginfield": "username",
        "username": "A12345",
        "password": "123456",
        "questionid": "0",
        "answer": ""
    }
    with l.client.post("/logging.php?action=login&loginsubmit=yes&floatlogin=yes&inajax=1",
                       headers=l.head, data=l.loginparameter, catch_response=True) as response:
        # 使用正则表达式获取返回的数据，进行检查点判断
        pattern = re.compile(
            r"\(\'messageleft\'\)\.innerHTML = \'<p>(.+)?</p>")
        page_content = response.content
        # print type(page_content)
        # print page_content
        reval = pattern.search(page_content)

        reval.group()
        if reval.group() != "('messageleft').innerHTML = '<p>欢迎您回来 新手上路 A12345</p>":
            response.failure(u"登录失败！")


def index(l):
    l.client.get("/")


def profile(l):
    l.client.get("/index.php")


class UserBebavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)


class WebsiteUser(HttpLocust):
    task_set = UserBebavior
    min_wait = 5000
    max_wait = 9000


# 执行脚本：run_test.py
# # -*-encoding:utf-8-*-

os.system("locust-script.py -f e:/py/login.py --host=http://localhost:8090/test ")
