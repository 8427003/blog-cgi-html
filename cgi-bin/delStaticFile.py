#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# # Copyright © 2014 coco <coco@coco-virtual-machine> #
# Distributed under terms of the MIT license.

"""

"""
import os

def delete(fileName):
	basepath = './8427003.github.io/'
	if fileName:
	    os.popen('rm -rf %s%s'%(basepath,fileName),'w')
