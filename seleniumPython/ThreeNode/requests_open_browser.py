#coding=utf-8
import requests
import json


class requests_webdriver:

    def __init__(self):
        self.driver = self.chrome_driver()
    def chrome_driver(self):
        url = 'http://127.0.0.1:4444/wd/hub/session/'
        # url = 'http://127.0.0.1:4444/wd/hub'
        data = json.dumps({
            'Capabilities':{
                'browserName':'chrome'
            }
        })
        res = requests.post(url, data).json()
        print(res)
        session = res['sessionId']
        driver = url+session
        return driver
    
    def get_url(self,url):
        base_url = self.driver+'/url'
        data = json.dumps({
            "url":url
        })
        requests.post(base_url,data)
    
    def find_element_by_id(self,value):
        base_url = self.driver+'/element'
        data = json.dumps({
            "using":'name',
            "value":value
        })
        res = requests.post(base_url,data).json()['value']['ELEMENT']
        return res


if __name__ == '__main__':
    request_driver = requests_webdriver()
    # request_driver.get_url('https://saas-test.11xiuge.com/')
    # request_driver.find_element_by_id('email')
