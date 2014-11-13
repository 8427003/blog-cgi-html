#!/usr/bin/python
#-*-coding: utf-8 -*- 



import cgitb; cgitb.enable() 
import json
import sys
import cgi
import os
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

print 'Content-type:application/json\n'



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
def _getArt():
	jsonStr = sys.stdin.read();
	pyObj = json.loads(jsonStr);
	return pyObj; 

def _add(art):
	aid = r.incr("aid")
	art["id"] = aid
	r.sadd("categoryAids:%s"%art["cid"],aid)	
	return r.hmset("article:%s"%aid,art)


def addInterface():
	art = _getArt()  

	if _add(art) > 0:
            result = {"status":0,"message":'',"data":{}}
            print os.popen('./statichtml.py').read()
            print os.popen('./git.py').read()
        
                
        else:
		result = {"status":-1,"message":'添加失败'}

	print json.dumps(result)

def _modify(aid,art):
	cid = r.hget("article:%s"%aid,"cid")
	
	if cid != art["cid"]:
		r.smove("categoryAids:%s"%cid,"categoryAids:%s"%art["cid"],aid)	

	return r.hmset("article:%s"%aid,art)
		
				
def modifyInterface(aid):
	art = _getArt()  

	if _modify(aid,art) > 0:
		result = {"status":0,"message":'',"data":{}}
	else:
		result = {"status":-1,"message":'修改失败'}

	print json.dumps(result)

	
def getByCidInterface(cid,callback):
	result = {"status":-1,"message":'添加失败'}
	aids = _getAidsByCid(cid)
	articles = []
	for aid in aids:
		art = r.hgetall("article:%s"%aid)
		articles.append(art);
				
	result = {"status":0,"data":articles}
        if callback :
            print callback+"("+json.dumps(result)+");"
        else:
            print json.dumps(result)

def _getAidsByCid(cid):
	return r.smembers("categoryAids:%s"%cid)
 
		
def getByIdInterface(aid):
	art = r.hgetall("article:%s"%aid)
	result = {"status":0,"data":art}
	print json.dumps(result)

			 
def _paramToObj(search):	
	result = {}
	searches = search.split("&")

	for k in searches:
		temp = k.split('=')
		if len(temp) >= 2 :
			result[temp[0]] = temp[1]

	return result

def _del(aid):
	cid = r.hget("article:%s"%aid,"cid") 
	return r.srem("categoryAids:%s"%cid,aid) and r.delete("article:%s"%aid)		
	#print cid

def delInterface(aid):
	result = {"status":-1,"data":aid}

	if _del(aid) :	
		result = {"status":0,"data":aid}

	print json.dumps(result)


def main():
	search = os.getenv('QUERY_STRING')	
	paramObj = _paramToObj(search)

	{
		"add":lambda:addInterface(),
		"modify":lambda:modifyInterface(paramObj["aid"]),
		"getbycid":lambda:getByCidInterface(paramObj["cid"],paramObj.get('callback')),
		"delbyaid":lambda:delInterface(paramObj["aid"]),
		"getbyaid":lambda:getByIdInterface(paramObj["aid"])
		
	}[paramObj["type"]]()


main()
