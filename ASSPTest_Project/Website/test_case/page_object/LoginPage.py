#coding=utf-8
from Basepage import *
from selenium.webdriver.common.by import By
class LoginPage(Page):
    url='/'
    # 定位器
    systemId_loc = (By.ID, "systemId")
    username_loc = (By.ID, 'username')
    usernameInput_loc = (By.ID, 'usernameInput')  #mtds登录按钮
    password_loc = (By.ID, 'password')
    submit_loc = (By.ID, 'btnSubmit')


    # 组织编码输入框元素
    def type_systemId(self,systemId):
        self.find_element(*self.systemId_loc).clear()
        self.find_element(*self.systemId_loc).send_keys(systemId)
    # 用户名输入框元素
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    #密码输入框元素
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    #MTDS登录用
    def type_username_mtds(self,usernameInput):
        self.find_element(*self.usernameInput_loc).clear()
        self.find_element(*self.usernameInput_loc).send_keys(usernameInput)

    def Login_action_mtds(self,systemId,usernameInput,password):
        self.open()
        self.type_systemId(systemId)
        self.type_username_mtds(usernameInput)
        self.type_password(password)
        self.type_submit()
        sleep(0.5)
        self.dr.switch_to.frame('content')


    LoginPass_loc=(By.LINK_TEXT,u'退出登录')
    loginFail_loc = (By.ID, 'username')

    def type_loginPass_hint(self):
        return self.find_element(*self.LoginPass_loc).text

    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text


class Zhonglogin(Page):
    def denglu(self,shenheren,password):
        self.open()
        self.by_clear_i("username")
        sleep(1)
        self.by_ids("username",shenheren)
        self.by_clear_i("password")
        self.by_ids("password",password)
        self.by_id("btnSubmit")

#首页进入活动页面
class Daiban(Page):
    def daiban(self,changliang):
        self.by_css_s('[placeholder="搜索待办事项"]',changliang)
        sleep(1)
        try:
            self.by_css('i[class="el-icon-search"]')
            sleep(1)
            self.by_css('span[style="cursor: pointer;"]')
        except:
            sleep(2)
            self.by_css('i[class="el-icon-search"]')
            sleep(1)
            self.by_css('span[style="cursor: pointer;"]')

#是否异常点将判断
class shifouyichang():
    def __init__(self,decoration_type,storefront_type,proportion):
        self.decoration_type = decoration_type
        self.storefront_type = storefront_type
        self.proportion = proportion
        self.zc = u"正常点将"
        self.yc = u"异常点将"

    def mianjipanduan_1(self):
        if self.proportion >= 150:
            type1 = "1"
            print u"展示面积大于等于150属于" + self.zc
        else:
            type1 = "2"
            print u"展示面积小于150属于" + self.yc
        return type1
    def mianjipanduan_2(self):
        if self.proportion >= 500:
            type1 = "1"
            print u"展示面积大于等于500属于" + self.zc
        else:
            type1 = "2"
            print u"展示面积小于500属于" + self.yc
        return type1
    def mianjipanduan_3(self):
        if self.proportion >= 50:
            type1 = "1"
            print u"展示面积大于等于50属于" + self.zc
        else:
            type1 = "2"
            print u"展示面积小于50属于" + self.yc
        return type1
    def mianjipanduan_4(self):
        if self.proportion >= 100:
            type1= "1"
            print u"展示面积大于等于100属于" +self.zc
        else:
            type1 = "2"
            print u"展示面积小于100属于" + self.yc
        return type1
    def mianjipanduan_5(self):
        if self.proportion >= 30:
            type1 = "1"
            print u"展示面积大于等于30属于" + self.zc
        else:
            type1 = "2"
            print u"展示面积小于30属于" + self.yc
        return type1
    def mianjipanduan_6(self):
        if self.proportion >= 300:
            type1 = "1"
            print u"展示面积大于等于300属于" + self.zc
        else:
            type1 = "2"
            print u"展示面积小于300属于" + self.yc
        return type1
    def storefront_type1(self):
        if self.storefront_type == '2':
            print u"店面类型：高端馆店"
            type1=self.mianjipanduan_1()
            return type1
        elif self.storefront_type == '3':
            print u"店面类型：橱柜旗舰店"
            type1=self.mianjipanduan_2()
            return type1
        elif self.storefront_type == '4':
            print u"店面类型：橱柜标准A店"
            type1=self.mianjipanduan_1()
            return type1
        elif self.storefront_type == '5':
            print u"店面类型：橱柜标准B店"
            type1=self.mianjipanduan_1()
            return type1
        elif self.storefront_type == '6':
            print u"店面类型：厨卫生活馆"
            type1=self.mianjipanduan_6()
            return type1
        elif self.storefront_type == '7':
            print u"店面类型：整装店"
            type1=self.mianjipanduan_5()
            return type1
        elif self.storefront_type == '8':
            print u"店面类型：家装店"
            type1=self.mianjipanduan_3()
            return type1
        elif self.storefront_type == '9':
            print u"店面类型：社区店"
            type1=self.mianjipanduan_3()
            return type1
        elif self.storefront_type == '10':
            print u"店面类型：购物中心店"
            type1=self.mianjipanduan_4()
            return type1
        elif self.storefront_type == '11':
            print u"店面类型：百货专卖"
            type1=self.mianjipanduan_3()
            return type1
        elif self.storefront_type == '12':
            print u"店面类型：国美店"
            type1=self.mianjipanduan_3()
            return type1
        elif self.storefront_type == '13':
            print u"店面类型：分销店面"
            type1=self.mianjipanduan_3()
            return type1
    def dayinzhuangtai(self):
        if   self.decoration_type == "2":
            print u'装修类型:新开店面'
            type1=self.storefront_type1()
            return type1
        elif self.decoration_type== "3":
            print u'装修类型:老店扩大'
            type1=self.storefront_type1()
            return type1
        elif self.decoration_type == "4":
            print u'装修类型:全新装修'
            type1=self.storefront_type1()
            return type1
        else:
            print u'装修类型:局部整改点将类型不受面积影响'
            type1="1"
            return type1


# import random
# decoration_type= str(random.randint(2,6))
# storefront_type=str(random.randint(2,13))
# proportion = random.randrange(5, 500, 10)
# type1=shifouyichang(decoration_type,storefront_type,100).dayinzhuangtai()
# print type1

