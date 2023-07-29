#!/usr/bin/env python

"""
Export raster as NumPy binary
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
import lidario as lio
import pyvista as pv

# set path
directory = pathlib.Path(__file__).parent.resolve()
basename = os.path.join(directory, 'elevation')
dataset = f'{basename}.tif'

# lidario
translator = lio.Translator("geotiff", "numpy")
xyz = translator.translate(dataset)

# export binary
np.save(basename, xyz)

# plot with hypsometric tinting
pv.plot(
    xyz,
    scalars=xyz[:, 2],
    cmap='cubehelix',
    point_size=5,
    ambient=0.4,
    cpos='xy',
    window_size=(2000, 2000),
    eye_dome_lighting=True,
    show_scalar_bar=False,
    show_axes=False,
    background='white'
    )

