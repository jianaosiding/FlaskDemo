#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: user_based_cf
@time: 2/5/17 PM5:04
"""

from orm import Collect,CollectSimilar
from init import mysqldb

collect=mysqldb.session.query(Collect)
mysqldb.session.query(CollectSimilar).delete()
sm=dict()
for i in collect:
    if sm.has_key(i.user_id):
        sm[i.user_id].add(i.resource_index)
    else:
        sm[i.user_id]=set()
        sm[i.user_id].add(i.resource_index)

for i in sm.keys():
    print 'user id:',i
    for j in sm.keys():
        if i !=j:
            u=sm[i].union(sm[j])
            n=sm[i].intersection(sm[j])
            score=len(n) / float(len(u))
            print i,j,score
            cs=CollectSimilar(i,j,score)
            mysqldb.session.add(cs)
            mysqldb.session.commit()
