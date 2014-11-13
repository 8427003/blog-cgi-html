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
print 'git pull .........................'
print os.popen('git pull').read()

print os.popen('git status').read()
print 'git add -A .........................'
print os.popen('git add -A').read()
print 'git commit -m .........................'
print os.popen('git commit -m "static html add"').read()
print os.popen('git status').read()
print 'git push orgin..........................................'
print os.popen('git push origin').read()
print 'git push orgin.....................................end'
