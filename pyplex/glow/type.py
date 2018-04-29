from pyplex import gl
import numpy as np
from ctypes import *

from typing import Union, Callable, Any


class Type:
    _GL_BASE = {
        gl.Type.HALF_FLOAT: gl.Type.HALF_FLOAT,

        gl.Type.FLOAT: gl.Type.FLOAT,
        gl.Type.FLOAT_VEC2: gl.Type.FLOAT,
        gl.Type.FLOAT_VEC3: gl.Type.FLOAT,
        gl.Type.FLOAT_VEC4: gl.Type.FLOAT,

        gl.Type.DOUBLE: gl.Type.DOUBLE,
        gl.Type.DOUBLE_VEC2: gl.Type.DOUBLE,
        gl.Type.DOUBLE_VEC3: gl.Type.DOUBLE,
        gl.Type.DOUBLE_VEC4: gl.Type.DOUBLE,

        gl.Type.INT: gl.Type.INT,
        gl.Type.INT_VEC2: gl.Type.INT,
        gl.Type.INT_VEC3: gl.Type.INT,
        gl.Type.INT_VEC4: gl.Type.INT,

        gl.Type.UNSIGNED_INT: gl.Type.UNSIGNED_INT,
        gl.Type.UNSIGNED_INT_VEC2: gl.Type.UNSIGNED_INT,
        gl.Type.UNSIGNED_INT_VEC3: gl.Type.UNSIGNED_INT,
        gl.Type.UNSIGNED_INT_VEC4: gl.Type.UNSIGNED_INT,

        gl.Type.BOOL: gl.Type.BOOL,
        gl.Type.BOOL_VEC2: gl.Type.BOOL,
        gl.Type.BOOL_VEC3: gl.Type.BOOL,
        gl.Type.BOOL_VEC4: gl.Type.BOOL,

        gl.Type.FLOAT_MAT2: gl.Type.FLOAT,
        gl.Type.FLOAT_MAT3: gl.Type.FLOAT,
        gl.Type.FLOAT_MAT4: gl.Type.FLOAT,
        gl.Type.FLOAT_MAT2x3: gl.Type.FLOAT,
        gl.Type.FLOAT_MAT2x4: gl.Type.FLOAT,
        gl.Type.FLOAT_MAT3x4: gl.Type.FLOAT,
        gl.Type.FLOAT_MAT4x2: gl.Type.FLOAT,
        gl.Type.FLOAT_MAT4x3: gl.Type.FLOAT,

        gl.Type.DOUBLE_MAT2: gl.Type.DOUBLE,
        gl.Type.DOUBLE_MAT3: gl.Type.DOUBLE,
        gl.Type.DOUBLE_MAT4: gl.Type.DOUBLE,
        gl.Type.DOUBLE_MAT2x3: gl.Type.DOUBLE,
        gl.Type.DOUBLE_MAT2x4: gl.Type.DOUBLE,
        gl.Type.DOUBLE_MAT3x4: gl.Type.DOUBLE,
        gl.Type.DOUBLE_MAT4x2: gl.Type.DOUBLE,
        gl.Type.DOUBLE_MAT4x3: gl.Type.DOUBLE,
    }

    _GL_CTYPES = {
        gl.Type.BYTE: c_byte,
        gl.Type.UNSIGNED_BYTE: c_ubyte,
        gl.Type.INT: c_int,
        gl.Type.UNSIGNED_INT: c_uint,
        gl.Type.BOOL: c_bool,
        gl.Type.FLOAT: c_float,
        gl.Type.DOUBLE: c_double,
    }

    _GL_NAME = {
        gl.Type.HALF_FLOAT: 'half',

        gl.Type.FLOAT: 'float',
        gl.Type.FLOAT_VEC2: 'vec2',
        gl.Type.FLOAT_VEC3: 'vec3',
        gl.Type.FLOAT_VEC4: 'vec4',

        gl.Type.DOUBLE: 'double',
        gl.Type.DOUBLE_VEC2: 'dvec2',
        gl.Type.DOUBLE_VEC3: 'dvec3',
        gl.Type.DOUBLE_VEC4: 'dvec4',

        gl.Type.INT: 'int',
        gl.Type.INT_VEC2: 'ivec2',
        gl.Type.INT_VEC3: 'ivec3',
        gl.Type.INT_VEC4: 'ivec4',

        gl.Type.UNSIGNED_INT: 'uint',
        gl.Type.UNSIGNED_INT_VEC2: 'uvec2',
        gl.Type.UNSIGNED_INT_VEC3: 'uvec3',
        gl.Type.UNSIGNED_INT_VEC4: 'uvec4',

        gl.Type.BOOL: 'bool',
        gl.Type.BOOL_VEC2: 'bvec2',
        gl.Type.BOOL_VEC3: 'bvec3',
        gl.Type.BOOL_VEC4: 'bvec4',

        gl.Type.FLOAT_MAT2: 'mat2',
        gl.Type.FLOAT_MAT3: 'mat3',
        gl.Type.FLOAT_MAT4: 'mat4',
        gl.Type.FLOAT_MAT2x3: 'mat2x3',
        gl.Type.FLOAT_MAT2x4: 'mat2x4',
        gl.Type.FLOAT_MAT3x4: 'mat3x4',
        gl.Type.FLOAT_MAT4x2: 'mat4x2',
        gl.Type.FLOAT_MAT4x3: 'mat4x3',

        gl.Type.DOUBLE_MAT2: 'dmat2',
        gl.Type.DOUBLE_MAT3: 'dmat3',
        gl.Type.DOUBLE_MAT4: 'dmat4',
        gl.Type.DOUBLE_MAT2x3: 'dmat2x3',
        gl.Type.DOUBLE_MAT2x4: 'dmat2x4',
        gl.Type.DOUBLE_MAT3x4: 'dmat3x4',
        gl.Type.DOUBLE_MAT4x2: 'dmat4x2',
        gl.Type.DOUBLE_MAT4x3: 'dmat4x3',
    }

    _GL_NP = {
        gl.Type.HALF_FLOAT: ((1,), np.dtype('f2')),

        gl.Type.FLOAT: ((1,), np.dtype('f4')),
        gl.Type.FLOAT_VEC2: ((2,), np.dtype('f4')),
        gl.Type.FLOAT_VEC3: ((3,), np.dtype('f4')),
        gl.Type.FLOAT_VEC4: ((4,), np.dtype('f4')),

        gl.Type.DOUBLE: ((1,), np.dtype('f8')),
        gl.Type.DOUBLE_VEC2: ((2,), np.dtype('f8')),
        gl.Type.DOUBLE_VEC3: ((3,), np.dtype('f8')),
        gl.Type.DOUBLE_VEC4: ((4,), np.dtype('f8')),

        gl.Type.INT: ((1,), np.dtype('i4')),
        gl.Type.INT_VEC2: ((2,), np.dtype('i4')),
        gl.Type.INT_VEC3: ((3,), np.dtype('i4')),
        gl.Type.INT_VEC4: ((4,), np.dtype('i4')),

        gl.Type.UNSIGNED_INT: ((1,), np.dtype('u4')),
        gl.Type.UNSIGNED_INT_VEC2: ((2,), np.dtype('u4')),
        gl.Type.UNSIGNED_INT_VEC3: ((3,), np.dtype('u4')),
        gl.Type.UNSIGNED_INT_VEC4: ((4,), np.dtype('u4')),

        gl.Type.BOOL: ((1,), np.dtype('bool')),
        gl.Type.BOOL_VEC2: ((2,), np.dtype('bool')),
        gl.Type.BOOL_VEC3: ((3,), np.dtype('bool')),
        gl.Type.BOOL_VEC4: ((4,), np.dtype('bool')),

        gl.Type.FLOAT_MAT2: ((2, 2), np.dtype('f4')),
        gl.Type.FLOAT_MAT3: ((3, 3), np.dtype('f4')),
        gl.Type.FLOAT_MAT4: ((4, 4), np.dtype('f4')),
        gl.Type.FLOAT_MAT2x3: ((2, 3), np.dtype('f4')),
        gl.Type.FLOAT_MAT2x4: ((2, 4), np.dtype('f4')),
        gl.Type.FLOAT_MAT3x4: ((3, 4), np.dtype('f4')),
        gl.Type.FLOAT_MAT4x2: ((4, 2), np.dtype('f4')),
        gl.Type.FLOAT_MAT4x3: ((4, 3), np.dtype('f4')),

        gl.Type.DOUBLE_MAT2: ((2, 2), np.dtype('f8')),
        gl.Type.DOUBLE_MAT3: ((3, 3), np.dtype('f8')),
        gl.Type.DOUBLE_MAT4: ((4, 4), np.dtype('f8')),
        gl.Type.DOUBLE_MAT2x3: ((2, 3), np.dtype('f8')),
        gl.Type.DOUBLE_MAT2x4: ((2, 4), np.dtype('f8')),
        gl.Type.DOUBLE_MAT3x4: ((3, 4), np.dtype('f8')),
        gl.Type.DOUBLE_MAT4x2: ((4, 2), np.dtype('f8')),
        gl.Type.DOUBLE_MAT4x3: ((4, 3), np.dtype('f8')),
    }

    _GL_UNIFORM = {
        # gl.Type.HALF_FLOAT: None,

        gl.Type.FLOAT: gl.GL41.program_uniform_1fv,
        gl.Type.FLOAT_VEC2: gl.GL41.program_uniform_2fv,
        gl.Type.FLOAT_VEC3: gl.GL41.program_uniform_3fv,
        gl.Type.FLOAT_VEC4: gl.GL41.program_uniform_4fv,

        # gl.Type.DOUBLE: gl.GL45.program_uniform1,
        # gl.Type.DOUBLE_VEC2: gl.GL45.program_uniform2dv,
        # gl.Type.DOUBLE_VEC3: gl.GL45.program_uniform3dv,
        # gl.Type.DOUBLE_VEC4: gl.GL45.program_uniform4dv,

        gl.Type.INT: gl.GL41.program_uniform_1iv,
        gl.Type.INT_VEC2: gl.GL41.program_uniform_2iv,
        gl.Type.INT_VEC3: gl.GL41.program_uniform_3iv,
        gl.Type.INT_VEC4: gl.GL41.program_uniform_4iv,

        gl.Type.UNSIGNED_INT: gl.GL41.program_uniform_1uiv,
        gl.Type.UNSIGNED_INT_VEC2: gl.GL41.program_uniform_2uiv,
        gl.Type.UNSIGNED_INT_VEC3: gl.GL41.program_uniform_3uiv,
        gl.Type.UNSIGNED_INT_VEC4: gl.GL41.program_uniform_4uiv,

        gl.Type.BOOL: gl.GL41.program_uniform_1iv,
        gl.Type.BOOL_VEC2: gl.GL41.program_uniform_2iv,
        gl.Type.BOOL_VEC3: gl.GL41.program_uniform_3iv,
        gl.Type.BOOL_VEC4: gl.GL41.program_uniform_4iv,

        gl.Type.FLOAT_MAT2: gl.GL41.program_uniform_matrix_2fv,
        gl.Type.FLOAT_MAT3: gl.GL41.program_uniform_matrix_3fv,
        gl.Type.FLOAT_MAT4: gl.GL41.program_uniform_matrix_4fv,
        gl.Type.FLOAT_MAT2x3: gl.GL41.program_uniform_matrix_2x3fv,
        gl.Type.FLOAT_MAT2x4: gl.GL41.program_uniform_matrix_2x4fv,
        gl.Type.FLOAT_MAT3x4: gl.GL41.program_uniform_matrix_3x4fv,
        gl.Type.FLOAT_MAT4x2: gl.GL41.program_uniform_matrix_4x2fv,
        gl.Type.FLOAT_MAT4x3: gl.GL41.program_uniform_matrix_4x3fv,

        # gl.Type.DOUBLE_MAT2: gl.GL45.program_uniform_matrix2dv,
        # gl.Type.DOUBLE_MAT3: gl.GL45.program_uniform_matrix3dv,
        # gl.Type.DOUBLE_MAT4: gl.GL45.program_uniform_matrix4dv,
        # gl.Type.DOUBLE_MAT2x3: gl.GL45.program_uniform_matrix2x3dv,
        # gl.Type.DOUBLE_MAT2x4: gl.GL45.program_uniform_matrix2x4dv,
        # gl.Type.DOUBLE_MAT3x4: gl.GL45.program_uniform_matrix3x4dv,
        # gl.Type.DOUBLE_MAT4x2: gl.GL45.program_uniform_matrix4x2dv,
        # gl.Type.DOUBLE_MAT4x3: gl.GL45.program_uniform_matrix4x3dv,
    }

    def __init__(self, gl_type: Union[gl.Type, int]):
        """
        OpenGL Type Information

        Parameters
        ----------
        gl_type: gl.Type or int
        """
        self._gl_type = gl_type
        self._gl_base = self._GL_BASE[gl_type]
        self._gl_name = self._GL_NAME[gl_type]
        self._ctypes = self._GL_CTYPES[self._gl_base]
        self._uniform = self._GL_UNIFORM[gl_type]
        self._shape, self._dtype = self._GL_NP[gl_type]

    @property
    def gl_type(self) -> gl.Type:
        """
        OpenGL Type

        Returns
        -------
        gl_type: gl.Type
        """
        return self._gl_type

    @property
    def gl_base(self) -> gl.Type:
        """
        OpenGL Base Type

        Returns
        -------
        gl_base: gl.Type
        """
        return self._gl_base

    @property
    def gl_name(self) -> str:
        """
        OpenGL Type Name

        Returns
        -------
        gl_name: str
        """
        return self._gl_name

    @property
    def ctypes(self):
        return self._ctypes

    @property
    def uniform_func(self) -> Callable[[gl.GL41, int, int, int, Any], None]:
        """
        Function to set uniform variable of this Type

        Returns
        -------
        uniform_func: callable
        """
        return self._uniform

    @property
    def dtype(self) -> np.dtype:
        """
        Numpy dtype corresponding with OpenGL Type

        Returns
        -------
        dtype: np.dtype
        """
        return self._dtype

    @property
    def shape(self) -> tuple:
        """
        Shape Corresponding with OpenGL Type

        Returns
        -------
        shape: tuple
        """
        return self._shape

    @property
    def count(self) -> int:
        """
        Number of 'dtype' items in Type

        Returns
        -------
        count: int
        """
        return int(np.prod(self.shape))

    @property
    def nbytes(self) -> int:
        """
        Size of Type in bytes

        Returns
        -------
        size: int
        """
        return self.count * self.dtype.itemsize

    def __str__(self):
        """
        Type string representation

        Returns
        -------
        __str__: str
        """
        return self.gl_name