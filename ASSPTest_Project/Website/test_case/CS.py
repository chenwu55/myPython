#coding=utf-8
import unittest
from model import function,myunit
from page_object.mtds_xz_service_no import *
from time import  sleep
class xzscTest(myunit.StartEnd):
    @unittest.skip('skip this case')
    def test_liucheng1(self):
        pl = "1"  # pl的值：1 为橱柜   2为衣柜  3为两个服务单都有
        print u'开始新增服务号测试'
        xz_service_no(self.dr).login_1("CCCCCC")
        service =xz_service_no(self.dr).service_no(pl)
        xz_service_no(self.dr).chuchi(service[0])
        xz_service_no(self.dr).hetongqianding()
        if pl=="1":
            xz_service_no(self.dr).cg_dingdanxiadan()
        else:
            xz_service_no(self.dr).yg_dingdanxiadan()
        sleep(2)
        function.insert_img(self.dr,u"新增服务号截图.png")

    # @unittest.skip('skip this case')
    def test_liuchen2(self):
        pl = "1"  # pl的值：1 为橱柜   2为衣柜  3为两个服务单都有
        print u'开始新增服务号测试'
        xz_service_no(self.dr).login_1("CCCCCC")
        xz_service_no(self.dr).chuchi("DS00004404818121200004")
        print u'完成初尺'
        xz_service_no(self.dr).tijiao()  # 出设计图
        xz_service_no(self.dr).tijiao()  # 出水电图
        xz_service_no(self.dr).tijiao()  # 出效果图
        xz_service_no(self.dr).tijiao()  # 出报价表
        xz_service_no(self.dr).tijiao()  # 方案确认
        xz_service_no(self.dr).tijiao()  # 合同下单
        xz_service_no(self.dr).tijiao()  # 合同审图
        xz_service_no(self.dr).tijiao()  # 合同审价
        xz_service_no(self.dr).tijiao()  # 签约预约
        xz_service_no(self.dr).hetongqianding()
        if pl=="1":
            xz_service_no(self.dr).cg_dingdanxiadan()
        else:
            xz_service_no(self.dr).yg_dingdanxiadan()
        sleep(2)
        function.insert_img(self.dr,u"新增服务号截图.png")

    @unittest.skip('skip this case')
    def test_liucheng3(self):
        pl = "4"  # pl的值：1 为橱柜   2为衣柜  3为两个服务单都有
        print u'开始新增服务号测试'
        xz_service_no(self.dr).login_1("CCCCCC")
        service = xz_service_no(self.dr).service_no(pl)
        xz_service_no(self.dr).chuchi(service[0])
        sleep(5)
        xz_service_no(self.dr).hetongqianding()
        if pl == "1":
            xz_service_no(self.dr).cg_dingdanxiadan()
        else:
            xz_service_no(self.dr).yg_dingdanxiadan()
        sleep(2)
        function.insert_img(self.dr, u"新增服务号截图.png")

    # @unittest.skip('skip this case')
    def test_liucheng4(self):
        pl = "4"  # pl的值：1 为橱柜   2为衣柜  3为两个服务单都有
        print u'开始新增服务号测试'
        xz_service_no(self.dr).login_1("CCCCCC")
        xz_service_no(self.dr).sousuo('DS00004404818111000002')
        xz_service_no(self.dr).yg_dingdanxiadan()
if __name__ == '__main__':
    unittest.main()
