#coding=utf-8
import unittest
from model import function,myunit
from page_object.mtds_xz_service_no import *
from time import sleep
class xzscTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_mtdsliucheng1(self):
        pl = "2"  # pl的值：1 为橱柜   2为衣柜  3为两个服务单都有
        print (u'开始新增服务号测试')
        xz_service_no(self.dr).login_1("CCCCCC")
        service =xz_service_no(self.dr).service_no(pl,u"小武设计")
        xz_service_no(self.dr).chuchi(service[0])
        print (u"完成初尺")
        xz_service_no(self.dr).tijiao()
        print ("完成出设计图")
        xz_service_no(self.dr).tijiao()
        print ("完成出水电图")
        xz_service_no(self.dr).tijiao()
        print ("完成出效果图")
        xz_service_no(self.dr).tijiao()
        print ("完成出报价表")
        xz_service_no(self.dr).tijiao()
        print ("完成方案审核")
        xz_service_no(self.dr).tijiao()
        print ("完成合同下单")
        xz_service_no(self.dr).tijiao()
        print ("完成合同审图")
        xz_service_no(self.dr).tijiao()
        print ("完成合同审价")
        xz_service_no(self.dr).tijiao()
        print ("完成签约预约")
        xz_service_no(self.dr).hetongqianding()
        print ("完成合同签订" )
        if pl=="1":
            xz_service_no(self.dr).cg_dingdanxiadan()
        else:
            xz_service_no(self.dr).yg_dingdanxiadan()
        sleep(2)
        function.insert_img(self.dr,u"新增服务号截图.png")

if __name__ == '__main__':
    unittest.main()
