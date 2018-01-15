from ctypes import c_uint


class Object(c_uint):
    """OpenGL Object (c_uint)"""

    def __str__(self):
        return "{}[{}]".format(self.__class__.__name__, self.value)


class Shader(Object):
    """OpenGL Shader Object (c_uint)"""
    pass


class Program(Object):
    """OpenGL Program Object (c_uint)"""
    pass


class Buffer(Object):
    """OpenGL Buffer Object (c_uint)"""
    pass


class VertexArray(Object):
    """OpenGL VertexArray Object (c_uint)"""
    pass


class Sampler(Object):
    """OpenGL Sampler Object (c_uint)"""
    pass


class Texture(Object):
    """OpenGL Texture Object (c_uint)"""
    pass