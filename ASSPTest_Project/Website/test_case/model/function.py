#coding=utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

####截图
def insert_img(dr,jietu_name):
    func_path=os.path.dirname(__file__)    #获取当前模块路径
    # print func_path
    bese_dir = os.path.dirname(func_path)  #获取上级路径
    # print bese_dir
    bese_dir = str(bese_dir)
    bese_dir = bese_dir.replace('\\', '/') #相对路径的转换（转换成字符串）
    # print bese_dir
    base = bese_dir.split('/Website')[0]  #拆分解
    # print base
    filepath = base + '/Website/test_report/picture/' + jietu_name
    # print filepath
    dr.get_screenshot_as_file(filepath)
####发邮箱
def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = 'cw55555cw@163.com'
    password = '1314179' #根据自己邮箱密码来设置

    sender = 'cw55555cw@163.com'
    receives = ['cw55555cw@163.com', 'chenwu_55@163.com']

    subject = 'Web Selenium 自动化测试报告'


    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")
####生成报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file
####


