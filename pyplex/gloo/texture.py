from pyplex import gl
from pyplex.gloo import ContextObject
import numpy as np

from typing import Optional


class TextureContext(ContextObject):
    def __init__(self,
                 ctx: gl.Context,
                 target: gl.TextureTarget,
                 type: gl.TextureType,
                 format: gl.TextureFormat,
                 internal_format: gl.TextureInternalFormat,
                 border_color: np.ndarray = np.array([0, 0, 0, 0], np.float32),
                 min_filter: gl.TextureFilter = gl.TextureFilter.LINEAR,
                 mag_filter: gl.TextureFilter = gl.TextureFilter.LINEAR,
                 ani_filter: float = 16,
                 wrap_s: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_t: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_r: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 swizzle_r: gl.TextureSwizzle = gl.TextureSwizzle.RED,
                 swizzle_g: gl.TextureSwizzle = gl.TextureSwizzle.GREEN,
                 swizzle_b: gl.TextureSwizzle = gl.TextureSwizzle.BLUE,
                 swizzle_a: gl.TextureSwizzle = gl.TextureSwizzle.ALPHA,
                 min_lod: float = -1000,
                 max_lod: float = 1000):

        self._ctx = ctx
        self._ptr = ctx.create_texture()
        self._target = target
        self._type = type
        self._format = format
        self._internal_format = internal_format

        self._border_color = border_color

        self._min_filter = min_filter
        self._mag_filter = mag_filter
        self._ani_filter = ani_filter

        self._wrap_s = wrap_s
        self._wrap_t = wrap_t
        self._wrap_r = wrap_r

        self._swizzle_r = swizzle_r
        self._swizzle_g = swizzle_g
        self._swizzle_b = swizzle_b
        self._swizzle_a = swizzle_a

        self._min_lod = min_lod
        self._max_lod = max_lod

        with self:
            self.ctx.texture_parameter(self.target, gl.TextureParameter.BORDER_COLOR, self.border_color)

            self.ctx.texture_parameter(self.target, gl.TextureParameter.MIN_FILTER, self.min_filter)
            self.ctx.texture_parameter(self.target, gl.TextureParameter.MAG_FILTER, self.mag_filter)
            self.ctx.texture_parameter(self.target, gl.TextureParameter.TEXTURE_MAX_ANISOTROPY, float(self.ani_filter))

            self.ctx.texture_parameter(self.target, gl.TextureParameter.WRAP_S, self.wrap_s)
            self.ctx.texture_parameter(self.target, gl.TextureParameter.WRAP_T, self.wrap_t)
            self.ctx.texture_parameter(self.target, gl.TextureParameter.WRAP_R, self.wrap_r)

            self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_R, self.swizzle_r)
            self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_G, self.swizzle_g)
            self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_B, self.swizzle_b)
            self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_A, self.swizzle_a)

            self.ctx.texture_parameter(self.target, gl.TextureParameter.MIN_LOD, float(self.min_lod))
            self.ctx.texture_parameter(self.target, gl.TextureParameter.MAX_LOD, float(self.max_lod))

    @property
    def ctx(self) -> gl.Context:
        return self._ctx

    @property
    def ptr(self) -> gl.Texture:
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
    def border_color(self) -> np.ndarray:
        return self._border_color

    @border_color.setter
    def border_color(self, value: np.ndarray):
        self._border_color = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.BORDER_COLOR, self.border_color)

    @property
    def min_filter(self) -> gl.TextureFilter:
        return self._min_filter

    @min_filter.setter
    def min_filter(self, value: gl.TextureFilter):
        self._min_filter = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.MIN_FILTER, self.min_filter)

    @property
    def mag_filter(self) -> gl.TextureFilter:
        return self._mag_filter

    @mag_filter.setter
    def mag_filter(self, value: gl.TextureFilter):
        self._mag_filter = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.MAG_FILTER, self.mag_filter)

    @property
    def ani_filter(self):
        return self._ani_filter

    @ani_filter.setter
    def ani_filter(self, value: float):
        self._ani_filter = float(value)
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.TEXTURE_MAX_ANISOTROPY, self.ani_filter)

    @property
    def wrap_s(self) -> gl.TextureWrap:
        return self._wrap_s

    @wrap_s.setter
    def wrap_s(self, value: gl.TextureWrap):
        self._wrap_s = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.WRAP_S, self.wrap_s)

    @property
    def wrap_t(self) -> gl.TextureWrap:
        return self._wrap_t
    
    @wrap_t.setter
    def wrap_t(self, value: gl.TextureWrap):
        self._wrap_t = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.WRAP_T, self.wrap_t)

    @property
    def wrap_r(self) -> gl.TextureWrap:
        return self._wrap_r
    
    @wrap_r.setter
    def wrap_r(self, value: gl.TextureWrap):
        self._wrap_r = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.WRAP_R, self.wrap_r)

    @property
    def swizzle_r(self) -> gl.TextureSwizzle:
        return self._swizzle_r
    
    @swizzle_r.setter
    def swizzle_r(self, value: gl.TextureSwizzle):
        self._swizzle_r = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_R, self.swizzle_r)
        
    @property
    def swizzle_g(self) -> gl.TextureSwizzle:
        return self._swizzle_g
    
    @swizzle_g.setter
    def swizzle_g(self, value: gl.TextureSwizzle):
        self._swizzle_g = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_G, self.swizzle_g)

    @property
    def swizzle_b(self) -> gl.TextureSwizzle:
        return self._swizzle_b
    
    @swizzle_b.setter
    def swizzle_b(self, value: gl.TextureSwizzle):
        self._swizzle_b = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_B, self.swizzle_b)

    @property
    def swizzle_a(self) -> gl.TextureSwizzle:
        return self._swizzle_a
    
    @swizzle_a.setter
    def swizzle_a(self, value: gl.TextureSwizzle):
        self._swizzle_a = value
        with self: self.ctx.texture_parameter(self.target, gl.TextureParameter.SWIZZLE_A, self.swizzle_a)

    @property
    def min_lod(self) -> float:
        return self._min_lod
    
    @min_lod.setter
    def min_lod(self, value: float):
        self._min_lod = float(value)
        self.ctx.texture_parameter(self.target, gl.TextureParameter.MIN_LOD, self.min_lod)
        
    @property
    def max_lod(self) -> float:
        return self._max_lod
    
    @max_lod.setter
    def max_lod(self, value: float):
        self._max_lod = float(value)
        self.ctx.texture_parameter(self.target, gl.TextureParameter.MAX_LOD, self.max_lod)

    def delete(self):
        self.ctx.delete_texture(self.ptr)

    def bind(self):
        """Bind Texture"""
        self.ctx.bind_texture(self.target, self.ptr)

    def unbind(self):
        """Unbind Texture"""
        self.ctx.bind_texture(self.target, None)

    def generate_mipmap(self):
        with self: self.ctx.generate_mipmap(self.target)


