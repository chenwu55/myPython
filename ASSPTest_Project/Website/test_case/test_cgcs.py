#coding=utf-8
import unittest
from model import myunit
from page_object.Cgdianjiang import *
import time
from page_object.Basepage import *

class CgdianjiangTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_dianjiang_normal(self):
        i = 0
        while i <3000:
            i = i + 1
            print u"第", i, u"次橱柜点将申请测试："
            now = time.strftime("%Y-%m-%d %H_%M_%S")+ u" 第"
            mum=str(i)
            # jietu_name =now +mum + u"次点将申请截图.png"
            op=dainjianshenqing(self.dr)
            proportion = random.randrange(10, 600, 10)
            decoration_type = str(random.randint(2,5))
            storefront_type = str(random.randint(2,13))
            type1=shifouyichang(decoration_type, storefront_type, proportion).dayinzhuangtai()
            op.dianjiang('admin@S003059','Aa111111',decoration_type,storefront_type,proportion,type1)
            sleep(2)
            self.assertEqual(op.dianjiangPass_hint(),U'登录')
            sleep(3)




# class CgdianjiangTest(myunit.StartEnd):
#  @unittest.skip('skip this case')
# def test_dianjiang_normal(self):
#     i = 0
#     while i <1:
#         i = i + 1
#         print u"第", i, u"次橱柜点将申请测试："
#         now = time.strftime("%Y-%m-%d %H_%M_%S")+ u" 第"
#         mum=str(i)
#         jietu_name =now +mum + u"次点将申请截图.png"
#         op=dainjianshenqing(self.dr)
#         op.dianjiang('admin@S003059','Aa111111',decoration_type,storefront_type,proportion)
#         sleep(2)
#         self.assertEqual(op.dianjiangPass_hint(),U'登录')
#         sleep(1)








