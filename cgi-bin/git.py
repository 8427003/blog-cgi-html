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
os.popen('git pull').read()
os.popen('git status').read()
os.popen('git add -A').read()
os.popen('git commit -m "static html add"').read()
os.popen('git status').read()
os.popen('git push origin').read()
  
