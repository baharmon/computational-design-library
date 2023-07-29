#!/usr/bin/env python

"""
Plot lidar data
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import pathlib
import os
import laspy
import pyvista as pv

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'laurus-nobilis-01-l.laz')

# read lidar
las = laspy.read(data)
xyz = las.xyz

# set plot theme
pv.set_plot_theme('document')

# plot with eye dome lighting
pv.plot(
    xyz,
    point_size=10,
    color='white',
    window_size=(4000, 4000),
    cpos='xz',
    show_axes=False,
    eye_dome_lighting=True,
    off_screen=True,
    screenshot='laurus-nobilis-edl.png',
    )