#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())
from App.Common.mysql import cli
from App.Model.Models import *
from datetime import datetime
# import json
types = ['css', 'js', 'png', 'jpg', 'jif', 'ico']


class GetData:

    def request(self, flow):

        self.request_url = flow.request.url
        # print("request_url:-------->", self.request_url)
        if "saas-test.banmacang.com" in flow.request.url:
            request_headers = flow.request.headers
            path = flow.request.path.split(".")
            t = path[len(path) - 1]
            if t not in types:
                print("请求路径==" + flow.request.path.split("?")[0])
                print("请求方法==" + flow.request.method)
                print("请求data==" + str(flow.request.text))
                c = Case()
                c.path = flow.request.path.split("?")[0]
                c.case_name = "测试用例"
                c.method = flow.request.method
                c.request_data = str(flow.request.text)
                c.request_url = flow.request.url
                c.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                DBsession = cli().get_session()
                DBsession.add(c)
                DBsession.commit()
                DBsession.close()

            # if 'image' in request_headers['accept']:
            #     print("图片不抓取了= " + flow.request.path)
            # elif '.js' in flow.request.path:
            #     print("js路径==" + flow.request.path)
            # else:
                # print(request_headers['Content-Type'])
                # ctx.log.warn("请求头==" + str(flow.request.headers))
                # print("请求路径==" + flow.request.path)
                # print("请求方法==" + flow.request.method)
                # print("请求url==" + flow.request.url)
                # print("请求主机==" + flow.request.host)
                # print("请求数据" + str(request_data))
            #
            # request_pr = request_data.query
            # request_form = request_data.urlencoded_form
            # print("request_pr:------------->",request_pr)
            # print("request_form:---------->",request_form)
            # print("request_form:---------->",request_data.headers)
            # print("=====222222222222========")
        #     c = Case()
        #     c.url = self.request_url
        #     c.case_name = "测试用例"
        #     c.method = request_data.urlencoded_form
        #     c.request_data = flow.
        #     c.response_data = "{'name':renren,''pass':'123334'}"
        #     c.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #     DBsession = cli().get_session()
        #     DBsession.add(c)
        #     DBsession.commit()
        #     DBsession.close()

    def response(self, flow):
        if 'ssbanmacang.com' in self.request_url:

            response_header = flow.response.headers
            # print("响应头==" + str(flow.response.headers))

            conten_type = response_header['Content-Type']
            print("conten_type========>", conten_type)
            if conten_type == 'image/jpeg':
                print("这个返回的是图片")
            elif 'json' in conten_type:
                print("响应状态码==" + str(flow.response.status_code))
                print("响应文本==" + flow.response.text)
            elif 'text' in conten_type:
                print("text==" + flow.response.text)
            else:
                print("格式不需要了")
            # host = self.request_url.split(".com")
            # base_url = host[0]
            # url = host[1]
            # # /api3/getbanneradvertver2
            # # api3/getbanneradvertver2?aaa=sss
            # if "?" in host[1]:
            #     url = url.split("?")[0]
            # print("====>", url)
            # data = json.dumps(get_value(url))
            # print("----->data:", data)
            # response_data.set_text(data)
            '''
            response_header = response_data.headers
            conten_type = response_header['Content-Type']
            print("========>",conten_type)
            if conten_type == 'image/jpeg':
                print("这个返回的是图片")
            elif  'json' in conten_type:
                print("code=========>",response_data.status_code)
                print("response=======>",response_data.text)
            else:
                print("格式不是我们预期的")
            '''
            # 1、高级得mock
            # mitmweb -s App\Controller\CaseController.py


addons = [
    GetData()
]
if __name__ == "__main__":
    print("3333")
