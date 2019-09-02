# -*-encoding:utf-8-*-
from locust import HttpLocust, TaskSet, task
from locust.clients import HttpSession
import re, random, json
import MyLog

"""
MyLog 自定义日志
使用HttpSession对象提交接口请求进行session信息的关联，
然后通过json或re 对页面内容进行提取，并把返回的结果作为检查点进行比较
思路：
1.将下单的每个步骤对应的请求分别封装到不同的方法中，并在方法中设置检查点进行判断响应结果是否正确
2.将用户信息在on_start()方法中初始化，如果数据量少的话，可以直接在脚步中直接配置，如果用户数据量大的话，可以放到txt文档中，再on_start()中读取即可
3.将接口中的用户信息参数进行参数化
4.按下单流程的各个步骤对应的方法，按顺序进行调用
5.调用压测脚本

"""


class loginHttpSession(TaskSet):
    # 登录并购买商品压力测试

    def on_start(self):
        """
        测试数据初始化
        1.创建session会话，提供给后面的请求
        2.初始化请求头的信息
        3.初始化用户信息（用户信息参数化）
        4.引用自定义日志
        """
        self.session = HttpSession(base_url="http://localhost:8081/tshop/")

        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br"
        }

        self.userinfo = {
            0: ["123@qq.com", "123456"],
            1: ["223@qq.com", "123456"],
            2: ["333@qq.com", "123456"]
        }

        self.log = MyLog.MyLog().get_logger()

    def get_user_info(self):
        # 获取随机用户ID
        user_id = random.randint(0, len(self.userinfo) - 1)
        return user_id

    def index(self):
        # 打开商城首页
        return self.session.get("/")

    def input_username(self, loginToken, uname):
        # 进入输入用户名页面
        # 需要传送session和登录token值
        # 返回响应信息response，和userId
        input_url = "index.php"
        param = {
            "con": "ajax",
            "act": "account",
            # "account":"123@qq.com"
            "account": uname,  # 参数化用户名信息
        }

        # self.log.debug("[input_username]:userId=%s" %userId)   #打印日志
        # response=self.session.post(input_url,params=param,headers=self.header)
        with self.session.post(input_url, params=param, headers=self.header, catch_response=True) as response:
            # 获取请求详情数据，并设置检查点
            print(response.text)
            response_value = response.text
            print(type(response_value))
            # 由于返回的数据是unicode类型，也就是字符串，所以只能截取有效数据进行后面的检查点的判断
            status = response_value[response_value.find('"status":') + len('"status":'):response_value.find(",")]
            msg = response_value[response_value.find('"msg":"') + len('"msg":"'):response_value.find('"}')]
            if status != "false":
                response.failure("input_username: status error!")
            elif msg != "\u6b64\u7528\u6237\u5df2\u7ecf\u6ce8\u518c":
                response.failure("input_username: msg error!")

            return response, uname

    def submit_login(self, loginToken, uname, upwd):
        # 输入用户名和密码提交登录
        # 需要传递loginToken，和userId用于用户登录
        # 返回响应信息response，和userId
        login_url = "index.php?con=simple&act=login_act"

        bodys = {
            "redirectURL": "/tshop/",
            # "account":"123@qq.com",
            # "password":"123456",
            "account": uname,  # 参数化用户名
            "password": upwd,  # 参数化密码
            "tiny_token_login": loginToken,
        }
        # self.log.debug("[submit_login]:userId=%s" %userId)

        with self.session.post(login_url, data=bodys, headers=self.header, catch_response=True) as response:
            text = response.text
            page_text = re.compile(r'<div class="sub-1">(.+)?-')
            page_userinfo = page_text.search(text)
            userinfo = page_userinfo.group(1)
            print(userinfo)
            print(uname)
            if userinfo.find(uname) < 0:  # str的find方法如果找不到元素，返回值为-1，所以判断小于0表示，在userinfo中无登录的用户名
                response.failure("submit_login: not found username in page!")
            return response, uname

    def go_goods_details(self):
        # 进入商品详情页面
        # 返回响应数据
        goodsDetails_url = "index.php"
        params = {
            "con": "index",
            "act": "product",
            "id": "16"
        }

        # response=self.session.get(goodsDetails_url,data=params,headers=self.header)
        with self.session.get(goodsDetails_url, data=params, headers=self.header, catch_response=True) as response:
            text = response.text
            page_text = re.compile(r'</span><b class="cart-total red" >(.+)?</b></span></span></div>')
            page_price = page_text.search(text)
            price = page_price.group(1)
            if price < 100:
                response.failure("go_goods_details: not found price!")

            return response

    def add_goods_tips(self, loginToken=None):
        # 在商品详情页面，点击进入到确认订单页面
        # 返回用户购物车清单的商品信息
        goods_tips_url = "index.php?con=index&act=goods_add&id=61&num=3"
        with self.session.get(goods_tips_url, headers=self.header, catch_response=True) as response:
            text = response.text
            page_text = re.compile(r"<li >(.+)?<em></em><i></i></li>")
            page_info = page_text.search(text)
            value = page_info.group(1)
            if value != "4、订购完成":
                response.failure("add_goods_tips: not found 4、订购完成")
            return response

    def fill_order_info(self):
        # 进入到填写订单信息页面
        # 使用正则表达式，抓取页面返回的order_Token
        # 返回响应数据与order_Token

        fill_order_url = "index.php?con=simple&act=order&cart_type=cart"

        with self.session.get(fill_order_url, headers=self.header, catch_response=True) as response:
            order_re = re.compile(r"'tiny_token_order' value='(.+)?'/>")
            order_token = None  # order_token赋默认值为None，如果取不到order_token以便下面进行判断，为None则抛出错误
            order_token = order_re.search(response.text).group(1)
            if order_token == None:
                response.failure("fill_order_info: not found order_token")

            return response, order_token

    def submit_order(self, orderToken, uname):
        # 提交订单
        # 需传递填写订单信息页面的orderToken，对提交订单进行参数化
        # 根据userId，登录的userId来区分不同用户的收货地址id
        # 返回响应信息，与orderToken
        sub_order_url = "index.php?con=simple&act=order_act"

        bodys = {
            "address_id": "30",
            "payment_id": "1",
            "user_remark": "",
            "invoice_type": "0",
            "invoice_title": "",
            "cart_type": "",
            "tiny_token_order": orderToken
        }

        # 根据不同的userId更新参数中的地址id，确保每个用户的收货地址正确
        if uname == "123@qq.com":
            bodys["address_id"] = "30"
        elif uname == "223@qq.com":
            bodys["address_id"] = "31"
        elif uname == "333@qq.com":
            bodys["address_id"] = "32"
        else:
            print("userId not found !!!")
        # self.log.debug("[submit_order]:userId=%s,address_id=%s" %(userId,bodys["address_id"]))

        with self.session.post(sub_order_url, data=bodys, headers=self.header, catch_response=True) as response:
            text = response.text
            textview = re.compile(r'<span><i class="icon-success-48"></i>(.+)?</span>')
            re_result = textview.search(text)
            page_info = re_result.group(1)
            # if page_info!="订单已成功提交！":
            #   response.failure("submit_order:not found 订单已成功提交！")
            return response, orderToken

    def logout(self):
        # 下单成功后，退出登录
        logout_url = "index.php?con=simple&act=logout"
        with self.session.get(logout_url, headers=self.header) as response:
            return response

    @task
    def go_shopping(self):
        # 购买商品流程：登录->进入商品详情页面->将商品添加到购物车->进入填写订单信息页面->提交订单

        user_id = self.get_user_info()  # 获取用户id
        username = self.userinfo[user_id][0]
        upassword = self.userinfo[user_id][1]

        self.index()  # 进入商城首页

        laster_url = "index.php?con=simple&act=login"

        first_reponse = self.session.get(laster_url, headers=self.header)
        lg_page = first_reponse.text

        re_token = re.compile(r"name='tiny_token_login' value='(.+)?'/>")

        # 通过正则表达式获取登录页面的token信息
        re_result = re_token.search(lg_page)
        lg_token = None
        if re_result:
            lg_token = re_result.group(1)

        # #输入用户名页面,并获取login_token 信息
        inp_username_response = self.input_username(loginToken=lg_token, uname=username)
        inp_username_userId = inp_username_response[1]  # 返回输入用户名时，参数化的userId

        # # #输入账号、密码，并提交登录
        sub_login_response = self.submit_login(loginToken=lg_token, uname=username, upwd=upassword)
        sub_login_userId = sub_login_response[1]  # 返回用户登录时，参数化的userId

        # #进入到商品详情页面
        goods_details_response = self.go_goods_details()
        # # print goods_details_response.text

        # #进入购物车清单页面
        goods_tips_response = self.add_goods_tips()
        # # print goods_tips_response.text

        # #点击购物车清单页面的-【立即支付】，跳转到填写订单信息页面
        fill_order_response = self.fill_order_info()
        orderToken_value = fill_order_response[1]

        # #点击填写订单信息页面【确认支付】按钮
        sub_order_response = self.submit_order(orderToken=orderToken_value, uname=username)

        # 退出用户登录状态
        logout = self.logout()


class WebUserLocust(HttpLocust):
    task_set = loginHttpSession