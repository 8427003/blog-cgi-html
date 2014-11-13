#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 coco <coco@coco-virtual-machine>
#
# Distributed under terms of the MIT license.

"""

"""
import os



result = []
os.chdir('Cloris')
print os.popen('git pull').read()
print os.popen('git status').read()
print os.popen('git add -A').read()
print os.popen('git commit -m "static html add"').read()
print os.popen('git status').read()
print os.popen('git push origin').read()
  
