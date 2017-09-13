#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: compute_idf
@time: 10/5/17 PM4:28
"""
import jieba
words_box=list()

with open('txt_store.txt') as f:
    txt=f.readline()
    while(len(txt)):
        seg_list = jieba.cut(txt, cut_all=False)
        word_count = dict()
        for i in seg_list:
            if word_count.has_key(i):
                word_count[i] = word_count[i] + 1
            else:
                word_count[i] = 1
        words_box.append(word_count)
        txt = f.readline()


with open('txt_store.txt','r') as f:
    txt=f.read()
seg_list=jieba.cut(txt,cut_all=False)
word_dict=dict()
for i in seg_list:
    if word_dict.has_key(i):
        word_dict[i]=word_dict[i]+1
    else:
        word_dict[i]=1
word_count=dict()
for k,v in word_dict.items():
    for i in words_box:
        if i.has_key(k):
            if word_count.has_key(k):
                word_count[k]=word_count[k]+1
            else:
                word_count[k]=1
from math import log
for k,v in word_count.items():
    word_count[k]=log(100.0/v)
    #print k,word_count[k]
#------------------------

with open('air_plane.txt','r') as f:
    txt=f.read()
seg_list=jieba.cut(txt,cut_all=False)

tf_idf=dict()
for i in seg_list:
    if tf_idf.has_key(i):
        tf_idf[i]=tf_idf[i]+1
    else:
        tf_idf[i]=1
for k,v in tf_idf.items():
    tf_idf[k]=v * word_count[k]
wordcount=sorted(tf_idf.items(), lambda x, y : cmp(x[1], y[1]), reverse=True)

for k,v in wordcount:
    print k,v
