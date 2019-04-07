#coding=utf-8
from LoginPage import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import datetime
import random
class xz_service_no(Page):
    #登录账户登录
    def login_1(self,shenheren):
        LoginPage(self.dr).Login_action_mtds("S000044",shenheren,"Aa111111")
    #根据服务单搜索任务
    def sousuo(self,fud):
        self.by_css('[title="任务列表"]')
        sleep(1)
        self.by_xpath('//ul[@class="nav nav-second-level collapse in"]/li[2]//a')
        sleep(1)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[2]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_ids('searchKeyWord',fud)
        sleep(2)
        self.by_id('search')
        sleep(2)
        self.dr.find_element_by_xpath('(//*[@title="办理"])[1]/a').send_keys(Keys.ENTER)
        self.dr.switch_to.parent_frame()
        sleep(2)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[3]')
        self.dr.switch_to.frame(xf)
        sleep(1)
    #提交任务
    def tijiao(self):
        self.by_xpath('//*[text()="完成并提交任务"]')
        sleep(1)
        self.by_css('input[value="保存"]')
        sleep(1)
        self.by_css('input[value="确定"]')
        sleep(1)
        self.by_css('input[value="确定"]')
        sleep(3)
    #新增服务号与服务单
    def service_no(self,pl,fpsjs):
        cc=u"MTDS流程测试"+time.strftime("%m%d%H%M")
        dh="155"+str(random.randint(10000000,99999999))
        # dh="13662646812"
        self.by_css('[title="客户列表"]')
        sleep(1)
        self.by_css('ul[class="nav nav-second-level collapse in"]>li>a')
        sleep(1)
        self.dr.switch_to.frame('iframe1')
        sleep(1.5)
        self.by_xpath('//*[text()="新增服务号"]')
        sleep(1)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('content')
        sleep(1.5)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[3]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_css_s('[placeholder="请输入客户姓名"]',cc)
        self.by_css_s('[placeholder="请输入客户电话"]',dh)
        self.by_css_s('[placeholder="请输入客户详细地址,不能输入特殊字符"]', u"白云区江高镇新镇庄119号")
        if pl=="1":
            print u"新增橱柜服务单"
            self.by_css('input[value="brand_oppein|category_chugui"]')
        elif pl=="2":
            print u"新增衣柜服务单"
            self.by_css('input[value="brand_oppein|category_yigui"]')
        elif pl=="3":
            self.by_css('input[value="brand_oppein|category_chugui"]')
            self.by_css('input[value="brand_oppein|category_yigui"]')
        sleep(3)
        js = "window.scrollTo(100,450)"
        self.dr.execute_script(js)
        sleep(3)
        khly=self.dr.find_element_by_id("customerSource")
        Select(khly).first_selected_option(self)
        sleep(1)
        self.by_xpath('//*[text()="保存"]')
        fud = (self.dr.find_element_by_xpath('//*[@id="orderGrid"]/tbody/tr[2]/td[11]')).text
        fuh=self.dr.find_element_by_xpath('//*[@id="serviceNo"]').get_attribute("value")
        print u"服务号：", fuh
        print u"服务单号：", fud
        sleep(2)
        self.dr.find_element_by_xpath('(//*[@title="编辑"])[1]/a').send_keys(Keys.ENTER)
        sleep(2)
        xf=self.dr.find_element_by_xpath('//*[@frameborder="0"]')
        self.dr.switch_to.frame(xf)
        sleep(2.5)
        self.by_xpath('(//a[@href="javascript:void(0);"])[9]')
        sleep(0.5)
        self.by_xpath('//*[@id="_designerId"]')
        sleep(1)
        self.by_xpath_s('.//*[@id="menuContent"]/div/input',fpsjs)
        sleep(1)
        self.by_xpath('.//*[@id="menuContent"]//*[@title="小武设计"]')
        self.by_id('bookMeasureDt')
        sleep(1)
        self.dr.switch_to.parent_frame()
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[2]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_xpath('//*[@id="dpTodayInput"]')
        sleep(1)
        self.dr.switch_to.parent_frame()
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[1]')
        self.dr.switch_to.frame(xf)
        self.by_id('submitDesigerBtn')
        sleep(2.5)
        self.by_xpath('//*[text()="关闭"]')
        sleep(1.5)
        self.dr.switch_to.frame('content')
        self.by_xpath('(//*[@class="fa fa-times-circle"])[1]')
        service=(fud,fuh)
        sleep(2)
        return service
    #给服务号添加服务单
    def xz_service_dan(self,fud):
        self.by_xpath('//*[text()="服务单"]')
        sleep(1)
        self.by_xpath('//*[text()="我的服务单"]')
        sleep(1)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[2]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_ids('searchKeyWord',fud)
        self.by_id('search')
        sleep(1)
        self.dr.find_element_by_xpath('(//*[@title="添加服务单"])[1]/a').send_keys(Keys.ENTER)
        sleep(2)
        self.dr.switch_to.parent_frame()     #回到上一级
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[3]')
        self.dr.switch_to.frame(xf)
        self.by_id("select2-brand-container")
        sleep(1)
        self.by_xpath('//*[@class="select2-results__option"]')
        self.by_id( 'select2-category-container')
        sleep(1)
        self.by_xpath('(//*[@class="select2-results__option"])[1]')
        self.by_id('submitBtnBackServcie')
        sleep(1)
        self.by_css('[class="ui_state_highlight"]')
        fud = (self.dr.find_element_by_xpath('//*[@id="orderGrid"]/tbody/tr[2]/td[11]')).text
        print "服务单编码：", fud
        sleep(1)
        self.by_xpath('//*[text()="保存并关闭"]')
        sleep(1)
        self.dr.switch_to.frame('content')
        self.by_xpath('(//*[@class="fa fa-times-circle"])[1]')
        sleep(4)
    #分配设计师
    def distribution_Designer(self,fud):
        self.by_xpath('//*[text()="服务单"]')
        sleep(1)
        self.by_xpath('//*[text()="我的服务单"]')
        sleep(1)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[2]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_ids('searchKeyWord',fud)
        self.by_id('search')
        sleep(1)
        self.dr.find_element_by_xpath('(//*[@title="编辑"])[1]/a').send_keys(Keys.ENTER)
        sleep(3)
        self.dr.switch_to.parent_frame()     #回到上一级
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[3]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_xpath('(//a[@href="javascript:void(0);"])[9]')
        sleep(0.5)
        self.by_xpath('//*[@id="_designerId"]')
        sleep(1)
        self.by_xpath_s('.//*[@id="menuContent"]/div/input',u'小武设计')
        sleep(1)
        self.by_xpath('(//*[text()="小武设计"])[1]')
        self.by_id('bookMeasureDt')
        sleep(1)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_xpath('//*[@id="dpTodayInput"]')
        sleep(1)
        self.dr.switch_to.parent_frame()
        self.by_id('submitDesigerBtn')
        sleep(2)
        self.by_xpath('//*[text()="关闭"]')
        sleep(1)
        self.dr.switch_to.frame('content')
        self.by_xpath('(//*[@class="fa fa-times-circle"])[1]')
        sleep(1)
    #完成初迟任务
    def chuchi(self,fud):
        self.sousuo(fud)
        js = "window.scrollTo(100,450)"
        self.dr.execute_script(js)
        sleep(1)
        self.by_xpath('//*[text()="保存全屋信息"]')
        sleep(1)
        self.by_xpath('//*[text()="添加空间"]')
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])')
        self.dr.switch_to.frame(xf)
        sleep(1)
        Select(self.dr.find_element_by_id("spaceType")).select_by_visible_text(u"多功能房")
        self.dr.find_element_by_id("uploadAttachmentJsonFile").send_keys("F:\\0.0.jpg")
        sleep(1.5)
        self.dr.switch_to.parent_frame()
        self.by_xpath('//input[@class="ui_state_highlight"]')
        sleep(1)
        self.by_css('input[class="ui_state_highlight"][value="确定"]')
        sleep(1)
        self.by_xpath('//*[text()="完成并提交任务"]')
        sleep(1)
        self.by_css('input[class="ui_state_highlight"][value="保存"]')
        sleep(1)
        self.by_css('input[class="ui_state_highlight"][value="确定"]')
        sleep(1.5)
        self.by_xpath('//*[@class="ui_state_highlight"]')
        sleep(2)
    #合同签订
    def hetongqianding(self):
        self.by_xpath_s('//*[@id="contractTotalAmount"]',"10000")
        self.by_xpath('//*[@id="contractDeliverDt"]')
        sleep(1)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])')
        self.dr.switch_to.frame(xf)
        sleep(0.5)
        self.by_xpath('//*[@id="dpTodayInput"]')
        self.dr.switch_to.parent_frame()
        self.tijiao()
    #橱柜—订单下单
    def cg_dingdanxiadan(self):
        dd = u"测试商场传单" + time.strftime("%m%d%H%M")
        js = "window.scrollTo(100,450)"
        self.dr.execute_script(js)
        self.by_xpath('//*[text()="新增工厂订单"]')
        sleep(1)
        self.by_css('input[class="ui_state_highlight"][value="确定"]')
        sleep(1)
        self.by_clear_x('//*[@id="productionOrderContractNo"]')
        self.by_xpath_s('//*[@id="productionOrderContractNo"]',dd)
        Select(self.dr.find_element_by_id("designSource")).select_by_visible_text("XML")
        self.by_xpath('.//*[@onclick="selectReceiver()"]')
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_xpath('.//*[@id="grid_frozen"]/tbody/tr[2]/td[2]/input')
        self.dr.switch_to.parent_frame()
        sleep(1)
        self.by_css('input[class="ui_state_highlight"][value="确定"]')
        sleep(1)
        today = datetime.date.today()
        mt = str(today + datetime.timedelta(days=100))
        js = "$('input[id=expectDeliveryDt]').removeAttr('readonly')"
        self.dr.execute_script(js)
        self.by_ids("expectDeliveryDt",mt)
        self.by_xpath('//*[@id="save1"]')
        sleep(2.5)
        ddbh=self.dr.find_element_by_xpath('(//*[@id="no"])[1]').get_attribute("value")
        print u"订单编号：",ddbh
        print u"工厂合同自编号：",dd
        sleep(1)
        js = "window.scrollTo(100,450)"
        self.dr.execute_script(js)
        sleep(1.5)
        self.by_xpath('//*[@id="attachment"]')
        sleep(1)
        self.dr.find_element_by_id("xmlAttachmentFile").send_keys("F:\\0.0.xml")
        sleep(1.5)
        self.by_xpath('//*[@id="tran"]')
        sleep(3)
        self.by_xpath('//*[@value="传单"]')
        sleep(4.5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('content')
        sleep(2)
        self.by_xpath('(//*[@class="fa fa-times-circle"])[2]')
        sleep(2)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[2]')
        self.dr.switch_to.frame(xf)
        sleep(2)
        self.by_id('search')
        sleep(2)
        self.dr.find_element_by_xpath('(//*[@title="办理"])[1]/a').send_keys(Keys.ENTER)
        self.dr.switch_to.parent_frame()
        sleep(1)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[3]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.tijiao()
        sleep(2)
    #衣柜—订单下单
    def yg_dingdanxiadan(self):
        # self.by_xpath("//*[text()='服务单详情']")
        # sleep(2)
        # htbh = self.dr.find_element_by_id('productionOrderContractNo').get_attribute("value")
        # print u"合同编号" ,htbh
        # self.by_xpath("//*[text()='订单下单节点']")
        # sleep(1)
        # dd = '测试传单功能'+time.strftime("%m%d%H%M")
        js = "window.scrollTo(100,450)"
        self.dr.execute_script(js)
        sleep(0.5)
        self.by_xpath('//*[text()="新增工厂订单"]')
        sleep(0.8)
        self.by_css('input[class="ui_state_highlight"][value="确定"]')
        sleep(0.5)
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])[1]')
        self.dr.switch_to.frame(xf)
        sleep(2)
        self.by_xpath('//*[@id="submitForm"]/div/input[6]')

        sleep(0.5)
        self.dr.switch_to.parent_frame()
        sleep(0.5)
        self.by_css('input[class="ui_state_highlight"][value="保存"]')
        sleep(0.5)
        # self.by_clear_x('//*[@id="productionOrderContractNo"]')
        # self.by_xpath_s('//*[@id="productionOrderContractNo"]',dd)
        Select(self.dr.find_element_by_id("designSource")).select_by_visible_text("XML")
        self.by_xpath('.//*[@onclick="selectReceiver()"]')
        xf=self.dr.find_element_by_xpath('(//*[@frameborder="0"])')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.by_xpath('.//*[@id="grid_frozen"]/tbody/tr[2]/td[2]/input')
        self.dr.switch_to.parent_frame()
        sleep(1)
        self.by_css('input[class="ui_state_highlight"][value="确定"]')
        sleep(1)
        today = datetime.date.today()
        mt = str(today + datetime.timedelta(days=100))
        js = "$('input[id=expectDeliveryDt]').removeAttr('readonly')"
        self.dr.execute_script(js)
        self.by_ids("expectDeliveryDt",mt)
        # cplx = u"CY单"
        # Select(self.dr.find_element_by_id("productCategory")).select_by_visible_text(cplx)
        # sleep(0.5)
        # self.by_css('input[value="确定"]')
        sleep(0.5)
        Select(self.dr.find_element_by_id("productOrderStyle")).select_by_visible_text(u"金粉世家")
        self.by_xpath('//*[@id="save1"]')
        sleep(1.5)
        js = "window.scrollTo(100,450)"
        self.dr.execute_script(js)
        sleep(1)
        self.by_xpath('//*[@id="attachment"]')
        sleep(1)
        self.dr.find_element_by_id("xmlAttachmentFile").send_keys("D:\\00.xml")
        sleep(1.5)
        self.by_xpath('//*[@id="tran"]')
        sleep(1)
        self.by_xpath('//*[@value="传单"]')
        sleep(4.5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('content')
        sleep(2)
        self.by_xpath('(//*[@class="fa fa-times-circle"])[2]')
        sleep(2)
        xf = self.dr.find_element_by_xpath('(//*[@frameborder="0"])[2]')
        self.dr.switch_to.frame(xf)
        sleep(2)
        self.by_id('search')
        sleep(2)
        self.dr.find_element_by_xpath('(//*[@title="办理"])[1]/a').send_keys(Keys.ENTER)
        self.dr.switch_to.parent_frame()
        sleep(1.5)
        xf = self.dr.find_element_by_xpath('(//*[@frameborder="0"])[3]')
        self.dr.switch_to.frame(xf)
        sleep(1)
        self.tijiao()
        sleep(2)

    #合同下单任务
    def hetongxiadan(self):
        self.dr.find_element_by_id("uploadAttachmentJsonFile").send_keys("F:\\0.0.jpg")






















