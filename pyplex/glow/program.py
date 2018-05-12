from pyplex import gl
from pyplex.glow.shader import Shader, VertexShader, FragmentShader, GeometryShader, TessEvaluationShader, TessControlShader, ComputeShader
from pyplex.glow.buffer import ArrayBuffer, UniformBuffer, ElementArrayBuffer
from pyplex.glow.texture import Texture
from pyplex.glow.type import Type
from pyplex.glow import abstract
import numpy as np
from ctypes import *

from typing import List, Union, Dict, Iterable


class LinkError(Exception):
    pass


class VertexArray(abstract.BindableObject):
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


class Program(abstract.BindableObject):

    TRANSPOSE_MATRICES = False

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

        self._input_interface = InputInterface(self._ctx, self)
        self._output_interface = OutputInterface(self._ctx, self)
        self._uniform_interface = UniformInterface(self._ctx, self)

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

    def vertices(self, buffer: ArrayBuffer):
        stride = buffer.dtype.itemsize

        with self._vao, buffer:
            for name, (dtype, offset) in buffer.dtype.fields.items():
                index = self._ctx.get_program_resource_index(self._ptr, gl.Interface.PROGRAM_INPUT, name.encode())
                location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.PROGRAM_INPUT, name.encode())

                t = Type(self._resource_parameters(gl.Interface.PROGRAM_INPUT, index, gl.ResourceParameter.TYPE)[0])

                self._ctx.vertex_attrib_pointer(location, t.count, t.gl_base, False, stride, c_void_p(offset))
                self._ctx.enable_vertex_attrib_array(location)

    def input(self, name: str, buffer: ArrayBuffer):
        index = self._ctx.get_program_resource_index(self._ptr, gl.Interface.PROGRAM_INPUT, name.encode())
        location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.PROGRAM_INPUT, name.encode())

        t = Type(self._resource_parameters(gl.Interface.PROGRAM_INPUT, index, gl.ResourceParameter.TYPE)[0])

        with buffer, self._vao:
            self._ctx.vertex_attrib_pointer(location, t.count, t.gl_base, False, 0, c_void_p(0))
            self._ctx.enable_vertex_attrib_array(location)

    def uniform_block(self, name: str, buffer: UniformBuffer):
        location = self._ctx.get_program_resource_index(self._ptr, gl.Interface.UNIFORM_BLOCK, name.encode())
        self._ctx.uniform_block_binding(self._ptr, location, buffer.ptr)

    def texture(self, name: str, texture: Texture):
        if not name in self._textures:
            unit = len(self._textures) + gl.TextureUnit.TEXTURE0
            self._textures[name] = (texture, unit)

        location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.UNIFORM, name.encode())
        self._ctx.program_uniform_1i(self._ptr, location, self._textures[name][1] - gl.TextureUnit.TEXTURE0)

    def uniform(self, name: str, value: np.ndarray):
        index = self._ctx.get_program_resource_index(self._ptr, gl.Interface.UNIFORM, name.encode())
        location = self._ctx.get_program_resource_location(self._ptr, gl.Interface.UNIFORM, name.encode())

        t = Type(self._resource_parameters(gl.Interface.UNIFORM, index, gl.ResourceParameter.TYPE)[0])
        func = self._ctx.__getattribute__(t.uniform_func.__name__)

        if t.gl_type.name in gl.MatrixType.__members__:
            func(self._ptr, location, int(value.nbytes / t.nbytes),
                 self.TRANSPOSE_MATRICES, value.ctypes.data_as(POINTER(t.ctypes)))
        else:
            func(self._ptr, location, int(value.nbytes / t.nbytes), value.ctypes.data_as(POINTER(t.ctypes)))

    def draw_arrays(self, mode: gl.DrawMode, start: int, count: int):
        with self: self._ctx.draw_arrays(mode, start, count)

    def draw_elements(self, mode: gl.DrawMode, buffer: ElementArrayBuffer):
        gl_type = Type.from_np(buffer.shape[1:], buffer.dtype).gl_type
        with self, buffer: self._ctx.draw_elements(mode, buffer.size, gl_type, c_void_p(0))

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

    def __setitem__(self, name: str, value: Union[ArrayBuffer, UniformBuffer, Texture, np.ndarray]):
        if isinstance(value, ArrayBuffer): self.input(name, value)
        elif isinstance(value, Texture): self.texture(name, value)
        elif isinstance(value, UniformBuffer): self.uniform_block(name, value)
        elif isinstance(value, np.ndarray): self.uniform(name, value)
        else: raise TypeError("Inappropriate type for argument 'value', type should be:\n"
                              "\tinput         : pyplex.glow.ArrayBuffer\n"
                              "\ttexture       : pyplex.glow.Texture\n"
                              "\tuniform block : pyplex.glow.UniformBuffer\n"
                              "\tuniform       : numpy.ndarray")


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
    def __init__(self, ctx: gl.GL_ANY, program: Program, interface: gl.Interface):
        self._ctx = ctx
        self._program = program
        self._interface = interface

    @property
    def program(self) -> Program:
        return self._program

    @property
    def interface(self) -> gl.Interface:
        return self._interface

    @property
    def resources(self) -> List[Resource]:
        raise NotImplementedError()

    def _num_active(self) -> int:
        active = c_int(0)
        self._ctx.get_program_interfaceiv(
            self.program.ptr,self._interface,gl.InterfaceParameter.ACTIVE_RESOURCES, active)
        return active.value

    def __iter__(self):
        return self.resources.__iter__()

    def _parameters(self, index: int, *properties: gl.ResourceParameter) -> List[int]:
        num = len(properties)
        props = (c_uint32 * len(properties))()
        for i, prop in enumerate(properties): props[i] = c_uint32(prop)

        results = (c_int * len(properties))()
        self._ctx.get_program_resourceiv(self.program.ptr, self.interface, index, num, props, num, None, results)
        return [results[i] for i in range(num)]


class InputInterface(Interface):
    def __init__(self, ctx: gl.GL_ANY, program: Program):
        super().__init__(ctx, program, gl.Interface.PROGRAM_INPUT)
        self._resources = [InputResource(ctx, program, i) for i in range(self._num_active())]

    @property
    def resources(self) -> List[InputResource]:
        return self._resources

    def __iter__(self) -> Iterable[InputResource]:
        return self.resources.__iter__()


class OutputInterface(Interface):
    def __init__(self, ctx: gl.GL_ANY, program: Program):
        super().__init__(ctx, program, gl.Interface.PROGRAM_OUTPUT)
        self._resources = [OutputResource(ctx, program, i) for i in range(self._num_active())]

    @property
    def resources(self) -> List[OutputResource]:
        return self._resources

    def __iter__(self) -> Iterable[OutputResource]:
        return self.resources.__iter__()


class UniformInterface(Interface):
    def __init__(self, ctx: gl.GL_ANY, program: Program):
        super().__init__(ctx, program, gl.Interface.UNIFORM)
        self._resources = [UniformResource(ctx, program, i) for i in range(self._num_active())]

    @property
    def resources(self) -> List[UniformResource]:
        return self._resources

    def __iter__(self) -> Iterable[UniformResource]:
        return self.resources.__iter__()