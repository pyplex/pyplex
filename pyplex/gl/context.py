from .constant import *
from .object import *
from ctypes import *

import numpy as np

from typing import Optional, List, Union


class ContextError(Exception):
    """Context Error"""
    pass


class Context:

    # Transpose Matrices sent to GL, reflecting row/column-major ordering on host system vs GPU
    TRANSPOSE_MATRICES = True

    def __init__(self):
        """OpenGL Context & Loader"""

        # Function Dictionary filled with loaded functions
        self._functions = {}

        # Windows
        self._dll = cdll.opengl32
        self._dll.wglGetProcAddress.restype = CFUNCTYPE(POINTER(c_int))
        self._dll.wglGetProcAddress.argtypes = [c_char_p]

        ## ..:: Function Loading ::.. ##
        # Errors
        self.load("glGetError", c_int)

        # State Requests
        self.load("glGetInteger64v", c_void_p, c_int, POINTER(c_int64))

        # Clear
        self.load("glClear", c_void_p, c_uint)
        self.load("glClearColor", c_void_p, c_float, c_float, c_float, c_float)

        # Viewport
        self.load("glViewport", c_void_p, c_int, c_int, c_uint, c_uint)

        # Shader
        self.load("glCreateShader", c_uint, c_uint)
        self.load("glDeleteShader", c_void_p, c_uint)
        self.load("glIsShader", c_bool, c_uint)
        self.load("glShaderSource", c_void_p, c_uint, c_uint, POINTER(c_char_p), POINTER(c_int))
        self.load('glCompileShader', c_void_p, c_uint)
        self.load('glReleaseShaderCompiler', c_void_p, c_void_p)
        self.load("glGetShaderiv", c_void_p, c_uint, c_uint, POINTER(c_int))
        self.load("glGetShaderInfoLog", c_void_p, c_uint, c_uint, POINTER(c_uint), c_char_p)

        # Program
        self.load("glCreateProgram", c_uint)
        self.load("glDeleteProgram", c_void_p, c_uint)
        self.load("glIsProgram", c_bool, c_uint)
        self.load("glAttachShader", c_void_p, c_uint, c_uint)
        self.load("glDetachShader", c_void_p, c_uint, c_uint)
        self.load("glLinkProgram", c_void_p, c_uint)
        self.load("glUseProgram", c_void_p, c_uint)
        self.load("glGetProgramiv", c_void_p, c_uint, c_uint, POINTER(c_int))
        self.load("glGetProgramInfoLog", c_void_p, c_uint, c_uint, POINTER(c_uint), c_char_p)

        # Program Interface & Resource
        self.load("glGetProgramInterfaceiv", c_void_p, c_uint, c_uint, c_uint, POINTER(c_int))
        self.load("glGetProgramResourceName", c_void_p, c_uint, c_uint, c_uint, c_uint, POINTER(c_uint), c_char_p)
        self.load("glGetProgramResourceIndex", c_uint, c_uint, c_uint, c_char_p)
        self.load("glGetProgramResourceLocation", c_int, c_uint, c_uint, c_char_p)
        self.load("glGetProgramResourceiv", c_void_p, c_uint, c_uint, c_uint, c_uint,
                  POINTER(c_uint), c_uint, POINTER(c_uint), POINTER(c_int))

        # Buffer
        self.load("glGenBuffers", c_void_p, c_uint, POINTER(c_uint))
        self.load("glDeleteBuffers", c_void_p, c_uint, POINTER(c_uint))
        self.load("glIsBuffer", c_bool, c_uint)
        self.load("glBindBuffer", c_void_p, c_uint, c_uint)
        self.load("glBufferData", c_void_p, c_uint, c_uint, c_void_p, c_uint)
        self.load("glBufferSubData", c_void_p, c_uint, c_uint, c_uint, c_void_p)
        self.load("glGetBufferSubData", c_void_p, c_uint, c_uint, c_uint, c_void_p)
        self.load("glGetBufferParameteriv", c_void_p, c_uint, c_uint, POINTER(c_int))

        # Uniform (Single Values)
        self.load("glProgramUniform1i", c_void_p, c_uint, c_int, c_int)
        self.load("glProgramUniform2i", c_void_p, c_uint, c_int, c_int, c_int)
        self.load("glProgramUniform3i", c_void_p, c_uint, c_int, c_int, c_int, c_int)
        self.load("glProgramUniform4i", c_void_p, c_uint, c_int, c_int, c_int, c_int, c_int)
        
        self.load("glProgramUniform1ui", c_void_p, c_uint, c_int, c_uint)
        self.load("glProgramUniform2ui", c_void_p, c_uint, c_int, c_uint, c_uint)
        self.load("glProgramUniform3ui", c_void_p, c_uint, c_int, c_uint, c_uint, c_uint)
        self.load("glProgramUniform4ui", c_void_p, c_uint, c_int, c_uint, c_uint, c_uint, c_uint)

        self.load("glProgramUniform1f", c_void_p, c_uint, c_int, c_float)
        self.load("glProgramUniform2f", c_void_p, c_uint, c_int, c_float, c_float)
        self.load("glProgramUniform3f", c_void_p, c_uint, c_int, c_float, c_float, c_float)
        self.load("glProgramUniform4f", c_void_p, c_uint, c_int, c_float, c_float, c_float, c_float)
        
        self.load("glProgramUniform1d", c_void_p, c_uint, c_int, c_double)
        self.load("glProgramUniform2d", c_void_p, c_uint, c_int, c_double, c_double)
        self.load("glProgramUniform3d", c_void_p, c_uint, c_int, c_double, c_double, c_double)
        self.load("glProgramUniform4d", c_void_p, c_uint, c_int, c_double, c_double, c_double, c_double)

        # Uniform (Arrays)
        self.load("glProgramUniform1iv", c_void_p, c_uint, c_int, c_uint, POINTER(c_int))
        self.load("glProgramUniform2iv", c_void_p, c_uint, c_int, c_uint, POINTER(c_int))
        self.load("glProgramUniform3iv", c_void_p, c_uint, c_int, c_uint, POINTER(c_int))
        self.load("glProgramUniform4iv", c_void_p, c_uint, c_int, c_uint, POINTER(c_int))

        self.load("glProgramUniform1uiv", c_void_p, c_uint, c_int, c_uint, POINTER(c_uint))
        self.load("glProgramUniform2uiv", c_void_p, c_uint, c_int, c_uint, POINTER(c_uint))
        self.load("glProgramUniform3uiv", c_void_p, c_uint, c_int, c_uint, POINTER(c_uint))
        self.load("glProgramUniform4uiv", c_void_p, c_uint, c_int, c_uint, POINTER(c_uint))
        
        self.load("glProgramUniform1fv", c_void_p, c_uint, c_int, c_uint, POINTER(c_float))
        self.load("glProgramUniform2fv", c_void_p, c_uint, c_int, c_uint, POINTER(c_float))
        self.load("glProgramUniform3fv", c_void_p, c_uint, c_int, c_uint, POINTER(c_float))
        self.load("glProgramUniform4fv", c_void_p, c_uint, c_int, c_uint, POINTER(c_float))
        
        self.load("glProgramUniform1dv", c_void_p, c_uint, c_int, c_uint, POINTER(c_double))
        self.load("glProgramUniform2dv", c_void_p, c_uint, c_int, c_uint, POINTER(c_double))
        self.load("glProgramUniform3dv", c_void_p, c_uint, c_int, c_uint, POINTER(c_double))
        self.load("glProgramUniform4dv", c_void_p, c_uint, c_int, c_uint, POINTER(c_double))

        # Uniform (Matrices)
        self.load("glProgramUniformMatrix2fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix3fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix4fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix2x3fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix3x2fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix2x4fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix4x2fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix3x4fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        self.load("glProgramUniformMatrix4x3fv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_float))
        
        self.load("glProgramUniformMatrix2dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix3dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix4dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix2x3dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix3x2dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix2x4dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix4x2dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix3x4dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))
        self.load("glProgramUniformMatrix4x3dv", c_void_p, c_uint, c_int, c_uint, c_bool, POINTER(c_double))

        # VertexArray
        self.load("glGenVertexArrays", c_void_p, c_uint, POINTER(c_uint))
        self.load("glDeleteVertexArrays", c_void_p, c_uint, POINTER(c_uint))
        self.load("glIsVertexArray", c_bool, c_uint)
        self.load("glBindVertexArray", c_void_p, c_uint)

        # Draw Commands
        self.load("glDrawArrays", c_void_p, c_uint, c_uint, c_uint)
        self.load("glDrawElements", c_void_p, c_uint, c_uint, c_uint, c_void_p)

        # Vertex Attribute
        self.load("glVertexAttribPointer", c_void_p, c_uint, c_int, c_uint, c_bool, c_uint, c_void_p)
        self.load("glEnableVertexAttribArray", c_void_p, c_uint)

        # Sampler
        self.load("glGenSamplers", c_void_p, c_uint, POINTER(c_uint))
        self.load("glBindSampler", c_void_p, c_uint, c_uint)
        self.load("glDeleteSamplers", c_void_p, c_uint, POINTER(c_uint))
        self.load("glIsSampler", c_bool, c_uint)
        self.load("glSamplerParameteri", c_void_p, c_uint, c_uint, c_int)
        self.load("glSamplerParameterf", c_void_p, c_uint, c_uint, c_float)

        # Texturing
        self.load("glGenTextures", c_void_p, c_uint, POINTER(c_uint))
        self.load("glBindTexture", c_void_p, c_int, c_uint)
        self.load("glDeleteTextures", c_void_p, c_uint, POINTER(c_uint))
        self.load("glIsTexture", c_bool, c_uint)
        self.load("glActiveTexture", c_void_p, c_int)
        self.load("glTexImage1D", c_void_p, c_int, c_int, c_int, c_uint, c_int, c_int, c_int, c_void_p)
        self.load("glTexImage2D", c_void_p, c_int, c_int, c_int, c_uint, c_uint, c_int, c_int, c_int, c_void_p)
        self.load("glTexImage3D", c_void_p, c_int, c_int, c_int, c_uint, c_uint, c_uint, c_int, c_int, c_int, c_void_p)
        self.load("glCopyTexImage1D", c_void_p, c_int, c_int, c_int, c_int, c_int, c_uint, c_int)
        self.load("glCopyTexImage2D", c_void_p, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_int)
        self.load("glGetTexImage", c_void_p, c_int, c_int, c_int, c_int, c_void_p)
        self.load("glGenerateMipmap", c_void_p, c_uint)
        self.load("glTexParameteri", c_void_p, c_int, c_int, c_int)
        self.load("glTexParameterf", c_void_p, c_int, c_int, c_float)
        self.load("glTexParameterfv", c_void_p, c_int, c_int, POINTER(c_float))


    ## ..:: Function Bindings ::.. ##
    # Error
    def error(self) -> int:
        return self.glGetError()

    # State Requests
    def get_int(self, parameter: StateParameter) -> int:
        value = c_int64(0)
        value_ptr = pointer(value)
        self.glGetInteger64v(parameter, value_ptr)
        return value.value

    # Clear
    def clear(self, color: bool = True, depth: bool = True, stencil: bool = True):
        """
        Clear Framebuffer

        Parameters
        ----------
        color: bool
            Clear Color Buffer
        depth: bool
            Clear Depth Buffer
        stencil: bool
            Clear Stencil Buffer
        """
        self.glClear(BufferBit.COLOR * color | BufferBit.DEPTH * depth | BufferBit.STENCIL * stencil)

    def clear_color(self, rgba: np.ndarray):
        """
        Set Framebuffer Clear Color

        Parameters
        ----------
        rgba: np.ndarray
            Red, Green, Blue and Alpha Component
        """
        self.glClearColor(*rgba)

    # Viewport
    def viewport(self, size: np.ndarray):
        """
        Set Viewport Size (w,h)

        Parameters
        ----------
        size: np.ndarray
            Viewport Size (w.h)
        """
        self.glViewport(0, 0, *size)

    # Shader
    def create_shader(self, shader_type: ShaderType) -> Shader:
        return Shader(self.glCreateShader(shader_type))

    def delete_shader(self, shader: Shader):
        self.glDeleteShader(shader)

    def is_shader(self, shader: Shader) -> bool:
        return self.glIsShader(shader)

    def shader_source(self, shader: Shader, source: str):
        buffer = pointer(c_char_p(source.encode()))
        length = pointer(c_int(len(source)))
        self.glShaderSource(shader, 1, buffer, length)

    def compile_shader(self, shader: Shader):
        self.glCompileShader(shader)

    def release_shader_compiler(self):
        self.glReleaseShaderCompiler()

    def shader_parameter(self, shader: Shader, parameter: ShaderParameter) -> int:
        result = c_int(0)
        result_ptr = pointer(result)
        self.glGetShaderiv(shader, parameter, result_ptr)
        return result.value

    def shader_info_log(self, shader: Shader) -> str:
        log_length = self.shader_parameter(shader, ShaderParameter.INFO_LOG_LENGTH)
        result = create_string_buffer(b"", size=log_length)
        self.glGetShaderInfoLog(shader, log_length, pointer(c_uint()), result)
        return result.value.decode()

    # Program
    def create_program(self) -> Program:
        return Program(self.glCreateProgram())

    def delete_program(self, program: Program):
        self.glDeleteProgram(program)

    def is_program(self, program: Program) -> bool:
        return self.glIsProgram(program)

    def attach_shader(self, program: Program, shader: Shader):
        self.glAttachShader(program, shader)

    def detach_shader(self, program: Program, shader: Shader):
        self.glDetachShader(program, shader)

    def link_program(self, program: Program):
        self.glLinkProgram(program)

    def use_program(self, program: Optional[Program]):
        self.glUseProgram(program if program else 0)

    def program_parameter(self, program: Program, parameter: ProgramParameter) -> int:
        result = c_int(0)
        result_ptr = pointer(result)
        self.glGetProgramiv(program, parameter, result_ptr)
        return result.value

    def program_info_log(self, program: Program) -> str:
        log_length = self.program_parameter(program, ProgramParameter.INFO_LOG_LENGTH)
        result = create_string_buffer(b"", size=log_length)
        self.glGetProgramInfoLog(program, log_length, pointer(c_uint()), result)
        return result.value.decode()

    # Program Interface
    def interface_parameter(self, program: Program, interface: Interface, parameter: InterfaceParameter) -> int:
        result = c_int(0)
        result_ptr = pointer(result)
        self.glGetProgramInterfaceiv(program, interface, parameter, result_ptr)
        return result.value

    def resource_name(self, program: Program, interface: Interface, index: int) -> str:
        buffer_size = self.interface_parameter(program, interface, InterfaceParameter.MAX_NAME_LENGTH)
        name = create_string_buffer(b"", size=buffer_size)
        self.glGetProgramResourceName(program, interface, index, buffer_size, pointer(c_uint()), name)
        return name.value.decode()

    def resource_index(self, program: Program, interface: Interface, name: str) -> int:
        return self.glGetProgramResourceIndex(program, interface, name.encode())

    def resource_location(self, program: Program, interface: Interface, name: str) -> int:
        return self.glGetProgramResourceLocation(program, interface, name.encode())

    def resource_parameter(self, program: Program, interface: Interface, index: int,
                           *parameters: ResourceParameter) -> List[int]:
        properties = (c_uint * len(parameters))(*parameters)
        values = (c_int * len(parameters))()

        self.glGetProgramResourceiv(program, interface, index, len(parameters), properties,
                                    len(parameters), pointer(c_uint()), values)

        return [int(values[i]) for i in range(len(parameters))]

    # Buffer
    def create_buffer(self) -> Buffer:
        buffer = Buffer(0)
        self.glGenBuffers(1, pointer(buffer))
        return buffer

    def delete_buffer(self, buffer: Buffer):
        self.glDeleteBuffers(1, pointer(buffer))

    def is_buffer(self, buffer: Buffer) -> bool:
        return self.glIsBuffer(buffer)

    def bind_buffer(self, target: BufferTarget, buffer: Optional[Buffer]):
        self.glBindBuffer(target, buffer if buffer else 0)

    def buffer_data(self, target: BufferTarget, data: np.ndarray, usage: BufferUsage):
        self.glBufferData(target, data.nbytes, data.ctypes.data_as(c_void_p), usage)

    def buffer_sub_data(self, target: BufferTarget, offset: int, data: np.ndarray):
        self.glBufferSubData(target, offset, data.nbytes, data.ctypes.data_as(c_void_p))

    def get_buffer_sub_data(self, target: BufferTarget, offset: int, size: int) -> np.ndarray:
        data = (c_uint8 * size)()
        self.glGetBufferSubData(target, offset, size, pointer(data))
        return np.ctypeslib.as_array(data)

    def buffer_parameter(self, target: BufferTarget, parameter: BufferParameter):
        data = c_int(0)
        data_ptr = pointer(data)
        self.glGetBufferParameteriv(target, parameter, data_ptr)
        return data.value

    # Uniform (Single Values)
    # TODO: Double Union Import (ctypes, typing) -> add typing.Union at all uniform_1*
    def uniform_1i(self, program: Program, location: int, value: Union[np.ndarray, int]):
        self.glProgramUniform1i(program, location, value)

    def uniform_2i(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform2i(program, location, *value)

    def uniform_3i(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3i(program, location, *value)

    def uniform_4i(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4i(program, location, *value)

    def uniform_1ui(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform1ui(program, location, value)

    def uniform_2ui(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUnifor2ui(program, location, *value)

    def uniform_3ui(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3ui(program, location, *value)

    def uniform_4ui(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4ui(program, location, *value)


    def uniform_1f(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform1f(program, location, *value)

    def uniform_2f(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform2f(program, location, *value)

    def uniform_3f(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3f(program, location, *value)

    def uniform_4f(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4f(program, location, *value)


    def uniform_1d(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform1d(program, location, *value)

    def uniform_2d(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform2d(program, location, *value)

    def uniform_3d(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3d(program, location, *value)

    def uniform_4d(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4d(program, location, *value)

    # Uniform (Array)
    def uniform_1iv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform1iv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_int)))

    def uniform_2iv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform2iv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_int)))

    def uniform_3iv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3iv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_int)))

    def uniform_4iv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4iv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_int)))


    def uniform_1uiv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform1uiv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_uint)))

    def uniform_2uiv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform2uiv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_uint)))

    def uniform_3uiv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3uiv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_uint)))

    def uniform_4uiv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4uiv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_uint)))


    def uniform_1fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform1fv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_float)))

    def uniform_2fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform2fv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_float)))

    def uniform_3fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3fv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_float)))

    def uniform_4fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4fv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_float)))


    def uniform_1dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform1dv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_double)))

    def uniform_2dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform2dv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_double)))

    def uniform_3dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform3dv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_double)))

    def uniform_4dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniform4dv(program, location, value.shape[0], value.ctypes.data_as(POINTER(c_double)))

    # Uniform Matrices
    def uniform_matrix_2fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix2fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                       value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_3fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix3fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                       value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_4fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix4fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                       value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_2x3fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix2x3fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_3x2fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix3x2fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_2x4fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix2x4fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_4x2fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix4x2fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_3x4fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix3x4fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_float)))

    def uniform_matrix_4x3fv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix4x3fv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_float)))
        
        
    def uniform_matrix_2dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix2dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                       value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_3dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix3dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                       value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_4dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix2dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                       value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_2x3dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix2x3dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_3x2dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix3x2dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_2x4dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix2x4dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_4x2dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix4x2dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_3x4dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix3x4dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_double)))

    def uniform_matrix_4x3dv(self, program: Program, location: int, value: np.ndarray):
        self.glProgramUniformMatrix4x3dv(program, location, value.shape[0], self.TRANSPOSE_MATRICES,
                                         value.ctypes.data_as(POINTER(c_double)))

    # Vertex Array
    def create_vertex_array(self) -> VertexArray:
        array = VertexArray(0)
        self.glGenVertexArrays(1, pointer(array))
        return array

    def delete_vertex_array(self, array: VertexArray):
        self.glDeleteVertexArrays(1, pointer(array))

    def is_vertex_array(self, array: VertexArray) -> bool:
        return self.glIsVertexArray(array)

    def bind_vertex_array(self, array: Optional[VertexArray]):
        self.glBindVertexArray(array if array else 0)

    # Draw Commands
    def draw_arrays(self, mode: DrawMode, first: int, count: int):
        self.glDrawArrays(mode, first, count)

    def draw_elements(self, mode: DrawMode, count: int, type: Type, indices: int):
        self.glDrawElements(mode, count, type, cast(indices, c_void_p))

    # Vertex Attribute
    def vertex_attribute_pointer(self, index: int, size: int, type: Type, normalised: bool, stride: int, offset: int):
        self.glVertexAttribPointer(index, size, type, normalised, stride, cast(offset, c_void_p))

    def enable_vertex_attribute_array(self, index: int):
        self.glEnableVertexAttribArray(index)

    # Samplers
    def create_sampler(self) -> Sampler:
        sampler = Sampler(0)
        self.glGenSamplers(1, pointer(sampler))
        return sampler

    def delete_sampler(self, sampler: Sampler):
        self.glDeleteSamplers(1, pointer(sampler))

    def is_sampler(self, sampler: Sampler) -> bool:
        return self.glIsSapler(sampler)

    def bind_sampler(self, unit: TextureUnit, sampler: Optional[Sampler]):
        self.glBindSampler(unit, sampler if sampler else 0)

    def sampler_parameter(self, sampler: Sampler, parameter: SamplerParameter, value: Union[int, float]):
        if isinstance(value, int):
            self.glSamplerParameteri(sampler, parameter, value)
        elif isinstance(value, float):
            self.glSamplerParamterf(sampler, parameter, value)

    # Texturing
    def create_texture(self) -> Texture:
        texture = Texture(0)
        self.glGenTextures(1, texture)
        return texture

    def delete_texture(self, texture: Texture):
        self.glDeleteTextures(1, pointer(texture))

    def is_texture(self, texture: Texture):
        return self.glIsTexture(texture)

    def bind_texture(self, target: TextureTarget, texture: Optional[Texture]):
        self.glBindTexture(target, texture if texture else 0)

    def active_texture(self, unit: Union[TextureUnit, int]):
        self.glActiveTexture(unit)

    def texture_image_1D(self, target: TextureTarget, level: int, internal_format: TextureInternalFormat,
                         format: TextureFormat, type: TextureType, data: np.ndarray):
        self.glTexImage1D(target, level, internal_format, data.shape[0], 0, format, type,
                          data.ctypes.data_as(c_void_p))

    def texture_image_2D(self, target: TextureTarget, level: int, internal_format: TextureInternalFormat,
                         format: TextureFormat, type: TextureType, data: np.ndarray):
        self.glTexImage2D(target, level, internal_format, data.shape[0], data.shape[1], 0, format, type,
                          data.ctypes.data_as(c_void_p))

    def texture_image_3D(self, target: TextureTarget, level: int, internal_format: TextureInternalFormat,
                         format: TextureFormat, type: TextureType, data: np.ndarray):
        self.glTexImage3D(target, level, internal_format, data.shape[0], data.shape[1], data.shape[2], 0, format, type,
                          data.ctypes.data_as(c_void_p))

    def texture_copy_1D(self, target: TextureTarget, level: int, internal_format: TextureInternalFormat,
                        format: TextureFormat, x: int, y: int, width: int):
        self.glCopyTexImage2D(target, level, internal_format, x, y, width, 0)

    def texture_copy_2D(self, target: TextureTarget, level: int, internal_format: TextureInternalFormat,
                        format: TextureFormat, x: int, y: int, width: int, height: int):
        self.glCopyTexImage2D(target, level, internal_format, x, y, width, height, 0)

    def get_texture(self, target: TextureTarget, level: int, format: TextureFormat, type: TextureType, dtype: np.dtype, shape: tuple) -> np.ndarray:
        data = (c_uint8 * np.prod(shape) * dtype.itemsize)()
        data_ptr = pointer(data)
        self.glGetTexImage(target, level, format, type, data_ptr)
        return np.ctypeslib.as_array(data).view(dtype).reshape(shape)

    def texture_parameter(self, target: TextureTarget, parameter: TextureParameter, value: Union[int, float, np.ndarray]):
        if isinstance(value, int):
            self.glTexParameteri(target, parameter, value)
        elif isinstance(value, float):
            self.glTexParameterf(target, parameter, value)
        elif isinstance(value, np.ndarray):
            self.glTexParameterfv(target, parameter, value.ctypes.data_as(POINTER(c_float)))

    def generate_mipmap(self, target: TextureTarget):
        self.glGenerateMipmap(target)

    # Function Loading
    def load(self, function_name: str, return_type, *argument_types) -> CFUNCTYPE:
        """
        Load OpenGL function

        Parameters
        ----------
        function_name: str
            Name of Function
        return_type
            Ctypes Return Type
        argument_types
            Ctypes Argument Types
        Returns
        -------
        function_handle: CFUNCTYPE
        """

        # Try loading functions directly from dll
        # This is the case for Mac and OpenGL 1.1 functions on Windows
        if hasattr(self._dll, function_name):
            function_handle = getattr(self._dll, function_name)
            function_handle.restype = return_type
            function_handle.argtypes = argument_types
            self._functions[function_name] = function_handle
            return function_handle

        # Windows: Get address of functions, using wglGetProcAddress function
        function_address = self._dll.wglGetProcAddress(function_name.encode())

        if not function_address:
            raise ContextError("Function '{}' does not exist in current context".format(function_name))

        function_type = CFUNCTYPE(return_type, *argument_types)
        function_handle = cast(function_address, function_type)
        self._functions[function_name] = function_handle
        return function_handle

    def __getattr__(self, function_name: str) -> CFUNCTYPE:
        """
        Get Loaded Function

        Parameters
        ----------
        function_name: str

        Returns
        -------
        function: CFUNCTYPE
        """
        function_handle = self._functions.get(function_name, None)
        if function_handle: return function_handle
        else: raise ContextError("Function '{}' is not loaded in current context".format(function_name))
