#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: recommend
@time: 9/5/17 PM6:12
"""
from sqlalchemy import desc
from init import app,session,jsonify,mysqldb,mongodb
from orm import CollectSimilar,Collect,Resource,User
from random import choice
from bson import ObjectId


@app.route("/similaruser")
def similar_user():
    respose=dict()
    if session.has_key('user'):
        user=session['user']
        uid=user['user_id']
        similar=CollectSimilar.query.filter_by(user_id=uid).order_by(desc(CollectSimilar.similar_score)).first()

        data=get_collect_by_similaruser(uid,similar.similar_id)
        suser=User.query.filter_by(user_id=similar.similar_id).first()
        if data:
            respose['status']=1
            respose['similaruser'] = {'uid': similar.similar_id, 'score': similar.similar_score,'name': suser.nickname}
            respose['data']=data
        else:
            respose = {'status': -1}

    else:
        respose={'status':-1}

    return jsonify(respose)

def get_collect_by_similaruser(uid,sid):
    uset=Collect.query.filter_by(user_id=uid)
    sset=Collect.query.filter_by(user_id=sid)
    u_items=set()
    s_items=set()
    for i in uset:
        u_items.add(i.resource_index)
    for i in sset:
        s_items.add(i.resource_index)
    # print u_items
    # print s_items
    re=list(s_items.difference(u_items))

    if len(re)!=0:
        rid=choice(re)
        resource=Resource.query.filter_by(resource_id=rid).first()
        oid=resource.objectid

        data = mongodb.doubaninfo.find_one({'tid': 3, '_id': ObjectId(oid)})
        data['short']['date']=data['date']
        print data['short']
        return data['short']
    else:
        return None


# respose = dict()
# uid = 1
# similar=CollectSimilar.query.filter_by(user_id=uid).order_by(desc(CollectSimilar.similar_score)).first()
# print similar.similar_id
# data=get_collect_by_similaruser(uid,similar.similar_id)
#
# suser=User.query.filter_by(user_id=similar.similar_id).first()
#
# if data:
#     respose['status']=1
#     respose['similaruser'] = {'uid': similar.similar_id, 'score': similar.similar_score,'name': suser.nickname}
#     respose['data']=data
# else:
#     respose = {'status': -1}
#
#
# print jsonify(respose)