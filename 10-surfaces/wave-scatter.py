#!/usr/bin/env python

"""
Plot sinusoidal wave field as points
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set theme
sns.set(style = "whitegrid")

# create plot
ax = plt.subplot(projection='3d')

# set variables
u = np.arange(0, 10, 0.1)
v = np.arange(0, 10, 0.1)
a = 1
b = 1
c = 0
d = 0
f = 0.1

# plot points
x, y = np.meshgrid(u, v)
z = (
    (a * np.sin(b * x - c) + d)
    * np.e**(-f * x)
    * (a * np.cos(b * y - c) + d)
    * np.e**(-f * y)
    )
plot = ax.scatter(
    x, y, z,
    c=z,
    s=5,
    cmap='inferno'
    )

# set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)

# create legend
fig = ax.get_figure()
fig.colorbar(plot, shrink=0.5, aspect=16)

# save as image
fig.set_size_inches(8.5, 8.5)
fig.savefig(
    'wave-scatter.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )
