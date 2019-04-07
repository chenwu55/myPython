#coding=utf-8
from LoginPage import *
from time import sleep
import random,time
import os
#######################################################        发起点将         #########################################
class dainjianshenqing(Page):
    url = '/'
    def dianjiang_tou(self,Designer,leixing,xingzhi):
        self.by_xpath('//*[@id="menuTree"]/ul/li[4]/div ')
        sleep(1)
        self.by_xpath('(//*[contains(text(),"我要点将")])[2]')
        sleep(1)
        self.by_xpath('//*[contains(text(),"欧派 -  橱柜")]')
        sleep(1)
        self.by_xpath('//*[text()="开始点将"]')
        sleep(1)
        self.by_xpath('(//button[@class="el-button el-button--primary el-button--small"])[4]')
        sleep(2)
        self.by_css_s('input[placeholder="设计师或独立工作室名称"]',Designer)
        sleep(2)
        self.by_css("button[class='el-button el-button--default el-button--small']")
        sleep(1)
        self.by_css('button[item-index="0"]')
        sleep(1)
        self.by_css('input[placeholder="选择计划装修日期"]')
        sleep(1)
        self.by_xpath('//*[text()="今天"]')
        self.by_css('input[placeholder="选择计划开店日期"]')
        sleep(1)
        self.by_xpath('/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[7]/td[7]')
        sleep(1)
        self.by_css('input[placeholder="请选择装修类型"]')
        sleep(1)
        self.by_xpath("/html/body/div[4]/div/div[1]/ul/li[" + leixing + "]")
        self.by_css('input[placeholder="请选择店面类型"]')
        sleep(1)
        self.by_xpath("/html/body/div[5]/div/div[1]/ul/li[" + xingzhi + "]")
        sleep(1)
        self.by_css('input[placeholder="请选择店面"]')
        sleep(1)
        self.by_xpath('//*[text()="二锅头"]')
    def dianjiang_fjb(self,a,b,c,d,e):
        self.by_xpath_y("6")
        self.by_xpath_s("(//input[@type='text'])[6]", e)
        self.by_xpath_y("7")
        self.by_xpath_s("(//input[@type='text'])[7]", b)
        self.by_xpath_y("8")
        self.by_xpath_s("(//input[@type='text'])[8]", c)
        self.by_xpath_y("9")
        self.by_xpath_s("(//input[@type='text'])[9]", d)
        self.by_xpath_y("10")
        self.by_xpath_s("(//input[@type='text'])[10]", a)
        self.by_xpath_y("11")
        self.by_xpath_s("(//input[@type='text'])[11]", "3")
        self.by_css('button[class="el-button el-button--primary"]')
    def dianjiang_jb(self):
        # self.by_xpath('//*[text()="申请提交"]')
        # self.by_xpath('//*[text()="更换"]')
        # sleep(2)
        # self.by_css('[placeholder="设计师或独立工作室名称"]')
        # sleep(2)
        # self.by_clear_css('[placeholder="设计师或独立工作室名称"]').clear()
        # sleep(2)
        # self.by_css_s('input[placeholder="设计师或独立工作室名称"]', u'杨朝允')
        # self.by_css("button[class='el-button el-button--default el-button--small']")
        # self.by_css('button[item-index="0"]')
        self.by_xpath_y("6")
        self.by_xpath_s("(//input[@type='text'])[6]",'8')
        self.by_xpath_y("7")
        self.by_xpath_s("(//input[@type='text'])[7]",'8')
        self.by_xpath_y("8")
        self.by_xpath_s("(//input[@type='text'])[8]",'8')
        self.by_xpath_y("9")
        self.by_xpath_s("(//input[@type='text'])[9]",'8')
        self.by_xpath_y("10")
        self.by_xpath_s("(//input[@type='text'])[10]",'88')
        self.by_xpath_y("11")
        self.by_xpath_s("(//input[@type='text'])[11]",'8')
        self.by_xpath_y("12")
        self.by_xpath_s("(//input[@type='text'])[12]",'8')
        self.by_xpath_y("13")
        self.by_xpath_s("(//input[@type='text'])[13]",'8')
        self.by_xpath_y("14")
        self.by_xpath_s("(//input[@type='text'])[14]",'8')
        self.by_css('button[class="el-button el-button--primary"]')
        sleep(2)
    def shifouyichang(self):
        try:
            sleep(4)
            self.by_xpath('//*[text()="搜索"]')
            zhuangtai=1
            print u"正常点将"
        except:
            self.by_css('button[class="el-button el-button--default el-button--primary "]')
            self.by_css_s('textarea[placeholder="请填写至少15字申请原因。"]', u'有钱任性，点的就是你，有钱任性，点的就是你，有钱任性，点的就是你')
            self.by_css('[class="el-button el-button--primary"]')
            self.by_css('button[class="el-button el-button--primary el-button--small"]')
            zhuangtai = 2
            print u"异常点将"
        sleep(5)
        text=self.dr.find_element_by_xpath("//div[@class='cell']/a")
        changliang =text.text
        # now =  u"测试活动："+changliang+u"  时间："+time.strftime("%Y-%m-%d %H_%M_%S")
        # jietu_name = now +  u"点将申请截图.png"
        # function.insert_img(self.dr, jietu_name)
        self.by_css("a[href='javascript:void(0)']")
        print u"活动编号：", changliang
        # str=[changliang,zhuangtai]
        return  changliang

    def dianjiang(self,shenheren):
        a = random.randint(99, 299)
        b = random.randint(99, 299)
        c = random.randint(99, 299)
        d = random.randint(99, 299)
        e = a + b + c + d
        print  u'总面积：',e,'cm'   u"橱柜面积:",a,'cm'   u'衣柜面积:',b,'cm'    u'电器面积:',c,'cm'   u'木门面积:',d,'cm'
        Designer=u'陈冲'
        leixing =str(random.randint(2,5))   #装修类型leixing( 2= 新开店面,3=老店扩大,4=全新装修,5=局部整改)'''
        xingzhi =str(random.randint(2,6))   #门店类型xingzhi( 2=标准店，3=综合店，4=微店，5=家装整装店，6=网销店）'''
        if leixing==2:
            print u'装修类型:新开店面'
        elif leixing==3:
            print u'装修类型:老店扩大'
        elif leixing==4:
            print u'装修类型:全新装修'
        else:
            print u'装修类型:局部整改'
        if  xingzhi==2:
            print u'门店类型:标准店'
        elif xingzhi==3:
            print u'门店类型:综合店'
        elif xingzhi==4:
            print u'门店类型:微店'
        elif xingzhi==5:
            print u'门店类型:家装整装店'
        else :
            print u'门店类型:网销店'
        po = LoginPage(self.dr)
        po.Login_action(shenheren,"111111")
        sleep(1)
        self.dianjiang_tou(Designer,leixing,xingzhi)
        if leixing == "5" and xingzhi != "5":   ####局部整改非家装店
            self.dianjiang_jb()
            print u"局部整改家装店不走满意度与打分"
        elif leixing == "5" and xingzhi == "5": ####局部整改家装店
            self.dianjiang_fjb(a,b,c,d,e)
            print u"局部整改家装店不走满意度与打分"
        else:
            self.dianjiang_fjb(a,b,c,d,e)
            print u"非局部整改"
        changliang=self.shifouyichang()
        return changliang
    dianjiangPass_loc=(By.LINK_TEXT,u'退出登录')
    dianjingFail_loc = (By.ID,'username')

    def dianjiangPass_hint(self):
        return self.find_element(*self.dianjiangPass_loc).text
    def dianjingFail_hint(self):
        return self.find_element(*self.dianjingFail_loc).text

    # def dianjiang_jb_jia(self,a,b,c,d,e):                 ####局部整改家装店
    #     self.by_xpath_y("6")
    #     self.by_xpath_s("(//input[@type='text'])[6]", e)
    #     self.by_xpath_y("7")
    #     self.by_xpath_s("(//input[@type='text'])[7]", b)
    #     self.by_xpath_y("8")
    #     self.by_xpath_s("(//input[@type='text'])[8]", c)
    #     self.by_xpath_y("9")
    #     self.by_xpath_s("(//input[@type='text'])[9]", d)
    #     self.by_xpath_y("10")
    #     self.by_xpath_s("(//input[@type='text'])[10]", a)
    #     self.by_xpath_y("11")
    #     self.by_xpath_s("(//input[@type='text'])[11]", "10")
    #     self.by_css('button[class="el-button el-button--primary"]')
    #     print '局部整改不走打分流程'
