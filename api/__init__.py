#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: init.py
@time: 17/4/17 PM8:14
"""
from init import session,jsonify
error_code={
    100:'User not find',
    101:'Password is wrong',
    102:'Unknow Data Format',
    103:'Unidentify error',
}

# def is_auth(func):
#     def _is_auth():
#         if session.has_key('user'):
#             func()
#         else:
#             return jsonify({'status':-1,'message':'auth failed'})
#     return _is_auth()



