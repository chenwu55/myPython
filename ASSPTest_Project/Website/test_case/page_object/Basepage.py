#coding=utf-8
from time import sleep
from selenium.webdriver.common.keys import Keys
import os
class Page():
    def __init__(self,dr,base_url='http://ucenterver.oppein.com'):
        self.dr=dr
        # self.base_url='https://assptest.oppein.com'
        # self.base_url='http://ucenteruat.oppein.com'
        self.base_url=base_url
        self.timeout=10

    def _open(self,url):
        url_=self.base_url+url
        # print u"当前测试页面 %s" %url_
        self.dr.maximize_window()
        self.dr.get(url_)
        # assert self.dr.current_url == url_, u'登录失败 %s' % url_

    def open(self):
        self._open(self.url)   ###打开网址浏览器


    def find_element(self,*loc):
        return self.dr.find_element(*loc)

    def link_text(self,text):
        return self.dr.find_element_by_link_text(text).click()

    def link_texts(self,text, tests):
        return self.dr.find_element_by_link_text(text).send_keys(tests)

    def by_xpath(self,path):
        return self.dr.find_element_by_xpath(path).click()

    def by_xpath_s(self,path, paths):
        return self.dr.find_element_by_xpath(path).send_keys(paths)

    def by_css(self,input):
        return self.dr.find_element_by_css_selector(input).click()

    def by_css_s(self,input, values):
        return self.dr.find_element_by_css_selector(input).send_keys(values)

    def by_id(self,id):
        return self.dr.find_element_by_id(id).click()

    def by_ids(self,di, dis):
        return self.dr.find_element_by_id(di).send_keys(dis)

    def by_class(self,cls):
        return self.dr.find_elements_by_class_name(self,cls).click()

    def by_clear_i(self,id):
        return self.dr.find_element_by_id(id).clear()

    def by_clear_x(self,xp):
        return self.dr.find_element_by_xpath(xp).clear()

    def by_clear_css(self,xp):
        return self.dr.find_element_by_xpath(xp).clear()

    def by_xpath_x(self,bb):
        return self.dr.find_element_by_xpath('(//*[@type="text"])[' + bb + ']').click()

    def by_xpath_y(self,yy):
        return self.dr.find_element_by_xpath('(//*[@type="text"])[' + yy + ']').clear()

    def by_xpath_z(self,xx,yy):
        return self.dr.find_element_by_xpath('(//*[@type="text"])[' + xx + ']').send_keys(yy)

    def by_xpath_b(self,nn):
        return self.dr.find_element_by_xpath('(//*[@type="button"])[' + nn + ']').click()

