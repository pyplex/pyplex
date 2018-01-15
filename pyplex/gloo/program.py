from pyplex import gl
from pyplex.gloo import ContextObject, Type, ArrayBuffer, Shader, TextureContext
from typing import List

import numpy as np


class ProgramLinkError(Exception):
    """Program Link Error"""
    pass


class VertexArray(ContextObject):
    def __init__(self, ctx: gl.Context):
        """
        Create Vertex Array

        Parameters
        ----------
        ctx: gl.Context
         OpenGL Context
        """
        self._ctx = ctx
        self._ptr = self.ctx.create_vertex_array()

    @property
    def ctx(self) -> gl.Context:
        """
        Returns
        -------
        ctx: gl.Context
            OpenGL Context
        """
        return self._ctx

    @property
    def ptr(self) -> gl.VertexArray:
        """
        Returns
        -------
        ptr: gl.VertexArray
            Pointer to OpenGL VertexArray object
        """
        return self._ptr

    def delete(self):
        self.ctx.delete_vertex_array(self.ptr)

    def bind(self):
        """Bind Vertex Array"""
        self.ctx.bind_vertex_array(self.ptr)

    def unbind(self):
        """Unbind Vertex Array"""
        self.ctx.bind_vertex_array(None)


class Program(ContextObject):
    def __init__(self, ctx: gl.Context, *shaders: Shader):
        """
        Create Program object

        Parameters
        ----------
        ctx: gl.Context
            OpenGL Context
        shaders: tuple of Shader
            Shaders to attach to this Program
        """

        self._ctx = ctx
        self._ptr = self.ctx.create_program()
        self._vao = VertexArray(self.ctx)

        self._vertex_count = 0
        self._textures = {}

        self._shaders = [shader for shader in shaders]
        self._link()

    @property
    def ctx(self) -> gl.Context:
        """
        Returns
        -------
        ctx: gl.Context
            OpenGL Context
        """
        return self._ctx

    @property
    def ptr(self) -> gl.Program:
        """
        Returns
        -------
        ptr: Pointer to OpenGL Program object
        """
        return self._ptr

    @property
    def vao(self) -> VertexArray:
        """
        Returns
        -------
        vao: VertexArray
            VertexArray object associated with Program
        """
        return self._vao

    @property
    def shaders(self) -> List[Shader]:
        """
        Returns
        -------
        shaders: list of Shader
            Shader objects associated with Program
        """
        return self._shaders

    @property
    def log(self) -> str:
        """
        Returns
        -------
        log: Program Info Log
        """
        return self.ctx.program_info_log(self.ptr)

    def delete(self):
        self.ctx.delete_program(self.ptr)

    def bind(self):
        self.vao.bind()
        self.ctx.use_program(self.ptr)
        for unit, texture in self._textures.values():
            self.ctx.active_texture(unit)
            texture.bind()
        self.ctx.active_texture(gl.TextureUnit.TEXTURE0)

    def unbind(self):
        for unit, texture in self._textures.values():
            self.ctx.active_texture(unit)
            texture.unbind()
        self.ctx.active_texture(gl.TextureUnit.TEXTURE0)

        self.ctx.use_program(None)
        self.vao.unbind()

    def input(self, name: str, buffer: ArrayBuffer):
        """
        Specify Program Input

        Parameters
        ----------
        name: str
            Program input name
        buffer: ArrayBuffer
            Program input data
        """

        # TODO: Add error handling when 'name' does not exist
        index = self.ctx.resource_index(self.ptr, gl.Interface.PROGRAM_INPUT, name)
        location = self.ctx.resource_location(self.ptr, gl.Interface.PROGRAM_INPUT, name)

        if location == -1: raise ValueError("'{}' is not an active Input".format(name))

        input_type = Type(self.ctx.resource_parameter(self.ptr, gl.Interface.PROGRAM_INPUT,
                                                      index, gl.ResourceParameter.TYPE)[0])

        if input_type.dtype != buffer.dtype:
            raise TypeError("Type mismatch for 'in {} {}': expected '{}', got '{}'".format(
                input_type, name, input_type.dtype, buffer.dtype))
        if buffer.shape[-len(input_type.shape):] != input_type.shape:
            raise TypeError("Shape mismatch for 'in {} {}': expected {}, got {}".format(
                input_type, name, '(:, {})'.format(', '.join(str(i) for i in input_type.shape)), buffer.shape
            ))

        # TODO: Clean this out!
        self._vertex_count = buffer.shape[0]

        with buffer, self.vao:
            # TODO: Location instead of Index here? Check OpenGL API
            self.ctx.vertex_attribute_pointer(location, input_type.count, input_type.gl_base, False, input_type.size, 0)
            self.ctx.enable_vertex_attribute_array(location)

    def uniform(self, name: str, value: np.ndarray):
        """
        Specify Program Uniform

        Parameters
        ----------
        name: str
            Program uniform name
        value: np.ndarray
            Program uniform data
        """
        index = self.ctx.resource_index(self.ptr, gl.Interface.UNIFORM, name)
        location = self.ctx.resource_location(self.ptr, gl.Interface.UNIFORM, name)

        if location == -1: print("WARNING: '{}' is not an active Uniform".format(name))
        else:
            type = Type(self.ctx.resource_parameter(
                self.ptr, gl.Interface.UNIFORM, index, gl.ResourceParameter.TYPE)[0])
            length = self.ctx.resource_parameter(self.ptr, gl.Interface.UNIFORM, index, gl.ResourceParameter.ARRAY_SIZE)[0]
            shape = (length, *type.shape)

            if type.dtype != value.dtype:
                raise TypeError("Type mismatch for 'uniform {} {}': expected '{}', got '{}'".format(
                    type, name, type.dtype, value.dtype))
            if length == 1:
                if value.shape != shape and value.shape != type.shape:
                    raise TypeError("Shape mismatch for 'uniform {} {}': expected {}, got {}".format(
                        type, name, type.shape, value.shape))
            elif value.shape != shape:
                raise TypeError("Shape mismatch for 'uniform {} {}[{}]': expected {}, got {}".format(
                    type, name, length, shape, value.shape))

            type.uniform_func(self.ctx, self.ptr, location, value.reshape(shape))

    def texture(self, name: str, texture: TextureContext):
        location = self.ctx.resource_index(self.ptr, gl.Interface.UNIFORM, name)

        if location == -1: raise ValueError("'{}' is not an active Texture".format(name))

        unit = self._get_unused_texture_unit()
        self.ctx.uniform_1i(self.ptr, location, unit - gl.TextureUnit.TEXTURE0)  # Needs Unit Number instead of ENUM...
        self._textures[name] = (unit, texture)

    def draw(self, mode: gl.DrawMode):
        """
        Draw Program

        Parameters
        ----------
        mode: gl.DrawMode
        """
        with self:
            self.ctx.draw_arrays(mode, 0, self._vertex_count)

    def _link(self):
        """Link Shaders to Program"""
        for shader in self.shaders:
            self.ctx.attach_shader(self.ptr, shader.ptr)
        self.ctx.link_program(self.ptr)

        if not self.ctx.program_parameter(self.ptr, gl.ProgramParameter.LINK_STATUS):
            ProgramLinkError(self.log)

    def _get_unused_texture_unit(self) -> int:
        used_units = set(unit for (unit, texture) in self._textures.values())
        max_units = self.ctx.get_int(gl.StateParameter.MAX_COMBINED_TEXTURE_IMAGE_UNITS)

        for i in range(gl.TextureUnit.TEXTURE0, gl.TextureUnit.TEXTURE0 + max_units):
            if i not in used_units:
                return i

        raise SystemError("Number of Textures exceeded system limit (= {})".format(max_units))

