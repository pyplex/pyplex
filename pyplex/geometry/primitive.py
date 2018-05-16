from .geometry import Geometry

import numpy as np
from math import *


class Cube(Geometry):
    _VERTICES = np.array([
        [-1,-1, 1],
        [ 1,-1, 1],
        [ 1, 1, 1],
        [-1, 1, 1],

        [-1,-1, -1],
        [ 1,-1, -1],
        [ 1, 1, -1],
        [-1, 1, -1],
    ], np.float32)

    _NORMALS = np.array([
        [ 0, 0, 1],
        [ 1, 0, 0],
        [ 0, 0, -1],
        [-1, 0, 0],
        [ 0,-1, 0],
        [ 0, 1, 0],
    ], np.float32)

    _ELEMENTS = np.array([
        0, 1, 2, 2, 3, 0,  # front
        1, 5, 6, 6, 2, 1,  # right
        7, 6, 5, 5, 4, 7,  # back
        4, 0, 3, 3, 7, 4,  # left
        4, 5, 1, 1, 0, 4,  # bottom
        3, 2, 6, 6, 7, 3,  # top
    ], np.uint8)

    _NORMAL_ELEMENTS = np.array([
        0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1,
        2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3,
        4, 4, 4, 4, 4, 4,
        5, 5, 5, 5, 5, 5
    ], np.uint8)

    def __init__(self):
        super().__init__(self._VERTICES[self._ELEMENTS], np.arange(0, len(self._ELEMENTS)).astype(np.uint8),
                         normals=self._NORMALS[self._NORMAL_ELEMENTS])


class Plane(Geometry):
    def __init__(self):
        super().__init__(
            np.array([[-1, 0, -1], [-1, 0, +1], [+1, 0, -1], [+1, 0, +1]], np.float32),
            np.array([0, 1, 2, 1, 3, 2], np.uint8),
            np.array([[0, 0], [0, 1], [1, 0], [1, 1]], np.float32),
            np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]], np.float32))


class Quad(Geometry):
    def __init__(self):
        super().__init__(
            np.array([[-1,-1], [-1, +1], [+1, -1], [+1, +1]], np.float32),
            np.array([0, 2, 1, 1, 2, 3], np.uint8),
            np.array([[0, 0], [0, 1], [1, 0], [1, 1]], np.float32))


class Sphere(Geometry):
    def __init__(self, segments: int, rings: int, dtype: np.dtype=np.float32):
        vertices = np.empty((segments * rings, 3), dtype)

        phi_space = np.linspace(0, 2*np.pi, segments, True, dtype=dtype)
        theta_space = np.linspace(0, np.pi, rings, True, dtype=dtype)

        for s, phi in enumerate(phi_space):
            for r, theta in enumerate(theta_space):
                vertices[s * rings + r] = [
                    sin(theta) * cos(phi),
                    sin(theta) * sin(phi),
                    cos(theta)]

        elements = np.zeros(((segments-1) * (rings-1) * 6), np.uint32)
        for s in range(segments-1):
            for r in range(rings-1):
                index = (s * (rings-1) +  r) * 6

                elements[index + 0] = s * rings + r
                elements[index + 1] = s * rings + r + 1
                elements[index + 2] = (s + 1) * rings + r

                elements[index + 3] = s * rings + r + 1
                elements[index + 4] = (s + 1) * rings + r + 1
                elements[index + 5] = (s + 1) * rings + r

        super().__init__(vertices, elements, normals=vertices)
