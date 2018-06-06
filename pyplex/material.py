from pyplex.mesh import Mesh
from pyplex.camera import Camera
from pyplex.light import Light

from typing import List


class Material:
    def render(self, mesh: Mesh):
        raise NotImplementedError()