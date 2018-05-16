from .util import normalize

import numpy as np
import math


def identity(dtype: np.dtype=np.float32) -> np.matrix:
    return np.matrix(np.eye(4, dtype=dtype))


def translation(translation, dtype: np.dtype=np.float32) -> np.matrix:
    matrix = identity(dtype)
    matrix[3, :3] = translation
    return matrix


def scale(scale, dtype: np.dtype=np.float32) -> np.matrix:
    matrix = identity(dtype)
    matrix[np.diag_indices(3)] = scale
    return matrix


def rotation(angle, dtype: np.ndarray=np.float32) -> np.matrix:
    cx, cy, cz = np.cos(angle)
    sx, sy, sz = np.sin(angle)

    sxsy = sx * sy
    cxsy = cx * sy

    return np.matrix([
        [ cy * cz, sxsy*cz+cx*sz,-cxsy*cz+sx*sz, 0],
        [-cy * sz,-sxsy*sz+cx*cz, cxsy*sz+sx*cz, 0],
        [ sy     ,-sx*cy        , cx*cy        , 0],
        [ 0      , 0            , 0            , 1]
    ], dtype)


def rotation_x(angle: float, dtype: np.dtype=np.float32) -> np.matrix:
    c = math.cos(angle)
    s = math.sin(angle)

    return np.matrix([
        [ 1, 0, 0, 0],
        [ 0, c, s, 0],
        [ 0,-s, c, 0],
        [ 0, 0, 0, 1]], dtype)


def rotation_y(angle: float, dtype: np.dtype=np.float32) -> np.matrix:
    c = math.cos(angle)
    s = math.sin(angle)

    return np.matrix([
        [ c, 0,-s, 0],
        [ 0, 1, 0, 0],
        [ s, 0, c, 0],
        [ 0, 0, 0, 1]], dtype)


def rotation_z(angle: float, dtype: np.dtype=np.float32) -> np.matrix:
    c = math.cos(angle)
    s = math.sin(angle)

    return np.matrix([
        [ c, s, 0, 0],
        [-s, c, 0, 0],
        [ 0, 0, 1, 0],
        [ 0, 0, 0, 1]], dtype)


def look_at(eye: np.ndarray, center: np.ndarray, up: np.ndarray, dtype: np.dtype=np.float32) -> np.matrix:
    f = normalize(center - eye)
    u = normalize(up)
    s = normalize(np.cross(f, u))
    u = np.cross(s, f)

    return np.matrix([
        [ s[0]          , u[0]         ,-f[0]          , 0],
        [ s[1]          , u[1]         ,-f[1]          , 0],
        [ s[2]          , u[2]         ,-f[2]          , 0],
        [-np.dot(s, eye),-np.dot(u,eye),np.dot(f, eye), 1]
    ], dtype)