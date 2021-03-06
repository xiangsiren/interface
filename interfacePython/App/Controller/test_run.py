#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.getcwd())

from interfacePython.App.Common.mysql import cli
import unittest
# from ddt import ddt,data,file_data,unpack
import ddt
from interfacePython.Util import HTMLTestRunner
from interfacePython.Base import request

DBsession = cli().get_session()
case1 = DBsession.query(Case).all()


@ddt.ddt
class TestRunMain(unittest.TestCase):

    @ddt.data(*case1)
    def test_case(self, case1):
        res = request.run_main(case1.method, case1.request_url + '&debug=true', case1.request_data)
        self.assertEqual(res['code'], 0)


def add_case():
    # case_path = os.path.join(base_path, "Run")
    case_path = '/Users/ren/Desktop/web/python/interface/App/Controller'
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
    return discover


if __name__ == "__main__":
    file_path = '/Users/ren/Desktop/web/python/interface/Report/report.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="斑马仓SaaS", description="慕容注释")
        runner.run(add_case())
    f.close()







