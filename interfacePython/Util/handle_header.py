#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from interfacePython.Util import read_json

def get_header():
    data = read_json("E:\python\interface\Config\header.json")
    return data

def header_md5():
    '''
    
    '''
    data = get_header()
    key = data['imooc_key']


if __name__ == "__main__":
    print(get_header()['imooc_key'])