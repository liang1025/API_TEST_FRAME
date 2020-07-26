#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: exception_demo.py
# @time: 2020/7/19 9:40 上午

import requests
from requests.exceptions import RequestException

res = requests.get(url='http://google.com.hk/')
print( res.status_code )

try:
    num_list = [1,2,3,4,5]
    print( num_list[6] )
except IndexError as e:
    print( '索引错误' )
except Exception as e:
    print( '系统错误' )  #已知可能会发生的异常写前面，不确定原因的异常写在最后

print( 'hello' )




