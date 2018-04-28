from pyplex import gl
from pyplex.glow.shader import Shader
from pyplex.glow.buffer import *
from pyplex.glow.type import BASE_TYPE
from ctypes import *


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
    def __init__(self, ctx: gl.GL_ANY, *shaders: Shader):
        self._ctx = ctx

        self._ptr = self._ctx.create_program()
        self._vao = VertexArray(self._ctx)

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

        print(index, location)

        resource_type = c_int(0)
        self._ctx.get_program_resourceiv(
            self._ptr, gl.Interface.PROGRAM_INPUT, index, 1,
            pointer(c_uint(gl.ResourceParameter.TYPE)), 1, None, pointer(resource_type))

        with buffer, self._vao:
            self._ctx.vertex_attrib_pointer(
                location, buffer.shape[-1], BASE_TYPE[resource_type.value], False, 0, c_void_p(0))
            self._ctx.enable_vertex_attrib_array(location)

    def draw(self, mode: gl.DrawMode, start: int, count: int):
        self._ctx.use_program(self._ptr)
        with self._vao: self._ctx.draw_arrays(mode, start, count)
        self._ctx.use_program(0)

    def log(self):
        log_length = self._parameter(gl.ProgramParameter.INFO_LOG_LENGTH)
        result = bytes(log_length)
        self._ctx.get_program_info_log(self._ptr, log_length, None, result)
        return result.decode()

    def _parameter(self, parameter: gl.ProgramParameter) -> int:
        result = c_int(0)
        self._ctx.get_programiv(self._ptr, parameter, pointer(result))
        return result.value
