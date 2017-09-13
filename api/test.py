#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: test
@time: 18/4/17 AM2:07
"""
# org
import random

# third part
from pymongo import MongoClient

# dry
from orm import Resource, Collect
from init import mysqldb as mysql_db
from init import app, jsonify, session


mongoConn = MongoClient("localhost", 27017)
scraping = mongoConn['scraping']
db = scraping['doubaninfo']


@app.route("/data")
def data():
    rs_list = []
    for i in range(3):
        cursor = db.find({"tid": 3})
        seed = random.randint(0, cursor.count() - 1)
        cursor.skip(seed)
        zhihu = cursor.next()
        zhihu['short']['date'] = zhihu['date']
        rs_list.append(zhihu['short'])
        # zhihu['oid']=str(zhihu.pop("_id"))

    response = jsonify(rs_list)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/detail/<int:id>")
def detail(id):
    rs = db.find_one({'tid': 3, 'id': id})
    rs = rs['content']['body']
    box = dict()
    box['content'] = rs.encode('utf8')
    response = jsonify(box)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/collect/<int:id>")
def collect(id):
    authed = session.has_key('user')
    if not authed:
        return jsonify({'status': -1, 'message': 'auth failed'})
    uid = session['user']['user_id']
    rs = db.find_one({'tid': 3, 'id': id})
    if not rs:
        return jsonify({'status': -1, 'message': 'Not find items in nosql'})
    oid = str(rs.pop("_id"))
    print oid
    resource = Resource.query.filter_by(objectid=oid).first()
    if resource:
        print '资源存在'
    else:
        print '插入资源'
        resource = Resource(objectid=oid, raw_id=id, type_id=3)
        mysql_db.session.add(resource)
        mysql_db.session.commit()
    collect = Collect.query.filter_by(resource_index=resource.resource_id, user_id=uid).first()
    if collect:
        return jsonify({'status': -1, 'message': 'You have do this'})
    else:
        collect = Collect(user_id=uid, resource_index=resource.resource_id)
        mysql_db.session.add(collect)
        mysql_db.session.commit()
        return jsonify({'status': 1, 'message': 'success add to your collection'})


@app.route("/is_logined")
def is_logined():
    uid = session.has_key('user')

    if uid:
        response = jsonify({'code': 'true'})
    else:
        response = jsonify({'code': 'false'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/test/login")
def test_login():
    session['user'] = 1
    response = jsonify({'code': 'true'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/test/logout")
def test_logout():
    session.pop('user')
    return jsonify({'code': 'true'})


@app.route("/test/userinfo")
def userinfo():
    rs = dict()
    if session.has_key('user'):
        user = session['user']
        rs['status'] = 1
        rs['message'] = user
    else:
        rs['status'] = -1
        rs['message'] = 'Auth Failed!'
    return jsonify(rs)


@app.route("/test/get_collect")
def get_collect():
    authed = session.has_key('user')
    if not authed:
        return jsonify({'status': -1, 'message': 'auth failed'})
    collect = Collect.query.filter_by(user_id=session['user']['user_id'])
    data_set = list()
    for i in collect:
        resource = Resource.query.filter_by(resource_id=i.resource_index).first()
        from bson import ObjectId
        data = db.find_one({'tid': 3, '_id': ObjectId(resource.objectid)})
        data_set.append(data['short'])
    return jsonify({'status': 1, 'content': data_set})


@app.route("/test/mv")
def test_mv():
    check = random.randint(0, 1)
    if check:
        c = db.find({'tid': 1})
        seed = random.randint(0, c.count() - 1)
        c.skip(seed)
        mv = c.next()
        oid = mv.pop("_id")
        summary = mv['content']['summary'].strip()
        mv['content']['summary'] = summary[0:60] + "...."
    else:
        c = db.find({'tid': 2})
        seed = random.randint(0, c.count() - 1)
        c.skip(seed)
        mv = c.next()
        oid = mv.pop("_id")
        mv['content']['summary'] = "Coming Soon!  stay hungry stay foolish \n------ Steve Jobs,Stanford 2005  "
    response = jsonify(mv)
    return response