#######################################################        审   核           #########################################
class Shenhe(Page):
    url='/'
#######################################################        一般审核         #########################################
    def shenhe(self,shenheren,changliang,password):
        LoginPage(self.dr).Login_action(shenheren,password)
        # Zhonglogin(self.dr).denglu(shenheren,password)
        Daiban(self.dr).daiban(changliang)
        sleep(5)
        self.by_css('button[class="el-button el-button--primary"]')
        sleep(5)
        self.by_css("a[href='javascript:void(0)']")
    ###################################################        日期确认审核       #######################################
    def yangbanriqi(self,shenheren, changliang,password):
        LoginPage(self.dr).Login_action(shenheren,password)
        sleep(2)
        Daiban(self.dr).daiban(changliang)
        sleep(5)
        self.by_css('button[class="el-button el-button--primary"]')
        sleep(2)
        self.by_css('i[class="el-input__icon el-icon-date"]')
        sleep(1)
        self.by_xpath('//*[text()="今天"]')
        sleep(1)
        self.by_xpath('(//*[@style="z-index: 2001;"])//*[@class="el-button el-button--primary el-button--small"]')
        sleep(3)
        self.by_css("a[href='javascript:void(0)']")
#######################################################        上传文件       ##########################################
class Shangchuan(Page):
    url='/'
    def tijiao(self,shenheren, changliang,password):
        LoginPage(self.dr).Login_action(shenheren,password)
        Daiban(self.dr).daiban(changliang)
        sleep(2)
        self.by_xpath('//*[text()="选择文件"]')
        sleep(1)
        os.system("D:\\upfile.exe")
        sleep(3)
        self.by_xpath('//*[contains(text(),"提交")]')
        sleep(3)
        self.by_css("a[href='javascript:void(0)']")
