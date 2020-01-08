#coding=utf-8
import sys
import os
base_path = os.getcwd()
import unittest
# sys.path.append(base_path)
import json
import mock
from Util import HTMLTestRunner
from Base.base_request import request
import requests


def read_json():
    with open("E:/python/interface/Config/user_data.json") as f:
        data = json.load(f)
    return data


def get_value(key):
    data = read_json()
    return data[key]


host = 'http://www.baidu.com/'


class RenrenCase(unittest.TestCase):

    def test_banner(self):
        url = host+'api3/getbanneradvertver2'
        data = {
            'timestamp':'1561269343481',
            'uid':'7213561',
            'token':'7ad09430cbaf927af642ab843ec374ef',
            'type':'1',
            'marking':'androidbanner',
            'uuid':'41b650ef846688193728ff7381eb6c1c',
            'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY'
        }
        # mock_method = mock.Mock(return_value=get_value('/api3/getbanneradvertver2'))
        # request.run_main = mock_method
        res = request.run_main('post',url,data)

        self.assertEqual(res['errorCode'],1000)

    def beta4(self):
        url = host+'api3/beta4'
        data = {
            'timestamp':'1561269343486',
            'uid':'7213561',
            'token':'66640986fb118dda4334719ac8afbf89',
            'uuid':'41b650ef846688193728ff7381eb6c1c',
            'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY',
        }
        mock_method = mock.Mock(return_value=get_value('api3/beta4'))
        request.run_main = mock_method
        res = request.run_main('post',url,data)

        self.assertEqual(res['errorCode'],1000)
    
    def test_login(self):

        url = "https://saas-test.banmacang.com/bmc_hb/1.0/account/login"
        data = {
            "account": "libai123",
            "password": "2ae849ff090b7205566e268123473e700d6957ce",
            "belong_to": 0,
            "group_type": 0,
            "sys_source": "PC",
            "sys_version": "V2.2.1"
        }

        # res = request.run_main('post',url,data)

        res = requests.post(url, data=json.dumps(data), verify=False).json()

        self.assertEqual(res["code"],0)


if __name__ == "__main__":

    print("5551= ",__name__)
    suite = unittest.TestSuite()
    suite.addTest(RenrenCase('test_banner'))
    suite.addTest(RenrenCase('test_login'))
    # file_path = base_path+'/Report/repor.html'
    file_path = 'E:\python\interface\Report\\report.html'
    with open(file_path, 'wb') as f:
        # for line in f.readlines(): print(line.strip())  # 把末尾的'\n'删掉
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is test", description="bammacang test")
        runner.run(suite)
    f.close()
    #unittest.main()
