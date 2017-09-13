#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence
@file: auth.py
@time: 17/4/17 PM8:15
"""
from init import (
    app,
    jsonify,
    request,
    mysqldb,
    session
)
from flask import redirect
from orm import User
from api import error_code


def fail(error):
    return {
        'status': 0,
        'error': error,
        'msg': error_code[error]
    }


def success(user):
    return {
        'status': 1,
        'content': user.to_dict()
    }


@app.route('/login', methods=['POST'])
def login():
    if not request.json:
        return jsonify(fail(102))
    else:
        username = request.json.get("username")
        password = request.json.get("password")
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify(fail(100))
        elif user.password != password:
            return jsonify(fail(101))
        elif user.password == password:
            session['user'] = user.to_dict()
            return jsonify(success(user))
        else:
            return jsonify(fail(103))


@app.route('/signup', methods=['POST', 'GET'])
def sigup():
    if request.method == 'POST':
        content = request.json.get("content")
        user = User(content)
        mysqldb.session.add(user)
        try:
            mysqldb.session.commit()
            return jsonify({"status": 1, "content": "success"})
        except Exception, e:
            return jsonify({"status": 0, "content": e.message})
    else:
        content = dict()
        content['username'] = request.args.get('username')
        content['password'] = request.args.get('password')
        content['nickname'] = request.args.get('nickname')
        content['gender'] = request.args.get('gender')
        content['bio'] = request.args.get('bio')
        user = User(content)
        mysqldb.session.add(user)
        try:
            mysqldb.session.commit()
            return redirect('/')
        except Exception, e:
            return jsonify({"status": 0, "content": e.message})


@app.route('/logout')
def logout():
    if session.has_key('user'):
        session.pop('user')
    return redirect('/')
