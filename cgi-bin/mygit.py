#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 coco <coco@coco-virtual-machine>
#
# Distributed under terms of the MIT license.

"""

"""
from gittle import Gittle

repo = Gittle('./Cloris','git@github.com:8427003/Cloris.git')
key_file = open('/home/coco/.ssh/id_rsa')
repo.auth(pkey=key_file)
key_file.close()
#repo.auth(username="8427003",password="lijun401338")

def push(filename):
    repo.pull()
    repo.stage(filename)
    repo.commit(name="8427003", email="8427003@qq.com", message="auto static html")
    repo.push()

    return 'ok'

