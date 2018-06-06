import numpy as np
from typing import Union


class Scalar(np.ndarray): pass


class Float32(Scalar): pass


class Int32(Scalar): pass


class Vec2(np.ndarray): pass


class Vec3(np.ndarray): pass


class Vec4(np.ndarray): pass


def scalar(x: Union[float, int], dtype: np.dtype=np.float32) -> Scalar:
    return np.array([x], dtype).view(Scalar)


def float32(x: float) -> Float32:
    return np.array([x], np.float32).view(Float32)


def int32(x: int) -> Int32:
    return np.array([x], np.int32).view(Int32)


def vec2(x: float, y: float) -> Vec2:
    return np.array([x, y], np.float32).view(Vec2)


def vec3(x: float, y: float, z: float) -> Vec3:
    return np.array([x, y, z], np.float32).view(Vec3)


def vec4(x: float, y: float, z: float, w: float) -> Vec4:
    return np.array([x, y, z, w], np.float32).view(Vec4)