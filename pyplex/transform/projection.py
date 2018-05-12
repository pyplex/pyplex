import numpy as np
import math


def orthographic(left: float, right: float, top: float, bottom: float, near: float, far: float,
                 dtype: np.dtype=np.float32) -> np.matrix:

    return np.matrix([
        [ 2 / (right - left)        , 0                         , 0                     , 0],
        [ 0                         , 2 / (top - bottom)        , 0                     , 0],
        [ 0                         , 0                         ,-2/(far-near)          , 0],
        [-(right+left)/(right-left) ,-(top+bottom)/(top-bottom) ,-(far+near)/(far-near) , 1]
    ], dtype)


def frustum(left: float, right: float, top: float, bottom: float, near: float, far: float,
            dtype: np.dtype=np.float32) -> np.matrix:

    return np.matrix([
        [ (2*near)/(right-left)     , 0                         , 0                         , 0],
        [ 0                         , (2*near)/(top-bottom)     , 0                         , 0],
        [ (right+left)/(right-left) , (top+bottom)/(top-bottom) ,-((far+near)/(far-near))   ,-1],
        [ 0                         , 0                         ,-((2*far*near)/(far-near)) , 0]
    ], dtype)


def perspective(fov: float, aspect: float, near: float, far: float, dtype: np.dtype=np.float32) -> np.matrix:
    fov = fov * np.pi / 180
    height = near * math.tan(fov/2.)
    left = -height * aspect
    right = height * aspect
    bottom = -height
    top = height

    return frustum(left, right, top, bottom, near, far, dtype)