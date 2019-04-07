#coding=utf-8
import unittest
from BSTestRunner import BSTestRunner
import time
report_dir='./test_report'
test_dir='./test_case'
print u"开始运行测试用例..."
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")
now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+u'登录测试.html'

print u"开始写报告..."
with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title=U"测试报告" ,description=u"ASSP登录测试")
    runner.run(discover)
    f.close()






