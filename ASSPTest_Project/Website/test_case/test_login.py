#coding=utf-8
import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import  sleep
class LoginTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        print u'''正确的账号密码点击登录'''
        print u'开始第 1 次测试'
        po=LoginPage(self.dr)
        po.Login_action('admin1@S003059',"111111")
        sleep(3)
        self.assertEqual(po.type_loginPass_hint(),u'退出登录')
        function.insert_img(self.dr,u"第 1 次测试截图.png")
        print u'第 1 次测试结束'

    # @unittest.skip('skip this case')
    def test_login2_PasswdError(self):
        print u'''正确的用户名和错误的密码点击登录'''
        print u'开始第 2 次测试'
        po=LoginPage(self.dr)
        po.Login_action('51zxw',3333)
        sleep(2)
        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.dr,u"第 2 次测试截图.png")
        print u'第 2 次测试结束'

    # @unittest.skip('skip this case')
    def test_login3_empty(self):
        print u'''用户名和密码为空点击登录'''
        print u'开始第 3 次测试'
        po=LoginPage(self.dr)
        po.Login_action('','')
        sleep(2)
        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.dr,u"第 3 次测试截图.png")
        print u'第 3 次测试结束'



if __name__ == '__main__':
    unittest.main()
