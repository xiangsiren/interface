#coding=utf-8
import sys
sys.path.append('/Users/ren/Desktop/web/python/interface/AppiumPython')
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from AppiumPython.util.read_init import ReadIni
from AppiumPython.util.get_by_local import GetByLocal


def get_driver():
	capabilities = {
	  "platformName": "Android",
	  #"automationName":"UiAutomator2",
	  "deviceName": "MUMU home",
	  "app": "/Users/ren/Documents/new_app_versionName_3.8.1_versionCode_38_packageTest_debug.apk",
	  # "appWaitActivity":"com.bckj.banmacang.activity.SplashActivity",
	  "noReset":"true"
	}
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
	time.sleep(10)
	return driver

#获取屏幕的宽高
def get_size():
	size = driver.get_window_size()
	width = size['width']
	height = size['height']
	return width,height

#向左边滑动
def swipe_left():
	#[100,200]
	x1 = get_size()[0]/10*9
	y1 = get_size()[1]/2
	x = get_size()[0]/10
	driver.swipe(x1,y1,x,y1,2000)

#向右边滑动
def swipe_right():
	#[100,200]
	x1 = get_size()[0]/10
	y1 = get_size()[1]/2
	x = get_size()[0]/10*9
	driver.swipe(x1,y1,x,y1,2000)

#向上滑动
def swipe_up():
	#[100,200]direction
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10*9
	y = get_size()[1]/10
	driver.swipe(x1,y1,x1,y,1000)

#向下滑动
def swipe_down():
	#[100,200]
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10
	y = get_size()[1]/10*9
	driver.swipe(x1,y1,x1,y)

def swipe_on(direction):
	if direction == 'up':
		swipe_up()
	elif direction == 'down':
		swipe_down()
	elif direction == 'left':
		swipe_left()
	else:
		swipe_right()

def go_login():
	print(driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login'))
	driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()

def login():
	get_by_local = GetByLocal(driver)	
	user_element = get_by_local.get_element('username')
	user_element.send_keys('libai123')
	
	get_by_local.get_element('password').send_keys('123456')
	get_by_local.get_element('login_button').click()

def login_by_class():
	element = driver.find_elements_by_class_name('android.widget.EditText')
	print("444444444")
	print(element)
	print("55555555")
	element[0].send_keys('libai123')
	element[1].send_keys('123456')
	elements = driver.find_elements_by_class_name('android.widget.TextView')
	print("666666666")
	print(elements)
	print("777777777777")
	elements[3].click()
	#element.click()

def login_by_node():

	driver.find_element_by_id('com.bckj.banmacang:id/et_login_password_mobile').send_keys('dishini')
	driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys('123456')

	driver.find_element_by_id('com.bckj.banmacang:id/tv_login').click()


def login_by_uiautomator():
	# driver.find_element_by_android_uiautomator('new UiSelector().text("libai123")').clear()
	driver.find_element_by_android_uiautomator('new UiSelector().text("请输入您的登录账号")').send_keys('dishini')
	driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.bckj.banmacang:id/et_login_password")').send_keys('123456')

def login_by_xpath():
	#driver.find_element_by_xpath('//*[contains(@text,"忘记")]').click()
	#driver.find_element_by_xpath('//android.widget.TextView[@text="忘记密码"]').click()
	driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::android.widget.RelativeLayout').send_keys('123123')
	driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::*[@index="2"]').send_keys('222222')
def get_web_view():
	time.sleep(10)
	webview = driver.contexts
	for viw in webview:
		if 'WEBVIEW_cn.com.open.mooc' in viw:
			driver.switch_to.context(viw)
			break
	driver.find_element_by_link_text('C').click()
	try:
		driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
	except Exception as e:
		
	
		driver.switch_to.context(webview[0])
		driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
		raise e
	print(webview)

def get_tost():
	time.sleep(2)
	driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('18513199586')
	tost_element = ("xpath","//*[contains(@text,'请输入密码')]")
	WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(tost_element))

driver =get_driver()
login_by_node()
swipe_on('up')
#time.sleep(1)
#swipe_on('left')
#time.sleep(1)
#swipe_on('right')
#time.sleep(1)
#swipe_on('left')
#time.sleep(1)
#swipe_on('up')
#time.sleep(10)
# login_by_class()
#login_by_xpath()
#get_tost()
# login()
# login_by_uiautomator()
