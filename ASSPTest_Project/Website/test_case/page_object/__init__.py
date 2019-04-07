#coding=utf-8
import unittest
from model import myunit
from page_object.Cgdianjiang import *
import time
from page_object.Basepage import *
changliang="ZSDJ-2018-003721"
class CgdianjiangTest(myunit.StartEnd):
    @unittest.skip('skip this case')
    def test_dianjiang_normal(self):
        i = 0
        while i <1:
            i = i + 1
            print u"第", i, u"次橱柜点将申请测试："
            now = time.strftime("%Y-%m-%d %H_%M_%S")+ u" 第"
            mum=str(i)
            jietu_name =now +mum + u"次点将申请截图.png"
            op=dainjianshenqing(self.dr)
            changliang=op.dianjiang('admin@S003059')
            sleep(2)
            self.assertEqual(op.dianjingFail_hint(),'')

            function.insert_img(self.dr,jietu_name)
            Shenhe(self.dr).shenhe('OP.14556',changliang,'111111')#经销部管理员（审核）	OP.14556	齐慧敏	经销部管理员
            Shenhe(self.dr).shenhe('OP.12695',changliang,'111111')#展示设计部总监（审核）	OP.12695	梁华蔚	展示设计总监
            Shangchuan(self.dr).tijiao('OP.00633',changliang,'111111')
            Shenhe(self.dr).shenhe('OP.00127',changliang,'111111')
    @unittest.skip('skip this case')
    def test_Cgliucheng_1(self):
        changliang=dainjianshenqing(self.dr).dianjiang('admin@S003059')
        return changliang


# 展示设计主管（审核）	OP.14316	胡国辉	展示设计主管
    # @unittest.skip('skip this case')
    def test_shenhe_31(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 展示设计部设计经理（审核）	OP.00468	姚建虹	展示设计经理
    # @unittest.skip('skip this case')
    def test_shenhe_32(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 展示设计部总监（审核	OP.12695	梁华蔚	展示设计部总监
    # @unittest.skip('skip this case')
    def test_shenhe_33(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 橱柜经销部各部总监（审核）	OP.07882	曾祥伟	经销部总监
    # @unittest.skip('skip this case')
    def test_shenhe_34(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 橱柜营销部副总（审核）	OP.14150	陈道品	营销副总经理
    # @unittest.skip('skip this case')
    def test_shenhe_35(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")





if __name__ == '__main__':
    unittest.main()