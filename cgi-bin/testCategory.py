#!/usr/bin/python
#-*-coding: utf-8 -*-
import cgitb; cgitb.enable()
import json
import sys
import cgi
import os
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

print 'Content-type:application/json\n\n'



#基本数据类型方式:
#读取表单属性
#data = cgi.FieldStorage()
#print data.getvalue('a') ;
 
#当然get可以直接从环境变量读取
#print os.getenv('QUERY_STRING')

#json方式:
#step1 读取json字符串参数
#jsonStr = sys.stdin.read();

#step2 将json字符串参数转为python对象
#pyObj = json.loads(jsonStr);

#这是一个python对象
#newPyObj = {"jack":4098,"sape":{"aa":"2"}} 

#将python对象转为json对象返回
#print json.dumps(newPyObj) #or "json.dump(result,sys.stdout)"
#print json.dumps(r.get('foo'))
def _getCtg():
	return {
		"id":1,
		"name":"css",
		"level":0,
		"state":1,
		"parent":0,
		"order":0,
		"desc":"css相关"		
		}

def add(ctg):
	r.set("category:%s:name"%ctg["id"],ctg["name"])
	r.set("category:%s:level"%ctg["id"],ctg["level"])
	r.set("category:%s:state"%ctg["id"],ctg["state"])
	r.set("category:%s:parent"%ctg["id"],ctg["parent"])
	r.set("category:%s:order"%ctg["id"],ctg["order"])
	r.set("category:%s:desc"%ctg["id"],ctg["desc"])
	return True;


print r.get("category:1:name")
