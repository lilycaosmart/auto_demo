'''
Created on 2019年3月29日

@author: yuweilxm
'''

from selenium import webdriver
import unittest



class Login(unittest.TestCase):
    
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver=webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(5)
        self.base_url="http://testtop.huikao8.cn/login"
        self.verificationErrors=[]
        self.accept_next_alert=True
        


    def test_login(self):
        driver=self.driver
        driver.get(self.base_url)
        
        driver.maximize_window()
        ss=driver.find_elements_by_class_name("el-input__inner")
        ss[0].send_keys("18317119693")
        ss[1].send_keys("123456")
        driver.find_element_by_tag_name("button").click()
        driver.implicitly_wait(5)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()