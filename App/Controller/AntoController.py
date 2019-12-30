#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import App.Common.mysql
from App.Common.mysql import cli
from App.Model.Models import *
from datetime import datetime

DBsession = cli().get_session()
case1 = DBsession.query(Case).filter(Case.id == 6).one()
# DBsession.commit()
# DBsession.close()

print(type(case1))
print(case1.path)
