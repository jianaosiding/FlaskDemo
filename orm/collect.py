#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: collect
@time: 6/5/17 PM1:19
"""
from init import mysqldb as db


class Collect(db.Model):
    __tablename__ = "collect"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    resource_index = db.Column(db.Integer)

    def __init__(self, user_id, resource_index):
        self.user_id = user_id
        self.resource_index = resource_index