#######################################################       平面图审图表     ##########################################
class Tianxiest(Page):
    url='/'
    def shentubiao (self,shenheren,changliang,password):
        LoginPage(self.dr).Login_action(shenheren,password)
        Daiban(self.dr).daiban(changliang)
        sleep(2)
        self.by_xpath("//form/div[1]/div/div/div[1]/i")
        sleep(1)
        # self.by_xpath("/html/body/div[2]/div/div[1]/ul/li["+yangban+"]")
        self.by_xpath('//*[text()="吴娟娟"]')
        j=range(2,18)
        for i in j :
            i = bytes(i)
            self.by_xpath_y(i)
            x = random.randrange(100, 1001, 50)
            self.by_xpath_z(i, x)
        self.by_css('button[class="el-button el-button--primary"]')
        sleep(3)
        self.by_css("a[href='javascript:void(0)']")
#######################################################        下样日期确认    ##########################################
class Xiayang(Page):
    url='/'
    def yangbanriqi(self,shenheren,changliang,pasword):
        LoginPage(self.dr).Login_action(shenheren,pasword)
        sleep(1)
        Daiban(self.dr).daiban(changliang)
        sleep(1)
        self.by_css('button[class="el-button el-button--primary"]')
        sleep(2)
        self.by_css('i[class="el-input__icon el-icon-date"]')
        sleep(1)
        self.by_xpath('//*[text()="今天"]')
        sleep(1)
        try:
            self.by_xpath('(//*[text()="确 定"])[1]')
        except:
            self.by_xpath('(//*[text()="确 定"])[2]')
        sleep(2)
        self.by_css("a[href='javascript:void(0)']")
