#coding=utf-8
import time
from appium import webdriver
from AppiumPython.util.write_user_command import WriteUserCommand
class BaseDriver:
	def android_driver(self,i):
		print("this is android_driver:",i)
		#devices_name adb devices
		#port
		write_file = WriteUserCommand()
		devices = write_file.get_value('user_info_'+str(i),'deviceName')
		port = write_file.get_value('user_info_'+str(i),'port')
		capabilities = {
		  "platformName": "Android",
		  #"automationName":"UiAutomator2",
		  "deviceName": devices,
		  "app": "/Users/ren/Documents/new_app_versionName_3.8.1_versionCode_38_packageTest_debug.apk",
		  "appWaitActivity":"cn.com.open.mooc.user.login.MCLoginActivity",
		  "noReset":"true",
		  # "platforVersion":"4.4.4",
		  # "appPackage":"cn.com.open.mooc"
		  #"newCommandTimeout":'180'
		}
		driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub",capabilities)
		time.sleep(10)
		return driver
