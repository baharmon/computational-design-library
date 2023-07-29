#!/usr/bin/env python

"""
Plot raster
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import pathlib
import os
import rasterio as rio
from rasterio.plot import show

# set path
datapath = pathlib.Path(__file__).parent.resolve()
dataset = os.path.join(datapath, 'elevation.tif')

# read raster
elevation = rio.open(dataset)

# print coordinate reference system
print(elevation.crs)

# plot raster
show(elevation, cmap='cubehelix')