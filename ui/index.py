#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: index.py
@time: 17/4/17 PM8:40
"""
import json

from init import app, session
from ui import render_template
from api.douban import get_book, get_movie



@app.route('/')
def index():
    uid = session.has_key('user')
    if uid:
        return render_template("index.html")
    else:
        return render_template("auth.html")
