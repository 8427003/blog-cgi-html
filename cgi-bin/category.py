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
def _getCtg():
	jsonStr = sys.stdin.read();
	pyObj = json.loads(jsonStr);
	return pyObj; 

def _add(ctg):
	cid = r.incr("cid")
	ctg["id"] = cid	
	r.sadd("parentcids:%s"%ctg["parent"],cid)	
	return r.hmset("category:%s"%cid,ctg)

def addInterface():
	ctg = _getCtg()  

	if _add(ctg) > 0:
		result = {"status":0,"message":'',"data":{}}
	else:
		result = {"status":-1,"message":'添加失败'}

	print json.dumps(result)

def _modify(cid,ctg):
	parent = r.hget("category:%s"%cid,"parent")
	
	if parent != ctg["parent"]:
		r.smove("parentcids:%s"%parent,"parentcids:%s"%ctg["parent"],cid)	

	return r.hmset("category:%s"%cid,ctg)
		
				
def modifyInterface(cid):
	ctg = _getCtg()  

	if _modify(cid,ctg) > 0:
		result = {"status":0,"message":'',"data":{}}
	else:
		result = {"status":-1,"message":'修改失败'}

	print json.dumps(result)
		
def _getAllChildByParent(parent,category):
	cids = _getCidByParent(parent)
	children = []
	for cid in cids:
		ctg = r.hgetall("category:%s"%cid)
		_getAllChildByParent(ctg['id'],ctg)	
		children.append(ctg);
	category['children'] = children
	return category.get('children') 

def getAllByParentInterface(parent,callback):
	result = {"status":-1,"message":'添加失败'}
	data = _getAllChildByParent(parent,{})
	result = {"status":0,"data":data}
        if callback : 
	    print callback+"("+json.dumps(result)+");"
        else:
            print json.dumps(result)

	
def getByParentInterface(parent,callback):
	result = {"status":-1,"message":'添加失败'}
	cids = _getCidByParent(parent)
	categores = []
	for cid in cids:
		ctg = r.hgetall("category:%s"%cid)
		categores.append(ctg);
				
	result = {"status":0,"data":categores}
        if callback : 
	    print callback+"("+json.dumps(result)+");"
        else:
            print json.dumps(result)

def _getByCid(cid):
	ctg = r.hgetall("category:%s"%cid)
	return ctg;
	

def getByCidInterface(cid):
	result = {"status":-1,"message":'添加失败'}
	ctg = _getByCid(cid)				
	result = {"status":0,"data":ctg}
	print json.dumps(result)

def _getCidByParent(parent):
	return r.smembers("parentcids:%s"%parent)	
	
			 
def _paramToObj(search):	
	result = {}
	searches = search.split("&")

	for k in searches:
		temp = k.split('=')
		if len(temp) >= 2 :
			result[temp[0]] = temp[1]

	return result


def _del(cid):
	parent = r.hget("category:%s"%cid,"parent") 
	return r.srem("parentcids:%s"%parent,cid) and r.delete("category:%s"%cid)		

def delInterface(cid):
	result = None;

	count = r.scard("categoryAids:%s"%cid);

        childCount = r.scard("parentcids:%s"%cid);

        if childCount <= 0 :
	    if count <= 0 :
	    	    if _del(cid) :	
			    result = {"status":0,"data":cid}
		    else:
			    result = {"status":-1,"message":cid}
	    else:
		    result = {"status":-1,"message":"请先删除该分类下文章"}
        else:
            result = {"status":-1,"message":"请先删除该分类下分类"}

	
	print json.dumps(result)


def main():
	search = os.getenv('QUERY_STRING')	
	paramObj = _paramToObj(search)

	{
		"add":lambda:addInterface(),
		"getbycid":lambda:getByCidInterface(paramObj["cid"]),
		"modify":lambda:modifyInterface(paramObj["cid"]),
		"getbyparent":lambda:getByParentInterface(paramObj["parent"],paramObj.get('callback')),
		"getallbyparent":lambda:getAllByParentInterface(paramObj["parent"],paramObj.get('callback')),
		"delbycid":lambda:delInterface(paramObj["cid"])
		
	}[paramObj["type"]]()


main()
