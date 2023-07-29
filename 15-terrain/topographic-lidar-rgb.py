#!/usr/bin/env python

"""
Plot topographic lidar with color
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import pathlib
import os
import numpy as np
import laspy
import pyvista as pv

# set path
datapath = pathlib.Path(__file__).parent.resolve()
dataset = os.path.join(datapath, 'all.laz')

# read lidar
las = laspy.read(dataset)
xyz = las.xyz

# set plot theme
pv.set_plot_theme('document')

# plot with color
rgb = np.column_stack((las.red, las.green, las.blue))
pv.plot(
    xyz,
    scalars=rgb,
    point_size=5,
    ambient=0.4,
    window_size=(2000, 2000),
    show_axes=False,
    eye_dome_lighting=True,
    rgba=True,
    off_screen=True,
    screenshot='lidar-rgb.png',
    )