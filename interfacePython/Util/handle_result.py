#coding=utf-8
import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)
from deepdiff import DeepDiff
from interfacePython.Util import get_value
# print(get_value('api3/getbanneradvertver2',"/Config/code_message.json"))
'''[
        {"1006,":"token error"},
        {"10001":"用户名错误"},
        {"10002":"密码错误"}
    ]'''


def handle_result(url, code):

    data = get_value(url, "E:\python\interface\Config\code_message.json")
    print(type(data))
    if data is not None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None


def get_result_json(url,status):
    data = get_value(url, "E:/python/interface/Config/result.json")
    if data !=None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None


def handle_result_json(dict1,dict2):
    '''
    校验格式
    '''
    if isinstance(dict1,dict) and isinstance(dict2,dict):
    #dict1={"aaa":"AAA","bbb":"BBBB","CC":[{"11":"22"},{"11":"44"}]}
    #dict2={"aaa":"123","bbb":"456","CC":[{"11":"111"},{"11":"44"}]}
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False
    
    
if __name__ == "__main__":
    dict2 = {"aaa":"ddd","aaa1":"A1A","bbb":"BBBB","CC":[{"11":"22"},{"11":"44"}]}
    dict1={"aaa":"AAA","bbb":"BBBB","aaa3":"A1A","CC":[{"11":"22"},{"11":"44"}]}
    print(dict1.get("CC"))
    # print(handle_result('api3/getbanneradvertver2',"10002"))
    #print(handle_result_json(dict1,dict2))
    # print(get_result_json("api3/newcourseskill","error"))