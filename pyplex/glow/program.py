from pyplex import gl
from pyplex.glow.shader import Shader
from pyplex.glow.buffer import ArrayBuffer
from pyplex.glow.texture import Texture
from pyplex.glow.type import Type
import numpy as np
from ctypes import *

from typing import List


class LinkError(Exception):
    pass


class VertexArray:
    def __init__(self, ctx: gl.GL30):
        self._ctx = ctx

        self._ptr = c_uint(0)
        self._ctx.gen_vertex_arrays(1, pointer(self._ptr))
        self._ptr = self._ptr.value

    @property
    def ptr(self) -> int:
        return self._ptr

    def bind(self):
        self._ctx.bind_vertex_array(self._ptr)

    def unbind(self):
        self._ctx.bind_vertex_array(0)

    def delete(self):
        self._ctx.delete_vertex_arrays(1, pointer(self._ptr))

    def __enter__(self):
        self._ctx.bind_vertex_array(self._ptr)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._ctx.bind_vertex_array(0)


class Program:
    def __init__(self, ctx: gl.GL43, *shaders: Shader):
        self._ctx = ctx

        self._ptr = self._ctx.create_program()
        self._vao = VertexArray(self._ctx)
        self._textures = {}

        for shader in shaders:
            self._ctx.attach_shader(self._ptr, shader.ptr)
        self._ctx.link_program(self._ptr)

        if not self._parameter(gl.ProgramParameter.LINK_STATUS):
            raise LinkError(self.log())

    @property
    def ptr(self) -> int:
        return self._ptr

    def input(self, name: str, buffer: ArrayBuffer):
        index = self._ctx.get_program_resource_index(self._ptr, gl.Interface.PROGRAM_INPUT, name.encode())
        location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.PROGRAM_INPUT, name.encode())

        t = Type(self._resource_parameters(gl.Interface.PROGRAM_INPUT, index, gl.ResourceParameter.TYPE)[0])

        with buffer, self._vao:
            self._ctx.vertex_attrib_pointer(location, t.count, t.gl_base, False, 0, c_void_p(0))
            self._ctx.enable_vertex_attrib_array(location)

    def uniform(self, name: str, value: np.ndarray):
        index = self._ctx.get_program_resource_index(self._ptr, gl.Interface.UNIFORM, name.encode())
        location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.UNIFORM, name.encode())

        t = Type(self._resource_parameters(gl.Interface.UNIFORM, index, gl.ResourceParameter.TYPE)[0])

        func = self._ctx.__getattribute__(t.uniform_func.__name__)
        func(self._ptr, location, int(value.nbytes / t.nbytes), value.ctypes.data_as(POINTER(t.ctypes)))

    def texture(self, name: str, texture: Texture):
        if not name in self._textures:
            unit = len(self._textures) + gl.TextureUnit.TEXTURE0
            self._textures[name] = (texture, unit)

        location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.UNIFORM, name.encode())
        self._ctx.program_uniform_1i(self._ptr, location, self._textures[name][1] - gl.TextureUnit.TEXTURE0)

    def draw(self, mode: gl.DrawMode, start: int, count: int):
        self.bind()
        self._ctx.draw_arrays(mode, start, count)
        self.unbind()

    def log(self):
        log_length = self._parameter(gl.ProgramParameter.INFO_LOG_LENGTH)
        result = bytes(log_length)
        self._ctx.get_program_info_log(self._ptr, log_length, None, result)
        return result.decode()

    def bind(self):
        self._ctx.use_program(self._ptr)
        self._vao.bind()

        for texture, unit in self._textures.values():
            self._ctx.active_texture(unit)
            self._ctx.bind_texture(texture.target, texture.ptr)

    def unbind(self):
        self._ctx.use_program(0)
        self._vao.unbind()

        for texture, unit in self._textures.values():
            self._ctx.active_texture(unit)
            self._ctx.bind_texture(texture.target, 0)

    def _parameter(self, parameter: gl.ProgramParameter) -> int:
        result = c_int(0)
        self._ctx.get_programiv(self._ptr, parameter, pointer(result))
        return result.value

    def _resource_parameters(self, interface: gl.Interface, index: int, *properties: gl.ResourceParameter) -> List[int]:
        num = len(properties)
        props = (c_uint32 * len(properties))()
        for i, prop in enumerate(properties): props[i] = c_uint32(prop)

        results = (c_int * len(properties))()

        self._ctx.get_program_resourceiv(
            self._ptr, interface, index,    # Where to Look
            num, props,                     # What to Query
            num, None, results)    # Return

        return [results[i] for i in range(num)]

