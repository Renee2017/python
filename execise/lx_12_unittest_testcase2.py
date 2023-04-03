#1.导包unittest
import unittest

#2.自定义测试类，需要继承unittest模块中的TestCase类
class TestDemo2(unittest.TestCase):
    #3.在测试类中书写测试方法，即用例代码，注意必须以test_开头
    def test_method1(self):
        print('测试⽅法 1')
    def test_method2(self):
        print('测试⽅法 2')
#4.执行用例，在游览测试栏中运行对应的类或测试方法。可以正常运行时看“python测试日志”，不能运行查看“python”。打开vscode的控制面板，配置unittest:ctrl+shift+p


