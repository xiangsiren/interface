#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get('https://saas-test.banmacang.com/#/?_k=2547vu')
'''
登陆页面
'''
driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/input").send_keys('admin')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[3]/input').send_keys('13412341234')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/button').click()
time.sleep(2)
'''
首页
'''


driver.close()
