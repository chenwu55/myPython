#coding=utf-8
import unittest
from model import function,myunit
from page_object.mtds_xz_service_no import *
from time import  sleep
pl = "2"   # pl的值：1 为橱柜   2为衣柜  3为两个服务单都有
class xzscTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login2_normal(self):
        print u'开始新增服务号测试'
        xz_service_no(self.dr).login_1("CCCCCC")
        xz_service_no(self.dr).service_no(pl)
        # xz_service_no(self.dr).sousuo("DS00004411618100800016")
        # xz_service_no(self.dr).yg_dingdanxiadan()
        sleep(2)
        function.insert_img(self.dr,u"新增服务号截图.png")


if __name__ == '__main__':
    unittest.main()
