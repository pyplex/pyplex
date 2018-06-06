from pyplex import gl
from pyplex.glow.shader import Shader, VertexShader, FragmentShader, GeometryShader, TessEvaluationShader, TessControlShader, ComputeShader
from pyplex.glow.buffer import ArrayBuffer, UniformBuffer, ElementArrayBuffer
from pyplex.glow.vertexarray import VertexArray
from pyplex.glow.texture import Texture
from pyplex.glow.type import Type
from pyplex.glow import abstract
import numpy as np
from ctypes import *

from typing import List, Union, Dict, Iterable, Optional


class LinkError(Exception):
    pass


class Program(abstract.BindableObject):

    TRANSPOSE_MATRICES = False

    def __init__(self, ctx: gl.GL43, *shaders: Shader):
        self._ctx = ctx
        self._ptr = self._ctx.create_program()

        for shader in shaders:
            self._ctx.attach_shader(self._ptr, shader.ptr)
        self._ctx.link_program(self._ptr)

        if not self._parameter(gl.ProgramParameter.LINK_STATUS):
            raise LinkError(self.log())

        self._input_interface = InputInterface(ctx, self)
        self._output_interface = OutputInterface(ctx, self)
        self._uniform_interface = UniformInterface(ctx, self)

        self._textures = {}
        self._uniform_buffers = {}

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def input_interface(self):
        return self._input_interface

    @property
    def output_interface(self):
        return self._output_interface

    @property
    def uniform_interface(self):
        return self._uniform_interface

    def uniform(self, name: str, value: np.ndarray):
        resource = self._uniform_interface.resources.get(name)

        if resource:
            if resource.is_matrix:
                resource.setter(self._ptr, resource.location, value.nbytes // resource.type.nbytes,
                                self.TRANSPOSE_MATRICES, value.ctypes.data_as(POINTER(resource.type.ctypes)))
            else:
                resource.setter(self._ptr, resource.location, value.nbytes // resource.type.nbytes,
                                value.ctypes.data_as(POINTER(resource.type.ctypes)))
        else:
            print("WARNING: {} is not an active uniform".format(name))

    def uniform_block(self, name: str, buffer: UniformBuffer):
        if not name in self._uniform_buffers:
            self._uniform_buffers[name] = len(self._uniform_buffers)
        binding = self._uniform_buffers[name]

        index = self._ctx.get_uniform_block_index(self._ptr, name.encode())

        if index != gl.Error.INVALID_INDEX:
            self._ctx.uniform_block_binding(self._ptr, index, binding)
            self._ctx.bind_buffer_base(buffer.target, binding, buffer.ptr)
        else:
            print("WARNING: {} is not an active uniform block".format(name))

    def texture(self, name: str, texture: Texture):
        if not name in self._textures:
            unit = len(self._textures) + gl.TextureUnit.TEXTURE0
            self._textures[name] = (texture, unit)

        location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.UNIFORM, name.encode())
        self._ctx.program_uniform_1i(self._ptr, location, self._textures[name][1] - gl.TextureUnit.TEXTURE0)

    def draw_arrays(self, vao: VertexArray, mode: gl.Primitive, start: int, count: int):
        with self, vao: self._ctx.draw_arrays(mode, start, count)

    def draw_elements(self, vao: VertexArray, mode: gl.Primitive, indices: ElementArrayBuffer):
        gl_type = Type.from_np((), indices.dtype).gl_type
        with self, vao, indices: self._ctx.draw_elements(mode, indices.size, gl_type, c_void_p(0))

    def log(self):
        log_length = self._parameter(gl.ProgramParameter.INFO_LOG_LENGTH)
        result = bytes(log_length)
        self._ctx.get_program_info_log(self._ptr, log_length, None, result)
        return result.decode()

    def bind(self):
        self._ctx.use_program(self._ptr)

        for texture, unit in self._textures.values():
            self._ctx.active_texture(unit)
            self._ctx.bind_texture(texture.target, texture.ptr)

    def unbind(self):
        self._ctx.use_program(0)

        for texture, unit in self._textures.values():
            self._ctx.active_texture(unit)
            self._ctx.bind_texture(texture.target, 0)

    def _parameter(self, parameter: gl.ProgramParameter) -> int:
        result = c_int(0)
        self._ctx.get_programiv(self._ptr, parameter, pointer(result))
        return result.value

    def __setitem__(self, name: str, value: Union[ArrayBuffer, UniformBuffer, Texture, np.ndarray]):
        if isinstance(value, np.ndarray): self.uniform(name, value)
        elif isinstance(value, UniformBuffer): self.uniform_block(name, value)
        elif isinstance(value, Texture): self.texture(name, value)
        else: raise TypeError("Inappropriate type for argument 'value', type should be:\n"
                              "\tuniform       : numpy.ndarray\n"
                              "\tuniform block : pyplex.glow.UniformBuffer\n"
                              "\ttexture       : pyplex.glow.Texture")


