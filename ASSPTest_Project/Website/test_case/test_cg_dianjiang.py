#coding=utf-8
import unittest
from model import myunit
from page_object.Cgdianjiang import *
import time
from page_object.Basepage import *


changliang="ZSDJ-2018-003718"
class CgdianjiangTest(myunit.StartEnd):

#商场管理员审核    OP.14556	齐慧敏	经销部管理员
    # @unittest.skip('skip this case')
    def test_shenhe_1(self):
        Shenhe(self.dr).shenhe('OP.14556',changliang,"111111")


#展示设计部总监（审核）	OP.12695	梁华蔚	展示设计总监
    # @unittest.skip('skip this case')
    def test_shenhe_10(self):
        Shenhe(self.dr).shenhe('OP.12695',changliang,"111111")


#展示设计师上传协议	OP.00633	陈冲	展示设计师
    # @unittest.skip('skip this case')
    def test_shenhe_11(self):
        Shangchuan(self.dr).tijiao('OP.00633',changliang,"111111")


#展示设计运营专员（审核）	OP.00127	黄丙凤	展示设计运营专员
    # @unittest.skip('skip this case')
    def test_shenhe_12(self):
        Shenhe(self.dr).shenhe('OP.00127',changliang,"111111")


#展示设计师上传	OP.00633	陈冲	展示设计师
    # @unittest.skip('skip this case')
    def test_shenhe_13(self):
        Shangchuan(self.dr).tijiao('OP.00633',changliang,"111111")


#营销中心经理	OP.13741	殷俊伟	营销中心经理
    # @unittest.skip('skip this case')
    def test_shenhe_14(self):
        Shenhe(self.dr).shenhe('OP.13741',changliang,"111111")


#审图设计师（审核）	OP.19882	杨路	审图设计师
    # @unittest.skip('skip this case')
    def test_shenhe_15(self):
        Shenhe(self.dr).shenhe('OP.19882',changliang,"111111")


#经销商（确认）	admin@S003059	黎老板	代理商
    # @unittest.skip('skip this case')
    def test_shenhe_16(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


#"审图设计师填写平面图审图表（审核）"	OP.19882	杨路	审图设计师
    # @unittest.skip('skip this case')
    def test_shenhe_17(self):
        Tianxiest(self.dr).shentubiao('OP.19882',changliang,"111111")


#设计主管（审核）	OP.14316	胡国辉	展示设计主管
    # @unittest.skip('skip this case')
    def test_shenhe_18(self):
        Shenhe(self.dr).shenhe('OP.14316',changliang,"111111")


#样板设计师上传	OP.13993	吴娟娟	样板设计师
    # @unittest.skip('skip this case')
    def test_shenhe_19(self):
        Shangchuan(self.dr).tijiao('OP.13993',changliang,"111111")


#点将展示设计师（确认）	OP.00633	陈冲	展示设计师
    # @unittest.skip('skip this case')
    def test_shenhe_20(self):
        Shenhe(self.dr).shenhe('OP.00633',changliang,"111111")

#经销商（确认）	admin@S003059	黎老板	代理商
    # @unittest.skip('skip this case')
    def test_shenhe_21(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


#经销部管理员（确认下样日期）	OP.14556	齐慧敏	经销部管理员
    # @unittest.skip('skip this case')
    def test_shenhe_22(self):
        Shenhe(self.dr).yangbanriqi('OP.14556',changliang,"111111")


#上传施工图展示设计师	OP.00633	陈冲	展示设计师
    # @unittest.skip('skip this case')
    def test_shenhe_23(self):
        Shangchuan(self.dr).tijiao('OP.00633',changliang,"111111")


#施工图审核（审图设计师（审核）	OP.19882	杨路	审图设计师
    # @unittest.skip('skip this case')
    def test_shenhe_24(self):
        Shenhe(self.dr).shenhe('OP.19882',changliang,"111111")


#填写施工图审图表（需优化）
    # @unittest.skip('skip this case')
    def test_shenhe_25(self):
        Shenhe(self.dr).shenhe('OP.19882',changliang,"111111")


#设计主管（审核）	OP.14316	胡国辉	展示设计主管
    # @unittest.skip('skip this case')
    def test_shenhe_26(self):
        Shenhe(self.dr).shenhe('OP.14316',changliang,"111111")



#展示设计师验收资料上传    OP.00633	陈冲	展示设计师
     # @unittest.skip('skip this case')
    def test_shenhe_27(self):
        Yanshou(self.dr).yanshou('OP.00633',changliang,"111111")



#审图设计师（审核）	OP.19882	杨路	审图设计师
     # @unittest.skip('skip this case')
    def test_shenhe_28(self):
        Shenhe(self.dr).shenhe('OP.19882',changliang,"111111")



#经销商（确认）	admin@S003059	黎老板	代理商
    # @unittest.skip('skip this case')
    def test_shenhe_29(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")

#经销商（确认）	admin@S003059	黎老板	代理商
    # @unittest.skip('skip this case')
    def test_shenhe_30(self):
        Manyidu(self.dr).manyidu('admin@S003059',changliang,"111111")

#营销中心经理（评价）	OP.13741	殷俊伟	营销中心经理
    # @unittest.skip('skip this case')
    def test_shenhe_31(self):
        Manyidu(self.dr).manyidu('OP.13741',changliang,"111111")

#（项目评估）	OP.00127	黄丙凤	展示设计运营专员
    # @unittest.skip('skip this case')
    def test_shenhe_32(self):
        Manyidu(self.dr).manyidu('OP.00127',changliang,"111111")


#OP.19882	杨路	审图设计师
    # @unittest.skip('skip this case')
    def test_shenhe_33(self):
        Dafen(self.dr).dafen('OP.19882',changliang,"111111")

# 展示设计主管（审核）	OP.14316	胡国辉	展示设计主管
    # @unittest.skip('skip this case')
    def test_shenhe_34(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 展示设计部设计经理（审核）	OP.00468	姚建虹	展示设计经理
    # @unittest.skip('skip this case')
    def test_shenhe_35(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 展示设计部总监（审核	OP.12695	梁华蔚	展示设计部总监
    # @unittest.skip('skip this case')
    def test_shenhe_36(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 橱柜经销部各部总监（审核）	OP.07882	曾祥伟	经销部总监
    # @unittest.skip('skip this case')
    def test_shenhe_37(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")


# 橱柜营销部副总（审核）	OP.14150	陈道品	营销副总经理
    # @unittest.skip('skip this case')
    def test_shenhe_38(self):
        Shenhe(self.dr).shenhe('admin@S003059',changliang,"111111")

#展示设计运营专员（审核）	OP.00127	黄丙凤	展示设计运营专员
    # @unittest.skip('skip this case')
    def test_shenhe_39(self):
        Suanqian(self.dr).suanqian('OP.00127',changliang,"111111")



if __name__ == '__main__':
    unittest.main()