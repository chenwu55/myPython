#coding=utf-8
from Basepage import *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    url='/'
    # 定位器
    systemId_loc = (By.ID, "systemId")
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    submit_loc = (By.ID, 'btnSubmit')
    usernameInput_loc=(By.ID, 'usernameInput')

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