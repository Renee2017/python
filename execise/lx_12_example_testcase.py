

import unittest


# from HTMLTestRunner import HTMLTestRunner

version=20
class TestDemo(unittest.TestCase):
    @unittest.skipIf(version>=20,"版本号大于等于20就跳过")
    def test_1(self):
        self.assertEqual(3,3)
    
        print('天气真好')
    def test_2(self):
        self.assertEqual(2,2)
        return '出去玩吧'
# suite=unittest.defaultTestLoader.discover('.','tools_1')
# file='report.html'
# with open(file,'wb') as f:
#         runner=HTMLTestRunner(f)
#         runner.run(suite)