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
        self._ptr = self.ctx.create_buffer()
        self._target = target
        self._usage = usage

        self._dtype = data.dtype
        self._shape = data.shape
        self._stride = np.prod(self.shape[1:]) * self.dtype.itemsize

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
    def dtype(self) -> np.dtype:
        """
        Returns
        -------
        dtype: np.dtype
            Buffer dtype
        """
        return self._dtype

    @property
    def shape(self) -> tuple:
        """
        Returns
        -------
        shape: tuple
            Buffer Shape
        """
        return self._shape

    @property
    def stride(self) -> int:
        """
        Returns
        -------
        stride: int
            Buffer Stride
        """
        return self._stride

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
            self._dtype = value.dtype
            self._shape = value.shape
            self._stride = np.prod(self.shape[1:]) * self.dtype.itemsize
            self.ctx.buffer_data(self.target, value, self.usage)

    def delete(self):
        """Delete Buffer"""
        self.ctx.delete_buffer(self.ptr)

    def bind(self):
        """Bind Buffer"""
        self.ctx.bind_buffer(self.target, self.ptr)

    def unbind(self):
        """Unbind Buffer"""
        self.ctx.bind_buffer(self.target, None)

    def __getitem__(self, index: Union[Iterable[Union[int, slice]], int, slice]) -> np.ndarray:
        """
        Slice Buffer Sub Data

        Parameters
        ----------
        index: int, slice or tuple of (int or slice)
            Slicing Index

        Returns
        -------
        data: np.ndarray
        """

        indices = [[0, size, 1] for size in self.shape]

        if isinstance(index, slice):
            indices[0] = index.indices(self.shape[0])
        elif isinstance(index, int):
            indices[0] = (index, index+1, 1)
        else:
            for i, (s, n) in enumerate(zip(index, self.shape)):
                if isinstance(s, slice):
                    indices[i] = s.indices(n)
                elif isinstance(s, int):
                    indices[i] = [s, s+1, 1]

        start, stop, step = indices[0]
        size = stop - start

        with self:
            data = self.ctx.get_buffer_sub_data(self.target, start * self.stride, size * self.stride)
            data = data.view(self.dtype).reshape(size, *self.shape[1:])
            slicing = [slice(0, size, step)] + [slice(*idx) for idx in indices[1:]]
            return np.squeeze(data[slicing])

    def __setitem__(self, index: Union[int, slice], value: np.ndarray):
        """
        Set Buffer Sub Data

        Parameters
        ----------
        index: int or slice
            Slicing Index
        value: np.ndarray
            New Data
        """

        if isinstance(index, slice):
            start, stop, step = index.indices(self.shape[0])
            if step != 1: raise ValueError("Buffer slice step must be equal to 1")
        elif isinstance(index, int): start, stop, step = (index, index + 1, 1)
        else: raise ValueError("Setter index should be slice or int")

        shape = (stop - start, *self.shape[1:])

        if value.shape != shape:
            raise ValueError("could not broadcast input array from shape {} into shape {}".format(value.shape, shape))
        if not value.dtype == self.dtype:
            raise ValueError("value dtype ({}) does not match Buffer dtype ({})".format(value.dtype, self.dtype))

        with self:
            self.ctx.buffer_sub_data(self.target, start * self.stride, value)

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
        Create Array Buffer | Source for Vertex Data

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
        Create Index Buffer | Indexed Rendering

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
        Create Uniform Buffer | Storage for Uniform Blocks

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