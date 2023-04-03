# 学习unittest.TestLoader和TestRunner的使用
# 1.导包（unittest）
from importlib.abc import Loader
from pdb import run
import unittest
# 2.实例化创建加载对象
# Loader= unittest.TestLoader()
# 2.实例化创建加载对象并添加用例
# unittest.TestLoader().discover(”用例所在的路径“，”用例的代码文件名“)
#  2.实例化创建加载对象并添加用例,用例所在的路径，建议使用相对路径，用例的代码文件名可以使用*通配符
suite=unittest.TestLoader().discover('./execise','lx_12_unittest_testcase1.py')
# 注意：当testloader和testsuite添加了相同的测试用例时，不重复执行，只执行一次


# 4.实例化运行对象
runner=unittest.TextTestRunner()
# 5.使用运行对象去执行套件对象：运行对象.run(suite)
runner.run(suite)
