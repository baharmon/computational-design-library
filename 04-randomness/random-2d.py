#!/usr/bin/env python

"""
Plot 2D random matrix
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import default_rng

# set theme
sns.set_theme(
    style="white",
    font_scale=0.75
    )

# create plot
ax = plt.subplot()

# generate random array
width = 8.5
height = 11
u = int(height * 2)
v = int(width * 2)
rng = default_rng(1234)
z = rng.integers(0, 10, (u, v))

# generate heatmap
sns.heatmap(
    z,
    cmap='viridis',
    linewidths=1,
    annot=True,
    cbar=False,
    yticklabels=False,
    xticklabels=False,
    square=True
    )

# save as image
fig = ax.get_figure()
fig.set_size_inches(width, height)
fig.savefig(
    'random-integer-grid.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )

