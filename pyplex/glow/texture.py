from pyplex import gl
import numpy as np
from ctypes import *


class TextureFilter:
    def __init__(self,
                 minification: gl.TextureFilter=gl.TextureFilter.LINEAR,
                 magnification: gl.TextureFilter=gl.TextureFilter.LINEAR,
                 anisotropy: float = 1.0):
        self.minification = minification
        self.magnification = magnification
        self.anisotropy = anisotropy


class TextureWrap:
    def __init__(self,
                 s: gl.TextureWrap=gl.TextureWrap.REPEAT,
                 t: gl.TextureWrap=gl.TextureWrap.REPEAT,
                 r: gl.TextureWrap=gl.TextureWrap.REPEAT):
        self.s = s
        self.t = t
        self.r = r


class TextureSwizzle:
    def __init__(self,
                 r: gl.TextureSwizzle=gl.TextureSwizzle.RED,
                 g: gl.TextureSwizzle=gl.TextureSwizzle.GREEN,
                 b: gl.TextureSwizzle=gl.TextureSwizzle.BLUE,
                 a: gl.TextureSwizzle=gl.TextureSwizzle.ALPHA):
        self.r = r
        self.g = g
        self.b = b
        self.a = a


class TextureLOD:
    def __init__(self, min: float=-1000, max: float=1000):
        self.min = min
        self.max = max


class Texture:
    def __init__(self, ctx: gl.GL_ANY, target: gl.TextureTarget, type: gl.TextureType,
                 format: gl.TextureFormat, internal_format: gl.TextureInternalFormat,
                 filter: TextureFilter = TextureFilter(), wrap: TextureWrap = TextureWrap(),
                 swizzle: TextureSwizzle = TextureSwizzle(), lod: TextureLOD = TextureLOD()):

        self._ctx = ctx
        self._target = target
        self._type = type
        self._format = format
        self._internal_format = internal_format

        self._filter = self._wrap = self._swizzle = self._lod = None

        self._ptr = c_uint(0)
        self._ctx.gen_textures(1, self._ptr)
        self._ptr = self._ptr.value

        self.filter = filter
        self.wrap = wrap
        self.swizzle = swizzle
        self.lod = lod

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def target(self) -> gl.TextureTarget:
        return self._target

    @property
    def type(self) -> gl.TextureType:
        return self._type

    @property
    def format(self) -> gl.TextureFormat:
        return self._format

    @property
    def internal_format(self) -> gl.TextureInternalFormat:
        return self._internal_format

    @property
    def filter(self) -> TextureFilter:
        return self._filter
    
    @filter.setter
    def filter(self, value: TextureFilter):
        self._ctx.bind_texture(self._target, self._ptr)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.MIN_FILTER, value.minification)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.MAG_FILTER, value.magnification)
        self._ctx.tex_parameterf(self._target, gl.TextureParameter.TEXTURE_MAX_ANISOTROPY, value.anisotropy)
        self._ctx.bind_texture(self._target, 0)
        self._filter = value

    @property
    def wrap(self) -> TextureWrap:
        return self._wrap

    @wrap.setter
    def wrap(self, value: TextureWrap):
        self._ctx.bind_texture(self._target, self._ptr)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.WRAP_S, value.s)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.WRAP_T, value.t)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.WRAP_R, value.r)
        self._ctx.bind_texture(self._target, 0)
        self._wrap = value

    @property
    def swizzle(self) -> TextureSwizzle:
        return self._swizzle

    @swizzle.setter
    def swizzle(self, value: TextureSwizzle):
        self._ctx.bind_texture(self._target, self._ptr)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.SWIZZLE_R, value.r)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.SWIZZLE_G, value.g)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.SWIZZLE_B, value.b)
        self._ctx.tex_parameteri(self._target, gl.TextureParameter.SWIZZLE_A, value.a)
        self._ctx.bind_texture(self._target, 0)
        self._swizzle = value

    @property
    def lod(self) -> TextureLOD:
        return self._lod

    @lod.setter
    def lod(self, value: TextureLOD):
        self._ctx.bind_texture(self._target, self._ptr)
        self._ctx.tex_parameterf(self._target, gl.TextureParameter.MIN_LOD, value.min)
        self._ctx.tex_parameterf(self._target, gl.TextureParameter.MAX_LOD, value.max)
        self._ctx.bind_texture(self._target, 0)
        self._lod = value


