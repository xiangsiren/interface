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
from datetime import datetime

DBsession = cli().get_session()
case1 = DBsession.query(Case).filter(Case.id == 6).one()
# DBsession.commit()
# DBsession.close()
res = request.run_main(case1.method,case1.path,case1.request_data)

print(res)