#######################################################       施工图审图表     ##########################################
class Shentubiao2(Page):
    def shentubiao2(self,shenheren,changliang,password):
      LoginPage(self.dr).Login_action(shenheren,password)
      Daiban(self.dr).daiban(changliang)
      sleep(1)
      if (self.dr.find_element_by_xpath('(//div[@class="panel-header"])[4]')).text==u'局部整改':
          self.by_xpath_y("1")
          self.by_xpath_s("(//input[@type='text'])[1]","888")
          self.by_xpath_y("2")
          self.by_xpath_s("(//input[@type='text'])[2]","8")
          self.by_xpath_y("3")
          self.by_xpath_s("(//input[@type='text'])[3]","8")
          self.by_xpath_y("4")
          self.by_xpath_s("(//input[@type='text'])[4]","8")
          self.by_xpath_y("5")
          self.by_xpath_s("(//input[@type='text'])[5]","88")
          self.by_xpath_y("6")
          self.by_xpath_s("(//input[@type='text'])[6]","8")
          self.by_xpath_y("7")
          self.by_xpath_s("(//input[@type='text'])[7]","8")
          self.by_xpath_y("8")
          self.by_xpath_s("(//input[@type='text'])[8]","8")
          self.by_xpath_y("9")
          self.by_xpath_s("(//input[@type='text'])[9]","8")
          self.by_xpath_y("10")
          self.by_xpath_s("(//input[@type='text'])[10]","8")
          self.by_xpath_y("11")
          self.by_xpath_s("(//input[@type='text'])[11]","8")
          self.by_xpath_y("12")
          self.by_xpath_s("(//input[@type='text'])[12]","8")
          self.by_xpath_y("13")
          self.by_xpath_s("(//input[@type='text'])[13]","8")
          self.by_xpath_y("14")
          self.by_xpath_s("(//input[@type='text'])[14]","8")
          self.by_xpath_y("15")
          self.by_xpath_s("(//input[@type='text'])[15]","8")
          self.by_xpath_y("16")
          self.by_xpath_s("(//input[@type='text'])[16]","88")
          self.by_xpath_y("17")
          self.by_xpath_s("(//input[@type='text'])[17]","88")
          self.by_xpath_y("18")
          self.by_xpath_s("(//input[@type='text'])[18]","88")
          self.by_xpath_y("19")
          self.by_xpath_s("(//input[@type='text'])[19]","88")
          self.by_xpath_y("20")
          self.by_xpath_s("(//input[@type='text'])[20]","88")
          self.by_xpath_y("21")
          self.by_xpath_s("(//input[@type='text'])[21]","88")
          self.by_xpath_y("22")
          self.by_xpath_s("(//input[@type='text'])[22]","8")
          self.by_xpath_y("23")
          self.by_xpath_s("(//input[@type='text'])[23]","8")
          self.by_xpath_y("24")
          self.by_xpath_s("(//input[@type='text'])[24]","8")
          self.by_css('[class="el-switch__label el-switch__label--right"]')
          self.by_xpath("(//span[@class='el-radio__inner'])[1]")
          self.by_xpath("(//span[@class='el-radio__inner'])[3]")
          self.by_xpath("(//span[@class='el-radio__inner'])[5]")
          self.by_xpath("(//span[@class='el-radio__inner'])[7]")
          self.by_xpath("(//span[@class='el-radio__inner'])[9]")
          self.by_xpath("(//span[@class='el-radio__inner'])[11]")
          self.by_xpath("(//span[@class='el-radio__inner'])[13]")
          self.by_xpath("(//span[@class='el-radio__inner'])[15]")
          self.by_xpath("(//span[@class='el-radio__inner'])[17]")
      elif (self.dr.find_element_by_xpath('(//div[@class="panel-header"])[5]')).text==u'电器面积':
          self.by_xpath_y("1")
          self.by_xpath_s("(//input[@type='text'])[1]","88")
          self.by_xpath_y("2")
          self.by_xpath_s("(//input[@type='text'])[2]","88")
          self.by_xpath_y("3")
          self.by_xpath_s("(//input[@type='text'])[3]","8")
          self.by_xpath_y("4")
          self.by_xpath_s("(//input[@type='text'])[4]","8")
          self.by_xpath_y("5")
          self.by_xpath_s("(//input[@type='text'])[5]","8")
          self.by_xpath_y("6")
          self.by_xpath_s("(//input[@type='text'])[6]","8")
          self.by_xpath_y("7")
          self.by_xpath_s("(//input[@type='text'])[7]","8")
          self.by_xpath_y("8")
          self.by_xpath_s("(//input[@type='text'])[8]","8")
          self.by_xpath_y("9")
          self.by_xpath_s("(//input[@type='text'])[9]","8")
          self.by_xpath_y("10")
          self.by_xpath_s("(//input[@type='text'])[10]","8")
          self.by_xpath_y("11")
          self.by_xpath_s("(//input[@type='text'])[11]","88")
          self.by_xpath_y("12")
          self.by_xpath_s("(//input[@type='text'])[12]","88")
          self.by_xpath_y("13")
          self.by_xpath_s("(//input[@type='text'])[13]","88")
          self.by_xpath_y("14")
          self.by_xpath_s("(//input[@type='text'])[14]","88")
          self.by_xpath_y("15")
          self.by_xpath_s("(//input[@type='text'])[15]","88")
          self.by_xpath_y("16")
          self.by_xpath_s("(//input[@type='text'])[16]","352")
          self.by_xpath_y("17")
          self.by_xpath_s("(//input[@type='text'])[17]","8")
          self.by_xpath_y("18")
          self.by_xpath_s("(//input[@type='text'])[18]","8")
          self.by_xpath_y("19")
          self.by_xpath_s("(//input[@type='text'])[19]","8")
          self.by_css('[class="el-switch__label el-switch__label--right"]')
          self.by_xpath("(//span[@class='el-radio__inner'])[1]")
          self.by_xpath("(//span[@class='el-radio__inner'])[3]")
          self.by_xpath("(//span[@class='el-radio__inner'])[5]")
          self.by_xpath("(//span[@class='el-radio__inner'])[7]")
          self.by_xpath("(//span[@class='el-radio__inner'])[9]")
          self.by_xpath("(//span[@class='el-radio__inner'])[11]")
          self.by_xpath("(//span[@class='el-radio__inner'])[13]")
          self.by_xpath("(//span[@class='el-radio__inner'])[15]")
          self.by_xpath("(//span[@class='el-radio__inner'])[17]")
          self.by_xpath("(//span[@class='el-radio__inner'])[19]")
      elif (self.dr.find_element_by_xpath('(//div[@class="panel-header"])[5]')).text==u'平面图公共面积审核':
          self.by_xpath_y("1")
          self.by_xpath_s("(//input[@type='text'])[1]","888")
          self.by_xpath_y("2")
          self.by_xpath_s("(//input[@type='text'])[2]","8")
          self.by_xpath_y("3")
          self.by_xpath_s("(//input[@type='text'])[3]","8")
          self.by_xpath_y("4")
          self.by_xpath_s("(//input[@type='text'])[4]","8")
          self.by_xpath_y("5")
          self.by_xpath_s("(//input[@type='text'])[5]","8")
          self.by_xpath_y("6")
          self.by_xpath_s("(//input[@type='text'])[6]","8")
          self.by_xpath_y("7")
          self.by_xpath_s("(//input[@type='text'])[7]","88")
          self.by_xpath_y("8")
          self.by_xpath_s("(//input[@type='text'])[8]","88")
          self.by_xpath_y("9")
          self.by_xpath_s("(//input[@type='text'])[9]","88")
          self.by_xpath_y("10")
          self.by_xpath_s("(//input[@type='text'])[10]","88")
          self.by_xpath_y("11")
          self.by_xpath_s("(//input[@type='text'])[11]","88")
          self.by_xpath_y("12")
          self.by_xpath_s("(//input[@type='text'])[12]","8")
          self.by_xpath_y("13")
          self.by_xpath_s("(//input[@type='text'])[13]","8")
          self.by_xpath_y("14")
          self.by_xpath_s("(//input[@type='text'])[14]","8")
          self.by_xpath_y("15")
          self.by_xpath_s("(//input[@type='text'])[15]","8")
          self.by_css('[class="el-switch__label el-switch__label--right"]')
          self.by_xpath("(//span[@class='el-radio__inner'])[1]")
          self.by_xpath("(//span[@class='el-radio__inner'])[3]")
          self.by_xpath("(//span[@class='el-radio__inner'])[5]")
          self.by_xpath("(//span[@class='el-radio__inner'])[7]")
          self.by_xpath("(//span[@class='el-radio__inner'])[9]")
          self.by_xpath("(//span[@class='el-radio__inner'])[11]")
          self.by_xpath("(//span[@class='el-radio__inner'])[13]")
          self.by_xpath("(//span[@class='el-radio__inner'])[15]")
          self.by_xpath("(//span[@class='el-radio__inner'])[17]")
      else:
          self.by_xpath_y("1")
          self.by_xpath_s("(//input[@type='text'])[1]","888")
          self.by_xpath_y("2")
          self.by_xpath_s("(//input[@type='text'])[2]","8")
          self.by_xpath_y("3")
          self.by_xpath_s("(//input[@type='text'])[3]","8")
          self.by_xpath_y("4")
          self.by_xpath_s("(//input[@type='text'])[4]","8")
          self.by_xpath_y("5")
          self.by_xpath_s("(//input[@type='text'])[5]","8")
          self.by_xpath_y("6")
          self.by_xpath_s("(//input[@type='text'])[6]","8")
          self.by_xpath_y("7")
          self.by_xpath_s("(//input[@type='text'])[7]","88")
          self.by_xpath_y("8")
          self.by_xpath_s("(//input[@type='text'])[8]","88")
          self.by_xpath_y("9")
          self.by_xpath_s("(//input[@type='text'])[9]","88")
          self.by_xpath_y("10")
          self.by_xpath_s("(//input[@type='text'])[10]","88")
          self.by_xpath_y("11")
          self.by_xpath_s("(//input[@type='text'])[11]","88")
          self.by_xpath_y("12")
          self.by_xpath_s("(//input[@type='text'])[12]","888")
          self.by_xpath_y("13")
          self.by_xpath_s("(//input[@type='text'])[13]","8")
          self.by_xpath_y("14")
          self.by_xpath_s("(//input[@type='text'])[14]","8")
          self.by_xpath_y("15")
          self.by_xpath_s("(//input[@type='text'])[15]","8")
          self.by_xpath_y("16")
          self.by_xpath_s("(//input[@type='text'])[16]","8")
          self.by_xpath("(//span[@class='el-radio__inner'])[1]")
          self.by_xpath("(//span[@class='el-radio__inner'])[3]")
          self.by_xpath("(//span[@class='el-radio__inner'])[5]")
          self.by_xpath("(//span[@class='el-radio__inner'])[7]")
          self.by_xpath("(//span[@class='el-radio__inner'])[9]")
          self.by_xpath("(//span[@class='el-radio__inner'])[11]")
          self.by_xpath("(//span[@class='el-radio__inner'])[13]")
          self.by_xpath("(//span[@class='el-radio__inner'])[15]")
          self.by_xpath("(//span[@class='el-radio__inner'])[17]")
          self.by_xpath("(//span[@class='el-radio__inner'])[19]")
          self.by_xpath("(//span[@class='el-radio__inner'])[21]")
          self.by_xpath("(//span[@class='el-radio__inner'])[23]")
          self.by_xpath("(//span[@class='el-radio__inner'])[25]")
          self.by_xpath("(//span[@class='el-radio__inner'])[27]")
          self.by_xpath("(//span[@class='el-radio__inner'])[29]")
          self.by_xpath("(//span[@class='el-radio__inner'])[31]")
          self.by_xpath("(//span[@class='el-radio__inner'])[33]")
          self.by_xpath("(//span[@class='el-radio__inner'])[35]")
      sleep(5)
      self.by_css('button[class="el-button el-button--primary"]')
      sleep(2)
      self.by_css("a[href='javascript:void(0)']")
