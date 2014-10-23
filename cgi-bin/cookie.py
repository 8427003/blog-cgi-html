#!/usr/bin/python
#-*-coding: utf-8 -*-
import os
import cgitb; cgitb.enable()
print "Content-type: text/html\n\n"
print 

print os.environ.get('HTTP_COOKIE')
#print 1/0
print "送"
print 'hello world!'
