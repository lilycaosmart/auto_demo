'''
Created on 2019年3月27日

@author: yuweilxm
'''

import unittest
import HTMLTestRunner
import time

import os
case_path=os.path.join(os.getcwd(),"cases")




#测试用例路径
listcase="G:\\auto\\test\\cases"

#遍历指定路径下用例文件，将测试用例放入测试套件中，返回测试套件
def creatsuits():
    testunit=unittest.TestSuite()
    #遍历用例
    discover=unittest.defaultTestLoader.discover(case_path,
                                                  pattern="start_*.py",
                                                  top_level_dir=None)
    #将测试用例加入到测试套件中
    for testsuite in discover:
        for test_case in testsuite:
            testunit.addTests(test_case)
    return testunit 

    
alltestname=creatsuits()


now=time.strftime("%Y-%m-%M %H_%M_%S ",time.localtime(time.time()))

#定义测试报告文件
filename="G:\\auto\\report\\"+now+"report.html"

fp=open(filename,"wb")

#执行测试
runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title="自动化测试报告",
    description="用例执行情况说明"
    )
runner.run(alltestname)