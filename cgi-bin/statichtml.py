#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# # Copyright © 2014 coco <coco@coco-virtual-machine> #
# Distributed under terms of the MIT license.

"""

"""
from string import Template
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def staticHtml(art):

    article = {}
    article["createDate"] = str(art["createDate"])
    article["cid"] = str(art["cid"])
    inf = open('../template/article.html','r')

    txt = inf.read() 

    inf.close()

    t = Template(txt)

    result = t.safe_substitute(title=art["title"],content=art["content"])
    path = './8427003.github.io/article/c%s/'%article["cid"]
    if not os.path.exists(path):
        os.makedirs(path)

    outf = open('%s%s.html'%(path,article["createDate"]),'w')
    outf.write(result)
    outf.close()
    
    staticFileName = 'article/c%s/%s.html'%(article["cid"],article["createDate"])
    return staticFileName 
