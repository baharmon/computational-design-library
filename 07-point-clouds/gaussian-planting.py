"""Gaussian Planting"""
#! python 3

# requirements: numpy
import Rhino.Collections as rc
import Rhino.Geometry as rg
import numpy as np
import math

if Run:

    # create empty sets
    points = rc.Point3dList()
    coordinates = np.empty(shape=[0, 3])
    Clouds = []

    # generate gaussian distribution of points
    for point in Points:

        # instantiate random number generator
        rng = np.random.default_rng()

        # generate random x, y, and z values
        n = int(Count)
        sigma = float(Deviation) # standard deviation
        x = rng.normal(point[0], sigma, n)
        y = rng.normal(point[1], sigma, n)
        z = np.zeros(n)

        # interweave coordinates
        xyz = np.column_stack((x, y, z))

        # add points to list
        xyz = xyz.tolist()
        for coordinate in xyz:
            point = rg.Point3d(
                coordinate[0],
                coordinate[1],
                coordinate[2]
                )
            points.AddRange([point])

    # transform point clouds
    Points = points
    for point in Points:

        # set variables
        vector = rg.Vector3d(0, 0, 1)
        angle = math.pi / rng.uniform(0.0, 360.0)
        scaling = rng.uniform(0.5, 1.0)

        # transform
        transform = Cloud.DuplicateShallow()
        transform.Rotate(angle, vector, point)
        transform.Scale(scaling)
        transform.Translate(point)
        Clouds.append(transform)