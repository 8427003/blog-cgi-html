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

    result = []
    os.chdir('Cloris')
    result.push(os.popen('git pull').read())
    result.push(os.popen('git status').read())
    result.push(os.popen('git add -A').read())
    result.push(os.popen('git commit -m "static html add"').read())
    result.push(os.popen('git status').read())
    result.push(os.popen('git push origin').read())
    
    return result
