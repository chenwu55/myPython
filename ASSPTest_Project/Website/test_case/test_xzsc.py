#coding=utf-8
import unittest
from model import myunit
from page_object.UCxzsc import *
class xzscTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_xzsc1_normal(self):
        print u'开始新增商场测试'
        Xzsc(self.dr).xzsc('OP.02349',"111111")
        self.assertEqual( Xzsc(self.dr).type_xzscPass_hint(),"555555555555555555")
if __name__ == '__main__':
    unittest.main()