#######################################################       验收资料审核     ##########################################
class Yanshou(Page):
    def yanshou(self,shenheren,changliang,password):
        LoginPage(self.dr).Login_action(shenheren,password)
        Daiban(self.dr).daiban(changliang)
        sleep(1)
        self.by_xpath("(//button[@class='el-button el-button--primary el-button--small'])[1]")
        sleep(1)
        os.system("D:\\upfile.exe")
        sleep(2)
        self.by_xpath("(//button[@class='el-button el-button--primary el-button--small'])[2]")
        sleep(1)
        os.system("D:\\upfile.exe")
        sleep(2)
        self.by_css('[class="el-button el-button--success el-button--small"]')
        sleep(1)
        self.by_css_s('[placeholder="请输入视频名称"]',U"百度")
        self.by_css_s('[placeholder="请输入视频地址"]',"www.baidu.com")
        self.by_xpath('(//button[@class="el-button el-button--primary el-button--small"])[3]')
        sleep(3)
        self.by_xpath('(//button[@class="el-button el-button--primary el-button--small"])[4]')
        sleep(3)
        self.by_css('button[class="el-button el-button--default el-button--primary "][type="button"]')
        sleep(2)
        self.by_css("a[href='javascript:void(0)']")
#######################################################       验收项目评价     ##########################################
class Dafen(Page):
    def dafen(self,shenheren,changliang,password):
      x=random.randint(99,399)
      y=random.randint(99,399)
      z=random.randint(99,399)
      zongmianji=x+y+z
      LoginPage(self.dr).Login_action(shenheren,password)
      Daiban(self.dr).daiban(changliang)
      if (self.dr.find_element_by_xpath('(//div[@class="el-tabs__item"])[1]')).text==u'验收结果评价':
          self.by_xpath('(//div[@class="el-tabs__item"])[1]')
          sleep(1)
          self.by_xpath('(//input[@type="text"])[1]')
          sleep(1)
          self.by_xpath('/html/body/div[2]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[2]')
          sleep(1)
          self.by_xpath('/html/body/div[3]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[3]')
          sleep(1)
          self.by_xpath('/html/body/div[4]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[4]')
          sleep(1)
          self.by_xpath('/html/body/div[5]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[5]')
          sleep(1)
          self.by_xpath('/html/body/div[6]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[6]')
          sleep(1)
          self.by_xpath('/html/body/div[7]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[7]')
          sleep(1)
          self.by_xpath('/html/body/div[8]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[8]')
          sleep(1)
          self.by_xpath('/html/body/div[9]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[9]')
          sleep(1)
          self.by_xpath('/html/body/div[10]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[10]')
          sleep(1)
          self.by_xpath('/html/body/div[11]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[11]')
          sleep(1)
          self.by_xpath('/html/body/div[12]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[12]')
          sleep(1)
          self.by_xpath('/html/body/div[13]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[13]')
          sleep(1)
          self.by_xpath('/html/body/div[14]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[14]')
          sleep(1)
          self.by_xpath('/html/body/div[15]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[15]')
          sleep(1)
          self.by_xpath('/html/body/div[16]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[16]')
          sleep(1)
          self.by_xpath('/html/body/div[17]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[17]')
          sleep(1)
          self.by_xpath('/html/body/div[18]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[18]')
          sleep(1)
          self.by_xpath('/html/body/div[19]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[19]')
          sleep(1)
          self.by_xpath('/html/body/div[20]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[20]')
          sleep(1)
          self.by_xpath('/html/body/div[21]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[21]')
          sleep(1)
          self.by_xpath('/html/body/div[22]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[22]')
          sleep(1)
          self.by_xpath('/html/body/div[23]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[23]')
          sleep(1)
          self.by_xpath('/html/body/div[24]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[24]')
          sleep(1)
          self.by_xpath('/html/body/div[25]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[25]')
          sleep(1)
          self.by_xpath('/html/body/div[26]/div/div[1]/ul/li[1]')
          self.by_xpath('(//input[@type="text"])[26]')
          sleep(1)
          self.by_xpath('/html/body/div[27]/div/div[1]/ul/li[1]')
          self.by_css('[class="el-button el-button--primary"]')
          sleep(1)
          self.by_xpath('(//div[@class="el-tabs__item"])[3]')
          sleep(1)
          self.by_clear_x('(//input[@class="el-input__inner"])[30]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[30]',zongmianji)
          self.by_clear_x('(//input[@class="el-input__inner"])[31]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[31]',x)
          self.by_clear_x('(//input[@class="el-input__inner"])[32]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[32]',y)
          self.by_clear_x('(//input[@class="el-input__inner"])[33]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[33]',z)
          self.by_xpath('(//button[@class="el-button el-button--primary"])[2]')
      else:
          self.by_xpath('(//div[@class="el-tabs__item"])[1]')
          self.by_clear_x('(//input[@class="el-input__inner"])[1]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[1]',zongmianji)
          self.by_clear_x('(//input[@class="el-input__inner"])[2]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[2]',x)
          self.by_clear_x('(//input[@class="el-input__inner"])[3]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[3]',y)
          self.by_clear_x('(//input[@class="el-input__inner"])[4]')
          self.by_xpath_s('(//input[@class="el-input__inner"])[4]',z)
          self.by_xpath('(//button[@class="el-button el-button--primary"])[1]')
      sleep(3)
      self.by_css("a[href='javascript:void(0)']")
