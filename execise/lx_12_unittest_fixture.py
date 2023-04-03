import unittest
# 1. 打开浏览器(整个测试过程中就打开一次浏览器) 类级别
# 2. 输入网址(每个测试方法都需要一次) 方法级别
# 3. 输入用户名密码验证码点击登录(不同的测试数据) 测试方法
# 4. 关闭当前页面(每个测试方法都需要一次) 方法级别
# 5. 关闭浏览器(整个测试过程中就关闭一次浏览器) 类级别
class testlogin(unittest.FunctionTestCase):
    def setUp(self) -> None:
        print('输入网址...')
    def tearDown(self) -> None:
        print('关闭当前页面...')
    def test_1(self):
        print('输入正确的用户名和密码')
    def test_2(self):
        print('输入正确的用户名和密码')
    @classmethod
    def setUp(self) -> None:
        print('————打开浏览器')
    @classmethod
    def teardown(self) -> None:
        print('————打开浏览器')
    