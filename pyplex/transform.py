import numpy as np
from typing import Tuple


def translation(vector) -> np.ndarray:
    """
    Get Translation Matrix

    Parameters
    ----------
    vector: 1 or 3 component float

    Returns
    -------
    matrix: np.ndarray
    """

    matrix = np.eye(4, dtype=np.float32)
    matrix[:3, 3] = _parse_vec3(vector)
    return matrix


def scale(vector) -> np.ndarray:
    """
    Get Scale Matrix

    Parameters
    ----------
    vector: 1 or 3 component float

    Returns
    -------
    matrix: np.ndarray
    """

    matrix = np.eye(4, dtype=np.float32)
    matrix[np.diag_indices(3)] = _parse_vec3(vector)
    return matrix


def rotation(vector) -> np.ndarray:
    """
    Get Rotation Matrix

    Parameters
    ----------
    vector: 1 or 3 component float

    Returns
    -------
    matrix: np.ndarray
    """

    yaw, pitch, roll = _parse_vec3(vector)
    return rotation_z(yaw) * rotation_y(pitch) * rotation_x(roll)


def rotation_x(theta: float):
    """
    Get X-Rotation Matrix

    Parameters
    ----------
    theta: float

    Returns
    -------
    matrix: np.ndarray
    """

    return np.array([
        [ 1             , 0             , 0             , 0],
        [ 0             , np.cos(theta) ,-np.sin(theta) , 0],
        [ 0             , np.sin(theta) , np.cos(theta) , 0],
        [ 0             , 0             , 0             , 1]
    ], np.float32)


def rotation_y(theta: float):
    """
    Get Y-Rotation Matrix

    Parameters
    ----------
    theta: float

    Returns
    -------
    matrix: np.ndarray
    """

    return np.array([
        [ np.cos(theta) , 0             , np.sin(theta) , 0],
        [ 0             , 1             , 0             , 0],
        [-np.sin(theta) , 0             , np.cos(theta) , 0],
        [ 0             , 0             , 0             , 1]
    ], np.float32)


def rotation_z(theta: float):
    """
    Get Z-Rotation Matrix

    Parameters
    ----------
    theta: float

    Returns
    -------
    matrix: np.ndarray
    """

    return np.array([
        [ np.cos(theta) ,-np.sin(theta) , 0             , 0],
        [ np.sin(theta) , np.cos(theta) , 0             , 0],
        [ 0             , 0             , 1             , 0],
        [ 0             , 0             , 0             , 1]
    ], np.float32)


def orthographic(left: float, right: float, bottom: float, top: float, clip: Tuple[float, float]) -> np.ndarray:
    """
    Get Orthographic Projection Matrix

    Parameters
    ----------
    left: float
        Left Offset of Projection
    right: float
        Right Offset of Projection
    bottom: float
        Bottom Offset of Projection
    top: float
        Top Offset of Projection
    clip: (float, float)
        Near and Far Clipping Planes

    Returns
    -------
    matrix: np.ndarray
    """

    M = np.zeros((4, 4), dtype=np.float32)
    M[0, 0] = 2 / (right - left)
    M[1, 1] = 2 / (top - bottom)
    M[2, 2] = -2 / (clip[1] - clip[0])
    M[0, 3] = - ((right + left) / (right - left))
    M[1, 3] = - ((top + bottom) / (top - bottom))
    M[2, 3] = - ((clip[1] - clip[0]) / (clip[1] - clip[0]))
    M[3, 3] = 1
    return M


def frustum(left: float, right: float, bottom: float, top: float, clip: Tuple[float, float]) -> np.ndarray:
    """
    Get Perspective Projection Matrix

    Parameters
    ----------
    left: float
        Left Offset of Frustum
    right: float
        Right Offset of Frustum
    bottom: float
        Bottom Offset of Frustum
    top: float
        Top Offset of Frustum
    clip: (float, float)
        Near and Far Clipping Planes

    Returns
    -------
    matrix: np.ndarray
    """

    M = np.zeros((4, 4), dtype=np.float32)
    M[0, 0] = +2.0 * clip[0] / float(right - left)
    M[0, 2] = (right + left) / float(right - left)
    M[1, 1] = +2.0 * clip[0] / float(top - bottom)
    M[1, 2] = (top + bottom) / float(top - bottom)
    M[2, 2] = -(clip[1] + clip[0]) / float(clip[1] - clip[0])
    M[2, 3] = -2.0 * clip[0] * clip[1] / float(clip[1] - clip[0])
    M[3, 2] = -1.0
    return M


def perspective(fov: float, aspect: float, clip: Tuple[float, float]) -> np.ndarray:
    """
    Get Perspective Projection Matrix

    Parameters
    ----------
    fov: float
        Field of View
    aspect: float
        Aspect Ratio (Width / Height of Projection Surface)
    clip: (float, float)
        Near and Far Clipping Planes

    Returns
    -------
    matrix: np.ndarray
    """

    h = np.tan(fov / 360.0 * np.pi) * clip[0]
    w = h * aspect
    return frustum(-w, w, -h, h, clip)


def _parse_vec3(vector)  -> np.ndarray:
    """
    Parse Scalar or Array as 3-Component Numpy Array

    Parameters
    ----------
    vector: 1 or 3 component float

    Returns
    -------
    array: np.ndarray
    """

    v = np.array(vector, np.float32).ravel()
    if len(v) == 3: return v
    elif len(v) == 1: return v.repeat(3)
    else: raise ValueError("Argument 'vector' should be either 3D or 1D.")