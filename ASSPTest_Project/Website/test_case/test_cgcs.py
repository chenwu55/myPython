#coding=utf-8
import unittest
from model import function,myunit
from page_object.SGshentubiao import *
from time import  sleep

class ShenheTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_shenhe2_normal(self):
        SGshentubiao(self.dr).sg_shentubiao('op.30513',"ZSDJ-2018-000147")
        sleep(2)
        # self.assertEqual(po.type_loginPass_hint(),u'退出登录')
        function.insert_img(self.dr,u"第 1 次测试截图.png")
        print u'第 1 次测试结束'


if __name__ == '__main__':
    unittest.main()





