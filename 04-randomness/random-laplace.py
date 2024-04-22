#!/usr/bin/env python

"""
Plot 1D matrix with Laplace distribution
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
sns.set_theme(style="darkgrid")

# generate laplace distribution
rng = np.random.default_rng()
z = rng.laplace(0, 10, 1000)
print(z)

# plot laplace distribution
ax = sns.displot(
    x=z, color='black',
    discrete=True,
    height=2,
    aspect=5/1
    )
plt.savefig(
    'random-laplace.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )
