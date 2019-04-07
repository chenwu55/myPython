#coding=utf-8
import unittest
from model import function,myunit
from page_object.mtds_xz_service_no import *
from time import sleep
class xzscTest(myunit.StartEnd):
    def test_mtdsliucheng1(self):
        print u'开始衣柜流程测试'
        pl = "2"
        xz_service_no(self.dr).login_1("CCCCCC")
        service =xz_service_no(self.dr).service_no(pl)
        print u'完成分配设计师'
        xz_service_no(self.dr).chuchi(service[0])
        print u'完成初尺'
        xz_service_no(self.dr).tijiao()     # 出设计图
        xz_service_no(self.dr).tijiao()     # 出水电图
        xz_service_no(self.dr).tijiao()     # 出效果图
        xz_service_no(self.dr).tijiao()     # 出报价表
        xz_service_no(self.dr).tijiao()     # 方案确认
        xz_service_no(self.dr).tijiao()     # 合同下单
        xz_service_no(self.dr).tijiao()     # 合同审图
        xz_service_no(self.dr).tijiao()     # 合同审价
        xz_service_no(self.dr).tijiao()     # 签约预约
        xz_service_no(self.dr).hetongqianding()
        if pl=="1":
            xz_service_no(self.dr).cg_dingdanxiadan()
        elif pl=="2":
            xz_service_no(self.dr).yg_dingdanxiadan()
        print u'完成订单下单'
        sleep(2)
        function.insert_img(self.dr,u"完成流程截图.png")
if __name__ == '__main__':
    unittest.main()