class Resource:
    def __init__(self, ctx: gl.GL_ANY, program: Program, interface: gl.Interface, index: int):
        self._ctx = ctx
        self._program = program
        self._interface = interface
        self._index = index

        self._name = self._query_name(index)
        self._location = self._query_location(self._name)

    @property
    def program(self) -> Program:
        return self._program

    @property
    def interface(self) -> gl.Interface:
        return self._interface

    @property
    def index(self) -> int:
        return self._index

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> int:
        return self._location

    def _query_name(self, index: int) -> str:
        max_name_length = c_int(0)
        self._ctx.get_program_interfaceiv(
            self.program.ptr, self._interface, gl.InterfaceParameter.MAX_NAME_LENGTH, max_name_length)
        name = create_string_buffer(b'', size=max_name_length.value)
        self._ctx.get_program_resource_name(
            self.program.ptr, self.interface, index, max_name_length.value, pointer(c_uint32()), name)
        return name.value.decode()

    def _query_location(self, name: str) -> int:
        return self._ctx.get_program_resource_location(self.program.ptr, self.interface, name.encode())

    def _parameters(self, *properties: gl.ResourceParameter) -> List[int]:
        num = len(properties)
        props = (c_uint32 * len(properties))()
        for i, prop in enumerate(properties): props[i] = c_uint32(prop)

        results = (c_int * len(properties))()
        self._ctx.get_program_resourceiv(self.program.ptr, self.interface, self.index, num, props, num, None, results)
        return [results[i] for i in range(num)]


class InputResource(Resource):
    def __init__(self, ctx: gl.GL_ANY, program: Program, index: int):
        super().__init__(ctx, program, gl.Interface.PROGRAM_INPUT, index)

        parameters = self._parameters(
            gl.ResourceParameter.TYPE,
            gl.ResourceParameter.ARRAY_SIZE,
            gl.ResourceParameter.IS_PER_PATCH,
            gl.ResourceParameter.REFERENCED_BY_VERTEX_SHADER,
            gl.ResourceParameter.REFERENCED_BY_FRAGMENT_SHADER,
            gl.ResourceParameter.REFERENCED_BY_GEOMETRY_SHADER,
            gl.ResourceParameter.REFERENCED_BY_TESS_CONTROL_SHADER,
            gl.ResourceParameter.REFERENCED_BY_TESS_EVALUATION_SHADER,
            gl.ResourceParameter.REFERENCED_BY_COMPUTE_SHADER)

        self._type = Type(parameters[0])
        self._size = int(parameters[1])
        self._per_patch = bool(parameters[2])
        self._referenced = {shader: bool(value) for shader, value in zip(
            [VertexShader, FragmentShader, TessControlShader, TessEvaluationShader, ComputeShader], parameters[3:])}

    @property
    def type(self) -> Type:
        return self._type

    @property
    def size(self) -> int:
        return self._size

    @property
    def per_patch(self) -> bool:
        return self._per_patch

    @property
    def referenced(self) -> Dict[Shader, bool]:
        return self._referenced


class OutputResource(Resource):
    def __init__(self, ctx: gl.GL_ANY, program: Program, index: int):
        super().__init__(ctx, program, gl.Interface.PROGRAM_OUTPUT, index)

        parameters = self._parameters(
            gl.ResourceParameter.TYPE,
            gl.ResourceParameter.ARRAY_SIZE,
            gl.ResourceParameter.IS_PER_PATCH,
            gl.ResourceParameter.REFERENCED_BY_VERTEX_SHADER,
            gl.ResourceParameter.REFERENCED_BY_FRAGMENT_SHADER,
            gl.ResourceParameter.REFERENCED_BY_GEOMETRY_SHADER,
            gl.ResourceParameter.REFERENCED_BY_TESS_CONTROL_SHADER,
            gl.ResourceParameter.REFERENCED_BY_TESS_EVALUATION_SHADER,
            gl.ResourceParameter.REFERENCED_BY_COMPUTE_SHADER)

        self._type = Type(parameters[0])
        self._size = int(parameters[1])
        self._per_patch = bool(parameters[2])
        self._referenced = {shader: bool(value) for shader, value in zip(
            [VertexShader, FragmentShader, TessControlShader, TessEvaluationShader, ComputeShader], parameters[3:])}

    @property
    def type(self) -> Type:
        return self._type

    @property
    def size(self) -> int:
        return self._size

    @property
    def per_patch(self) -> bool:
        return self._per_patch

    @property
    def referenced(self) -> Dict[Shader, bool]:
        return self._referenced


