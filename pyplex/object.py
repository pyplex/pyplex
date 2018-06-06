from pyplex.mesh import Mesh
from pyplex.material import Material
import numpy as np


class Object:
    def __init__(self, mesh: Mesh, transform: np.ndarray, material: Material):
        self._mesh = mesh
        self._transform = transform
        self._material = material

    def render(self):
        raise NotImplementedError()