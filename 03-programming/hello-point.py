#!/usr/bin/env python

"""
Plot a single point at the origin
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='whitegrid')

# set coordinates
x = 0
y = 0
z = 0

# print coordinates
print(x, y, z)

# create plot
ax = plt.subplot(projection='3d')

# plot coordinates
plot = ax.scatter(x, y, z, c='black', s=100)

# set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)

# create figure
fig = ax.get_figure()

# save as image
fig.set_size_inches(8.5, 8.5)
fig.savefig(
    'point.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )