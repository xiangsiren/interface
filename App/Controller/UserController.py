#! /usr/bin/env python
# -*- coding: utf-8 -*-
from App.Common.mysql import cli
from App.Model.Models import *
from datetime import datetime

class User:
    def __init__(self):
        self.db = cli().get_session()

    def get_list(self):

        return self.db.query(Users).first()


if __name__ == "__main__":

    u = Case()
    u.url = "user/login"
    u.case_name = "测试用例"
    u.method = 'post'
    u.request_data = "{'name':renren,''pass':'123334'}"
    u.response_data = "{'name':renren,''pass':'123334'}"
    u.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    DBsession = cli().get_session()
    DBsession.add(u)
    DBsession.commit()
    DBsession.close()






