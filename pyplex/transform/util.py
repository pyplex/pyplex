import numpy as np


def apply(vertices: np.ndarray, transform: np.matrix, normalize: bool=False) -> np.ndarray:
    vertices_pad = np.asmatrix(np.hstack([vertices, np.ones((len(vertices), 1), vertices.dtype)])) * transform
    if normalize: vertices_pad /= vertices_pad[:, 3]
    return np.asarray(vertices_pad)[:, :3]


def normalize(vector: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(vector)
    if norm: return vector / norm
    else: return vector