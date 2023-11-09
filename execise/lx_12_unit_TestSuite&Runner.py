# 学习unittest.TestSuite和TestRunner的使用
# 1.导包（unittest）
from pdb import run
import unittest
# 2.实例化创建套件对象
suite = unittest.TestSuite()
#3.使用套件对象添加用例方法(添加用例方法后会自然出现修复选项来导入模块)
from execise.lx_12_unit_testcase1 import TestDemo1
# from execise.lx_12_unit_testcase2 import TestDemo2

# 方式一：套件对象.addTest（测试类名（'方法名'）），建议直接复制不要手写
suite.addTest(TestDemo1('test_method1'))
suite.addTest(TestDemo1('test_method2'))
# suite.addTest(TestDemo2('test_method1'))
# suite.addTest(TestDemo2('test_method2'))
# 方式二：将一个测试类中的所有方法进行添加：套件对象.addTest(unittest.unittest.makeSuite(测试类名))
            # suite.addTest(unittest.makeSuite(TestDemo1))
            # suite.addTest(unittest.makeSuite(TestDemo2))

# 4.实例化运行对象
runner=unittest.TextTestRunner()
# 5.使用运行对象去执行套件对象：运行对象.run(suite)
runner.run(suite)
