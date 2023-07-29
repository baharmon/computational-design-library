"""
Generate color point cloud from compressed NumPy binary in Rhino
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# requirements: numpy, matplotlib
import pathlib
import os
import numpy as np
import rhinoscriptsyntax as rs

# set path
filename = 'elevation.npz'
datapath = pathlib.Path(__file__).parent.absolute()
dataset = os.path.join(datapath, filename)


# load array
array = np.load(dataset)
xyz = array['xyz']
rgb = array['rgb'].tolist()

# sort points by elevation
xyz = xyz[xyz[:, 2].argsort()]

# generate colored point cloud
rs.AddPointCloud(xyz, rgb)