#!/usr/bin/env python

"""
Voxelize point cloud data
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import pathlib
import os
import open3d as o3d

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'laurus-nobilis-01-l.pcd')

# read point cloud
cloud = o3d.io.read_point_cloud(data, format='pcd')

# voxelize
size = 0.05
volume = o3d.geometry.VoxelGrid.create_from_point_cloud(
    cloud,
    voxel_size=size
    )

# render voxels
o3d.visualization.draw_geometries([volume])

# convert voxels to mesh
mesh = o3d.geometry.TriangleMesh()
voxels = volume.get_voxels()
for voxel in voxels:
    box = o3d.geometry.TriangleMesh.create_box()
    box.paint_uniform_color(voxel.color)
    box.translate(voxel.grid_index)
    mesh += box

# export mesh
o3d.io.write_triangle_mesh(
    'voxels.stl',
    mesh.compute_triangle_normals()
    )