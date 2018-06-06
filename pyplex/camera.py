from pyplex import gl
from pyplex.abstract import UniformObject
from pyplex.glow.buffer import UniformBuffer
from pyplex.transform import *

import numpy as np

from math import sin, cos


class Camera(UniformObject):
    def __init__(self, ctx: gl.GL_ANY, projection: np.matrix, view: np.matrix):

        self._projection = projection
        self._view = view
        self._position = invert(view)[3, :3]

        buffer = np.empty(1, [('projection', '(4,4)f4'), ('view', '(4,4)f4'), ('position', '3f4')])
        buffer['projection'] = self._projection
        buffer['view'] = self._view
        buffer['position'] = self._position

        self._buffer = UniformBuffer(ctx, buffer, gl.BufferUsage.STREAM_DRAW)

    @property
    def buffer(self) -> UniformBuffer:
        return self._buffer

    @property
    def projection(self) -> np.matrix:
        return self._projection

    @projection.setter
    def projection(self, value: np.matrix):
        self._projection = np.asmatrix(value)
        self._buffer['projection'] = self._projection

    @property
    def view(self) -> np.matrix:
        return self._view

    @view.setter
    def view(self, value: np.matrix):
        self._view = np.asmatrix(value)
        self._position = np.asarray(invert(self._view))[3, :3]

        self._buffer['view'] = self._view
        self._buffer['position'] = self._position

    @property
    def position(self) -> np.ndarray:
        return self._position




class PerspectiveCamera(Camera):
    def __init__(self, ctx: gl.GL_ANY, fov: float, aspect: float, near: float, far: float, view: np.matrix):
        super().__init__(ctx, perspective(fov, aspect, near, far), view)

        self._fov = fov
        self._aspect = aspect
        self._near = near
        self._far = far

    @property
    def fov(self) -> float:
        return self._fov

    @fov.setter
    def fov(self, value: float):
        self._fov = value
        self._update_projection()

    @property
    def aspect(self) -> float:
        return self._aspect

    @aspect.setter
    def aspect(self, value: float):
        self._aspect = value
        self._update_projection()

    @property
    def near(self) -> float:
        return self._near

    @near.setter
    def near(self, value: float):
        self._near = value
        self._update_projection()

    @property
    def far(self) -> float:
        return self._far

    @far.setter
    def far(self, value: float):
        self._far = value
        self._update_projection()

    def _update_projection(self):
        self.projection = perspective(self._fov, self._aspect, self._near, self._far)



class TrackBallCamera(PerspectiveCamera):
    def __init__(self, ctx: gl.GL_ANY, fov: float, aspect: float, near: float, far: float,
                 pivot: np.ndarray, up: np.ndarray, theta: float, phi: float, radius: float):

        self._pivot = pivot
        self._up = up
        self._theta = theta
        self._phi = phi
        self._radius = radius

        self._rotation = np.array([
            sin(self._theta) * cos(self._phi),
            cos(self._theta),
            sin(self._theta) * sin(self._phi)],
            np.float32)

        self._position = self._pivot + self._radius * self._rotation

        super().__init__(ctx, fov, aspect, near, far, look_at(self._position, self._pivot, self._up))

    @property
    def position(self) -> np.ndarray:
        return self._position

    @property
    def pivot(self) -> np.ndarray:
        return self._pivot

    @pivot.setter
    def pivot(self, value: np.ndarray):
        self._pivot = value
        self._update_view()

    @property
    def rotation(self) -> np.ndarray:
        return self._rotation

    @rotation.setter
    def rotation(self, value: np.ndarray):
        self._rotation = value
        self._update_view()

    @property
    def up(self) -> np.ndarray:
        return self._up

    @up.setter
    def up(self, value: np.ndarray):
        self._up = value
        self._update_view()

    @property
    def theta(self) -> float:
        return self._theta

    @theta.setter
    def theta(self, value: float):
        self._theta = value
        self._update_view()

    @property
    def phi(self) -> float:
        return self._phi

    @phi.setter
    def phi(self, value: float):
        self._phi = value
        self._update_view()

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value
        self._update_view()

    def _update_view(self):
        self._rotation = np.array([
            sin(self._theta) * cos(self._phi),
            cos(self._theta),
            sin(self._theta) * sin(self._phi)],
            np.float32)
        self._position = self._pivot + self._radius * self._rotation
        self.view = look_at(self._position, self._pivot, self._up)
