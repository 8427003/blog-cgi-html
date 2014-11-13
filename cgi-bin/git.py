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


def push():

    var result = []
    os.chdir('Cloris')
    result.push(print os.popen('git pull').read())
    result.push(print os.popen('git status').read())
    result.push(print os.popen('git add -A').read())
    result.push(print os.popen('git commit -m "static html add"').read())
    result.push(print os.popen('git status').read())
    result.push(print os.popen('git push origin').read())
    
    return result
