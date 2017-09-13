#!/usr/bin/env python
# encoding: utf-8

"""

for test

@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence
@file: get_data
@time: 25/4/17 PM10:56
"""
from init import app, mongodb, jsonify
import random
from flask import render_template

# @app.route('/')
# def index():
#     return render_template('index.html')
#     return jsonify({'message':'api version v1.0.1'})

@app.route('/movies')
def get_movie():
    content=list()
    for i in range(10):
        cursor=mongodb.doubaninfo.find({"tid":1})
        seed=random.randint(0, cursor.count()-1)
        cursor.skip(seed)
        dl=cursor.next()
        dl['oid']=str(dl.pop('_id'))
        content.append(dl)
        if len(content)>=3:
            break

    return jsonify(content)

@app.route('/books')
def get_book():
    content=list()
    for i in range(10):
        cursor=mongodb.data.find({"tid":2})
        seed=random.randint(0, cursor.count()-1)
        cursor.skip(seed)
        dl=cursor.next()
        oid=dl.pop('_id')
        dl['oid']=str(oid)
        content.append(dl)
        if len(content)>=1:
            break

    return jsonify(content)
