#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: compute_idf
@time: 10/5/17 PM3:27
"""

import jieba
with open('air_plane.txt','r') as f:
    txt=f.read()
seg_list=jieba.cut(txt,cut_all=False)

word_count=dict()
for i in seg_list:
    if word_count.has_key(i):
        word_count[i]=word_count[i]+1
    else:
        word_count[i]=1
wordcount=sorted(word_count.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

for k,v in wordcount:
    print '关键词：',k,' --出现次数:',v