class ImageTexture(Texture):

    _CHANNELS = {
        1: (gl.TextureFormat.RED, gl.TextureInternalFormat.RED),
        2: (gl.TextureFormat.RG, gl.TextureInternalFormat.RG),
        3: (gl.TextureFormat.RGB, gl.TextureInternalFormat.RGB),
        4: (gl.TextureFormat.RGBA, gl.TextureInternalFormat.RGBA)
    }

    _SETTER = {
        gl.TextureTarget.TEXTURE_1D: gl.GL20.tex_image_1d,
        gl.TextureTarget.TEXTURE_2D: gl.GL20.tex_image_2d,
        gl.TextureTarget.TEXTURE_3D: gl.GL20.tex_image_3d
    }

    _TYPE = {
        np.dtype(np.int8): gl.TextureType.BYTE,
        np.dtype(np.uint8): gl.TextureType.UNSIGNED_BYTE,
        np.dtype(np.int16): gl.TextureType.SHORT,
        np.dtype(np.uint16): gl.TextureType.UNSIGNED_SHORT,
        np.dtype(np.int32): gl.TextureType.INT,
        np.dtype(np.uint32): gl.TextureType.UNSIGNED_INT,
        np.dtype(np.float32): gl.TextureType.FLOAT,
        np.dtype(np.float16): gl.TextureType.HALF_FLOAT
    }

    def __init__(self, ctx: gl.GL_ANY, data: np.ndarray, target: gl.TextureTarget,
                 filter: TextureFilter = TextureFilter(), wrap: TextureWrap = TextureWrap(),
                 swizzle: TextureSwizzle = TextureSwizzle(), lod: TextureLOD = TextureLOD()):

        type = self._TYPE[data.dtype]
        format, internal_format = self._CHANNELS[data.shape[-1]]

        super().__init__(ctx, target, type, format, internal_format, filter, wrap, swizzle, lod)

        self._setter = self._ctx.__getattribute__(self._SETTER[target].__name__)
        self._dtype = self._size = self._itemsize = self._nbytes = self._ndim = self._shape = None

        self.data = data

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
    def data(self) -> np.ndarray:
        data = np.empty(self._shape, self._dtype)
        self._ctx.bind_texture(self._target, self._ptr)
        self._ctx.get_tex_image(self._target, 0, self._format, self._type, data.ctypes.data_as(c_void_p))
        self._ctx.bind_texture(self._target, 0)
        return data

    @data.setter
    def data(self, value: np.ndarray):
        self._ctx.bind_texture(self._target, self._ptr)
        self._setter(self._target, 0, self._internal_format, *value.shape[:-1],
                     0, self._format, self._type, value.ctypes.data_as(c_void_p))
        self._ctx.bind_texture(self._target, 0)
        self._update_dimensionality(value)

    def _update_dimensionality(self, data: np.ndarray):
        self._dtype = data.dtype
        self._size = data.size
        self._itemsize = data.itemsize
        self._nbytes = data.nbytes
        self._ndim = data.ndim
        self._shape = data.shape


class Texture1D(ImageTexture):
    def __init__(self, ctx: gl.GL_ANY, data: np.ndarray,
                 filter: TextureFilter = TextureFilter(), wrap: TextureWrap = TextureWrap(),
                 swizzle: TextureSwizzle = TextureSwizzle(), lod: TextureLOD = TextureLOD()):
        super().__init__(ctx, data, gl.TextureTarget.TEXTURE_1D, filter, wrap, swizzle, lod)


class Texture2D(ImageTexture):
    def __init__(self, ctx: gl.GL_ANY, data: np.ndarray,
                 filter: TextureFilter = TextureFilter(), wrap: TextureWrap = TextureWrap(),
                 swizzle: TextureSwizzle = TextureSwizzle(), lod: TextureLOD = TextureLOD()):
        super().__init__(ctx, data, gl.TextureTarget.TEXTURE_2D, filter, wrap, swizzle, lod)


class Texture3D(ImageTexture):
    def __init__(self, ctx: gl.GL_ANY, data: np.ndarray,
                 filter: TextureFilter = TextureFilter(), wrap: TextureWrap = TextureWrap(),
                 swizzle: TextureSwizzle = TextureSwizzle(), lod: TextureLOD = TextureLOD()):
        super().__init__(ctx, data, gl.TextureTarget.TEXTURE_3D, filter, wrap, swizzle, lod)