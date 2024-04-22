#!/usr/bin/env python

"""
Plot dampened sinusoidal waves with the form:
y = a sin(bx - c) + e^(-f * x)
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
steps = 200
count = 5
minimum = 0.2
maximum = 0.6
t = 4
a = 2
b = 2
c = 0
d = 0

# plot sinusoidal wave
x = np.linspace(0, t * np.pi, steps)
f = np.linspace(maximum, minimum, count)
for i in f:
    y = a * np.sin(b * x - c) * np.e**(-i * x) + d 
    plot = sns.lineplot(
        x=x,
        y=y,
        color='black',
        hue=i,
        hue_norm=(minimum, maximum),
        palette='Greys_r',
        linewidth=1,
        legend=False
        )

# save plot
plot.set_aspect('equal')
fig = plot.get_figure()
fig.set_size_inches(4, 2)
fig.savefig(
    'dampened-curves.png',
    dpi=1200,
    bbox_inches='tight',
    pad_inches=0
    )