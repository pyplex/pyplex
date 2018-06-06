from pyplex import gl
from pyplex import Vec3, vec3, Float32, float32, normalize
from pyplex.abstract import UniformObject
from pyplex.glow.buffer import UniformBuffer
import numpy as np


class Light(UniformObject):
    def data(self) -> np.ndarray:
        raise NotImplementedError()


class DirectionalLight(Light):
    def __init__(self, ctx: gl.GL31, direction: Vec3, color: Vec3, strength: Float32):
        self._direction = direction
        self._color = color
        self._strength = strength

        self._buffer = UniformBuffer(ctx, np.hstack((normalize(direction), strength, color, float32(1))))

    @property
    def buffer(self) -> UniformBuffer:
        return self._buffer

    @property
    def direction(self) -> Vec3:
        return self._direction

    @direction.setter
    def direction(self, value: Vec3):
        self._direction = normalize(value)
        self._update_buffer()

    @property
    def color(self) -> Vec3:
        return self._color

    @color.setter
    def color(self, value: Vec3):
        self._color = value
        self._update_buffer()

    @property
    def strength(self) -> Float32:
        return self._strength

    @strength.setter
    def strength(self, value: Float32):
        self._strength = value
        self._update_buffer()

    def _update_buffer(self):
        self._buffer.data = np.hstack((normalize(self._direction), self._strength, self._color, float32(1)))


class PointLight(Light):
    def __init__(self, ctx: gl.GL31, position: Vec3, color: Vec3, strength: Float32, falloff: Float32):
        self._position = position
        self._color = color
        self._strength = strength
        self._falloff = falloff

        self._buffer = UniformBuffer(ctx, np.hstack((position, strength, color, falloff)))

    @property
    def buffer(self) -> UniformBuffer:
        return self._buffer

    @property
    def position(self) -> Vec3:
        return self._position

    @position.setter
    def position(self, value: Vec3):
        self._position = value
        self._update_buffer()

    @property
    def color(self) -> Vec3:
        return self._color

    @color.setter
    def color(self, value: Vec3):
        self._color = value
        self._update_buffer()

    @property
    def strength(self) -> Float32:
        return self._strength

    @strength.setter
    def strength(self, value: Float32):
        self._strength = value
        self._update_buffer()

    @property
    def falloff(self) -> float32:
        return self._falloff

    @falloff.setter
    def falloff(self, value: float32):
        self._falloff = value
        self._update_buffer()

    def _update_buffer(self):
        self._buffer.data = np.hstack((self._position, self._strength, self._color, self._falloff))