#!/usr/bin/env python

"""
Plot a scaled sinusoidal wave with the form: y = a sin(bx - c) + d
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
    style="darkgrid"
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
plot = sns.scatterplot(
    x=x,
    y=y,
    size=x,
    hue=x,
    palette='viridis',
    legend=False
    )

# set variables
steps = 100
t = 2
a = 1
b = 1
c = 0
d = 0
e = 0.5

# plot sinusoidal wave
x = np.linspace(0, t * np.pi, steps)
y = a * np.sin(b * x - c) + d
plot = sns.scatterplot(
    x=x * e, 
    y=y * e, 
    size=x, 
    hue=x, 
    palette='magma', 
    legend=False
    )

# save figure
fig = plot.get_figure()
fig.set_size_inches(8.5, 2)
fig.savefig(
    'scaled-wave.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )

