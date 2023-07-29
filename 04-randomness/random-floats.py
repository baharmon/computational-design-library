#!/usr/bin/env python

"""
Plot 2D matrix of random floats
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# set theme
sns.set_theme(style="white")

# create plot
ax = plt.subplot()

# generate random array
rng = np.random.default_rng(1234)
z = rng.random((10, 10))

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
fig.set_size_inches(8.5, 8.5)
fig.savefig('random-floats.png', dpi=300, bbox_inches='tight', pad_inches=0)

