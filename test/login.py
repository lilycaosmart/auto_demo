#coding=utf-8

from selenium import webdriver
import time
from distutils.tests.test_register import Inputs

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

dr=webdriver.Chrome(chrome_options=option)

dr.maximize_window()
dr.implicitly_wait(5)

dr.get("http://testtop.huikao8.cn/login")
#dr.get("http://www.baidu.com")
dr.implicitly_wait(5)
ss=dr.find_elements_by_class_name("el-input__inner")
ss[0].send_keys("18317119693")
ss[1].send_keys("123456")

# for s in ss:
#     if s.__getattribute__("type") =="text":
#         s.sendkeys("18317119693")
#     elif s.__getattribute__("type")=="password":
#         s.sendkeys("111111")
#         
dr.find_element_by_tag_name("button").click()
dr.implicitly_wait(5)
dr.maximize_window()
# try:
username=dr.find_element_by_class_name("people-info").text
if username=="test测试（18317119693）":
    print("登录成功!")
else:
    print("登录失败")
    
# except AssertionError as e:
#     print("登录失败")

#dr.quit() 
