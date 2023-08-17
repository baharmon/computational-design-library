"""
Generate color point cloud from lidar in Rhino
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
filename = 'ground.laz'
datapath = pathlib.Path(__file__).parent.absolute()
data = os.path.join(datapath, filename)

# set variables
decimation = 2

# read lidar
las = laspy.read(data)

# decimate point cloud
xyz = las.xyz[::decimation]

# set colors
rgb = np.column_stack((las.red, las.green, las.blue))
rgb = rgb[::decimation].tolist()

# generate colored point cloud
rs.AddPointCloud(xyz, rgb)