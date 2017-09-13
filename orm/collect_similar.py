#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: collect_similar
@time: 9/5/17 PM6:00
"""
from init import mysqldb as db


class CollectSimilar(db.Model):
    __tablename__ = "collect_similar"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    similar_id = db.Column(db.Integer)
    similar_score = db.Column(db.Float)

    def __init__(self, user_id, similar_id, similar_score):
        self.user_id = user_id
        self.similar_id = similar_id
        self.similar_score = similar_score
