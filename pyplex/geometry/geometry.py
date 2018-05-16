import numpy as np
from typing import Optional



class Geometry:
    def __init__(self, vertices: np.ndarray, elements: np.ndarray,
                 uvs: Optional[np.ndarray]=None,
                 normals: Optional[np.ndarray]=None,
                 tangents: Optional[np.ndarray]=None):

        self._vertices = vertices
        self._elements = elements
        self._uvs = uvs
        self._normals = normals
        self._tangents = tangents

    @property
    def vertices(self) -> np.ndarray:
        return self._vertices

    @property
    def elements(self) -> np.ndarray:
        return self._elements

    @property
    def uvs(self) -> Optional[np.ndarray]:
        return self._uvs

    @property
    def normals(self) -> Optional[np.ndarray]:
        return self._normals

    @property
    def tangents(self) -> Optional[np.ndarray]:
        return self._tangents

    def recalculate_normals(self):
        elements = self.elements.reshape(-1, 3)
        face_normals = np.cross(
            self.vertices[elements[:, 0]] - self.vertices[elements[:, 1]],
            self.vertices[elements[:, 0]] - self.vertices[elements[:, 2]])

        self._normals = np.zeros_like(self.vertices)

        for element, face_normal in zip(elements, face_normals):
            self._normals[element] += face_normal

        self._normals /= np.linalg.norm(self._normals, axis=-1, keepdims=True)
