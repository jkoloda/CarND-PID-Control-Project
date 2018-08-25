#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:21:25 2018

@author: janko
"""

import os
import base64

for ii in range(0, 5000):
    filename = 'build/temp/txt/frame_' + str(ii) + '.txt'
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r') as f:
        data = f.read().replace('\n', '')
    
    imgdata = base64.b64decode(data)    
    with open('build/temp/jpg/frame_' + str(ii).zfill(4) + '.jpg', 'wb') as f:
        f.write(imgdata)