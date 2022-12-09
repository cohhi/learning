'''
有一个函数login, 这个函数接收用户名和密码两个参数,函数的功能判断用户名和密码是否正确
假设正确的用户名和密码是admin和123456,函数根据用户名和密码的情况返回 '登录成功' '密码错误' '用户名错误'

写3个测试用例方法,完成对这个方法的测试

admin 123456 登录成功
admin1 123456 用户名错误
admin 222222 密码错误
'''
import unittest


def login(username, pwd):
    if username == 'admin':
        if pwd == '123456':
            return '登录成功'
        else:
            return '密码错误'
    else:
        return '用户名错误'


class TestLogin(unittest.TestCase):
    def test_login_ok(self):
        result = ('admin', '123456')
        if result == "登录成功":
            print("正确的用户名,密码功能正常")
        elif result == "密码错误":
            print("正确的用户名,密码功能异常")

    def test_login_username_error(self):
        result = login('admin1', '123456')
        if result == "用户名错误":
            print("账户功能正常")
        elif result == "密码错误":
            print("账户功能功能异常")

    def test_login_pwd_error(self):
        result = login('admin', '22222')
        if result == "登录成功":
            print("密码功能正常")
        elif result == "密码错误":
            print("密码功能正常")