class ImageTexture(TextureContext):

    _SETTER = {
        gl.TextureTarget.TEXTURE_1D: gl.Context.texture_image_1D,
        gl.TextureTarget.TEXTURE_2D: gl.Context.texture_image_2D,
        gl.TextureTarget.TEXTURE_3D: gl.Context.texture_image_3D
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

    _CHANNELS = {
        1: (gl.TextureFormat.RED, gl.TextureInternalFormat.RED),
        2: (gl.TextureFormat.RG, gl.TextureInternalFormat.RG),
        3: (gl.TextureFormat.RGB, gl.TextureInternalFormat.RGB),
        4: (gl.TextureFormat.RGBA, gl.TextureInternalFormat.RGBA)
    }

    _MIPMAP_FILTERS = [
        gl.TextureFilter.LINEAR_MIPMAP_LINEAR,
        gl.TextureFilter.LINEAR_MIPMAP_NEAREST,
        gl.TextureFilter.NEAREST_MIPMAP_LINEAR,
        gl.TextureFilter.NEAREST_MIPMAP_NEAREST
    ]

    def __init__(self,
                 ctx: gl.Context,
                 target: gl.TextureTarget,
                 image: np.ndarray,
                 format: Optional[gl.TextureFormat] = None,
                 internal_format: Optional[gl.TextureInternalFormat] = None,
                 border_color: np.ndarray = np.array([0, 0, 0, 0], np.float32),
                 min_filter: gl.TextureFilter = gl.TextureFilter.LINEAR,
                 mag_filter: gl.TextureFilter = gl.TextureFilter.LINEAR,
                 ani_filter: float = 16,
                 wrap_s: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_t: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_r: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 swizzle_r: gl.TextureSwizzle = gl.TextureSwizzle.RED,
                 swizzle_g: gl.TextureSwizzle = gl.TextureSwizzle.GREEN,
                 swizzle_b: gl.TextureSwizzle = gl.TextureSwizzle.BLUE,
                 swizzle_a: gl.TextureSwizzle = gl.TextureSwizzle.ALPHA,
                 min_lod: float = -1000,
                 max_lod: float = 1000):

        if not isinstance(image, np.ndarray):
            raise TypeError("Texture image should be of type np.ndarray")
        if not image.dtype in self._TYPE:
            raise ValueError("Texture image dtype '{}' not supported".format(image.dtype))
        if not (len(image.shape) == 3 and image.shape[2] in self._CHANNELS.keys()):
            raise ValueError("Texture image should have shape (width, height, channels), with 1 <= len(channels) <= 4")
        if format is None or internal_format is None:
            format, internal_format = self._CHANNELS[image.shape[2]]
        if target not in self._SETTER:
            raise ValueError("Texture target {} is not currently supported".format(target))

        type = self._TYPE[image.dtype]

        super().__init__(ctx, target, type, format, internal_format, border_color, min_filter, mag_filter, ani_filter,
                         wrap_s, wrap_t, wrap_r, swizzle_r, swizzle_g, swizzle_b, swizzle_a, min_lod, max_lod)

        # Obtain image data type and shape
        self._dtype = image.dtype
        self._shape = image.shape

        # Upload image to GPU
        with self:
            self._SETTER[self.target](self.ctx, self.target, 0, self.internal_format, self.format, self.type, image)

        # TODO: Keep or discard this?
        # Generate Mipmap when appropriate filter is chosen
        with self:
            if self.min_filter in self._MIPMAP_FILTERS:
                self.ctx.generate_mipmap(self.target)

    @property
    def dtype(self) -> np.dtype:
        return self._dtype

    @property
    def shape(self) -> tuple:
        return self._shape

    @property
    def image(self) -> np.ndarray:
        with self:
            return self.ctx.get_texture(self.target, 0, self.format, self.type, self.dtype, self.shape)

    @image.setter
    def image(self, value: np.ndarray):
        raise NotImplementedError()


class Texture1D(ImageTexture):
    def __init__(self,
                 ctx: gl.Context,
                 image: np.ndarray,
                 format: Optional[gl.TextureFormat] = None,
                 internal_format: Optional[gl.TextureInternalFormat] = None,
                 border_color: np.ndarray = np.array([0, 0, 0, 0], np.float32),
                 min_filter: gl.TextureFilter = gl.TextureFilter.LINEAR_MIPMAP_LINEAR,
                 mag_filter: gl.TextureFilter = gl.TextureFilter.LINEAR,
                 ani_filter: float = 16,
                 wrap_s: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_t: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_r: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 swizzle_r: gl.TextureSwizzle = gl.TextureSwizzle.RED,
                 swizzle_g: gl.TextureSwizzle = gl.TextureSwizzle.GREEN,
                 swizzle_b: gl.TextureSwizzle = gl.TextureSwizzle.BLUE,
                 swizzle_a: gl.TextureSwizzle = gl.TextureSwizzle.ALPHA,
                 min_lod: float = -1000,
                 max_lod: float = 1000):

        super().__init__(ctx, gl.TextureTarget.TEXTURE_1D, image,
                         format, internal_format, border_color, min_filter, mag_filter, ani_filter,
                         wrap_s, wrap_t, wrap_r, swizzle_r, swizzle_g, swizzle_b, swizzle_a, min_lod, max_lod)


class Texture2D(ImageTexture):
    def __init__(self,
                 ctx: gl.Context,
                 image: np.ndarray,
                 format: Optional[gl.TextureFormat] = None,
                 internal_format: Optional[gl.TextureInternalFormat] = None,
                 border_color: np.ndarray = np.array([0, 0, 0, 0], np.float32),
                 min_filter: gl.TextureFilter = gl.TextureFilter.LINEAR_MIPMAP_LINEAR,
                 mag_filter: gl.TextureFilter = gl.TextureFilter.LINEAR,
                 ani_filter: float = 16,
                 wrap_s: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_t: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_r: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 swizzle_r: gl.TextureSwizzle = gl.TextureSwizzle.RED,
                 swizzle_g: gl.TextureSwizzle = gl.TextureSwizzle.GREEN,
                 swizzle_b: gl.TextureSwizzle = gl.TextureSwizzle.BLUE,
                 swizzle_a: gl.TextureSwizzle = gl.TextureSwizzle.ALPHA,
                 min_lod: float = -1000,
                 max_lod: float = 1000):

        super().__init__(ctx, gl.TextureTarget.TEXTURE_2D, image,
                         format, internal_format, border_color, min_filter, mag_filter, ani_filter,
                         wrap_s, wrap_t, wrap_r, swizzle_r, swizzle_g, swizzle_b, swizzle_a, min_lod, max_lod)


class Texture3D(ImageTexture):
    def __init__(self,
                 ctx: gl.Context,
                 image: np.ndarray,
                 format: Optional[gl.TextureFormat] = None,
                 internal_format: Optional[gl.TextureInternalFormat] = None,
                 border_color: np.ndarray = np.array([0, 0, 0, 0], np.float32),
                 min_filter: gl.TextureFilter = gl.TextureFilter.LINEAR_MIPMAP_LINEAR,
                 mag_filter: gl.TextureFilter = gl.TextureFilter.LINEAR,
                 ani_filter: float = 16,
                 wrap_s: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_t: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 wrap_r: gl.TextureWrap = gl.TextureWrap.REPEAT,
                 swizzle_r: gl.TextureSwizzle = gl.TextureSwizzle.RED,
                 swizzle_g: gl.TextureSwizzle = gl.TextureSwizzle.GREEN,
                 swizzle_b: gl.TextureSwizzle = gl.TextureSwizzle.BLUE,
                 swizzle_a: gl.TextureSwizzle = gl.TextureSwizzle.ALPHA,
                 min_lod: float = -1000,
                 max_lod: float = 1000):

        super().__init__(ctx, gl.TextureTarget.TEXTURE_3D, image,
                         format, internal_format, border_color, min_filter, mag_filter, ani_filter,
                         wrap_s, wrap_t, wrap_r, swizzle_r, swizzle_g, swizzle_b, swizzle_a, min_lod, max_lod)
