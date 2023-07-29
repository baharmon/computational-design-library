"""
Generate point cloud from NumPy binary in Rhino
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# requirements: numpy
import pathlib
import os
import numpy as np
import rhinoscriptsyntax as rs

# set path
filename = 'elevation.npy'
datapath = pathlib.Path(__file__).parent.absolute()
dataset = os.path.join(datapath, filename)

# load array
xyz = np.load(dataset)

# generate point cloud
rs.AddPointCloud(xyz)
