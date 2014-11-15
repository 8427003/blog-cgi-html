#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 coco <coco@coco-virtual-machine>
#
# Distributed under terms of the MIT license.

"""

"""
import thread
import os
import time
from gittle import Gittle

repo = Gittle('./Cloris','git@github.com:8427003/Cloris.git')
key_file = open('/home/lijun/.ssh/id_rsa')
repo.auth(pkey=key_file)
key_file.close()
#repo.auth(username="8427003",password="lijun401338")
def push(filename):
    thread.start_new_thread(_push,(filename,))
    time.sleep(15)

def _push(filename):
    repo.pull()
    repo.stage(filename)
    repo.commit(name="8427003", email="8427003@qq.com", message="auto static html")
    repo.push()
    os._exit(0)
