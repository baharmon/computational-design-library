#!/usr/bin/env python

"""
Plot a sine wave with the form y=sin(x)
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import numpy as np
import seaborn as sns
sns.set_theme(context='paper', style='darkgrid')

# plot sine wave
x = np.linspace(0, 6 * np.pi, 100)
y = np.sin(x)
plot = sns.scatterplot(
    x=x,
    y=y,
    size=x,
    hue=x,
    palette='flare',
    legend=False
    )
fig = plot.get_figure()
fig.set_size_inches(8.5, 2)
fig.savefig(
    'sine-wave.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )