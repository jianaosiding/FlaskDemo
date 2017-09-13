#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: resource_index
@time: 26/4/17 AM12:19
"""
from init import mysqldb as db


class Resource(db.Model):
    __tablename__ = "resource_index"
    resource_id = db.Column(db.Integer, primary_key=True)
    raw_id = db.Column(db.Integer)
    type_id = db.Column(db.Integer)
    objectid = db.Column(db.String(120))

    def __init__(self, objectid, type_id, raw_id):
        self.raw_id = raw_id
        self.type_id = type_id
        self.objectid = objectid
