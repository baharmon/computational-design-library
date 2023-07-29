"""
Import White Sands lidar in Rhino
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# requirements: lazrs, laspy
import pathlib
import os
import laspy
import rhinoscriptsyntax as rs

# set path
filename = 'points.laz'
datapath = pathlib.Path(__file__).parent.absolute()
data = os.path.join(datapath, filename)

# read lidar
las = laspy.read(data)

# decimate point cloud
xyz = las.xyz[::10]

# generate point cloud
cloud = rs.AddPointCloud(xyz)

# scale point cloud
origin = xyz[0]
scale = (1, 1, 2)
rs.ScaleObject(cloud, origin, scale)