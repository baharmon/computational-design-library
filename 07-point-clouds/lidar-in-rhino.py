"""
Import a lidar point cloud into Rhino
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# requirements: lazrs, laspy, numpy
import pathlib
import os
import laspy
import numpy as np
import rhinoscriptsyntax as rs

# set path
filename = 'laurus-nobilis-01-l.laz'
datapath = pathlib.Path(__file__).parent.absolute()
data = os.path.join(datapath, filename)

# read lidar
las = laspy.read(data)

# convert colors
red = (las.red/256).astype('uint8')
green = (las.green/256).astype('uint8')
blue = (las.blue/256).astype('uint8')

# stack colors
rgb = np.column_stack((red, green, blue)).tolist()

# generate colored point cloud
rs.AddPointCloud(las.xyz, rgb)