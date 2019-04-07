#coding=utf-8
import unittest
from model import myunit
from page_object.UCxzsc import *
class xzscTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_xzsc1_normal(self):
        i = 4
        while i < 20:
            i = i + 1
            print u"第", i, u"个商场"
            # print u'开始新增商场测试'
            Xzsc(self.dr).xzsc('OP.06073',"111111")
            # self.assertEqual( Xzsc(self.dr).type_xzscPass_hint(),"555555555555555555")
            sleep(3)
if __name__ == '__main__':
    unittest.main()
#
#'OP.02349'
#









