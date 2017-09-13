#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: training_cobuild
@time: 10/5/17 PM5:28
"""
from bs4 import BeautifulSoup
from init import mongodb


all_text=""
count=mongodb.doubaninfo.find({'tid':3}).count()
cursor=mongodb.doubaninfo.find({'tid':3})
print 'collections numbles：',count
for i in range(count):

    content=cursor.next()
    txt=content['content']['body']
    soup=BeautifulSoup(txt, 'lxml')
    title=soup.find("h2",class_="question-title").text
    text=""
    tempdiv=soup.find("div",class_="content")
    p=tempdiv.find_all("p")
    for i in p:
        text=text+(i.text).encode('utf-8')
    all_text=all_text+text+"\n"

with open("Cobuild.txt",'w') as f:
    f.write(all_text)


#----------------------------------------------------#
import jieba
#将每个文档的词统计出来
words_collections=list()
with open('Cobuild.txt','r') as f:
    txt=f.readline()
    while(len(txt)):
        seg_list = jieba.cut(txt, cut_all=False)
        word_count = dict()
        for i in seg_list:
            if word_count.has_key(i):
                word_count[i] = word_count[i] + 1
            else:
                word_count[i] = 1
        words_collections.append(word_count)
        txt = f.readline()


with open('Cobuild.txt','r') as f:
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
    for i in words_collections:
        if i.has_key(k):
            if word_count.has_key(k):
                word_count[k]=word_count[k]+1
            else:
                word_count[k]=1
from math import log
f=open('cobuild.txt.big','w')
print word_count.pop(' ')
for k,v in word_count.items():
    word_count[k]=log(100.0/v)
    idf=k+' '+str(word_count[k])+'\n'
    print idf
    f.write(idf.encode('utf8'))
f.close()
