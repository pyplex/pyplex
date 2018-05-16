from pyplex import gl
import numpy as np
from ctypes import *

from typing import Optional, Union, Any


class Type:
    _GL_BASE = {
        gl.Type.BYTE: gl.Type.BYTE,
        gl.Type.UNSIGNED_BYTE: gl.Type.UNSIGNED_BYTE,

        gl.Type.SHORT: gl.Type.SHORT,
        gl.Type.UNSIGNED_SHORT: gl.Type.UNSIGNED_SHORT,

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
        gl.Type.SHORT: c_short,
        gl.Type.UNSIGNED_SHORT: c_ushort,
        gl.Type.INT: c_int,
        gl.Type.UNSIGNED_INT: c_uint,
        gl.Type.BOOL: c_bool,
        gl.Type.FLOAT: c_float,
        gl.Type.DOUBLE: c_double,
    }

    _GL_NAME = {
        gl.Type.UNSIGNED_BYTE: 'ubyte',
        gl.Type.BYTE: 'byte',

        gl.Type.UNSIGNED_SHORT: 'ushort',
        gl.Type.SHORT: 'short',

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
        
        gl.Type.SAMPLER_1D: 'sampler1D',
        gl.Type.SAMPLER_2D: 'sampler2D',
        gl.Type.SAMPLER_3D: 'sampler3D',
        gl.Type.SAMPLER_CUBE: 'samplerCube',
        gl.Type.SAMPLER_1D_SHADOW: 'sampler1DShadow',
        gl.Type.SAMPLER_2D_SHADOW: 'sampler2DShadow',
        gl.Type.SAMPLER_1D_ARRAY: 'sampler1DArray',
        gl.Type.SAMPLER_2D_ARRAY: 'sampler2DArray',
        gl.Type.SAMPLER_1D_ARRAY_SHADOW: 'sampler1DArrayShadow',
        gl.Type.SAMPLER_2D_ARRAY_SHADOW: 'sampler2DArrayShadow',
        gl.Type.SAMPLER_CUBE_MAP_ARRAY: 'samplerCubeArray',
        gl.Type.SAMPLER_2D_MULTISAMPLE: 'sampler2DMS',
        gl.Type.SAMPLER_2D_MULTISAMPLE_ARRAY: 'sampler2DMSArray',
        gl.Type.SAMPLER_CUBE_SHADOW: 'samplerCubeShadow',
        gl.Type.SAMPLER_CUBE_MAP_ARRAY_SHADOW: 'samplerCubeArrayShadow',
        gl.Type.SAMPLER_BUFFER: 'samplerBuffer',
        gl.Type.SAMPLER_2D_RECT: 'sampler2DRect',
        gl.Type.SAMPLER_2D_RECT_SHADOW: 'sampler2DRectShadow',

        gl.Type.INT_SAMPLER_1D: 'isampler1D',
        gl.Type.INT_SAMPLER_2D: 'isampler2D',
        gl.Type.INT_SAMPLER_3D: 'isampler3D',
        gl.Type.INT_SAMPLER_CUBE: 'isamplerCube',
        gl.Type.INT_SAMPLER_1D_ARRAY: 'isampler1DArray',
        gl.Type.INT_SAMPLER_2D_ARRAY: 'isampler2DArray',
        gl.Type.INT_SAMPLER_CUBE_MAP_ARRAY: 'isamplerCubeArray',
        gl.Type.INT_SAMPLER_2D_MULTISAMPLE: 'isampler2DMS',
        gl.Type.INT_SAMPLER_2D_MULTISAMPLE_ARRAY: 'isampler2DMSArray',
        gl.Type.INT_SAMPLER_BUFFER: 'isamplerBuffer',
        gl.Type.INT_SAMPLER_2D_RECT: 'isampler2DRect',

        gl.Type.UNSIGNED_INT_SAMPLER_1D: 'usampler1D',
        gl.Type.UNSIGNED_INT_SAMPLER_2D: 'usampler2D',
        gl.Type.UNSIGNED_INT_SAMPLER_3D: 'usampler3D',
        gl.Type.UNSIGNED_INT_SAMPLER_CUBE: 'usamplerCube',
        gl.Type.UNSIGNED_INT_SAMPLER_1D_ARRAY: 'usampler1DArray',
        gl.Type.UNSIGNED_INT_SAMPLER_2D_ARRAY: 'usampler2DArray',
        gl.Type.UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY: 'usamplerCubeArray',
        gl.Type.UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: 'usampler2DMS',
        gl.Type.UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: 'usampler2DMSArray',
        gl.Type.UNSIGNED_INT_SAMPLER_BUFFER: 'usamplerBuffer',
        gl.Type.UNSIGNED_INT_SAMPLER_2D_RECT: 'usampler2DRect',

        gl.Type.IMAGE_1D: 'image1D',
        gl.Type.IMAGE_2D: 'image2D',
        gl.Type.IMAGE_3D: 'image3D',
        gl.Type.IMAGE_CUBE: 'imageCube',
        gl.Type.IMAGE_1D_ARRAY: 'image1DArray',
        gl.Type.IMAGE_2D_ARRAY: 'image2DArray',
        gl.Type.IMAGE_CUBE_MAP_ARRAY: 'imageCubeArray',
        gl.Type.IMAGE_2D_MULTISAMPLE: 'image2DMS',
        gl.Type.IMAGE_2D_MULTISAMPLE_ARRAY: 'image2DMSArray',
        gl.Type.IMAGE_BUFFER: 'imageBuffer',
        gl.Type.IMAGE_2D_RECT: 'image2DRect',

        gl.Type.INT_IMAGE_1D: 'iimage1D',
        gl.Type.INT_IMAGE_2D: 'iimage2D',
        gl.Type.INT_IMAGE_3D: 'iimage3D',
        gl.Type.INT_IMAGE_CUBE: 'iimageCube',
        gl.Type.INT_IMAGE_1D_ARRAY: 'iimage1DArray',
        gl.Type.INT_IMAGE_2D_ARRAY: 'iimage2DArray',
        gl.Type.INT_IMAGE_CUBE_MAP_ARRAY: 'iimageCubeArray',
        gl.Type.INT_IMAGE_2D_MULTISAMPLE: 'iimage2DMS',
        gl.Type.INT_IMAGE_2D_MULTISAMPLE_ARRAY: 'iimage2DMSArray',
        gl.Type.INT_IMAGE_BUFFER: 'iimageBuffer',
        gl.Type.INT_IMAGE_2D_RECT: 'iimage2DRect',

        gl.Type.UNSIGNED_INT_IMAGE_1D: 'uimage1D',
        gl.Type.UNSIGNED_INT_IMAGE_2D: 'uimage2D',
        gl.Type.UNSIGNED_INT_IMAGE_3D: 'uimage3D',
        gl.Type.UNSIGNED_INT_IMAGE_CUBE: 'uimageCube',
        gl.Type.UNSIGNED_INT_IMAGE_1D_ARRAY: 'uimage1DArray',
        gl.Type.UNSIGNED_INT_IMAGE_2D_ARRAY: 'uimage2DArray',
        gl.Type.UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY: 'uimageCubeArray',
        gl.Type.UNSIGNED_INT_IMAGE_2D_MULTISAMPLE: 'uimage2DMS',
        gl.Type.UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY: 'uimage2DMSArray',
        gl.Type.UNSIGNED_INT_IMAGE_BUFFER: 'uimageBuffer',
        gl.Type.UNSIGNED_INT_IMAGE_2D_RECT: 'uimage2DRect',
    }

    _GL_NP = {
        gl.Type.BYTE: ((), np.dtype('i1')),
        gl.Type.UNSIGNED_BYTE: ((), np.dtype('u1')),

        gl.Type.SHORT: ((), np.dtype('i2')),
        gl.Type.UNSIGNED_SHORT: ((), np.dtype('u2')),

        gl.Type.HALF_FLOAT: ((), np.dtype('f2')),

        gl.Type.FLOAT: ((), np.dtype('f4')),
        gl.Type.FLOAT_VEC2: ((2,), np.dtype('f4')),
        gl.Type.FLOAT_VEC3: ((3,), np.dtype('f4')),
        gl.Type.FLOAT_VEC4: ((4,), np.dtype('f4')),

        gl.Type.DOUBLE: ((), np.dtype('f8')),
        gl.Type.DOUBLE_VEC2: ((2,), np.dtype('f8')),
        gl.Type.DOUBLE_VEC3: ((3,), np.dtype('f8')),
        gl.Type.DOUBLE_VEC4: ((4,), np.dtype('f8')),

        gl.Type.INT: ((), np.dtype('i4')),
        gl.Type.INT_VEC2: ((2,), np.dtype('i4')),
        gl.Type.INT_VEC3: ((3,), np.dtype('i4')),
        gl.Type.INT_VEC4: ((4,), np.dtype('i4')),

        gl.Type.UNSIGNED_INT: ((), np.dtype('u4')),
        gl.Type.UNSIGNED_INT_VEC2: ((2,), np.dtype('u4')),
        gl.Type.UNSIGNED_INT_VEC3: ((3,), np.dtype('u4')),
        gl.Type.UNSIGNED_INT_VEC4: ((4,), np.dtype('u4')),

        gl.Type.BOOL: ((), np.dtype('bool')),
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

    _NP_GL = {value: key for key, value in _GL_NP.items()}

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
        self._gl_type = gl.Type(gl_type)
        self._gl_name = self._GL_NAME[gl_type]
        self._opaque = self._gl_type.name in gl.OpaqueType.__members__

        self._gl_base = self._ctypes = self._shape = self._dtype = self._uniform = None

        if not self._opaque:
            self._gl_base = self._GL_BASE[gl_type]
            self._ctypes = self._GL_CTYPES[self._gl_base]
            self._shape, self._dtype = self._GL_NP[gl_type]
            if self._shape == (): self._shape = (1,)
            self._uniform = self._GL_UNIFORM[gl_type] if gl_type in self._GL_UNIFORM else None

    @classmethod
    def from_np(cls, shape: tuple, dtype: np.dtype):
        return cls(Type._NP_GL[(shape, dtype)])

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
    def gl_name(self) -> str:
        """
        OpenGL Type Name

        Returns
        -------
        gl_name: str
        """
        return self._gl_name

    @property
    def gl_base(self) -> Optional[gl.Type]:
        """
        OpenGL Base Type

        Returns
        -------
        gl_base: gl.Type
        """
        return self._gl_base

    @property
    def ctypes(self) -> Optional[Any]:
        return self._ctypes

    @property
    def uniform_func(self):
        """
        Function to set uniform variable of this Type

        Returns
        -------
        uniform_func: callable
        """
        return self._uniform

    @property
    def dtype(self) -> Optional[np.dtype]:
        """
        Numpy dtype corresponding with OpenGL Type

        Returns
        -------
        dtype: np.dtype
        """
        return self._dtype

    @property
    def shape(self) -> Optional[tuple]:
        """
        Shape Corresponding with OpenGL Type

        Returns
        -------
        shape: tuple
        """
        return self._shape

    @property
    def count(self) -> Optional[int]:
        """
        Number of 'dtype' items in Type

        Returns
        -------
        count: int
        """
        return int(np.prod(self.shape)) if self.shape else None

    @property
    def nbytes(self) -> Optional[int]:
        """
        Size of Type in bytes

        Returns
        -------
        size: int
        """
        return self.count * self.dtype.itemsize if self.count and self.dtype else None

    def __str__(self):
        """
        Type string representation

        Returns
        -------
        __str__: str
        """
        return self.gl_name