#######################################################        满意度评价      ##########################################
class Manyidu(Page):
    def manyidu(self,shenheren,changliang,password):
      LoginPage(self.dr).Login_action(shenheren,password)
      sleep(2)
      if shenheren=="OP.00127":
          self.by_xpath_s('(//input[@type="text"])[1]', "1")
          self.by_xpath_s('(//input[@type="text"])[2]', "1")
          self.by_xpath_s('(//input[@type="text"])[3]', "1")
          self.by_xpath_s('(//input[@type="text"])[4]', "1")
          self.by_xpath_s('(//input[@type="text"])[5]', "1")
          self.by_xpath_s('(//input[@type="text"])[6]', "1")
          self.by_xpath_s('(//input[@type="text"])[7]', "1")
          self.by_xpath_s('(//input[@type="text"])[8]', "1")
      else:
          self.by_xpath_s('(//input[@type="text"])[1]', "5")
          self.by_xpath_s('(//input[@type="text"])[2]', "5")
          self.by_xpath_s('(//input[@type="text"])[3]', "5")
          self.by_xpath_s('(//input[@type="text"])[4]', "10")
      self.by_css('button[class="el-button el-button--primary"]')
      sleep(2)
      self.by_css("a[href='javascript:void(0)']")
#######################################################        结算算钱了      ##########################################
class Suanqian(Page):
    def suanqian(self,shenheren,changliang,password):
      LoginPage(self.dr).Login_action(shenheren,password)
      sleep(2)
      self.by_css('button[class="el-button el-button--default"]')
      sleep(2)
      self.by_css('button[class="el-button el-button--danger"]')
      sleep(1)
      self.by_css('button[class="el-button el-button--default el-button--primary "]')
      sleep(2)
      self.by_css("a[href='javascript:void(0)']")
      sleep(2)
