#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: critics
@time: 26/4/17 AM12:48
"""
from init import mysqldb as db
class Critics(db.Model):
    __tablename__ = "critics"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer)
    resource_id=db.Column(db.Integer)
    critics=db.Column(db.Integer)
    def __init__(self,user_id,resource_id,critics):
        self.user_id=user_id
        self.resource_id=resource_id
        self.critics=critics


