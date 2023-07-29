#!/usr/bin/env python

"""
Read lidar data
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ =  "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import pathlib
import os
import laspy

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'laurus-nobilis-01-l.laz')

# read lidar
las = laspy.read(data)
print(las.xyz)