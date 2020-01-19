#! /usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
import time
import sys
import os
import app
# base_path = os.getcwd()
# sys.path.append(base_path)


from Base.base_request import request
from App.Common.mysql import cli
from App.Model.Models import *

DBsession = cli().get_session()
case1 = DBsession.query(Case).filter(Case.id == 1).one()
res = request.run_main(case1.method, case1.request_url + '&debug=true', case1.request_data.encode())
print(res)



# i = 1
# DBsession = cli().get_session()
# try:
#     counts = DBsession.query(Case).count()
#     while(i<= counts):
#         case1 = DBsession.query(Case).filter(Case.id == i).one()
#         res = request.run_main(case1.method, case1.request_url + '&debug=true', case1.request_data)
#         i += 1
#         print(res)
# except Exception as e:
#     '''异常的父类，可以捕获所有的异常'''
#     print(e)
# finally:
#     # DBsession.commit()
#     DBsession.close()


# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['noReset'] = 'true'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appWaitActivity'] = 'com.bckj.banmacang.activity.SplashActivity'
# desired_caps['app'] ='/Users/ren/Documents/new_app_versionName_3.8.1_versionCode_38_packageTest_debug.apk'
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# time.sleep(5)
# driver.find_element_by_id('com.bckj.banmacang:id/goto_settings').click()
# driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
# driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
# driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
# print("3333333333")
# sizes = driver.get_window_size()
# x1 = sizes['width']/10 * 9
# y1 = sizes['height']
# x = sizes['width']/10
# driver.swipe(x1,y1,x,y1)
# driver.swipe(x1,y1,x,y1)
# driver.swipe(x1,y1,x,y1)
# print(x1,y1,x)
# driver.find_element_by_id('com.bckj.banmacang:id/et_login_password_mobile').send_keys("libai123")
# driver.find_element_by_id('com.bckj.banmacang:id/et_login_password').send_keys("123456")
# driver.find_element_by_id('com.bckj.banmacang:id/tv_login').click()

