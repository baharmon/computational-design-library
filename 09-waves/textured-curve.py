#!/usr/bin/env python

"""
Plot a textured sinusoidal wave with the form: y = a sin(bx - c) + d + sin(x)
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

# set variables
steps = 100
t = 2
a = 1
b = 1
c = 0
d = 0

# plot sinusoidal wave
x = np.linspace(0, t * np.pi, steps)
y = a * np.sin(b * x - c) + d
plot = sns.lineplot(
    x=x,
    y=y,
    color='gray',
    linewidth=1.5,
    legend=False
    )

# set variables
steps = 100
t = 2
a = 0.5
c = 0
d = 0

# plot sinusoidal wave
x = np.linspace(0, t * np.pi, steps)
y = a * np.sin(a**-1 * x - c) + d + np.sin(x)
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
fig.set_size_inches(4, 2)
fig.savefig(
    'textured-curve.png',
    dpi=1200,
    bbox_inches='tight',
    pad_inches=0
    )
