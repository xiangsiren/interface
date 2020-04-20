#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC



# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get('https://saas-test.banmacang.com/#/?_k=2547vu')
driver.find_element_by_name('email').send_keys('admin')
driver.find_element_by_name('password').send_keys('13412341234')
driver.find_element_by_class_name('moco-btn').click()
# time.sleep(2)
# driver.get('https://www.imooc.com/user/setbindsns')
# driver.find_elements_by_class_name('inner-i-box')[1].find_element_by_class_name('moco-btn-normal').click()
# handl_list = driver.window_handles
# current_handle = driver.current_window_handle
# print(handl_list)
# #[1,2,3,4]
# time.sleep(15)
# for i in handl_list:
#     if i != current_handle:
#         time.sleep(2)
#         driver.switch_to.window(i)
#         ti = EC.title_contains("网站连接")
#         if ti(driver) == True:
#             break
# time.sleep(5)
# driver.find_element_by_id('userId').send_keys('test')
# time.sleep(5)
# driver.close()



# from selenium import webdriver
#
# firefox_options = webdriver.ChromeOptions()
# driver = webdriver.Remote(
#     # command_executor='http://180.76.56.118:4444/wd/hub',
#     command_executor='http://localhost:4444/wd/hub',
#     options=firefox_options
# )
# driver.get("http://www.baidu.com")
# driver.quit()
