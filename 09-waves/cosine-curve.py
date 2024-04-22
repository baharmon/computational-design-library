#!/usr/bin/env python

"""
Plot a cosine wave with the form y=sin(x)
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import numpy as np
import seaborn as sns

# set theme
sns.set_theme(
    context='paper', 
    style="darkgrid",
    font = 'IBM Plex Sans'
    )

# plot sine wave
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plot = sns.lineplot(
    x=x,
    y=y,
    color='gray',
    linewidth=1.5,
    legend=False
    )

# plot cosine wave
x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)
plot = sns.lineplot(
    x=x,
    y=y,
    color='black',
    linewidth=1.5,
    legend=False
    )

# save plot
plot.set_aspect('equal')
fig = plot.get_figure()
fig.set_size_inches(8.5, 2)
fig.savefig(
    'cosine-curve.png',
    dpi=1200,
    bbox_inches='tight',
    pad_inches=0
    )

