#!/usr/bin/env python
# encoding: utf-8


#数据库读取收藏的文章
#对所有文章提取关键字
#提取关键字

from orm import Collect,Resource
import jieba
from init import session,mongodb,app,jsonify
import jieba.analyse
from bs4 import BeautifulSoup
from bson import ObjectId


@app.route('/labels')
def get_labels():
    if session.has_key('user'):
        user=session['user']
        uid=user['user_id']
    else:
        return "<h1>Hello World"
    try:
        cs = Collect.query.filter_by(user_id=uid)

        all_tags = list()
        for tmp in cs:
            rid = tmp.resource_index
            resource = Resource.query.filter_by(resource_id=rid).first()
            oid = resource.objectid

            data = mongodb.doubaninfo.find_one({'tid': 3, "_id": ObjectId(oid)})
            txt = data['content']['body']
            soup = BeautifulSoup(txt, 'lxml')

            text = ""
            tempdiv = soup.find("div", class_="content")
            p = tempdiv.findAll("p")
            for i in p:
                text = text + (i.get_text()).encode('utf-8')

            # jieba.analyse.set_idf_path("/home/wen/python/projects/recommendation/utils/tfidf/cobuild.txt")
            tags = jieba.analyse.extract_tags(text, topK=2)
            print type(tags)
            print tags
            all_tags.extend(tags)
            print ','.join(all_tags)
        return jsonify(all_tags)
    except Exception, e:
        print e


# cs = Collect.query.filter_by(user_id=1)
#
# all_tags = list()
# for tmp in cs:
#     rid = tmp.resource_index
#     resource = Resource.query.filter_by(resource_id=rid).first()
#     oid = resource.objectid
#
#     data = mongodb.doubaninfo.find_one({'tid': 3, "_id": ObjectId(oid)})
#
#     txt = data['content']['body']
#     soup = BeautifulSoup(txt, 'lxml')
#
#     text = ""
#     tempdiv = soup.find("div", class_="content")
#     p = tempdiv.findAll("p")
#     for i in p:
#         text = text + (i.get_text()).encode('utf-8')
#
#     # jieba.analyse.set_idf_path("/home/wen/python/projects/recommendation/utils/tfidf/cobuild.txt.big")
#     topK = 2
#     tags = jieba.analyse.extract_tags(text, topK=topK)
#     all_tags.extend(tags)
# print all_tags