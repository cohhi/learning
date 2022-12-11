"""
http://hmshop-test.itheima.net/Home/user/login.html
测试:
    1. ：
        正确的用户名
        正确的密码
        正确的验证码
    2. ：
        错误的用户名
        正确的密码
        正确的验证码
    3. ：
        正确的用户名
        错误的密码
        正确的验证码
    4. ：
        正确的用户名
        正确的密码
        错误的验证码

"""
import unittest
from selenium import webdriver
from time import sleep
import time


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:  # 夹具开始
        print("开始测试....")
        self.starttime = time.time()
        self.driver = webdriver.Chrome()
        self.driver.get('http://hmshop-test.itheima.net/Home/user/login.html')
        # 打开网页
        self.driver.maximize_window()
        # 最大化
        self.username = self.driver.find_element_by_css_selector('#username')
        # 用户名
        self.password = self.driver.find_element_by_css_selector('#password')
        # 密码
        self.code = self.driver.find_element_by_css_selector('#verify_code')
        # 验证码
        self.message = self.driver.find_element_by_css_selector('.J-login-submit')
        # 登录按钮

    def tearDown(self) -> None:  # 夹具结束
        endtime = time.time()
        print("测试结束...")
        print("本次测试用时:{}".format(endtime - self.starttime))
        self.driver.quit()  # 退出浏览器

    def test_login_ok(self):
        print('全部正确')
        self.username.send_keys('13600001111')
        self.password.send_keys('123456')
        self.code.send_keys('8888')
        self.message.click()
        sleep(2)
        userinfo = self.driver.find_element_by_css_selector('.userinfo')
        if userinfo.text == '13600001111':
            print('测试成功')
        else:
            print('测试失败')

    def test_login_username(self):
        print('错误的用户名')
        self.username.send_keys('13612341111')
        self.password.send_keys('123456')
        self.code.send_keys('8888')
        self.message.click()
        sleep(2)
        message = self.driver.find_element_by_css_selector('.layui-layer-content')
        if message.text == '账号不存在!':
            print('测试成功')
        else:
            print('测试失败')

    def test_login_password(self):
        print("错误的密码")
        self.username.send_keys('13600001111')
        self.password.send_keys('111111')
        self.code.send_keys('8888')
        self.message.click()
        sleep(2)
        message = self.driver.find_element_by_css_selector('.layui-layer-content')
        if message.text == '密码错误!':
            print('测试成功')
        else:
            print('测试失败')

    def test_login_code(self):
        print('错误的验证码')
        self.username.send_keys('13600001111')
        self.password.send_keys('123456')
        self.code.send_keys('9999')
        self.message.click()
        sleep(2)
        message = self.driver.find_element_by_css_selector('.layui-layer-content')
        if message.text == '验证码错误':
            print('测试成功')
        else:
            print('测试失败')
