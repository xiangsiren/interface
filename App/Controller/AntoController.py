#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
