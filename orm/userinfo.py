#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: userinfo
@time: 17/4/17 PM9:03
"""
import time
from init import mysqldb as db


class User(db.Model):
    __tablename__ = "userinfo"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    nickname = db.Column(db.String(45))
    gender = db.Column(db.SmallInteger)
    bio = db.Column(db.String(120))
    register_date = db.Column(db.DATETIME)
    id = user_id

    def to_dict(self):
        return {"user_id": self.id, "username": self.username, "nickname": self.nickname, "bio": self.bio}

    def __init__(self, content=None):
        if content:
            self.username = content['username']
            self.password = content['password']
            self.nickname = content['nickname']
            self.bio = content['bio']
            self.gender = content['gender']
            self.register_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
