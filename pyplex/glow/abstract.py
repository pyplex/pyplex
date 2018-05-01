import numpy as np


class Object:
    @property
    def ptr(self) -> int:
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()


class BindableObject(Object):
    def bind(self):
        raise NotImplementedError()

    def unbind(self):
        raise NotImplementedError()

    def __enter__(self):
        return self.bind()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unbind()


class Array:
    @property
    def dtype(self) -> np.dtype:
        raise NotImplementedError()

    @property
    def size(self) -> int:
        raise NotImplementedError()

    @property
    def itemsize(self) -> int:
        raise NotImplementedError()

    @property
    def nbytes(self) -> int:
        raise NotImplementedError()

    @property
    def ndim(self) -> int:
        raise NotImplementedError()

    @property
    def shape(self) -> tuple:
        raise NotImplementedError()

    @property
    def data(self) -> np.ndarray:
        raise NotImplementedError()

    @data.setter
    def data(self, value: np.ndarray):
        raise NotImplementedError()