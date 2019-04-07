#coding=utf-8
import unittest
from model.function import *
from BSTestRunner import BSTestRunner
import time
report_dir='./test_report'
test_dir='./test_case'
print u"开始运行测试用例..."
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_cg_dianjiang.py")
now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+u'新增商场.html'

print u"开始写报告..."
with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title=U"测试报告" ,description=u"ASSP橱柜点将申请测试")
    runner.run(discover)
    f.close()






