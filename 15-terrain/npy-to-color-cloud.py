"""
Generate color point cloud from Numpy binary in Rhino
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
import matplotlib as mpl
import rhinoscriptsyntax as rs

# set path
filename = 'elevation.npy'
datapath = pathlib.Path(__file__).parent.absolute()
dataset = os.path.join(datapath, filename)

# set color map
colormap = 'cubehelix'

# load array
xyz = np.load(dataset)

# generate color gradient
z = xyz[:, 2]
gradient = mpl.colormaps[colormap].resampled(z.size)
rgba = (gradient(range(z.size)) * 255).astype('uint8')
rgb = rgba[:,:-1].tolist()

# sort points by elevation
xyz = xyz[xyz[:, 2].argsort()]

# generate colored point cloud
rs.AddPointCloud(xyz, rgb)
