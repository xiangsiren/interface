#coding=utf-8
import requests


paths = "/dist_new/goodsManage/singleProductL.64e8b.chunk.js"
ss = paths.split(".")
type = ss[len(ss) - 1]
types = ['.css', 'js', '.png', '.jpg', '.jif', '.ico']
if type not in types:
    print("dssdsdsd")