class UniformResource(Resource):
    def __init__(self, ctx: gl.GL_ANY, program: Program, index: int):
        super().__init__(ctx, program, gl.Interface.UNIFORM, index)

        parameters = self._parameters(
            gl.ResourceParameter.TYPE,

            gl.ResourceParameter.ARRAY_SIZE,
            gl.ResourceParameter.OFFSET,
            gl.ResourceParameter.BLOCK_INDEX,
            gl.ResourceParameter.ARRAY_STRIDE,
            gl.ResourceParameter.MATRIX_STRIDE,

            gl.ResourceParameter.ATOMIC_COUNTER_BUFFER_INDEX,

            gl.ResourceParameter.IS_ROW_MAJOR,

            gl.ResourceParameter.REFERENCED_BY_VERTEX_SHADER,
            gl.ResourceParameter.REFERENCED_BY_GEOMETRY_SHADER,
            gl.ResourceParameter.REFERENCED_BY_TESS_CONTROL_SHADER,
            gl.ResourceParameter.REFERENCED_BY_TESS_EVALUATION_SHADER,
            gl.ResourceParameter.REFERENCED_BY_COMPUTE_SHADER,
        )

        self._type = Type(parameters[0])
        self._matrix_type = self._type.gl_type.name in gl.MatrixType.__members__
        self._setter = ctx.__getattribute__(self._type.uniform_func.__name__)

        self._size = int(parameters[1])
        self._offset = int(parameters[2])
        self._block_index = int(parameters[3])
        self._array_stride = int(parameters[4])
        self._matrix_stride = int(parameters[5])

        self._atomic_counter_buffer_index = int(parameters[6])
        self._per_patch = bool(parameters[7])
        self._row_major = bool(parameters[8])

        self._referenced = {shader: bool(value) for shader, value in zip(
            [VertexShader, GeometryShader, TessControlShader, TessEvaluationShader, ComputeShader], parameters[9:])}

    @property
    def type(self) -> Type:
        return self._type

    @property
    def is_matrix(self) -> bool:
        return self._matrix_type

    @property
    def setter(self):
        return self._setter

    @property
    def size(self) -> int:
        return self._size

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def block_index(self) -> int:
        return self._block_index

    @property
    def array_stride(self) -> int:
        return self._array_stride

    @property
    def matrix_stride(self) -> int:
        return self._matrix_stride

    @property
    def row_major(self) -> bool:
        return self._row_major

    @property
    def referenced(self) -> Dict[Shader, bool]:
        return self._referenced


class Interface:
    def __init__(self, ctx: gl.GL_ANY, program: Program, interface: gl.Interface, resources: List[Resource]):
        self._ctx = ctx
        self._program = program
        self._interface = interface
        self._resources = {resource.name: resource for resource in resources}

    @property
    def program(self) -> Program:
        return self._program

    @property
    def interface(self) -> gl.Interface:
        return self._interface

    @property
    def resources(self) -> Dict[str, Resource]:
        return self._resources

    @staticmethod
    def _num_active(ctx: gl.GL_ANY, program: Program, interface: gl.Interface) -> int:
        active = c_int(0)
        ctx.get_program_interfaceiv(program.ptr, interface, gl.InterfaceParameter.ACTIVE_RESOURCES, active)
        return active.value

    def _parameters(self, index: int, *properties: gl.ResourceParameter) -> List[int]:
        num = len(properties)
        props = (c_uint32 * len(properties))()
        for i, prop in enumerate(properties): props[i] = c_uint32(prop)

        results = (c_int * len(properties))()
        self._ctx.get_program_resourceiv(self.program.ptr, self.interface, index, num, props, num, None, results)
        return [results[i] for i in range(num)]


class InputInterface(Interface):
    def __init__(self, ctx: gl.GL_ANY, program: Program):
        super().__init__(ctx, program, gl.Interface.PROGRAM_INPUT,
                         [InputResource(ctx, program, i) for i in range(self._num_active(
                             ctx, program, gl.Interface.PROGRAM_INPUT))])

    @property
    def resources(self) -> Dict[str, InputResource]:
        return self._resources


class OutputInterface(Interface):
    def __init__(self, ctx: gl.GL_ANY, program: Program):
        super().__init__(ctx, program, gl.Interface.PROGRAM_OUTPUT,
                         [OutputResource(ctx, program, i) for i in range(self._num_active(
                             ctx, program, gl.Interface.PROGRAM_OUTPUT))])

    @property
    def resources(self) -> Dict[str, OutputResource]:
        return self._resources


class UniformInterface(Interface):
    def __init__(self, ctx: gl.GL_ANY, program: Program):
        super().__init__(ctx, program, gl.Interface.UNIFORM,
                         [UniformResource(ctx, program, i) for i in range(self._num_active(
                             ctx, program, gl.Interface.UNIFORM))])

    @property
    def resources(self) -> Dict[str, UniformResource]:
        return self._resources