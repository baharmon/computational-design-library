#!/usr/bin/env python

"""
Plot perlin noise as 3D surface
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import pyfastnoisesimd as fns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# set theme
sns.set_theme(style="whitegrid")

# create plot
ax = plt.subplot(projection='3d')

# set threads
threads = fns.num_virtual_cores()

# set dimensions
i = threads * 100
j = threads * 100
shape = [i, j]

# generate perlin noise
perlin = fns.Noise()
perlin.noiseType = fns.NoiseType.PerlinFractal
perlin.frequency = 0.005
perlin.seed = 1

# set fractal properties
perlin.fractal.fractalType = fns.FractalType.RigidMulti
perlin.fractal.octaves = 2
perlin.fractal.lacunarity = 2.1
perlin.fractal.gain = 0.45

# set perturbation properties
perlin.perturb.perturbType = fns.PerturbType.Gradient
perlin.perturb.amp = 0.5
perlin.perturb.frequency = 0.5

# plot perlin noise
z = perlin.genAsGrid(shape=shape)
u = np.arange(0, i)
v = np.arange(0, j)
x, y = np.meshgrid(u, v)
plot = ax.plot_surface(x, y, z, cmap='cubehelix', linewidth=0)

# set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)
ax.set_zlim3d(-2, 3)

# create legend
fig = ax.get_figure()
ax.view_init(elev=50, azim=45, vertical_axis='z')
fig.colorbar(plot, shrink=0.5, aspect=16)

# save as image
fig.set_size_inches(8.5, 8.5)
fig.savefig(
    'perlin-noise-surface.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0)
