#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 coco <coco@coco-virtual-machine>
#
# Distributed under terms of the MIT license.

"""

"""
from string import Template
import os


inf = open('../template/article.html','r')

txt = inf.read() 

inf.close()

t = Template(txt)

result = t.safe_substitute(hello='wwwwwwwwwwwwww')

path = './Cloris/article/'

if not os.path.exists(path):
    os.makedirs(path)
outf = open('%sindex3.html'%path,'w')

outf.write(result)
outf.close()

