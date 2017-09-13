#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence
@file: init.py
@time: 17/4/17 PM8:33
"""
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient


mgclient = MongoClient('localhost', 27017)
app = Flask(__name__)


app.secret_key = 'what the fucking key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jian@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mysqldb = SQLAlchemy(app)
mongodb = mgclient['scraping']
