from pyplex import gl
from pyplex.glow import abstract
from pyplex.glow.type import Type
import numpy as np
from ctypes import *


class Buffer(abstract.BindableObject, abstract.Array):
    def __init__(self, ctx: gl.GL20, target: gl.BufferTarget, data: np.ndarray, usage: gl.BufferUsage):

        self._ctx = ctx
        self._target = target
        self._usage = usage

        self._type = self._dtype = self._size = self._itemsize = self._nbytes = self._ndim = self._shape = None

        self._ptr = c_uint(0)
        self._ctx.gen_buffers(1, pointer(self._ptr))
        self._ptr = self._ptr.value

        self.data = data

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def type(self) -> Type:
        return self._type

    @property
    def dtype(self) -> np.dtype:
        return self._dtype

    @property
    def size(self) -> int:
        return self._size

    @property
    def itemsize(self) -> int:
        return self._itemsize

    @property
    def nbytes(self) -> int:
        return self._nbytes

    @property
    def ndim(self) -> int:
        return self._ndim

    @property
    def shape(self) -> tuple:
        return self._shape

    @property
    def target(self) -> gl.BufferTarget:
        return self._target

    @property
    def usage(self) -> gl.BufferUsage:
        return self._usage

    @property
    def data(self) -> np.ndarray:
        data = np.empty(self._shape, self._dtype)
        self._ctx.bind_buffer(self._target, self._ptr)
        self._ctx.get_buffer_sub_data(self._target, 0, self._nbytes, data.ctypes.data_as(c_void_p))
        self._ctx.bind_buffer(self._target, 0)
        return data

    @data.setter
    def data(self, value: np.ndarray):
        self._ctx.bind_buffer(self._target, self._ptr)
        self._ctx.buffer_data(self._target, value.nbytes, value.ctypes.data_as(c_void_p), self._usage)
        self._ctx.bind_buffer(self._target, 0)
        self._update_metadata(value)

    def bind(self):
        self._ctx.bind_buffer(self._target, self._ptr)

    def unbind(self):
        self._ctx.bind_buffer(self._target, 0)

    def delete(self):
        self._ctx.delete_buffers(1, pointer(self._ptr))

    def _update_metadata(self, data: np.ndarray):
        self._type = Type.from_np(data.shape[1:], data.dtype)
        self._dtype = data.dtype
        self._size = data.size
        self._itemsize = data.itemsize
        self._nbytes = data.nbytes
        self._ndim = data.ndim
        self._shape = data.shape


class ArrayBuffer(Buffer):
    def __init__(self, ctx: gl.GL20, data: np.ndarray, usage: gl.BufferUsage = gl.BufferUsage.STATIC_DRAW):
        super().__init__(ctx, gl.BufferTarget.ARRAY_BUFFER, data, usage)


class ElementArrayBuffer(Buffer):
    def __init__(self, ctx: gl.GL20, data: np.ndarray, usage: gl.BufferUsage = gl.BufferUsage.STATIC_DRAW):
        super().__init__(ctx, gl.BufferTarget.ELEMENT_ARRAY_BUFFER, data, usage)


class UniformBuffer(Buffer):
    def __init__(self, ctx: gl.GL20, data: np.ndarray, usage: gl.BufferUsage = gl.BufferUsage.STATIC_DRAW):
        super().__init__(ctx, gl.BufferTarget.UNIFORM_BUFFER, data, usage)