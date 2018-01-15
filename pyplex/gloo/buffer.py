from pyplex import gl
from pyplex.gloo import ContextObject

import numpy as np

from typing import Iterable, Union


class Buffer(ContextObject):
    def __init__(self, ctx: gl.Context, target: gl.BufferTarget, data: np.ndarray, usage: gl.BufferUsage):
        """
        Create GPU Buffer

        Parameters
        ----------
        ctx: gl.Context
            OpenGL Context
        target: gl.BufferTarget
            Buffer Target
        data: np.ndarray
            Data to put in Buffer
        usage: gl.BufferUsage
            Buffer Usage Hint
        """
        self._ctx = ctx
        self._target = target
        self._usage = usage
        self._shape = data.shape
        self._dtype = data.dtype

        self._ptr = self.ctx.create_buffer()
        self.data = data

    @property
    def ctx(self) -> gl.Context:
        """
        Returns
        -------
        ctx: gl.Context
            OpenGL Context
        """
        return self._ctx

    @property
    def ptr(self) -> gl.Buffer:
        """
        Returns
        -------
        ptr: gl.Buffer
            Pointer to OpenGL Buffer object
        """
        return self._ptr

    @property
    def target(self) -> gl.BufferTarget:
        """
        Returns
        -------
        target: gl.BufferTarget
            Buffer Target
        """
        return self._target

    @property
    def usage(self) -> gl.BufferUsage:
        """
        Returns
        -------
        usage: gl.BufferUsage
            Buffer Usage Hint
        """
        return self._usage

    @property
    def shape(self) -> tuple:
        """
        Returns
        -------
        shape: np.ndarray
            Buffer Shape
        """
        return self._shape

    @property
    def dtype(self) -> np.dtype:
        """
        Returns
        -------
        dtype: np.dtype
            Buffer dtype
        """
        # TODO: No Reference to gloo.Type?
        return self._dtype

    @property
    def data(self) -> np.ndarray:
        """
        Get GPU Buffer Data

        Returns
        -------
        data: np.ndarray
        """
        with self:
            n_bytes = int(np.prod(self.shape) * self.dtype.itemsize)
            data = self.ctx.get_buffer_sub_data(self.target, 0, n_bytes).view(self.dtype)
        return data

    @data.setter
    def data(self, value: np.ndarray):
        """
        Set GPU Buffer Data

        Parameters
        ----------
        value: np.ndarray
        """
        with self:
            self.ctx.buffer_data(self.target, value, self.usage)

    def delete(self):
        self.ctx.delete_buffer(self.ptr)

    def bind(self):
        """Bind Buffer"""
        self.ctx.bind_buffer(self.target, self.ptr)

    def unbind(self):
        """Unbind Buffer"""
        self.ctx.bind_buffer(self.target, None)

    def __getitem__(self, index: Iterable[Union[int, slice]]) -> np.ndarray:
        """
        Slice Buffer Sub Data

        Parameters
        ----------
        index: tuple of (int or slice)
            Slicing Index

        Returns
        -------
        data: np.ndarray
        """
        raise NotImplementedError()

    def __setitem__(self, index: Iterable[Union[int, slice]], value: np.ndarray):
        """
        Set Buffer Sub Data

        Parameters
        ----------
        index: tuple of (int or slice)
            Slicing Index
        value: np.ndarray
            New Data
        """
        raise NotImplementedError()

    def __str__(self):
        """
        Buffer string representation

        Returns
        -------
        __str__: str
        """
        return "{}{}".format(self.__class__.__name__, self.shape)


class ArrayBuffer(Buffer):
    def __init__(self, ctx: gl.Context, data: np.ndarray, usage: gl.BufferUsage = gl.BufferUsage.STATIC_DRAW):
        """
        Create Array Buffer

        Parameters
        ----------
        ctx: gl.Context
            OpenGL Context
        data: np.ndarray
            Data to put in Buffer
        usage: gl.BufferUsage
            Buffer Usage Hint
        """
        super().__init__(ctx, gl.BufferTarget.ARRAY_BUFFER, data, usage)


class IndexBuffer(Buffer):
    def __init__(self, ctx: gl.Context, data: np.ndarray, usage: gl.BufferUsage = gl.BufferUsage.STATIC_DRAW):
        """
        Create Index Buffer

        Parameters
        ----------
        ctx: gl.Context
            OpenGL Context
        data: np.ndarray
            Data to put in Buffer
        usage: gl.BufferUsage
            Buffer Usage Hint
        """
        super().__init__(ctx, gl.BufferTarget.ELEMENT_ARRAY_BUFFER, data, usage)


class UniformBuffer(Buffer):
    def __init__(self, ctx: gl.Context, data: np.ndarray, usage: gl.BufferUsage = gl.BufferUsage.STATIC_DRAW):
        """
        Create Uniform Buffer

        Parameters
        ----------
        ctx: gl.Context
            OpenGL Context
        data: np.ndarray
            Data to put in Buffer
        usage: gl.BufferUsage
            Buffer Usage Hint
        """
        super().__init__(ctx, gl.BufferTarget.UNIFORM_BUFFER, data, usage)