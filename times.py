#!/usr/bin/env python
#-*-coding:UTF-8-*-
#encoding=utf-8
#coding=utf-8

import sys
import re
import operator

with open ('./test.txt') as f:
	fileopen =str.lower(f.read())
   

#test = '1 22 333 333 333 22 1'

all = re.split(" |\n",fileopen)


#all = [1,2,3,3,3,2,]

#set_a = set(a)
 
#print(set01)
 
dict_a = {}
 
for item in all:
    dict_a.update({item:all.count(item)})

f = sorted(dict_a.items(),key = operator.itemgetter(1))

#print f


#i =  sorted(f, key=lambda s: s[1], reverse=True)   

for one in f:
    print one


#for key, value in f.items():
 #   print (key, ' value : ', value)







