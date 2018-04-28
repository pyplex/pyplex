from pyplex.glfw import GLFW
from ctypes import *
from typing import Union

class GL:

    MAJOR = None
    MINOR = None

    def __init__(self, glfw: GLFW):
        self._glfw = glfw

    def _load(self, target, name, restype=None, *argtypes):
        function = cast(self._glfw.get_proc_address(name.encode()), CFUNCTYPE(restype, *argtypes))
        self.__setattr__(target.__name__, function)


class GL20(GL):

    MAJOR = 2
    MINOR = 0

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.active_texture, 'glActiveTexture',
                   None, c_uint)
        self._load(self.attach_shader, 'glAttachShader',
                   None, c_uint, c_uint)
        self._load(self.begin_query, 'glBeginQuery',
                   None, c_uint, c_uint)
        self._load(self.end_query, 'glEndQuery',
                   None, c_uint)
        self._load(self.bind_attrib_location, 'glBindAttribLocation',
                   None, c_uint, c_uint, c_char_p)
        self._load(self.bind_buffer, 'glBindBuffer',
                   None, c_uint, c_uint)
        self._load(self.bind_texture, 'glBindTexture',
                   None, c_uint, c_uint)
        self._load(self.blend_color, 'glBlendColor',
                   None, c_float, c_float, c_float, c_float)
        self._load(self.blend_equation, 'glBlendEquation',
                   None, c_uint)
        self._load(self.blend_equation_separate, 'glBlendEquationSeparate',
                   None, c_uint, c_uint)
        self._load(self.blend_func, 'glBlendFunc',
                   None, c_uint, c_uint)
        self._load(self.blend_func_separate, 'glBlendFuncSeparate',
                   None, c_uint, c_uint, c_uint, c_uint)
        self._load(self.buffer_data, 'glBufferData',
                   None, c_uint, POINTER(c_uint32), c_void_p, c_uint)
        self._load(self.buffer_sub_data, 'glBufferSubData',
                   None, c_uint, POINTER(c_int), POINTER(c_uint32), c_void_p)
        self._load(self.clear, 'glClear',
                   None, c_uint32)
        self._load(self.clear_color, 'glClearColor',
                   None, c_float, c_float, c_float, c_float)
        self._load(self.clear_depth, 'glClearDepth',
                   None, c_double)
        self._load(self.clear_stencil, 'glClearStencil',
                   None, c_int)
        self._load(self.color_mask, 'glColorMask',
                   None, c_bool, c_bool, c_bool, c_bool)
        self._load(self.compile_shader, 'glCompileShader',
                   None, c_uint)
        self._load(self.create_program, 'glCreateProgram',
                   c_uint, )
        self._load(self.create_shader, 'glCreateShader',
                   c_uint, c_uint)
        self._load(self.cull_face, 'glCullFace',
                   None, c_uint)
        self._load(self.delete_buffers, 'glDeleteBuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.delete_program, 'glDeleteProgram',
                   None, c_uint)
        self._load(self.delete_queries, 'glDeleteQueries',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.delete_shader, 'glDeleteShader',
                   None, c_uint)
        self._load(self.delete_textures, 'glDeleteTextures',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.depth_func, 'glDepthFunc',
                   None, c_uint)
        self._load(self.depth_mask, 'glDepthMask',
                   None, c_bool)
        self._load(self.depth_range, 'glDepthRange',
                   None, c_double, c_double)
        self._load(self.detach_shader, 'glDetachShader',
                   None, c_uint, c_uint)
        self._load(self.draw_arrays, 'glDrawArrays',
                   None, c_uint, c_int, c_uint32)
        self._load(self.draw_buffer, 'glDrawBuffer',
                   None, c_uint)
        self._load(self.draw_buffers, 'glDrawBuffers',
                   None, c_uint32, POINTER(c_uint32))
        self._load(self.draw_elements, 'glDrawElements',
                   None, c_uint, c_uint32, c_uint, c_void_p)
        self._load(self.draw_range_elements, 'glDrawRangeElements',
                   None, c_uint, c_uint, c_uint, c_uint32, c_uint, c_void_p)
        self._load(self.enable, 'glEnable',
                   None, c_uint)
        self._load(self.disable, 'glDisable',
                   None, c_uint)
        self._load(self.enable_vertex_attrib_array, 'glEnableVertexAttribArray',
                   None, c_uint)
        self._load(self.disable_vertex_attrib_array, 'glDisableVertexAttribArray',
                   None, c_uint)
        self._load(self.finish, 'glFinish',
                   None, )
        self._load(self.flush, 'glFlush',
                   None, )
        self._load(self.front_face, 'glFrontFace',
                   None, c_uint)
        self._load(self.gen_buffers, 'glGenBuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.gen_queries, 'glGenQueries',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.gen_textures, 'glGenTextures',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.get_booleanv, 'glGetBooleanv',
                   None, c_uint, POINTER(c_bool))
        self._load(self.get_doublev, 'glGetDoublev',
                   None, c_uint, POINTER(c_double))
        self._load(self.get_floatv, 'glGetFloatv',
                   None, c_uint, POINTER(c_float))
        self._load(self.get_integerv, 'glGetIntegerv',
                   None, c_uint, POINTER(c_int))
        self._load(self.get_active_attrib, 'glGetActiveAttrib',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint32), POINTER(c_int), POINTER(c_uint32), c_char_p)
        self._load(self.get_active_uniform, 'glGetActiveUniform',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint32), POINTER(c_int), POINTER(c_uint32), c_char_p)
        self._load(self.get_attached_shaders, 'glGetAttachedShaders',
                   None, c_uint, c_uint32, POINTER(c_uint32), POINTER(c_uint))
        self._load(self.get_attrib_location, 'glGetAttribLocation',
                   c_int, c_uint, c_char_p)
        self._load(self.get_buffer_parameteriv, 'glGetBufferParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_buffer_pointerv, 'glGetBufferPointerv',
                   None, c_uint, c_uint, POINTER(c_void_p))
        self._load(self.get_buffer_sub_data, 'glGetBufferSubData',
                   None, c_uint, POINTER(c_int), POINTER(c_uint32), c_void_p)
        self._load(self.get_compressed_tex_image, 'glGetCompressedTexImage',
                   None, c_uint, c_int, c_void_p)
        self._load(self.get_error, 'glGetError',
                   c_uint, )
        self._load(self.get_programiv, 'glGetProgramiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_program_info_log, 'glGetProgramInfoLog',
                   None, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_queryiv, 'glGetQueryiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_query_objectiv, 'glGetQueryObjectiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_query_objectuiv, 'glGetQueryObjectuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.get_shaderiv, 'glGetShaderiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_shader_info_log, 'glGetShaderInfoLog',
                   None, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_shader_source, 'glGetShaderSource',
                   None, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_string, 'glGetString',
                   POINTER(c_ubyte), c_uint)
        self._load(self.get_tex_image, 'glGetTexImage',
                   None, c_uint, c_int, c_uint, c_uint, c_void_p)
        self._load(self.get_tex_level_parameterfv, 'glGetTexLevelParameterfv',
                   None, c_uint, c_int, c_uint, POINTER(c_float))
        self._load(self.get_tex_level_parameteriv, 'glGetTexLevelParameteriv',
                   None, c_uint, c_int, c_uint, POINTER(c_int))
        self._load(self.get_tex_parameterfv, 'glGetTexParameterfv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.get_tex_parameteriv, 'glGetTexParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_uniformfv, 'glGetUniformfv',
                   None, c_uint, c_int, POINTER(c_float))
        self._load(self.get_uniformiv, 'glGetUniformiv',
                   None, c_uint, c_int, POINTER(c_int))
        self._load(self.get_uniform_location, 'glGetUniformLocation',
                   c_int, c_uint, c_char_p)
        self._load(self.get_vertex_attribdv, 'glGetVertexAttribdv',
                   None, c_uint, c_uint, POINTER(c_double))
        self._load(self.get_vertex_attribfv, 'glGetVertexAttribfv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.get_vertex_attribiv, 'glGetVertexAttribiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_vertex_attrib_pointerv, 'glGetVertexAttribPointerv',
                   None, c_uint, c_uint, POINTER(c_void_p))
        self._load(self.hint, 'glHint',
                   None, c_uint, c_uint)
        self._load(self.is_buffer, 'glIsBuffer',
                   c_bool, c_uint)
        self._load(self.is_enabled, 'glIsEnabled',
                   c_bool, c_uint)
        self._load(self.is_program, 'glIsProgram',
                   c_bool, c_uint)
        self._load(self.is_query, 'glIsQuery',
                   c_bool, c_uint)
        self._load(self.is_shader, 'glIsShader',
                   c_bool, c_uint)
        self._load(self.is_texture, 'glIsTexture',
                   c_bool, c_uint)
        self._load(self.line_width, 'glLineWidth',
                   None, c_float)
        self._load(self.link_program, 'glLinkProgram',
                   None, c_uint)
        self._load(self.logic_op, 'glLogicOp',
                   None, c_uint)
        self._load(self.map_buffer, 'glMapBuffer',
                   c_void_p, c_uint, c_uint)
        self._load(self.multi_draw_arrays, 'glMultiDrawArrays',
                   None, c_uint, POINTER(c_int), POINTER(c_uint32), c_uint32)
        self._load(self.multi_draw_elements, 'glMultiDrawElements',
                   None, c_uint, POINTER(c_uint32), c_uint, c_uint32)
        self._load(self.pixel_storef, 'glPixelStoref',
                   None, c_uint, c_float)
        self._load(self.pixel_storei, 'glPixelStorei',
                   None, c_uint, c_int)
        self._load(self.point_parameterf, 'glPointParameterf',
                   None, c_uint, c_float)
        self._load(self.point_parameteri, 'glPointParameteri',
                   None, c_uint, c_int)
        self._load(self.point_parameterfv, 'glPointParameterfv',
                   None, c_uint, POINTER(c_float))
        self._load(self.point_parameteriv, 'glPointParameteriv',
                   None, c_uint, POINTER(c_int))
        self._load(self.point_size, 'glPointSize',
                   None, c_float)
        self._load(self.polygon_mode, 'glPolygonMode',
                   None, c_uint, c_uint)
        self._load(self.polygon_offset, 'glPolygonOffset',
                   None, c_float, c_float)
        self._load(self.read_buffer, 'glReadBuffer',
                   None, c_uint)
        self._load(self.read_pixels, 'glReadPixels',
                   None, c_int, c_int, c_uint32, c_uint32, c_uint, c_uint, c_void_p)
        self._load(self.sample_coverage, 'glSampleCoverage',
                   None, c_float, c_bool)
        self._load(self.scissor, 'glScissor',
                   None, c_int, c_int, c_uint32, c_uint32)
        self._load(self.shader_source, 'glShaderSource',
                   None, c_uint, c_uint32, POINTER(c_char_p), POINTER(c_int))
        self._load(self.stencil_func, 'glStencilFunc',
                   None, c_uint, c_int, c_uint)
        self._load(self.stencil_func_separate, 'glStencilFuncSeparate',
                   None, c_uint, c_uint, c_int, c_uint)
        self._load(self.stencil_mask, 'glStencilMask',
                   None, c_uint)
        self._load(self.stencil_mask_separate, 'glStencilMaskSeparate',
                   None, c_uint, c_uint)
        self._load(self.stencil_op, 'glStencilOp',
                   None, c_uint, c_uint, c_uint)
        self._load(self.stencil_op_separate, 'glStencilOpSeparate',
                   None, c_uint, c_uint, c_uint, c_uint)
        self._load(self.tex_parameterf, 'glTexParameterf',
                   None, c_uint, c_uint, c_float)
        self._load(self.tex_parameteri, 'glTexParameteri',
                   None, c_uint, c_uint, c_int)
        self._load(self.tex_parameterfv, 'glTexParameterfv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.tex_parameteriv, 'glTexParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.uniform1f, 'glUniform1f',
                   None, c_int, c_float)
        self._load(self.uniform2f, 'glUniform2f',
                   None, c_int, c_float, c_float)
        self._load(self.uniform3f, 'glUniform3f',
                   None, c_int, c_float, c_float, c_float)
        self._load(self.uniform4f, 'glUniform4f',
                   None, c_int, c_float, c_float, c_float, c_float)
        self._load(self.uniform1i, 'glUniform1i',
                   None, c_int, c_int)
        self._load(self.uniform2i, 'glUniform2i',
                   None, c_int, c_int, c_int)
        self._load(self.uniform3i, 'glUniform3i',
                   None, c_int, c_int, c_int, c_int)
        self._load(self.uniform4i, 'glUniform4i',
                   None, c_int, c_int, c_int, c_int, c_int)
        self._load(self.uniform1fv, 'glUniform1fv',
                   None, c_int, c_uint32, POINTER(c_float))
        self._load(self.uniform2fv, 'glUniform2fv',
                   None, c_int, c_uint32, POINTER(c_float))
        self._load(self.uniform3fv, 'glUniform3fv',
                   None, c_int, c_uint32, POINTER(c_float))
        self._load(self.uniform4fv, 'glUniform4fv',
                   None, c_int, c_uint32, POINTER(c_float))
        self._load(self.uniform1iv, 'glUniform1iv',
                   None, c_int, c_uint32, POINTER(c_int))
        self._load(self.uniform2iv, 'glUniform2iv',
                   None, c_int, c_uint32, POINTER(c_int))
        self._load(self.uniform3iv, 'glUniform3iv',
                   None, c_int, c_uint32, POINTER(c_int))
        self._load(self.uniform4iv, 'glUniform4iv',
                   None, c_int, c_uint32, POINTER(c_int))
        self._load(self.uniform_matrix2fv, 'glUniformMatrix2fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.uniform_matrix3fv, 'glUniformMatrix3fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.uniform_matrix4fv, 'glUniformMatrix4fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.unmap_buffer, 'glUnmapBuffer',
                   c_bool, c_uint)
        self._load(self.use_program, 'glUseProgram',
                   None, c_uint)
        self._load(self.validate_program, 'glValidateProgram',
                   None, c_uint)
        self._load(self.vertex_attrib1f, 'glVertexAttrib1f',
                   None, c_uint, c_float)
        self._load(self.vertex_attrib1s, 'glVertexAttrib1s',
                   None, c_uint, c_int16)
        self._load(self.vertex_attrib1d, 'glVertexAttrib1d',
                   None, c_uint, c_double)
        self._load(self.vertex_attrib2f, 'glVertexAttrib2f',
                   None, c_uint, c_float, c_float)
        self._load(self.vertex_attrib2s, 'glVertexAttrib2s',
                   None, c_uint, c_int16, c_int16)
        self._load(self.vertex_attrib2d, 'glVertexAttrib2d',
                   None, c_uint, c_double, c_double)
        self._load(self.vertex_attrib3f, 'glVertexAttrib3f',
                   None, c_uint, c_float, c_float, c_float)
        self._load(self.vertex_attrib3s, 'glVertexAttrib3s',
                   None, c_uint, c_int16, c_int16, c_int16)
        self._load(self.vertex_attrib3d, 'glVertexAttrib3d',
                   None, c_uint, c_double, c_double, c_double)
        self._load(self.vertex_attrib4f, 'glVertexAttrib4f',
                   None, c_uint, c_float, c_float, c_float, c_float)
        self._load(self.vertex_attrib4s, 'glVertexAttrib4s',
                   None, c_uint, c_int16, c_int16, c_int16, c_int16)
        self._load(self.vertex_attrib4d, 'glVertexAttrib4d',
                   None, c_uint, c_double, c_double, c_double, c_double)
        self._load(self.vertex_attrib4_nub, 'glVertexAttrib4Nub',
                   None, c_uint, c_ubyte, c_ubyte, c_ubyte, c_ubyte)
        self._load(self.vertex_attrib1fv, 'glVertexAttrib1fv',
                   None, c_uint, POINTER(c_float))
        self._load(self.vertex_attrib1sv, 'glVertexAttrib1sv',
                   None, c_uint, POINTER(c_int16))
        self._load(self.vertex_attrib1dv, 'glVertexAttrib1dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib2fv, 'glVertexAttrib2fv',
                   None, c_uint, POINTER(c_float))
        self._load(self.vertex_attrib2sv, 'glVertexAttrib2sv',
                   None, c_uint, POINTER(c_int16))
        self._load(self.vertex_attrib2dv, 'glVertexAttrib2dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib3fv, 'glVertexAttrib3fv',
                   None, c_uint, POINTER(c_float))
        self._load(self.vertex_attrib3sv, 'glVertexAttrib3sv',
                   None, c_uint, POINTER(c_int16))
        self._load(self.vertex_attrib3dv, 'glVertexAttrib3dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib4fv, 'glVertexAttrib4fv',
                   None, c_uint, POINTER(c_float))
        self._load(self.vertex_attrib4sv, 'glVertexAttrib4sv',
                   None, c_uint, POINTER(c_int16))
        self._load(self.vertex_attrib4dv, 'glVertexAttrib4dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib4iv, 'glVertexAttrib4iv',
                   None, c_uint, POINTER(c_int))
        self._load(self.vertex_attrib4bv, 'glVertexAttrib4bv',
                   None, c_uint, POINTER(c_byte))
        self._load(self.vertex_attrib4ubv, 'glVertexAttrib4ubv',
                   None, c_uint, POINTER(c_ubyte))
        self._load(self.vertex_attrib4usv, 'glVertexAttrib4usv',
                   None, c_uint, POINTER(c_ushort))
        self._load(self.vertex_attrib4uiv, 'glVertexAttrib4uiv',
                   None, c_uint, POINTER(c_uint))
        self._load(self.vertex_attrib4_nbv, 'glVertexAttrib4Nbv',
                   None, c_uint, POINTER(c_byte))
        self._load(self.vertex_attrib4_nsv, 'glVertexAttrib4Nsv',
                   None, c_uint, POINTER(c_int16))
        self._load(self.vertex_attrib4_niv, 'glVertexAttrib4Niv',
                   None, c_uint, POINTER(c_int))
        self._load(self.vertex_attrib4_nubv, 'glVertexAttrib4Nubv',
                   None, c_uint, POINTER(c_ubyte))
        self._load(self.vertex_attrib4_nusv, 'glVertexAttrib4Nusv',
                   None, c_uint, POINTER(c_ushort))
        self._load(self.vertex_attrib4_nuiv, 'glVertexAttrib4Nuiv',
                   None, c_uint, POINTER(c_uint))
        self._load(self.vertex_attrib_pointer, 'glVertexAttribPointer',
                   None, c_uint, c_int, c_uint, c_bool, c_uint32, c_void_p)
        self._load(self.viewport, 'glViewport',
                   None, c_int, c_int, c_uint32, c_uint32)

    def active_texture(self, texture: int):
        """
        Select active texture unit

        Wrapper for glActiveTexture

        Parameters
        ----------
        texture: int
            Specifies which texture unit to make active. The number of texture units is implementation
            dependent, but must be at least 80. texture must be one of GL_TEXTURE i, where i ranges from zero
            to the value of GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS minus one. The initial value is GL_TEXTURE0.

        Raises
        ------
        GL_INVALID_ENUM is generated if texture is not one of GL_TEXTURE i, where i ranges from zero to the
            value of GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS minus one.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glActiveTexture.xhtml
        """
        pass

    def attach_shader(self, program: int, shader: int):
        """
        Attaches a shader object to a program object

        Wrapper for glAttachShader

        Parameters
        ----------
        program: int
            Specifies the program object to which a shader object will be attached.
        shader: int
            Specifies the shader object that is to be attached.

        Raises
        ------
        GL_INVALID_VALUE is generated if either program or shader is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if shader is not a shader object.
        GL_INVALID_OPERATION is generated if shader is already attached to program.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glAttachShader.xhtml
        """
        pass

    def begin_query(self, target: int, id: int):
        """
        Delimit the boundaries of a query object

        Wrapper for glBeginQuery

        Parameters
        ----------
        target: int
            Specifies the target type of query object to be concluded. The symbolic constant must be one of
            GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED_CONSERVATIVE,
            GL_PRIMITIVES_GENERATED, GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN, or GL_TIME_ELAPSED.
        id: int
            Specifies the name of a query object.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of the accepted tokens.
        GL_INVALID_OPERATION is generated if glBeginQuery is executed while a query object of the same
            target is already active.
        GL_INVALID_OPERATION is generated if glEndQuery is executed when a query object of the same target
            is not active.
        GL_INVALID_OPERATION is generated if id is 0.
        GL_INVALID_OPERATION is generated if id is the name of an already active query object.
        GL_INVALID_OPERATION is generated if id refers to an existing query object whose type does not does
            not match target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginQuery.xhtml
        """
        pass

    def end_query(self, target: int):
        """
        Delimit the boundaries of a query object

        Wrapper for glEndQuery

        Parameters
        ----------
        target: int
            Specifies the target type of query object to be concluded. The symbolic constant must be one of
            GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED_CONSERVATIVE,
            GL_PRIMITIVES_GENERATED, GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN, or GL_TIME_ELAPSED.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of the accepted tokens.
        GL_INVALID_OPERATION is generated if glBeginQuery is executed while a query object of the same
            target is already active.
        GL_INVALID_OPERATION is generated if glEndQuery is executed when a query object of the same target
            is not active.
        GL_INVALID_OPERATION is generated if id is 0.
        GL_INVALID_OPERATION is generated if id is the name of an already active query object.
        GL_INVALID_OPERATION is generated if id refers to an existing query object whose type does not does
            not match target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginQuery.xhtml
        """
        pass

    def bind_attrib_location(self, program: int, index: int, name: bytes):
        """
        Associates a generic vertex attribute index with a named attribute variable

        Wrapper for glBindAttribLocation

        Parameters
        ----------
        program: int
            Specifies the handle of the program object in which the association is to be made.
        index: int
            Specifies the index of the generic vertex attribute to be bound.
        name: bytes
            Specifies a null terminated string containing the name of the vertex shader attribute variable to
            which index is to be bound.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_OPERATION is generated if name starts with the reserved prefix "gl_".
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindAttribLocation.xhtml
        """
        pass

    def bind_buffer(self, target: int, buffer: int):
        """
        Bind a named buffer object

        Wrapper for glBindBuffer

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound, which must be one of the buffer binding
            targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER Vertex attributes
            GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy source
            GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch
            commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array
            indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        buffer: int
            Specifies the name of a buffer object.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of the allowable values.
        GL_INVALID_VALUE is generated if buffer is not a name previously returned from a call to
            glGenBuffers.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindBuffer.xhtml
        """
        pass

    def bind_texture(self, target: int, texture: int):
        """
        Bind a named texture to a texturing target

        Wrapper for glBindTexture

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound. Must be one of GL_TEXTURE_1D, GL_TEXTURE_2D,
            GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_RECTANGLE, GL_TEXTURE_CUBE_MAP,
            GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_BUFFER, GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY.
        texture: int
            Specifies the name of a texture.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of the allowable values.
        GL_INVALID_VALUE is generated if texture is not a name returned from a previous call to
            glGenTextures.
        GL_INVALID_OPERATION is generated if texture was previously created with a target that doesn't
            match that of target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindTexture.xhtml
        """
        pass

    def blend_color(self, red: float, green: float, blue: float, alpha: float):
        """
        Set the blend color

        Wrapper for glBlendColor

        Parameters
        ----------
        red, green, blue, alpha: float
            specify the components of GL_BLEND_COLOR

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendColor.xhtml
        """
        pass

    def blend_equation(self, mode: int):
        """
        Specify the equation used for both the RGB blend equation and the Alpha blend equation

        Wrapper for glBlendEquation

        Parameters
        ----------
        mode: int
            specifies how source and destination colors are combined. It must be GL_FUNC_ADD, GL_FUNC_SUBTRACT,
            GL_FUNC_REVERSE_SUBTRACT, GL_MIN, GL_MAX.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of GL_FUNC_ADD, GL_FUNC_SUBTRACT,
            GL_FUNC_REVERSE_SUBTRACT, GL_MAX, or GL_MIN.
        GL_INVALID_VALUE is generated by glBlendEquationi if buf is greater than or equal to the value of
            GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendEquation.xhtml
        """
        pass

    def blend_equation_separate(self, mode_rgb: int, mode_alpha: int):
        """
        Set the RGB blend equation and the alpha blend equation separately

        Wrapper for glBlendEquationSeparate

        Parameters
        ----------

        Raises
        ------
        GL_INVALID_ENUM is generated if either modeRGB or modeAlpha is not one of GL_FUNC_ADD,
            GL_FUNC_SUBTRACT, GL_FUNC_REVERSE_SUBTRACT, GL_MAX, or GL_MIN.
        GL_INVALID_VALUE is generated by glBlendEquationSeparatei if buf is greater than or equal to the
            value of GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendEquationSeparate.xhtml
        """
        pass

    def blend_func(self, sfactor: int, dfactor: int):
        """
        Specify pixel arithmetic

        Wrapper for glBlendFunc

        Parameters
        ----------
        sfactor: int
            Specifies how the red, green, blue, and alpha source blending factors are computed. The initial
            value is GL_ONE.
        dfactor: int
            Specifies how the red, green, blue, and alpha destination blending factors are computed. The
            following symbolic constants are accepted: GL_ZERO, GL_ONE, GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR,
            GL_DST_COLOR, GL_ONE_MINUS_DST_COLOR, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_DST_ALPHA,
            GL_ONE_MINUS_DST_ALPHA. GL_CONSTANT_COLOR, GL_ONE_MINUS_CONSTANT_COLOR, GL_CONSTANT_ALPHA, and
            GL_ONE_MINUS_CONSTANT_ALPHA. The initial value is GL_ZERO.

        Raises
        ------
        GL_INVALID_ENUM is generated if either sfactor or dfactor is not an accepted value.
        GL_INVALID_VALUE is generated by glBlendFunci if buf is greater than or equal to the value of
            GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFunc.xhtml
        """
        pass

    def blend_func_separate(self, src_rgb: int, dst_rgb: int, src_alpha: int, dst_alpha: int):
        """
        Specify pixel arithmetic for RGB and alpha components separately

        Wrapper for glBlendFuncSeparate

        Parameters
        ----------

        Raises
        ------
        GL_INVALID_ENUM is generated if either srcRGB or dstRGB is not an accepted value.
        GL_INVALID_VALUE is generated by glBlendFuncSeparatei if buf is greater than or equal to the value
            of GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFuncSeparate.xhtml
        """
        pass

    def buffer_data(self, target: int, size: POINTER(c_uint32), data: c_void_p, usage: int):
        """
        Creates and initializes a buffer object's data store

        Wrapper for glBufferData

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glBufferData, which must be one of the
            buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER Vertex
            attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy source
            GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch
            commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array
            indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        size: POINTER(c_uint32)
            Specifies the size in bytes of the buffer object's new data store.
        data: c_void_p
            Specifies a pointer to data that will be copied into the data store for initialization, or NULL if
            no data is to be copied.
        usage: int
            Specifies the expected usage pattern of the data store. The symbolic constant must be
            GL_STREAM_DRAW, GL_STREAM_READ, GL_STREAM_COPY, GL_STATIC_DRAW, GL_STATIC_READ, GL_STATIC_COPY,
            GL_DYNAMIC_DRAW, GL_DYNAMIC_READ, or GL_DYNAMIC_COPY.

        Raises
        ------
        GL_INVALID_ENUM is generated by glBufferData if target is not one of the accepted buffer targets.
        GL_INVALID_ENUM is generated if usage is not GL_STREAM_DRAW, GL_STREAM_READ, GL_STREAM_COPY,
            GL_STATIC_DRAW, GL_STATIC_READ, GL_STATIC_COPY, GL_DYNAMIC_DRAW, GL_DYNAMIC_READ, or
            GL_DYNAMIC_COPY.
        GL_INVALID_VALUE is generated if size is negative.
        GL_INVALID_OPERATION is generated by glBufferData if the reserved buffer object name 0 is bound to
            target.
        GL_INVALID_OPERATION is generated by glNamedBufferData if buffer is not the name of an existing
            buffer object.
        GL_INVALID_OPERATION is generated if the GL_BUFFER_IMMUTABLE_STORAGE flag of the buffer object is
            GL_TRUE.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store with the specified size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBufferData.xhtml
        """
        pass

    def buffer_sub_data(self, target: int, offset: POINTER(c_int), size: POINTER(c_uint32), data: c_void_p):
        """
        Updates a subset of a buffer object's data store

        Wrapper for glBufferSubData

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glBufferSubData, which must be one of
            the buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER
            Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy
            source GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute
            dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex
            array indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        offset: POINTER(c_int)
            Specifies the offset into the buffer object's data store where data replacement will begin,
            measured in bytes.
        size: POINTER(c_uint32)
            Specifies the size in bytes of the data store region being replaced.
        data: c_void_p
            Specifies a pointer to the new data that will be copied into the data store.

        Raises
        ------
        GL_INVALID_ENUM is generated by glBufferSubData if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glBufferSubData if zero is bound to target.
        GL_INVALID_OPERATION is generated by glNamedBufferSubData if buffer is not the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if offset or size is negative, or if $offset + size$ is greater than
            the value of GL_BUFFER_SIZE for the specified buffer object.
        GL_INVALID_OPERATION is generated if any part of the specified range of the buffer object is mapped
            with glMapBufferRange or glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set
            in the glMapBufferRange access flags.
        GL_INVALID_OPERATION is generated if the value of the GL_BUFFER_IMMUTABLE_STORAGE flag of the
            buffer object is GL_TRUE and the value of GL_BUFFER_STORAGE_FLAGS for the buffer object does not
            have the GL_DYNAMIC_STORAGE_BIT bit set.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBufferSubData.xhtml
        """
        pass

    def clear(self, mask: int):
        """
        Clear buffers to preset values

        Wrapper for glClear

        Parameters
        ----------
        mask: int
            Bitwise OR of masks that indicate the buffers to be cleared. The three masks are
            GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, and GL_STENCIL_BUFFER_BIT.

        Raises
        ------
        GL_INVALID_VALUE is generated if any bit other than the three defined bits is set in mask.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClear.xhtml
        """
        pass

    def clear_color(self, red: float, green: float, blue: float, alpha: float):
        """
        Specify clear values for the color buffers

        Wrapper for glClearColor

        Parameters
        ----------
        red, green, blue, alpha: float
            Specify the red, green, blue, and alpha values used when the color buffers are cleared. The initial
            values are all 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearColor.xhtml
        """
        pass

    def clear_depth(self, depth: float):
        """
        Specify the clear value for the depth buffer

        Wrapper for glClearDepth

        Parameters
        ----------
        depth: float
            Specifies the depth value used when the depth buffer is cleared. The initial value is 1.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearDepth.xhtml
        """
        pass

    def clear_stencil(self, s: int):
        """
        Specify the clear value for the stencil buffer

        Wrapper for glClearStencil

        Parameters
        ----------
        s: int
            Specifies the index used when the stencil buffer is cleared. The initial value is 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearStencil.xhtml
        """
        pass

    def color_mask(self, red: bool, green: bool, blue: bool, alpha: bool):
        """
        Enable and disable writing of frame buffer color components

        Wrapper for glColorMask

        Parameters
        ----------
        red, green, blue, alpha: bool
            Specify whether red, green, blue, and alpha are to be written into the frame buffer. The initial
            values are all GL_TRUE, indicating that the color components are written.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glColorMask.xhtml
        """
        pass

    def compile_shader(self, shader: int):
        """
        Compiles a shader object

        Wrapper for glCompileShader

        Parameters
        ----------
        shader: int
            Specifies the shader object to be compiled.

        Raises
        ------
        GL_INVALID_VALUE is generated if shader is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if shader is not a shader object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCompileShader.xhtml
        """
        pass

    def create_program(self) -> int:
        """
        Creates a program object

        Wrapper for glCreateProgram

        Raises
        ------
        This function returns 0 if an error occurs creating the program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateProgram.xhtml
        """
        pass

    def create_shader(self, shader_type: int) -> int:
        """
        Creates a shader object

        Wrapper for glCreateShader

        Parameters
        ----------

        Raises
        ------
        This function returns 0 if an error occurs creating the shader object.
        GL_INVALID_ENUM is generated if shaderType is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateShader.xhtml
        """
        pass

    def cull_face(self, mode: int):
        """
        Specify whether front- or back-facing facets can be culled

        Wrapper for glCullFace

        Parameters
        ----------
        mode: int
            Specifies whether front- or back-facing facets are candidates for culling. Symbolic constants
            GL_FRONT, GL_BACK, and GL_FRONT_AND_BACK are accepted. The initial value is GL_BACK.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCullFace.xhtml
        """
        pass

    def delete_buffers(self, n: int, buffers: POINTER(c_uint)):
        """
        Delete named buffer objects

        Wrapper for glDeleteBuffers

        Parameters
        ----------
        n: int
            Specifies the number of buffer objects to be deleted.
        buffers: POINTER(c_uint)
            Specifies an array of buffer objects to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteBuffers.xhtml
        """
        pass

    def delete_program(self, program: int):
        """
        Deletes a program object

        Wrapper for glDeleteProgram

        Parameters
        ----------
        program: int
            Specifies the program object to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteProgram.xhtml
        """
        pass

    def delete_queries(self, n: int, ids: POINTER(c_uint)):
        """
        Delete named query objects

        Wrapper for glDeleteQueries

        Parameters
        ----------
        n: int
            Specifies the number of query objects to be deleted.
        ids: POINTER(c_uint)
            Specifies an array of query objects to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteQueries.xhtml
        """
        pass

    def delete_shader(self, shader: int):
        """
        Deletes a shader object

        Wrapper for glDeleteShader

        Parameters
        ----------
        shader: int
            Specifies the shader object to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if shader is not a value generated by OpenGL.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteShader.xhtml
        """
        pass

    def delete_textures(self, n: int, textures: POINTER(c_uint)):
        """
        Delete named textures

        Wrapper for glDeleteTextures

        Parameters
        ----------
        n: int
            Specifies the number of textures to be deleted.
        textures: POINTER(c_uint)
            Specifies an array of textures to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteTextures.xhtml
        """
        pass

    def depth_func(self, func: int):
        """
        Specify the value used for depth buffer comparisons

        Wrapper for glDepthFunc

        Parameters
        ----------
        func: int
            Specifies the depth comparison function. Symbolic constants GL_NEVER, GL_LESS, GL_EQUAL, GL_LEQUAL,
            GL_GREATER, GL_NOTEQUAL, GL_GEQUAL, and GL_ALWAYS are accepted. The initial value is GL_LESS.

        Raises
        ------
        GL_INVALID_ENUM is generated if func is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthFunc.xhtml
        """
        pass

    def depth_mask(self, flag: bool):
        """
        Enable or disable writing into the depth buffer

        Wrapper for glDepthMask

        Parameters
        ----------
        flag: bool
            Specifies whether the depth buffer is enabled for writing. If flag is GL_FALSE, depth buffer
            writing is disabled. Otherwise, it is enabled. Initially, depth buffer writing is enabled.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthMask.xhtml
        """
        pass

    def depth_range(self, near_val: float, far_val: float):
        """
        Specify mapping of depth values from normalized device coordinates to window coordinates

        Wrapper for glDepthRange

        Parameters
        ----------

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthRange.xhtml
        """
        pass

    def detach_shader(self, program: int, shader: int):
        """
        Detaches a shader object from a program object to which it is attached

        Wrapper for glDetachShader

        Parameters
        ----------
        program: int
            Specifies the program object from which to detach the shader object.
        shader: int
            Specifies the shader object to be detached.

        Raises
        ------
        GL_INVALID_VALUE is generated if either program or shader is a value that was not generated by
            OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if shader is not a shader object.
        GL_INVALID_OPERATION is generated if shader is not attached to program.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDetachShader.xhtml
        """
        pass

    def draw_arrays(self, mode: int, first: int, count: int):
        """
        Render primitives from array data

        Wrapper for glDrawArrays

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        first: int
            Specifies the starting index in the enabled arrays.
        count: int
            Specifies the number of indices to be rendered.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if count is negative.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawArrays.xhtml
        """
        pass

    def draw_buffer(self, buf: int):
        """
        Specify which color buffers are to be drawn into

        Wrapper for glDrawBuffer

        Parameters
        ----------
        buf: int
            For default framebuffer, the argument specifies up to four color buffers to be drawn into. Symbolic
            constants GL_NONE, GL_FRONT_LEFT, GL_FRONT_RIGHT, GL_BACK_LEFT, GL_BACK_RIGHT, GL_FRONT, GL_BACK,
            GL_LEFT, GL_RIGHT, and GL_FRONT_AND_BACK are accepted. The initial value is GL_FRONT for
            single-buffered contexts, and GL_BACK for double-buffered contexts. For framebuffer objects,
            GL_COLOR_ATTACHMENT$m$ and GL_NONE enums are accepted, where $m$ is a value between 0 and
            GL_MAX_COLOR_ATTACHMENTS.

        Raises
        ------
        GL_INVALID_OPERATION error is generated by glNamedFramebufferDrawBuffer if framebuffer is not zero
            or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if buf is not an accepted value.
        GL_INVALID_OPERATION is generated if the default framebuffer is affected and none of the buffers
            indicated by buf exists.
        GL_INVALID_OPERATION is generated if a framebuffer object is affected and buf is not equal to
            GL_NONE or GL_COLOR_ATTACHMENT$m$, where $m$ is a value between 0 and GL_MAX_COLOR_ATTACHMENTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawBuffer.xhtml
        """
        pass

    def draw_buffers(self, n: int, bufs: POINTER(c_uint32)):
        """
        Specifies a list of color buffers to be drawn into

        Wrapper for glDrawBuffers

        Parameters
        ----------
        n: int
            Specifies the number of buffers in bufs.
        bufs: POINTER(c_uint32)
            Points to an array of symbolic constants specifying the buffers into which fragment colors or data
            values will be written.
        n: int
            The fragment shader output value is written into the n th color attachment of the current
            framebuffer. n may range from zero to the value of GL_MAX_COLOR_ATTACHMENTS.

        Raises
        ------
        GL_INVALID_OPERATION error is generated by glNamedFramebufferDrawBuffers if framebuffer is not zero
            or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if one of the values in bufs is not an accepted value.
        GL_INVALID_ENUM is generated if the API call refers to the default framebuffer and one or more of
            the values in bufs is one of the GL_COLOR_ATTACHMENT n tokens.
        GL_INVALID_ENUM is generated if the API call refers to a framebuffer object and one or more of the
            values in bufs is anything other than GL_NONE or one of the GL_COLOR_ATTACHMENT n tokens.
        GL_INVALID_ENUM is generated if n is less than 0.
        GL_INVALID_OPERATION is generated if a symbolic constant other than GL_NONE appears more than once
            in bufs.
        GL_INVALID_OPERATION is generated if any of the entries in bufs (other than GL_NONE) indicates a
            color buffer that does not exist in the current GL context.
        GL_INVALID_OPERATION is generated if any value in bufs is GL_BACK, and n is not one.
        GL_INVALID_VALUE is generated if n is greater than GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawBuffers.xhtml
        """
        pass

    def draw_elements(self, mode: int, count: int, type: int, indices: c_void_p):
        """
        Render primitives from array data

        Wrapper for glDrawElements

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if count is negative.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawElements.xhtml
        """
        pass

    def draw_range_elements(self, mode: int, start: int, end: int, count: int, type: int, indices: c_void_p):
        """
        Render primitives from array data

        Wrapper for glDrawRangeElements

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        start: int
            Specifies the minimum array index contained in indices.
        end: int
            Specifies the maximum array index contained in indices.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.

        Raises
        ------
        It is an error for indices to lie outside the range start end, but implementations may not check
            for this situation. Such indices cause implementation-dependent behavior.
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if count is negative.
        GL_INVALID_VALUE is generated if end &lt; start.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawRangeElements.xhtml
        """
        pass

    def enable(self, cap: int):
        """
        Enable or disable server-side GL capabilities

        Wrapper for glEnable

        Parameters
        ----------
        cap: int
            Specifies a symbolic constant indicating a GL capability.

        Raises
        ------
        GL_INVALID_ENUM is generated if cap is not one of the values listed previously.
        GL_INVALID_VALUE is generated by glEnablei and glDisablei if index is greater than or equal to the
            number of indexed capabilities for cap.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml
        """
        pass

    def disable(self, cap: int):
        """
        Enable or disable server-side GL capabilities

        Wrapper for glDisable

        Parameters
        ----------
        cap: int
            Specifies a symbolic constant indicating a GL capability.

        Raises
        ------
        GL_INVALID_ENUM is generated if cap is not one of the values listed previously.
        GL_INVALID_VALUE is generated by glEnablei and glDisablei if index is greater than or equal to the
            number of indexed capabilities for cap.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml
        """
        pass

    def enable_vertex_attrib_array(self, index: int):
        """
        Enable or disable a generic vertex attribute array

        Wrapper for glEnableVertexAttribArray

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be enabled or disabled.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glEnableVertexAttribArray and glDisableVertexAttribArray if no
            vertex array object is bound.
        GL_INVALID_OPERATION is generated by glEnableVertexArrayAttrib and glDisableVertexArrayAttrib if
            vaobj is not the name of an existing vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnableVertexAttribArray.xhtml
        """
        pass

    def disable_vertex_attrib_array(self, index: int):
        """
        Enable or disable a generic vertex attribute array

        Wrapper for glDisableVertexAttribArray

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be enabled or disabled.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glEnableVertexAttribArray and glDisableVertexAttribArray if no
            vertex array object is bound.
        GL_INVALID_OPERATION is generated by glEnableVertexArrayAttrib and glDisableVertexArrayAttrib if
            vaobj is not the name of an existing vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnableVertexAttribArray.xhtml
        """
        pass

    def finish(self):
        """
        Block until all GL execution is complete

        Wrapper for glFinish

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFinish.xhtml
        """
        pass

    def flush(self):
        """
        Force execution of GL commands in finite time

        Wrapper for glFlush

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFlush.xhtml
        """
        pass

    def front_face(self, mode: int):
        """
        Define front- and back-facing polygons

        Wrapper for glFrontFace

        Parameters
        ----------
        mode: int
            Specifies the orientation of front-facing polygons. GL_CW and GL_CCW are accepted. The initial
            value is GL_CCW.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFrontFace.xhtml
        """
        pass

    def gen_buffers(self, n: int, buffers: POINTER(c_uint)):
        """
        Generate buffer object names

        Wrapper for glGenBuffers

        Parameters
        ----------
        n: int
            Specifies the number of buffer object names to be generated.
        buffers: POINTER(c_uint)
            Specifies an array in which the generated buffer object names are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenBuffers.xhtml
        """
        pass

    def gen_queries(self, n: int, ids: POINTER(c_uint)):
        """
        Generate query object names

        Wrapper for glGenQueries

        Parameters
        ----------
        n: int
            Specifies the number of query object names to be generated.
        ids: POINTER(c_uint)
            Specifies an array in which the generated query object names are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenQueries.xhtml
        """
        pass

    def gen_textures(self, n: int, textures: POINTER(c_uint)):
        """
        Generate texture names

        Wrapper for glGenTextures

        Parameters
        ----------
        n: int
            Specifies the number of texture names to be generated.
        textures: POINTER(c_uint)
            Specifies an array in which the generated texture names are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenTextures.xhtml
        """
        pass

    def get_booleanv(self, pname: int, data: POINTER(c_bool)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetBooleanv

        Parameters
        ----------
        pname: int
            Specifies the parameter value to be returned for non-indexed versions of glGet. The symbolic
            constants in the list below are accepted.
        data: POINTER(c_bool)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_doublev(self, pname: int, data: POINTER(c_double)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetDoublev

        Parameters
        ----------
        pname: int
            Specifies the parameter value to be returned for non-indexed versions of glGet. The symbolic
            constants in the list below are accepted.
        data: POINTER(c_double)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_floatv(self, pname: int, data: POINTER(c_float)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetFloatv

        Parameters
        ----------
        pname: int
            Specifies the parameter value to be returned for non-indexed versions of glGet. The symbolic
            constants in the list below are accepted.
        data: POINTER(c_float)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_integerv(self, pname: int, data: POINTER(c_int)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetIntegerv

        Parameters
        ----------
        pname: int
            Specifies the parameter value to be returned for non-indexed versions of glGet. The symbolic
            constants in the list below are accepted.
        data: POINTER(c_int)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_active_attrib(self, program: int, index: int, buf_size: int, length: POINTER(c_uint32), size: POINTER(c_int), type: POINTER(c_uint32), name: bytes):
        """
        Returns information about an active attribute variable for the specified program object

        Wrapper for glGetActiveAttrib

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        index: int
            Specifies the index of the attribute variable to be queried.
        length: POINTER(c_uint32)
            Returns the number of characters actually written by OpenGL in the string indicated by name
            (excluding the null terminator) if a value other than NULL is passed.
        size: POINTER(c_int)
            Returns the size of the attribute variable.
        type: POINTER(c_uint32)
            Returns the data type of the attribute variable.
        name: bytes
            Returns a null terminated string containing the name of the attribute variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_VALUE is generated if index is greater than or equal to the number of active attribute
            variables in program.
        GL_INVALID_VALUE is generated if bufSize is less than 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveAttrib.xhtml
        """
        pass

    def get_active_uniform(self, program: int, index: int, buf_size: int, length: POINTER(c_uint32), size: POINTER(c_int), type: POINTER(c_uint32), name: bytes):
        """
        Returns information about an active uniform variable for the specified program object

        Wrapper for glGetActiveUniform

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        index: int
            Specifies the index of the uniform variable to be queried.
        length: POINTER(c_uint32)
            Returns the number of characters actually written by OpenGL in the string indicated by name
            (excluding the null terminator) if a value other than NULL is passed.
        size: POINTER(c_int)
            Returns the size of the uniform variable.
        type: POINTER(c_uint32)
            Returns the data type of the uniform variable.
        name: bytes
            Returns a null terminated string containing the name of the uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_VALUE is generated if index is greater than or equal to the number of active uniform
            variables in program.
        GL_INVALID_VALUE is generated if bufSize is less than 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveUniform.xhtml
        """
        pass

    def get_attached_shaders(self, program: int, max_count: int, count: POINTER(c_uint32), shaders: POINTER(c_uint)):
        """
        Returns the handles of the shader objects attached to a program object

        Wrapper for glGetAttachedShaders

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        count: POINTER(c_uint32)
            Returns the number of names actually returned in shaders.
        shaders: POINTER(c_uint)
            Specifies an array that is used to return the names of attached shader objects.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_VALUE is generated if maxCount is less than 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetAttachedShaders.xhtml
        """
        pass

    def get_attrib_location(self, program: int, name: bytes) -> int:
        """
        Returns the location of an attribute variable

        Wrapper for glGetAttribLocation

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        name: bytes
            Points to a null terminated string containing the name of the attribute variable whose location is
            to be queried.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetAttribLocation.xhtml
        """
        pass

    def get_buffer_parameteriv(self, target: int, value: int, data: POINTER(c_int)):
        """
        Return parameters of a buffer object

        Wrapper for glGetBufferParameteriv

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glGetBufferParameteriv and
            glGetBufferParameteri64v. Must be one of the buffer binding targets in the following table: Buffer
            Binding Target Purpose GL_ARRAY_BUFFER Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter
            storage GL_COPY_READ_BUFFER Buffer copy source GL_COPY_WRITE_BUFFER Buffer copy destination
            GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect
            command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array indices GL_PIXEL_PACK_BUFFER Pixel read
            target GL_PIXEL_UNPACK_BUFFER Texture data source GL_QUERY_BUFFER Query result buffer
            GL_SHADER_STORAGE_BUFFER Read-write storage for shaders GL_TEXTURE_BUFFER Texture data buffer
            GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer GL_UNIFORM_BUFFER Uniform block storage
        value: int
            Specifies the name of the buffer object parameter to query.
        data: POINTER(c_int)
            Returns the requested parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetBufferParameter* if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glGetBufferParameter* if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferParameter* if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if pname is not one of the buffer object parameter names described
            above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferParameter.xhtml
        """
        pass

    def get_buffer_pointerv(self, target: int, pname: int, params: POINTER(c_void_p)):
        """
        Return the pointer to a mapped buffer object's data store

        Wrapper for glGetBufferPointerv

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glGetBufferPointerv, which must be one
            of the buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER
            Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy
            source GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute
            dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex
            array indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        pname: int
            Specifies the name of the pointer to be returned. Must be GL_BUFFER_MAP_POINTER.
        params: POINTER(c_void_p)
            Returns the pointer value specified by pname.

        Raises
        ------
        GL_INVALID_ENUM is generated if by glGetBufferPointerv if target is not one of the accepted buffer
            targets, or if pname is not GL_BUFFER_MAP_POINTER.
        GL_INVALID_OPERATION is generated by glGetBufferPointerv if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferPointerv if buffer is not the name of an
            existing buffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferPointerv.xhtml
        """
        pass

    def get_buffer_sub_data(self, target: int, offset: POINTER(c_int), size: POINTER(c_uint32), data: c_void_p):
        """
        Returns a subset of a buffer object's data store

        Wrapper for glGetBufferSubData

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glGetBufferSubData, which must be one
            of the buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER
            Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy
            source GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute
            dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex
            array indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        offset: POINTER(c_int)
            Specifies the offset into the buffer object's data store from which data will be returned, measured
            in bytes.
        size: POINTER(c_uint32)
            Specifies the size in bytes of the data store region being returned.
        data: c_void_p
            Specifies a pointer to the location where buffer object data is returned.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetBufferSubData if target is not one of the generic buffer
            binding targets.
        GL_INVALID_OPERATION is generated by glGetBufferSubData if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferSubData if buffer is not the name of an
            existing buffer object.
        GL_INVALID_VALUE is generated if offset or size is negative, or if $offset + size$ is greater than
            the value of GL_BUFFER_SIZE for the buffer object.
        GL_INVALID_OPERATION is generated if the buffer object is mapped with glMapBufferRange or
            glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set in the glMapBufferRange
            access flags.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferSubData.xhtml
        """
        pass

    def get_compressed_tex_image(self, target: int, level: int, pixels: c_void_p):
        """
        Return a compressed texture image

        Wrapper for glGetCompressedTexImage

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetCompressedTexImage and
            glGetnCompressedTexImage functions. GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D,
            GL_TEXTURE_2D_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_CUBE_MAP_POSITIVE_X,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Z, and GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, GL_TEXTURE_RECTANGLE are
            accepted.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level
            $n$ is the $n$-th mipmap reduction image.
        pixels: c_void_p
            Returns the compressed texture image.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glGetCompressedTextureImage if texture is not the name of an
            existing texture object.
        GL_INVALID_VALUE is generated if level is less than zero or greater than the maximum number of LODs
            permitted by the implementation.
        GL_INVALID_OPERATION is generated if glGetCompressedTexImage, glGetnCompressedTexImage, and
            glGetCompressedTextureImage is used to retrieve a texture that is in an uncompressed internal
            format.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target, the buffer storage was not initialized with glBufferStorage using
            GL_MAP_PERSISTENT_BIT flag, and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and the data would be packed to the buffer object such that the memory
            writes required would exceed the data store size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetCompressedTexImage.xhtml
        """
        pass

    def get_error(self) -> int:
        """
        Return error information

        Wrapper for glGetError

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetError.xhtml
        """
        pass

    def get_programiv(self, program: int, pname: int, params: POINTER(c_int)):
        """
        Returns a parameter from a program object

        Wrapper for glGetProgramiv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        pname: int
            Specifies the object parameter. Accepted symbolic names are GL_DELETE_STATUS, GL_LINK_STATUS,
            GL_VALIDATE_STATUS, GL_INFO_LOG_LENGTH, GL_ATTACHED_SHADERS, GL_ACTIVE_ATOMIC_COUNTER_BUFFERS,
            GL_ACTIVE_ATTRIBUTES, GL_ACTIVE_ATTRIBUTE_MAX_LENGTH, GL_ACTIVE_UNIFORMS, GL_ACTIVE_UNIFORM_BLOCKS,
            GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH, GL_ACTIVE_UNIFORM_MAX_LENGTH, GL_COMPUTE_WORK_GROUP_SIZE
            GL_PROGRAM_BINARY_LENGTH, GL_TRANSFORM_FEEDBACK_BUFFER_MODE, GL_TRANSFORM_FEEDBACK_VARYINGS,
            GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH, GL_GEOMETRY_VERTICES_OUT, GL_GEOMETRY_INPUT_TYPE, and
            GL_GEOMETRY_OUTPUT_TYPE.
        params: POINTER(c_int)
            Returns the requested object parameter.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program does not refer to a program object.
        GL_INVALID_OPERATION is generated if pname is GL_GEOMETRY_VERTICES_OUT, GL_GEOMETRY_INPUT_TYPE, or
            GL_GEOMETRY_OUTPUT_TYPE, and program does not contain a geometry shader.
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if pname is GL_COMPUTE_WORK_GROUP_SIZE and program does not
            contain a binary for the compute shader stage.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgram.xhtml
        """
        pass

    def get_program_info_log(self, program: int, max_length: int, length: POINTER(c_uint32), info_log: bytes):
        """
        Returns the information log for a program object

        Wrapper for glGetProgramInfoLog

        Parameters
        ----------
        program: int
            Specifies the program object whose information log is to be queried.
        length: POINTER(c_uint32)
            Returns the length of the string returned in infoLog (excluding the null terminator).

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_VALUE is generated if maxLength is less than 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramInfoLog.xhtml
        """
        pass

    def get_queryiv(self, target: int, pname: int, params: POINTER(c_int)):
        """
        Return parameters of a query object target

        Wrapper for glGetQueryiv

        Parameters
        ----------
        target: int
            Specifies a query object target. Must be GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED,
            GL_ANY_SAMPLES_PASSED_CONSERVATIVE GL_PRIMITIVES_GENERATED,
            GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN, GL_TIME_ELAPSED, or GL_TIMESTAMP.
        pname: int
            Specifies the symbolic name of a query object target parameter. Accepted values are
            GL_CURRENT_QUERY or GL_QUERY_COUNTER_BITS.
        params: POINTER(c_int)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_ENUM is generated if target or pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetQueryiv.xhtml
        """
        pass

    def get_query_objectiv(self, id: int, pname: int, params: POINTER(c_int)):
        """
        Return parameters of a query object

        Wrapper for glGetQueryObjectiv

        Parameters
        ----------
        id: int
            Specifies the name of a query object.
        pname: int
            Specifies the symbolic name of a query object parameter. Accepted values are GL_QUERY_RESULT or
            GL_QUERY_RESULT_AVAILABLE.
        params: POINTER(c_int)
            If a buffer is bound to the GL_QUERY_RESULT_BUFFER target, then params is treated as an offset to a
            location within that buffer's data store to receive the result of the query. If no buffer is bound
            to GL_QUERY_RESULT_BUFFER, then params is treated as an address in client memory of a variable to
            receive the resulting data.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if id is not the name of a query object.
        GL_INVALID_OPERATION is generated if id is the name of a currently active query object.
        GL_INVALID_OPERATION is generated if a buffer is currently bound to the GL_QUERY_RESULT_BUFFER
            target and the command would cause data to be written beyond the bounds of that buffer's data
            store.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetQueryObject.xhtml
        """
        pass

    def get_query_objectuiv(self, id: int, pname: int, params: POINTER(c_uint)):
        """
        Return parameters of a query object

        Wrapper for glGetQueryObjectuiv

        Parameters
        ----------
        id: int
            Specifies the name of a query object.
        pname: int
            Specifies the symbolic name of a query object parameter. Accepted values are GL_QUERY_RESULT or
            GL_QUERY_RESULT_AVAILABLE.
        params: POINTER(c_uint)
            If a buffer is bound to the GL_QUERY_RESULT_BUFFER target, then params is treated as an offset to a
            location within that buffer's data store to receive the result of the query. If no buffer is bound
            to GL_QUERY_RESULT_BUFFER, then params is treated as an address in client memory of a variable to
            receive the resulting data.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if id is not the name of a query object.
        GL_INVALID_OPERATION is generated if id is the name of a currently active query object.
        GL_INVALID_OPERATION is generated if a buffer is currently bound to the GL_QUERY_RESULT_BUFFER
            target and the command would cause data to be written beyond the bounds of that buffer's data
            store.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetQueryObject.xhtml
        """
        pass

    def get_shaderiv(self, shader: int, pname: int, params: POINTER(c_int)):
        """
        Returns a parameter from a shader object

        Wrapper for glGetShaderiv

        Parameters
        ----------
        shader: int
            Specifies the shader object to be queried.
        pname: int
            Specifies the object parameter. Accepted symbolic names are GL_SHADER_TYPE, GL_DELETE_STATUS,
            GL_COMPILE_STATUS, GL_INFO_LOG_LENGTH, GL_SHADER_SOURCE_LENGTH.
        params: POINTER(c_int)
            Returns the requested object parameter.

        Raises
        ------
        GL_INVALID_VALUE is generated if shader is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if shader does not refer to a shader object.
        GL_INVALID_ENUM is generated if pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShader.xhtml
        """
        pass

    def get_shader_info_log(self, shader: int, max_length: int, length: POINTER(c_uint32), info_log: bytes):
        """
        Returns the information log for a shader object

        Wrapper for glGetShaderInfoLog

        Parameters
        ----------
        shader: int
            Specifies the shader object whose information log is to be queried.
        length: POINTER(c_uint32)
            Returns the length of the string returned in infoLog (excluding the null terminator).

        Raises
        ------
        GL_INVALID_VALUE is generated if shader is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if shader is not a shader object.
        GL_INVALID_VALUE is generated if maxLength is less than 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShaderInfoLog.xhtml
        """
        pass

    def get_shader_source(self, shader: int, buf_size: int, length: POINTER(c_uint32), source: bytes):
        """
        Returns the source code string from a shader object

        Wrapper for glGetShaderSource

        Parameters
        ----------
        shader: int
            Specifies the shader object to be queried.
        length: POINTER(c_uint32)
            Returns the length of the string returned in source (excluding the null terminator).
        source: bytes
            Specifies an array of characters that is used to return the source code string.

        Raises
        ------
        GL_INVALID_VALUE is generated if shader is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if shader is not a shader object.
        GL_INVALID_VALUE is generated if bufSize is less than 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShaderSource.xhtml
        """
        pass

    def get_string(self, name: int) -> POINTER(c_ubyte):
        """
        Return a string describing the current GL connection

        Wrapper for glGetString

        Parameters
        ----------
        name: int
            Specifies a symbolic constant, one of GL_VENDOR, GL_RENDERER, GL_VERSION, or
            GL_SHADING_LANGUAGE_VERSION. Additionally, glGetStringi accepts the GL_EXTENSIONS token.

        Raises
        ------
        GL_INVALID_ENUM is generated if name is not an accepted value.
        GL_INVALID_VALUE is generated by glGetStringi if index is outside the valid range for indexed state
            name.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetString.xhtml
        """
        pass

    def get_tex_image(self, target: int, level: int, format: int, type: int, pixels: c_void_p):
        """
        Return a texture image

        Wrapper for glGetTexImage

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexImage and glGetnTexImage functions.
            GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_RECTANGLE, GL_TEXTURE_CUBE_MAP_POSITIVE_X, GL_TEXTURE_CUBE_MAP_NEGATIVE_X,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, GL_TEXTURE_CUBE_MAP_POSITIVE_Z,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, and GL_TEXTURE_CUBE_MAP_ARRAY are acceptable.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n
            is the n th mipmap reduction image.
        format: int
            Specifies a pixel format for the returned data. The supported formats are GL_STENCIL_INDEX,
            GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL, GL_RED, GL_GREEN, GL_BLUE, GL_RG, GL_RGB, GL_RGBA, GL_BGR,
            GL_BGRA, GL_RED_INTEGER, GL_GREEN_INTEGER, GL_BLUE_INTEGER, GL_RG_INTEGER, GL_RGB_INTEGER,
            GL_RGBA_INTEGER, GL_BGR_INTEGER, GL_BGRA_INTEGER.
        type: int
            Specifies a pixel type for the returned data. The supported types are GL_UNSIGNED_BYTE, GL_BYTE,
            GL_UNSIGNED_SHORT, GL_SHORT, GL_UNSIGNED_INT, GL_INT, GL_HALF_FLOAT, GL_FLOAT,
            GL_UNSIGNED_BYTE_3_3_2, GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5,
            GL_UNSIGNED_SHORT_5_6_5_REV, GL_UNSIGNED_SHORT_4_4_4_4, GL_UNSIGNED_SHORT_4_4_4_4_REV,
            GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV, GL_UNSIGNED_INT_8_8_8_8,
            GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, GL_UNSIGNED_INT_2_10_10_10_REV,
            GL_UNSIGNED_INT_24_8, GL_UNSIGNED_INT_10F_11F_11F_REV, GL_UNSIGNED_INT_5_9_9_9_REV, and
            GL_FLOAT_32_UNSIGNED_INT_24_8_REV.
        pixels: c_void_p
            Returns the texture image. Should be a pointer to an array of the type specified by type.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetTexImage and glGetnTexImage functions if target is not an
            accepted value. These include:
        GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_RECTANGLE, GL_TEXTURE_CUBE_MAP_POSITIVE_X,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Z, and GL_TEXTURE_CUBE_MAP_NEGATIVE_Z for glGetTexImage and
            glGetnTexImage functions.
        GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_RECTANGLE, and GL_TEXTURE_CUBE_MAP for glGetTextureImage
            function.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml
        """
        pass

    def get_tex_level_parameterfv(self, target: int, level: int, pname: int, params: POINTER(c_float)):
        """
        Return texture parameter values for a specific level of detail

        Wrapper for glGetTexLevelParameterfv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexLevelParameterfv and
            glGetTexLevelParameteriv functions. Must be one of the following values: GL_TEXTURE_1D,
            GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_RECTANGLE,
            GL_TEXTURE_2D_MULTISAMPLE, GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_CUBE_MAP_POSITIVE_X,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Z, GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, GL_PROXY_TEXTURE_1D,
            GL_PROXY_TEXTURE_2D, GL_PROXY_TEXTURE_3D, GL_PROXY_TEXTURE_1D_ARRAY, GL_PROXY_TEXTURE_2D_ARRAY,
            GL_PROXY_TEXTURE_RECTANGLE, GL_PROXY_TEXTURE_2D_MULTISAMPLE, GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY,
            GL_PROXY_TEXTURE_CUBE_MAP, or GL_TEXTURE_BUFFER.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n
            is the n th mipmap reduction image.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_TEXTURE_WIDTH, GL_TEXTURE_HEIGHT,
            GL_TEXTURE_DEPTH, GL_TEXTURE_INTERNAL_FORMAT, GL_TEXTURE_RED_SIZE, GL_TEXTURE_GREEN_SIZE,
            GL_TEXTURE_BLUE_SIZE, GL_TEXTURE_ALPHA_SIZE, GL_TEXTURE_DEPTH_SIZE, GL_TEXTURE_COMPRESSED,
            GL_TEXTURE_COMPRESSED_IMAGE_SIZE, and GL_TEXTURE_BUFFER_OFFSET are accepted.
        params: POINTER(c_float)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glGetTextureLevelParameterfv and glGetTextureLevelParameteriv
            functions if texture is not the name of an existing texture object.
        GL_INVALID_ENUM is generated by glGetTexLevelParameterfv and glGetTexLevelParameteriv functions if
            target or pname is not an accepted value.
        GL_INVALID_VALUE is generated if level is less than 0.
        GL_INVALID_VALUE may be generated if level is greater than log 2 max, where max is the returned
            value of GL_MAX_TEXTURE_SIZE.
        GL_INVALID_VALUE is generated if target is GL_TEXTURE_BUFFER and level is not zero.
        GL_INVALID_OPERATION is generated if GL_TEXTURE_COMPRESSED_IMAGE_SIZE is queried on texture images
            with an uncompressed internal format or on proxy targets.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexLevelParameter.xhtml
        """
        pass

    def get_tex_level_parameteriv(self, target: int, level: int, pname: int, params: POINTER(c_int)):
        """
        Return texture parameter values for a specific level of detail

        Wrapper for glGetTexLevelParameteriv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexLevelParameterfv and
            glGetTexLevelParameteriv functions. Must be one of the following values: GL_TEXTURE_1D,
            GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_RECTANGLE,
            GL_TEXTURE_2D_MULTISAMPLE, GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_CUBE_MAP_POSITIVE_X,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Z, GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, GL_PROXY_TEXTURE_1D,
            GL_PROXY_TEXTURE_2D, GL_PROXY_TEXTURE_3D, GL_PROXY_TEXTURE_1D_ARRAY, GL_PROXY_TEXTURE_2D_ARRAY,
            GL_PROXY_TEXTURE_RECTANGLE, GL_PROXY_TEXTURE_2D_MULTISAMPLE, GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY,
            GL_PROXY_TEXTURE_CUBE_MAP, or GL_TEXTURE_BUFFER.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n
            is the n th mipmap reduction image.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_TEXTURE_WIDTH, GL_TEXTURE_HEIGHT,
            GL_TEXTURE_DEPTH, GL_TEXTURE_INTERNAL_FORMAT, GL_TEXTURE_RED_SIZE, GL_TEXTURE_GREEN_SIZE,
            GL_TEXTURE_BLUE_SIZE, GL_TEXTURE_ALPHA_SIZE, GL_TEXTURE_DEPTH_SIZE, GL_TEXTURE_COMPRESSED,
            GL_TEXTURE_COMPRESSED_IMAGE_SIZE, and GL_TEXTURE_BUFFER_OFFSET are accepted.
        params: POINTER(c_int)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glGetTextureLevelParameterfv and glGetTextureLevelParameteriv
            functions if texture is not the name of an existing texture object.
        GL_INVALID_ENUM is generated by glGetTexLevelParameterfv and glGetTexLevelParameteriv functions if
            target or pname is not an accepted value.
        GL_INVALID_VALUE is generated if level is less than 0.
        GL_INVALID_VALUE may be generated if level is greater than log 2 max, where max is the returned
            value of GL_MAX_TEXTURE_SIZE.
        GL_INVALID_VALUE is generated if target is GL_TEXTURE_BUFFER and level is not zero.
        GL_INVALID_OPERATION is generated if GL_TEXTURE_COMPRESSED_IMAGE_SIZE is queried on texture images
            with an uncompressed internal format or on proxy targets.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexLevelParameter.xhtml
        """
        pass

    def get_tex_parameterfv(self, target: int, pname: int, params: POINTER(c_float)):
        """
        Return texture parameter values

        Wrapper for glGetTexParameterfv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexParameterfv, glGetTexParameteriv,
            glGetTexParameterIiv, and glGetTexParameterIuiv functions. GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE, GL_TEXTURE_2D_MULTISAMPLE_ARRAY,
            GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_RECTANGLE, and GL_TEXTURE_CUBE_MAP_ARRAY are
            accepted.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_float)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_tex_parameteriv(self, target: int, pname: int, params: POINTER(c_int)):
        """
        Return texture parameter values

        Wrapper for glGetTexParameteriv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexParameterfv, glGetTexParameteriv,
            glGetTexParameterIiv, and glGetTexParameterIuiv functions. GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE, GL_TEXTURE_2D_MULTISAMPLE_ARRAY,
            GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_RECTANGLE, and GL_TEXTURE_CUBE_MAP_ARRAY are
            accepted.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_int)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_uniformfv(self, program: int, location: int, params: POINTER(c_float)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetUniformfv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_float)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def get_uniformiv(self, program: int, location: int, params: POINTER(c_int)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetUniformiv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_int)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def get_uniform_location(self, program: int, name: bytes) -> int:
        """
        Returns the location of a uniform variable

        Wrapper for glGetUniformLocation

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        name: bytes
            Points to a null terminated string containing the name of the uniform variable whose location is to
            be queried.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniformLocation.xhtml
        """
        pass

    def get_vertex_attribdv(self, index: int, pname: int, params: POINTER(c_double)):
        """
        Return a generic vertex attribute parameter

        Wrapper for glGetVertexAttribdv

        Parameters
        ----------
        index: int
            Specifies the generic vertex attribute parameter to be queried.
        pname: int
            Specifies the symbolic name of the vertex attribute parameter to be queried. Accepted values are
            GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING, GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or GL_CURRENT_VERTEX_ATTRIB.
        params: POINTER(c_double)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pname is not GL_CURRENT_VERTEX_ATTRIB and there is no
            currently bound vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if index is 0 and pname is GL_CURRENT_VERTEX_ATTRIB.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexAttrib.xhtml
        """
        pass

    def get_vertex_attribfv(self, index: int, pname: int, params: POINTER(c_float)):
        """
        Return a generic vertex attribute parameter

        Wrapper for glGetVertexAttribfv

        Parameters
        ----------
        index: int
            Specifies the generic vertex attribute parameter to be queried.
        pname: int
            Specifies the symbolic name of the vertex attribute parameter to be queried. Accepted values are
            GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING, GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or GL_CURRENT_VERTEX_ATTRIB.
        params: POINTER(c_float)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pname is not GL_CURRENT_VERTEX_ATTRIB and there is no
            currently bound vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if index is 0 and pname is GL_CURRENT_VERTEX_ATTRIB.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexAttrib.xhtml
        """
        pass

    def get_vertex_attribiv(self, index: int, pname: int, params: POINTER(c_int)):
        """
        Return a generic vertex attribute parameter

        Wrapper for glGetVertexAttribiv

        Parameters
        ----------
        index: int
            Specifies the generic vertex attribute parameter to be queried.
        pname: int
            Specifies the symbolic name of the vertex attribute parameter to be queried. Accepted values are
            GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING, GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or GL_CURRENT_VERTEX_ATTRIB.
        params: POINTER(c_int)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pname is not GL_CURRENT_VERTEX_ATTRIB and there is no
            currently bound vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if index is 0 and pname is GL_CURRENT_VERTEX_ATTRIB.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexAttrib.xhtml
        """
        pass

    def get_vertex_attrib_pointerv(self, index: int, pname: int, pointer: POINTER(c_void_p)):
        """
        Return the address of the specified generic vertex attribute pointer

        Wrapper for glGetVertexAttribPointerv

        Parameters
        ----------
        index: int
            Specifies the generic vertex attribute parameter to be returned.
        pname: int
            Specifies the symbolic name of the generic vertex attribute parameter to be returned. Must be
            GL_VERTEX_ATTRIB_ARRAY_POINTER.
        pointer: POINTER(c_void_p)
            Returns the pointer value.

        Raises
        ------
        GL_INVALID_OPERATION is generated if no vertex array object is currently bound.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexAttribPointerv.xhtml
        """
        pass

    def hint(self, target: int, mode: int):
        """
        Specify implementation-specific hints

        Wrapper for glHint

        Parameters
        ----------
        target: int
            Specifies a symbolic constant indicating the behavior to be controlled. GL_LINE_SMOOTH_HINT,
            GL_POLYGON_SMOOTH_HINT, GL_TEXTURE_COMPRESSION_HINT, and GL_FRAGMENT_SHADER_DERIVATIVE_HINT are
            accepted.
        mode: int
            Specifies a symbolic constant indicating the desired behavior. GL_FASTEST, GL_NICEST, and
            GL_DONT_CARE are accepted.

        Raises
        ------
        GL_INVALID_ENUM is generated if either target or mode is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glHint.xhtml
        """
        pass

    def is_buffer(self, buffer: int) -> bool:
        """
        Determine if a name corresponds to a buffer object

        Wrapper for glIsBuffer

        Parameters
        ----------
        buffer: int
            Specifies a value that may be the name of a buffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsBuffer.xhtml
        """
        pass

    def is_enabled(self, cap: int) -> bool:
        """
        Test whether a capability is enabled

        Wrapper for glIsEnabled

        Parameters
        ----------
        cap: int
            Specifies a symbolic constant indicating a GL capability.

        Raises
        ------
        GL_INVALID_ENUM is generated if cap is not an accepted value.
        GL_INVALID_VALUE is generated by glIsEnabledi if index is outside the valid range for the indexed
            state cap.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsEnabled.xhtml
        """
        pass

    def is_program(self, program: int) -> bool:
        """
        Determines if a name corresponds to a program object

        Wrapper for glIsProgram

        Parameters
        ----------
        program: int
            Specifies a potential program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsProgram.xhtml
        """
        pass

    def is_query(self, id: int) -> bool:
        """
        Determine if a name corresponds to a query object

        Wrapper for glIsQuery

        Parameters
        ----------
        id: int
            Specifies a value that may be the name of a query object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsQuery.xhtml
        """
        pass

    def is_shader(self, shader: int) -> bool:
        """
        Determines if a name corresponds to a shader object

        Wrapper for glIsShader

        Parameters
        ----------
        shader: int
            Specifies a potential shader object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsShader.xhtml
        """
        pass

    def is_texture(self, texture: int) -> bool:
        """
        Determine if a name corresponds to a texture

        Wrapper for glIsTexture

        Parameters
        ----------
        texture: int
            Specifies a value that may be the name of a texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsTexture.xhtml
        """
        pass

    def line_width(self, width: float):
        """
        Specify the width of rasterized lines

        Wrapper for glLineWidth

        Parameters
        ----------
        width: float
            Specifies the width of rasterized lines. The initial value is 1.

        Raises
        ------
        GL_INVALID_VALUE is generated if width is less than or equal to 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glLineWidth.xhtml
        """
        pass

    def link_program(self, program: int):
        """
        Links a program object

        Wrapper for glLinkProgram

        Parameters
        ----------
        program: int
            Specifies the handle of the program object to be linked.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program is the currently active program object and transform
            feedback mode is active.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glLinkProgram.xhtml
        """
        pass

    def logic_op(self, opcode: int):
        """
        Specify a logical pixel operation for rendering

        Wrapper for glLogicOp

        Parameters
        ----------
        opcode: int
            Specifies a symbolic constant that selects a logical operation. The following symbols are accepted:
            GL_CLEAR, GL_SET, GL_COPY, GL_COPY_INVERTED, GL_NOOP, GL_INVERT, GL_AND, GL_NAND, GL_OR, GL_NOR,
            GL_XOR, GL_EQUIV, GL_AND_REVERSE, GL_AND_INVERTED, GL_OR_REVERSE, and GL_OR_INVERTED. The initial
            value is GL_COPY.

        Raises
        ------
        GL_INVALID_ENUM is generated if opcode is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glLogicOp.xhtml
        """
        pass

    def map_buffer(self, target: int, access: int) -> c_void_p:
        """
        Map all of a buffer object's data store into the client's address space

        Wrapper for glMapBuffer

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glMapBuffer, which must be one of the
            buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER Vertex
            attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy source
            GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch
            commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array
            indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        access: int
            Specifies the access policy for glMapBuffer and glMapNamedBuffer, indicating whether it will be
            possible to read from, write to, or both read from and write to the buffer object's mapped data
            store. The symbolic constant must be GL_READ_ONLY, GL_WRITE_ONLY, or GL_READ_WRITE.

        Raises
        ------
        GL_INVALID_ENUM is generated by glMapBuffer if target is not one of the buffer binding targets
            listed above.
        GL_INVALID_OPERATION is generated by glMapBuffer if zero is bound to target.
        GL_INVALID_OPERATION is generated by glMapNamedBuffer if buffer is not the name of an existing
            buffer object.
        GL_INVALID_ENUM is generated if access is not GL_READ_ONLY, GL_WRITE_ONLY, or GL_READ_WRITE.
        GL_OUT_OF_MEMORY is generated if the GL is unable to map the buffer object's data store. This may
            occur for a variety of system-specific reasons, such as the absence of sufficient remaining virtual
            memory.
        GL_INVALID_OPERATION is generated if the buffer object is in a mapped state.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMapBuffer.xhtml
        """
        pass

    def multi_draw_arrays(self, mode: int, first: POINTER(c_int), count: POINTER(c_uint32), drawcount: int):
        """
        Render multiple sets of primitives from array data

        Wrapper for glMultiDrawArrays

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        first: POINTER(c_int)
            Points to an array of starting indices in the enabled arrays.
        count: POINTER(c_uint32)
            Points to an array of the number of indices to be rendered.
        drawcount: int
            Specifies the size of the first and count

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if drawcount is negative.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMultiDrawArrays.xhtml
        """
        pass

    def multi_draw_elements(self, mode: int, count: POINTER(c_uint32), type: int, drawcount: int):
        """
        Render multiple sets of primitives by specifying indices of array data elements

        Wrapper for glMultiDrawElements

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        count: POINTER(c_uint32)
            Points to an array of the elements counts.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        drawcount: int
            Specifies the size of the count and indices arrays.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if drawcount is negative.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMultiDrawElements.xhtml
        """
        pass

    def pixel_storef(self, pname: int, param: float):
        """
        Set pixel storage modes

        Wrapper for glPixelStoref

        Parameters
        ----------
        pname: int
            Specifies the symbolic name of the parameter to be set. Six values affect the packing of pixel data
            into memory: GL_PACK_SWAP_BYTES, GL_PACK_LSB_FIRST, GL_PACK_ROW_LENGTH, GL_PACK_IMAGE_HEIGHT,
            GL_PACK_SKIP_PIXELS, GL_PACK_SKIP_ROWS, GL_PACK_SKIP_IMAGES, and GL_PACK_ALIGNMENT. Six more affect
            the unpacking of pixel data from memory: GL_UNPACK_SWAP_BYTES, GL_UNPACK_LSB_FIRST,
            GL_UNPACK_ROW_LENGTH, GL_UNPACK_IMAGE_HEIGHT, GL_UNPACK_SKIP_PIXELS, GL_UNPACK_SKIP_ROWS,
            GL_UNPACK_SKIP_IMAGES, and GL_UNPACK_ALIGNMENT.
        param: float
            Specifies the value that pname is set to.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated if a negative row length, pixel skip, or row skip value is specified,
            or if alignment is specified as other than 1, 2, 4, or 8.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelStore.xhtml
        """
        pass

    def pixel_storei(self, pname: int, param: int):
        """
        Set pixel storage modes

        Wrapper for glPixelStorei

        Parameters
        ----------
        pname: int
            Specifies the symbolic name of the parameter to be set. Six values affect the packing of pixel data
            into memory: GL_PACK_SWAP_BYTES, GL_PACK_LSB_FIRST, GL_PACK_ROW_LENGTH, GL_PACK_IMAGE_HEIGHT,
            GL_PACK_SKIP_PIXELS, GL_PACK_SKIP_ROWS, GL_PACK_SKIP_IMAGES, and GL_PACK_ALIGNMENT. Six more affect
            the unpacking of pixel data from memory: GL_UNPACK_SWAP_BYTES, GL_UNPACK_LSB_FIRST,
            GL_UNPACK_ROW_LENGTH, GL_UNPACK_IMAGE_HEIGHT, GL_UNPACK_SKIP_PIXELS, GL_UNPACK_SKIP_ROWS,
            GL_UNPACK_SKIP_IMAGES, and GL_UNPACK_ALIGNMENT.
        param: int
            Specifies the value that pname is set to.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated if a negative row length, pixel skip, or row skip value is specified,
            or if alignment is specified as other than 1, 2, 4, or 8.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelStore.xhtml
        """
        pass

    def point_parameterf(self, pname: int, param: float):
        """
        Specify point parameters

        Wrapper for glPointParameterf

        Parameters
        ----------
        pname: int
            Specifies a single-valued point parameter. GL_POINT_FADE_THRESHOLD_SIZE, and
            GL_POINT_SPRITE_COORD_ORIGIN are accepted.
        param: float
            For glPointParameterf and glPointParameteri, specifies the value that pname will be set to.

        Raises
        ------
        GL_INVALID_VALUE is generated if the value specified for GL_POINT_FADE_THRESHOLD_SIZE is less than
            zero.
        GL_INVALID_ENUM is generated If the value specified for GL_POINT_SPRITE_COORD_ORIGIN is not
            GL_LOWER_LEFT or GL_UPPER_LEFT.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPointParameter.xhtml
        """
        pass

    def point_parameteri(self, pname: int, param: int):
        """
        Specify point parameters

        Wrapper for glPointParameteri

        Parameters
        ----------
        pname: int
            Specifies a single-valued point parameter. GL_POINT_FADE_THRESHOLD_SIZE, and
            GL_POINT_SPRITE_COORD_ORIGIN are accepted.
        param: int
            For glPointParameterf and glPointParameteri, specifies the value that pname will be set to.

        Raises
        ------
        GL_INVALID_VALUE is generated if the value specified for GL_POINT_FADE_THRESHOLD_SIZE is less than
            zero.
        GL_INVALID_ENUM is generated If the value specified for GL_POINT_SPRITE_COORD_ORIGIN is not
            GL_LOWER_LEFT or GL_UPPER_LEFT.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPointParameter.xhtml
        """
        pass

    def point_parameterfv(self, pname: int, params: POINTER(c_float)):
        """
        Specify point parameters

        Wrapper for glPointParameterfv

        Parameters
        ----------
        pname: int
            Specifies a single-valued point parameter. GL_POINT_FADE_THRESHOLD_SIZE, and
            GL_POINT_SPRITE_COORD_ORIGIN are accepted.
        params: POINTER(c_float)
            For glPointParameterfv and glPointParameteriv, specifies a pointer to an array where the value or
            values to be assigned to pname are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if the value specified for GL_POINT_FADE_THRESHOLD_SIZE is less than
            zero.
        GL_INVALID_ENUM is generated If the value specified for GL_POINT_SPRITE_COORD_ORIGIN is not
            GL_LOWER_LEFT or GL_UPPER_LEFT.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPointParameter.xhtml
        """
        pass

    def point_parameteriv(self, pname: int, params: POINTER(c_int)):
        """
        Specify point parameters

        Wrapper for glPointParameteriv

        Parameters
        ----------
        pname: int
            Specifies a single-valued point parameter. GL_POINT_FADE_THRESHOLD_SIZE, and
            GL_POINT_SPRITE_COORD_ORIGIN are accepted.
        params: POINTER(c_int)
            For glPointParameterfv and glPointParameteriv, specifies a pointer to an array where the value or
            values to be assigned to pname are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if the value specified for GL_POINT_FADE_THRESHOLD_SIZE is less than
            zero.
        GL_INVALID_ENUM is generated If the value specified for GL_POINT_SPRITE_COORD_ORIGIN is not
            GL_LOWER_LEFT or GL_UPPER_LEFT.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPointParameter.xhtml
        """
        pass

    def point_size(self, size: float):
        """
        Specify the diameter of rasterized points

        Wrapper for glPointSize

        Parameters
        ----------
        size: float
            Specifies the diameter of rasterized points. The initial value is 1.

        Raises
        ------
        GL_INVALID_VALUE is generated if size is less than or equal to 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPointSize.xhtml
        """
        pass

    def polygon_mode(self, face: int, mode: int):
        """
        Select a polygon rasterization mode

        Wrapper for glPolygonMode

        Parameters
        ----------
        face: int
            Specifies the polygons that mode applies to. Must be GL_FRONT_AND_BACK for front- and back-facing
            polygons.
        mode: int
            Specifies how polygons will be rasterized. Accepted values are GL_POINT, GL_LINE, and GL_FILL. The
            initial value is GL_FILL for both front- and back-facing polygons.

        Raises
        ------
        GL_INVALID_ENUM is generated if either face or mode is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPolygonMode.xhtml
        """
        pass

    def polygon_offset(self, factor: float, units: float):
        """
        Set the scale and units used to calculate depth values

        Wrapper for glPolygonOffset

        Parameters
        ----------
        factor: float
            Specifies a scale factor that is used to create a variable depth offset for each polygon. The
            initial value is 0.
        units: float
            Is multiplied by an implementation-specific value to create a constant depth offset. The initial
            value is 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPolygonOffset.xhtml
        """
        pass

    def read_buffer(self, mode: int):
        """
        Select a color buffer source for pixels

        Wrapper for glReadBuffer

        Parameters
        ----------
        mode: int
            Specifies a color buffer. Accepted values are GL_FRONT_LEFT, GL_FRONT_RIGHT, GL_BACK_LEFT,
            GL_BACK_RIGHT, GL_FRONT, GL_BACK, GL_LEFT, GL_RIGHT, and the constants GL_COLOR_ATTACHMENT i.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of the twelve (or more) accepted values.
        GL_INVALID_OPERATION is generated if mode specifies a buffer that does not exist.
        GL_INVALID_OPERATION is generated by glNamedFramebufferReadBuffer if framebuffer is not zero or the
            name of an existing framebuffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glReadBuffer.xhtml
        """
        pass

    def read_pixels(self, x: int, y: int, width: int, height: int, format: int, type: int, data: c_void_p):
        """
        Read a block of pixels from the frame buffer

        Wrapper for glReadPixels

        Parameters
        ----------
        x, y: int
            Specify the window coordinates of the first pixel that is read from the frame buffer. This location
            is the lower left corner of a rectangular block of pixels.
        width, height: int
            Specify the dimensions of the pixel rectangle. width and height of one correspond to a single
            pixel.
        format: int
            Specifies the format of the pixel data. The following symbolic values are accepted:
            GL_STENCIL_INDEX, GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL, GL_RED, GL_GREEN, GL_BLUE, GL_RGB, GL_BGR,
            GL_RGBA, and GL_BGRA.
        type: int
            Specifies the data type of the pixel data. Must be one of GL_UNSIGNED_BYTE, GL_BYTE,
            GL_UNSIGNED_SHORT, GL_SHORT, GL_UNSIGNED_INT, GL_INT, GL_HALF_FLOAT, GL_FLOAT,
            GL_UNSIGNED_BYTE_3_3_2, GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5,
            GL_UNSIGNED_SHORT_5_6_5_REV, GL_UNSIGNED_SHORT_4_4_4_4, GL_UNSIGNED_SHORT_4_4_4_4_REV,
            GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV, GL_UNSIGNED_INT_8_8_8_8,
            GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, GL_UNSIGNED_INT_2_10_10_10_REV,
            GL_UNSIGNED_INT_24_8, GL_UNSIGNED_INT_10F_11F_11F_REV, GL_UNSIGNED_INT_5_9_9_9_REV, or
            GL_FLOAT_32_UNSIGNED_INT_24_8_REV.
        data: c_void_p
            Returns the pixel data.

        Raises
        ------
        GL_INVALID_ENUM is generated if format or type is not an accepted value.
        GL_INVALID_VALUE is generated if either width or height is negative.
        GL_INVALID_OPERATION is generated if format is GL_STENCIL_INDEX and there is no stencil buffer.
        GL_INVALID_OPERATION is generated if format is GL_DEPTH_COMPONENT and there is no depth buffer.
        GL_INVALID_OPERATION is generated if format is GL_DEPTH_STENCIL and there is no depth buffer or if
            there is no stencil buffer.
        GL_INVALID_ENUM is generated if format is GL_DEPTH_STENCIL and type is not GL_UNSIGNED_INT_24_8 or
            GL_FLOAT_32_UNSIGNED_INT_24_8_REV.
        GL_INVALID_OPERATION is generated if type is one of GL_UNSIGNED_BYTE_3_3_2,
            GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5, or GL_UNSIGNED_SHORT_5_6_5_REV and format is
            not GL_RGB.
        GL_INVALID_OPERATION is generated if type is one of GL_UNSIGNED_SHORT_4_4_4_4,
            GL_UNSIGNED_SHORT_4_4_4_4_REV, GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV,
            GL_UNSIGNED_INT_8_8_8_8, GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, or
            GL_UNSIGNED_INT_2_10_10_10_REV and format is neither GL_RGBA nor GL_BGRA.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and the data would be packed to the buffer object such that the memory
            writes required would exceed the data store size.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and data is not evenly divisible into the number of bytes needed to
            store in memory a datum indicated by type.
        GL_INVALID_OPERATION is generated if GL_READ_FRAMEBUFFER_BINDING is non-zero, the read framebuffer
            is complete, and the value of GL_SAMPLE_BUFFERS for the read framebuffer is greater than zero.
        GL_INVALID_OPERATION is generated by glReadnPixels if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glReadPixels.xhtml
        """
        pass

    def sample_coverage(self, value: float, invert: bool):
        """
        Specify multisample coverage parameters

        Wrapper for glSampleCoverage

        Parameters
        ----------
        value: float
            Specify a single floating-point sample coverage value. The value is clamped to the range 0 1. The
            initial value is 1.0.
        invert: bool
            Specify a single boolean value representing if the coverage masks should be inverted. GL_TRUE and
            GL_FALSE are accepted. The initial value is GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSampleCoverage.xhtml
        """
        pass

    def scissor(self, x: int, y: int, width: int, height: int):
        """
        Define the scissor box

        Wrapper for glScissor

        Parameters
        ----------
        x, y: int
            Specify the lower left corner of the scissor box. Initially (0, 0).
        width, height: int
            Specify the width and height of the scissor box. When a GL context is first attached to a window,
            width and height are set to the dimensions of that window.

        Raises
        ------
        GL_INVALID_VALUE is generated if either width or height is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glScissor.xhtml
        """
        pass

    def shader_source(self, shader: int, count: int, string: POINTER(c_char_p), length: POINTER(c_int)):
        """
        Replaces the source code in a shader object

        Wrapper for glShaderSource

        Parameters
        ----------
        shader: int
            Specifies the handle of the shader object whose source code is to be replaced.
        count: int
            Specifies the number of elements in the string and length arrays.
        string: POINTER(c_char_p)
            Specifies an array of pointers to strings containing the source code to be loaded into the shader.
        length: POINTER(c_int)
            Specifies an array of string lengths.

        Raises
        ------
        GL_INVALID_VALUE is generated if shader is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if shader is not a shader object.
        GL_INVALID_VALUE is generated if count is less than 0.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glShaderSource.xhtml
        """
        pass

    def stencil_func(self, func: int, ref: int, mask: int):
        """
        Set front and back function and reference value for stencil testing

        Wrapper for glStencilFunc

        Parameters
        ----------
        func: int
            Specifies the test function. Eight symbolic constants are valid: GL_NEVER, GL_LESS, GL_LEQUAL,
            GL_GREATER, GL_GEQUAL, GL_EQUAL, GL_NOTEQUAL, and GL_ALWAYS. The initial value is GL_ALWAYS.
        ref: int
            Specifies the reference value for the stencil test. ref is clamped to the range 0 2 n - 1, where n
            is the number of bitplanes in the stencil buffer. The initial value is 0.
        mask: int
            Specifies a mask that is ANDed with both the reference value and the stored stencil value when the
            test is done. The initial value is all 1's.

        Raises
        ------
        GL_INVALID_ENUM is generated if func is not one of the eight accepted values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilFunc.xhtml
        """
        pass

    def stencil_func_separate(self, face: int, func: int, ref: int, mask: int):
        """
        Set front and/or back function and reference value for stencil testing

        Wrapper for glStencilFuncSeparate

        Parameters
        ----------
        face: int
            Specifies whether front and/or back stencil state is updated. Three symbolic constants are valid:
            GL_FRONT, GL_BACK, and GL_FRONT_AND_BACK.
        func: int
            Specifies the test function. Eight symbolic constants are valid: GL_NEVER, GL_LESS, GL_LEQUAL,
            GL_GREATER, GL_GEQUAL, GL_EQUAL, GL_NOTEQUAL, and GL_ALWAYS. The initial value is GL_ALWAYS.
        ref: int
            Specifies the reference value for the stencil test. ref is clamped to the range 0 2 n - 1, where n
            is the number of bitplanes in the stencil buffer. The initial value is 0.
        mask: int
            Specifies a mask that is ANDed with both the reference value and the stored stencil value when the
            test is done. The initial value is all 1's.

        Raises
        ------
        GL_INVALID_ENUM is generated if func is not one of the eight accepted values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilFuncSeparate.xhtml
        """
        pass

    def stencil_mask(self, mask: int):
        """
        Control the front and back writing of individual bits in the stencil planes

        Wrapper for glStencilMask

        Parameters
        ----------
        mask: int
            Specifies a bit mask to enable and disable writing of individual bits in the stencil planes.
            Initially, the mask is all 1's.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilMask.xhtml
        """
        pass

    def stencil_mask_separate(self, face: int, mask: int):
        """
        Control the front and/or back writing of individual bits in the stencil planes

        Wrapper for glStencilMaskSeparate

        Parameters
        ----------
        face: int
            Specifies whether the front and/or back stencil writemask is updated. Three symbolic constants are
            valid: GL_FRONT, GL_BACK, and GL_FRONT_AND_BACK.
        mask: int
            Specifies a bit mask to enable and disable writing of individual bits in the stencil planes.
            Initially, the mask is all 1's.

        Raises
        ------
        GL_INVALID_ENUM is generated if face is not one of the accepted tokens.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilMaskSeparate.xhtml
        """
        pass

    def stencil_op(self, sfail: int, dpfail: int, dppass: int):
        """
        Set front and back stencil test actions

        Wrapper for glStencilOp

        Parameters
        ----------
        sfail: int
            Specifies the action to take when the stencil test fails. Eight symbolic constants are accepted:
            GL_KEEP, GL_ZERO, GL_REPLACE, GL_INCR, GL_INCR_WRAP, GL_DECR, GL_DECR_WRAP, and GL_INVERT. The
            initial value is GL_KEEP.
        dpfail: int
            Specifies the stencil action when the stencil test passes, but the depth test fails. dpfail accepts
            the same symbolic constants as sfail. The initial value is GL_KEEP.
        dppass: int
            Specifies the stencil action when both the stencil test and the depth test pass, or when the
            stencil test passes and either there is no depth buffer or depth testing is not enabled. dppass
            accepts the same symbolic constants as sfail. The initial value is GL_KEEP.

        Raises
        ------
        GL_INVALID_ENUM is generated if sfail, dpfail, or dppass is any value other than the defined
            constant values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilOp.xhtml
        """
        pass

    def stencil_op_separate(self, face: int, sfail: int, dpfail: int, dppass: int):
        """
        Set front and/or back stencil test actions

        Wrapper for glStencilOpSeparate

        Parameters
        ----------
        face: int
            Specifies whether front and/or back stencil state is updated. Three symbolic constants are valid:
            GL_FRONT, GL_BACK, and GL_FRONT_AND_BACK.
        sfail: int
            Specifies the action to take when the stencil test fails. Eight symbolic constants are accepted:
            GL_KEEP, GL_ZERO, GL_REPLACE, GL_INCR, GL_INCR_WRAP, GL_DECR, GL_DECR_WRAP, and GL_INVERT. The
            initial value is GL_KEEP.
        dpfail: int
            Specifies the stencil action when the stencil test passes, but the depth test fails. dpfail accepts
            the same symbolic constants as sfail. The initial value is GL_KEEP.
        dppass: int
            Specifies the stencil action when both the stencil test and the depth test pass, or when the
            stencil test passes and either there is no depth buffer or depth testing is not enabled. dppass
            accepts the same symbolic constants as sfail. The initial value is GL_KEEP.

        Raises
        ------
        GL_INVALID_ENUM is generated if face is any value other than GL_FRONT, GL_BACK, or
            GL_FRONT_AND_BACK.
        GL_INVALID_ENUM is generated if sfail, dpfail, or dppass is any value other than the eight defined
            constant values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilOpSeparate.xhtml
        """
        pass

    def tex_parameterf(self, target: int, pname: int, param: float):
        """
        Set texture parameters

        Wrapper for glTexParameterf

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glTexParameter functions. Must be one of
            GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY, or
            GL_TEXTURE_RECTANGLE.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        param: float
            For the scalar commands, specifies the value of pname.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def tex_parameteri(self, target: int, pname: int, param: int):
        """
        Set texture parameters

        Wrapper for glTexParameteri

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glTexParameter functions. Must be one of
            GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY, or
            GL_TEXTURE_RECTANGLE.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        param: int
            For the scalar commands, specifies the value of pname.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def tex_parameterfv(self, target: int, pname: int, params: POINTER(c_float)):
        """
        Set texture parameters

        Wrapper for glTexParameterfv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glTexParameter functions. Must be one of
            GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY, or
            GL_TEXTURE_RECTANGLE.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        params: POINTER(c_float)
            For the vector commands, specifies a pointer to an array where the value or values of pname are
            stored.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def tex_parameteriv(self, target: int, pname: int, params: POINTER(c_int)):
        """
        Set texture parameters

        Wrapper for glTexParameteriv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glTexParameter functions. Must be one of
            GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY, or
            GL_TEXTURE_RECTANGLE.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        params: POINTER(c_int)
            For the vector commands, specifies a pointer to an array where the value or values of pname are
            stored.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def uniform1f(self, location: int, v0: float):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform1f

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform2f(self, location: int, v0: float, v1: float):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform2f

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform3f(self, location: int, v0: float, v1: float, v2: float):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform3f

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform4f(self, location: int, v0: float, v1: float, v2: float, v3: float):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform4f

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2, v3: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform1i(self, location: int, v0: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform1i

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform2i(self, location: int, v0: int, v1: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform2i

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform3i(self, location: int, v0: int, v1: int, v2: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform3i

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform4i(self, location: int, v0: int, v1: int, v2: int, v3: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform4i

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2, v3: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform1fv(self, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform1fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform2fv(self, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform2fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform3fv(self, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform3fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform4fv(self, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform4fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform1iv(self, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform1iv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform2iv(self, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform2iv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform3iv(self, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform3iv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform4iv(self, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform4iv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix2fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix2fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix3fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix3fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix4fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix4fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def unmap_buffer(self, target: int) -> bool:
        """
        Release the mapping of a buffer object's data store into the client's address space

        Wrapper for glUnmapBuffer

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glUnmapBuffer, which must be one of
            the buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER
            Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy
            source GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute
            dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex
            array indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage

        Raises
        ------
        GL_INVALID_ENUM is generated by glUnmapBuffer if target is not one of the buffer binding targets
            listed above.
        GL_INVALID_OPERATION is generated by glUnmapBuffer if zero is bound to target.
        GL_INVALID_OPERATION is generated by glUnmapNamedBuffer if buffer is not the name of an existing
            buffer object.
        GL_INVALID_OPERATION is generated if the buffer object is not in a mapped state.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUnmapBuffer.xhtml
        """
        pass

    def use_program(self, program: int):
        """
        Installs a program object as part of current rendering state

        Wrapper for glUseProgram

        Parameters
        ----------
        program: int
            Specifies the handle of the program object whose executables are to be used as part of current
            rendering state.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is neither 0 nor a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program could not be made part of current state.
        GL_INVALID_OPERATION is generated if transform feedback mode is active.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUseProgram.xhtml
        """
        pass

    def validate_program(self, program: int):
        """
        Validates a program object

        Wrapper for glValidateProgram

        Parameters
        ----------
        program: int
            Specifies the handle of the program object to be validated.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glValidateProgram.xhtml
        """
        pass

    def vertex_attrib1f(self, index: int, v0: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib1f

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib1s(self, index: int, v0: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib1s

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib1d(self, index: int, v0: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib1d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib2f(self, index: int, v0: float, v1: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib2f

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib2s(self, index: int, v0: int, v1: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib2s

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib2d(self, index: int, v0: float, v1: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib2d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib3f(self, index: int, v0: float, v1: float, v2: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib3f

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib3s(self, index: int, v0: int, v1: int, v2: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib3s

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib3d(self, index: int, v0: float, v1: float, v2: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib3d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4f(self, index: int, v0: float, v1: float, v2: float, v3: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4f

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2, v3: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4s(self, index: int, v0: int, v1: int, v2: int, v3: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4s

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2, v3: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4d(self, index: int, v0: float, v1: float, v2: float, v3: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2, v3: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4_nub(self, index: int, v0: c_ubyte, v1: c_ubyte, v2: c_ubyte, v3: c_ubyte):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4Nub

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2, v3: c_ubyte
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib1fv(self, index: int, v: POINTER(c_float)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib1fv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_float)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib1sv(self, index: int, v: POINTER(c_int16)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib1sv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int16)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib1dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib1dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib2fv(self, index: int, v: POINTER(c_float)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib2fv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_float)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib2sv(self, index: int, v: POINTER(c_int16)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib2sv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int16)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib2dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib2dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib3fv(self, index: int, v: POINTER(c_float)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib3fv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_float)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib3sv(self, index: int, v: POINTER(c_int16)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib3sv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int16)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib3dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib3dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4fv(self, index: int, v: POINTER(c_float)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4fv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_float)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4sv(self, index: int, v: POINTER(c_int16)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4sv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int16)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4iv(self, index: int, v: POINTER(c_int)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4iv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4bv(self, index: int, v: POINTER(c_byte)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4bv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_byte)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4ubv(self, index: int, v: POINTER(c_ubyte)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4ubv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_ubyte)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4usv(self, index: int, v: POINTER(c_ushort)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4usv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_ushort)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4uiv(self, index: int, v: POINTER(c_uint)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4uiv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_uint)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4_nbv(self, index: int, v: POINTER(c_byte)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4Nbv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_byte)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4_nsv(self, index: int, v: POINTER(c_int16)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4Nsv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int16)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4_niv(self, index: int, v: POINTER(c_int)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4Niv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4_nubv(self, index: int, v: POINTER(c_ubyte)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4Nubv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_ubyte)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4_nusv(self, index: int, v: POINTER(c_ushort)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4Nusv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_ushort)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib4_nuiv(self, index: int, v: POINTER(c_uint)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttrib4Nuiv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_uint)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_pointer(self, index: int, size: int, type: int, normalized: bool, stride: int, pointer: c_void_p):
        """
        Define an array of generic vertex attribute data

        Wrapper for glVertexAttribPointer

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        size: int
            Specifies the number of components per generic vertex attribute. Must be 1, 2, 3, 4. Additionally,
            the symbolic constant GL_BGRA is accepted by glVertexAttribPointer. The initial value is 4.
        type: int
            Specifies the data type of each component in the array. The symbolic constants GL_BYTE,
            GL_UNSIGNED_BYTE, GL_SHORT, GL_UNSIGNED_SHORT, GL_INT, and GL_UNSIGNED_INT are accepted by
            glVertexAttribPointer and glVertexAttribIPointer. Additionally GL_HALF_FLOAT, GL_FLOAT, GL_DOUBLE,
            GL_FIXED, GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV and GL_UNSIGNED_INT_10F_11F_11F_REV
            are accepted by glVertexAttribPointer. GL_DOUBLE is also accepted by glVertexAttribLPointer and is
            the only token accepted by the type parameter for that function. The initial value is GL_FLOAT.
        normalized: bool
            For glVertexAttribPointer, specifies whether fixed-point data values should be normalized (GL_TRUE)
            or converted directly as fixed-point values (GL_FALSE) when they are accessed.
        stride: int
            Specifies the byte offset between consecutive generic vertex attributes. If stride is 0, the
            generic vertex attributes are understood to be tightly packed in the array. The initial value is 0.
        pointer: c_void_p
            Specifies a offset of the first component of the first generic vertex attribute in the array in the
            data store of the buffer currently bound to the GL_ARRAY_BUFFER target. The initial value is 0.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not 1, 2, 3, 4 or (for glVertexAttribPointer), GL_BGRA.
        GL_INVALID_ENUM is generated if type is not an accepted value.
        GL_INVALID_VALUE is generated if stride is negative.
        GL_INVALID_OPERATION is generated if size is GL_BGRA and type is not GL_UNSIGNED_BYTE,
            GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV.
        GL_INVALID_OPERATION is generated if type is GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV and size is not 4 or GL_BGRA.
        GL_INVALID_OPERATION is generated if type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        GL_INVALID_OPERATION is generated by glVertexAttribPointer if size is GL_BGRA and noramlized is
            GL_FALSE.
        GL_INVALID_OPERATION is generated if zero is bound to the GL_ARRAY_BUFFER buffer object binding
            point and the pointer argument is not NULL.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribPointer.xhtml
        """
        pass

    def viewport(self, x: int, y: int, width: int, height: int):
        """
        Set the viewport

        Wrapper for glViewport

        Parameters
        ----------
        x, y: int
            Specify the lower left corner of the viewport rectangle, in pixels. The initial value is (0,0).
        width, height: int
            Specify the width and height of the viewport. When a GL context is first attached to a window,
            width and height are set to the dimensions of that window.

        Raises
        ------
        GL_INVALID_VALUE is generated if either width or height is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glViewport.xhtml
        """
        pass

class GL21(GL20):

    MAJOR = 2
    MINOR = 1

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.uniform_matrix2x3fv, 'glUniformMatrix2x3fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.uniform_matrix3x2fv, 'glUniformMatrix3x2fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.uniform_matrix2x4fv, 'glUniformMatrix2x4fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.uniform_matrix4x2fv, 'glUniformMatrix4x2fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.uniform_matrix3x4fv, 'glUniformMatrix3x4fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.uniform_matrix4x3fv, 'glUniformMatrix4x3fv',
                   None, c_int, c_uint32, c_bool, POINTER(c_float))

    def uniform_matrix2x3fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix2x3fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix3x2fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix3x2fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix2x4fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix2x4fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix4x2fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix4x2fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix3x4fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix3x4fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform_matrix4x3fv(self, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniformMatrix4x3fv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

class GL30(GL21):

    MAJOR = 3
    MINOR = 0

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.begin_conditional_render, 'glBeginConditionalRender',
                   None, c_uint, c_uint)
        self._load(self.end_conditional_render, 'glEndConditionalRender',
                   None, )
        self._load(self.begin_transform_feedback, 'glBeginTransformFeedback',
                   None, c_uint)
        self._load(self.end_transform_feedback, 'glEndTransformFeedback',
                   None, )
        self._load(self.bind_buffer_base, 'glBindBufferBase',
                   None, c_uint, c_uint, c_uint)
        self._load(self.bind_buffer_range, 'glBindBufferRange',
                   None, c_uint, c_uint, c_uint, POINTER(c_int), POINTER(c_uint32))
        self._load(self.bind_frag_data_location, 'glBindFragDataLocation',
                   None, c_uint, c_uint, c_char_p)
        self._load(self.bind_framebuffer, 'glBindFramebuffer',
                   None, c_uint, c_uint)
        self._load(self.bind_renderbuffer, 'glBindRenderbuffer',
                   None, c_uint, c_uint)
        self._load(self.bind_vertex_array, 'glBindVertexArray',
                   None, c_uint)
        self._load(self.blit_framebuffer, 'glBlitFramebuffer',
                   None, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint32, c_uint)
        self._load(self.check_framebuffer_status, 'glCheckFramebufferStatus',
                   c_uint, c_uint)
        self._load(self.clamp_color, 'glClampColor',
                   None, c_uint, c_uint)
        self._load(self.clear_bufferiv, 'glClearBufferiv',
                   None, c_uint, c_int, POINTER(c_int))
        self._load(self.clear_bufferuiv, 'glClearBufferuiv',
                   None, c_uint, c_int, POINTER(c_uint))
        self._load(self.clear_bufferfv, 'glClearBufferfv',
                   None, c_uint, c_int, POINTER(c_float))
        self._load(self.clear_bufferfi, 'glClearBufferfi',
                   None, c_uint, c_int, c_float, c_int)
        self._load(self.color_maski, 'glColorMaski',
                   None, c_uint, c_bool, c_bool, c_bool, c_bool)
        self._load(self.delete_framebuffers, 'glDeleteFramebuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.delete_renderbuffers, 'glDeleteRenderbuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.delete_vertex_arrays, 'glDeleteVertexArrays',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.enablei, 'glEnablei',
                   None, c_uint, c_uint)
        self._load(self.disablei, 'glDisablei',
                   None, c_uint, c_uint)
        self._load(self.flush_mapped_buffer_range, 'glFlushMappedBufferRange',
                   None, c_uint, POINTER(c_int), POINTER(c_uint32))
        self._load(self.framebuffer_renderbuffer, 'glFramebufferRenderbuffer',
                   None, c_uint, c_uint, c_uint, c_uint)
        self._load(self.framebuffer_texture1_d, 'glFramebufferTexture1D',
                   None, c_uint, c_uint, c_uint, c_uint, c_int)
        self._load(self.framebuffer_texture2_d, 'glFramebufferTexture2D',
                   None, c_uint, c_uint, c_uint, c_uint, c_int)
        self._load(self.framebuffer_texture3_d, 'glFramebufferTexture3D',
                   None, c_uint, c_uint, c_uint, c_uint, c_int, c_int)
        self._load(self.framebuffer_texture_layer, 'glFramebufferTextureLayer',
                   None, c_uint, c_uint, c_uint, c_int, c_int)
        self._load(self.generate_mipmap, 'glGenerateMipmap',
                   None, c_uint)
        self._load(self.gen_framebuffers, 'glGenFramebuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.gen_renderbuffers, 'glGenRenderbuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.gen_vertex_arrays, 'glGenVertexArrays',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.get_booleani_v, 'glGetBooleani_v',
                   None, c_uint, c_uint, POINTER(c_bool))
        self._load(self.get_integeri_v, 'glGetIntegeri_v',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_frag_data_location, 'glGetFragDataLocation',
                   c_int, c_uint, c_char_p)
        self._load(self.get_framebuffer_attachment_parameteriv, 'glGetFramebufferAttachmentParameteriv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_renderbuffer_parameteriv, 'glGetRenderbufferParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_stringi, 'glGetStringi',
                   POINTER(c_ubyte), c_uint, c_uint)
        self._load(self.get_tex_parameter_iiv, 'glGetTexParameterIiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_tex_parameter_iuiv, 'glGetTexParameterIuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.get_transform_feedback_varying, 'glGetTransformFeedbackVarying',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), c_char_p)
        self._load(self.get_uniformuiv, 'glGetUniformuiv',
                   None, c_uint, c_int, POINTER(c_uint))
        self._load(self.get_vertex_attrib_iiv, 'glGetVertexAttribIiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_vertex_attrib_iuiv, 'glGetVertexAttribIuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.is_enabledi, 'glIsEnabledi',
                   c_bool, c_uint, c_uint)
        self._load(self.is_framebuffer, 'glIsFramebuffer',
                   c_bool, c_uint)
        self._load(self.is_renderbuffer, 'glIsRenderbuffer',
                   c_bool, c_uint)
        self._load(self.is_vertex_array, 'glIsVertexArray',
                   c_bool, c_uint)
        self._load(self.map_buffer_range, 'glMapBufferRange',
                   c_void_p, c_uint, POINTER(c_int), POINTER(c_uint32), c_uint32)
        self._load(self.renderbuffer_storage, 'glRenderbufferStorage',
                   None, c_uint, c_uint, c_uint32, c_uint32)
        self._load(self.renderbuffer_storage_multisample, 'glRenderbufferStorageMultisample',
                   None, c_uint, c_uint32, c_uint, c_uint32, c_uint32)
        self._load(self.tex_parameter_iiv, 'glTexParameterIiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.tex_parameter_iuiv, 'glTexParameterIuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.transform_feedback_varyings, 'glTransformFeedbackVaryings',
                   None, c_uint, c_uint32, POINTER(c_char_p), c_uint)
        self._load(self.uniform1ui, 'glUniform1ui',
                   None, c_int, c_uint)
        self._load(self.uniform2ui, 'glUniform2ui',
                   None, c_int, c_uint, c_uint)
        self._load(self.uniform3ui, 'glUniform3ui',
                   None, c_int, c_uint, c_uint, c_uint)
        self._load(self.uniform4ui, 'glUniform4ui',
                   None, c_int, c_uint, c_uint, c_uint, c_uint)
        self._load(self.uniform1uiv, 'glUniform1uiv',
                   None, c_int, c_uint32, POINTER(c_uint))
        self._load(self.uniform2uiv, 'glUniform2uiv',
                   None, c_int, c_uint32, POINTER(c_uint))
        self._load(self.uniform3uiv, 'glUniform3uiv',
                   None, c_int, c_uint32, POINTER(c_uint))
        self._load(self.uniform4uiv, 'glUniform4uiv',
                   None, c_int, c_uint32, POINTER(c_uint))
        self._load(self.vertex_attrib_i1i, 'glVertexAttribI1i',
                   None, c_uint, c_int)
        self._load(self.vertex_attrib_i1ui, 'glVertexAttribI1ui',
                   None, c_uint, c_uint)
        self._load(self.vertex_attrib_i2i, 'glVertexAttribI2i',
                   None, c_uint, c_int, c_int)
        self._load(self.vertex_attrib_i2ui, 'glVertexAttribI2ui',
                   None, c_uint, c_uint, c_uint)
        self._load(self.vertex_attrib_i3i, 'glVertexAttribI3i',
                   None, c_uint, c_int, c_int, c_int)
        self._load(self.vertex_attrib_i3ui, 'glVertexAttribI3ui',
                   None, c_uint, c_uint, c_uint, c_uint)
        self._load(self.vertex_attrib_i4i, 'glVertexAttribI4i',
                   None, c_uint, c_int, c_int, c_int, c_int)
        self._load(self.vertex_attrib_i4ui, 'glVertexAttribI4ui',
                   None, c_uint, c_uint, c_uint, c_uint, c_uint)
        self._load(self.vertex_attrib_i1iv, 'glVertexAttribI1iv',
                   None, c_uint, POINTER(c_int))
        self._load(self.vertex_attrib_i1uiv, 'glVertexAttribI1uiv',
                   None, c_uint, POINTER(c_uint))
        self._load(self.vertex_attrib_i2iv, 'glVertexAttribI2iv',
                   None, c_uint, POINTER(c_int))
        self._load(self.vertex_attrib_i2uiv, 'glVertexAttribI2uiv',
                   None, c_uint, POINTER(c_uint))
        self._load(self.vertex_attrib_i3iv, 'glVertexAttribI3iv',
                   None, c_uint, POINTER(c_int))
        self._load(self.vertex_attrib_i3uiv, 'glVertexAttribI3uiv',
                   None, c_uint, POINTER(c_uint))
        self._load(self.vertex_attrib_i4bv, 'glVertexAttribI4bv',
                   None, c_uint, POINTER(c_byte))
        self._load(self.vertex_attrib_i4ubv, 'glVertexAttribI4ubv',
                   None, c_uint, POINTER(c_ubyte))
        self._load(self.vertex_attrib_i4sv, 'glVertexAttribI4sv',
                   None, c_uint, POINTER(c_int16))
        self._load(self.vertex_attrib_i4usv, 'glVertexAttribI4usv',
                   None, c_uint, POINTER(c_ushort))
        self._load(self.vertex_attrib_i4iv, 'glVertexAttribI4iv',
                   None, c_uint, POINTER(c_int))
        self._load(self.vertex_attrib_i4uiv, 'glVertexAttribI4uiv',
                   None, c_uint, POINTER(c_uint))
        self._load(self.vertex_attrib_ipointer, 'glVertexAttribIPointer',
                   None, c_uint, c_int, c_uint, c_uint32, c_void_p)

    def begin_conditional_render(self, id: int, mode: int):
        """
        Start conditional rendering

        Wrapper for glBeginConditionalRender

        Parameters
        ----------
        id: int
            Specifies the name of an occlusion query object whose results are used to determine if the
            rendering commands are discarded.
        mode: int
            Specifies how glBeginConditionalRender interprets the results of the occlusion query.

        Raises
        ------
        GL_INVALID_VALUE is generated if id is not the name of an existing query object.
        GL_INVALID_ENUM is generated if mode is not one of the accepted tokens.
        GL_INVALID_OPERATION is generated if glBeginConditionalRender is called while conditional rendering
            is active, or if glEndConditionalRender is called while conditional rendering is inactive.
        GL_INVALID_OPERATION is generated if id is the name of a query object with a target other than
            GL_SAMPLES_PASSED or GL_ANY_SAMPLES_PASSED.
        GL_INVALID_OPERATION is generated if id is the name of a query currently in progress.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginConditionalRender.xhtml
        """
        pass

    def end_conditional_render(self):
        """
        Start conditional rendering

        Wrapper for glEndConditionalRender

        Raises
        ------
        GL_INVALID_VALUE is generated if id is not the name of an existing query object.
        GL_INVALID_ENUM is generated if mode is not one of the accepted tokens.
        GL_INVALID_OPERATION is generated if glBeginConditionalRender is called while conditional rendering
            is active, or if glEndConditionalRender is called while conditional rendering is inactive.
        GL_INVALID_OPERATION is generated if id is the name of a query object with a target other than
            GL_SAMPLES_PASSED or GL_ANY_SAMPLES_PASSED.
        GL_INVALID_OPERATION is generated if id is the name of a query currently in progress.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginConditionalRender.xhtml
        """
        pass

    def begin_transform_feedback(self, primitive_mode: int):
        """
        Start transform feedback operation

        Wrapper for glBeginTransformFeedback

        Parameters
        ----------

        Raises
        ------
        GL_INVALID_OPERATION is generated if glBeginTransformFeedback is executed while transform feedback
            is active.
        GL_INVALID_OPERATION is generated if glEndTransformFeedback is executed while transform feedback is
            not active.
        GL_INVALID_OPERATION is generated by glDrawArrays if no geometry shader is present, transform
            feedback is active and mode is not one of the allowed modes.
        GL_INVALID_OPERATION is generated by glDrawArrays if a geometry shader is present, transform
            feedback is active and the output primitive type of the geometry shader does not match the
            transform feedback primitiveMode.
        GL_INVALID_OPERATION is generated by glBeginTransformFeedback if any binding point used in
            transform feedback mode does not have a buffer object bound.
        GL_INVALID_OPERATION is generated by glBeginTransformFeedback if no binding points would be used,
            either because no program object is active of because the active program object has specified no
            varying variables to record.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginTransformFeedback.xhtml
        """
        pass

    def end_transform_feedback(self):
        """
        Start transform feedback operation

        Wrapper for glEndTransformFeedback

        Raises
        ------
        GL_INVALID_OPERATION is generated if glBeginTransformFeedback is executed while transform feedback
            is active.
        GL_INVALID_OPERATION is generated if glEndTransformFeedback is executed while transform feedback is
            not active.
        GL_INVALID_OPERATION is generated by glDrawArrays if no geometry shader is present, transform
            feedback is active and mode is not one of the allowed modes.
        GL_INVALID_OPERATION is generated by glDrawArrays if a geometry shader is present, transform
            feedback is active and the output primitive type of the geometry shader does not match the
            transform feedback primitiveMode.
        GL_INVALID_OPERATION is generated by glBeginTransformFeedback if any binding point used in
            transform feedback mode does not have a buffer object bound.
        GL_INVALID_OPERATION is generated by glBeginTransformFeedback if no binding points would be used,
            either because no program object is active of because the active program object has specified no
            varying variables to record.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginTransformFeedback.xhtml
        """
        pass

    def bind_buffer_base(self, target: int, index: int, buffer: int):
        """
        Bind a buffer object to an indexed buffer target

        Wrapper for glBindBufferBase

        Parameters
        ----------
        target: int
            Specify the target of the bind operation. target must be one of GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER or GL_SHADER_STORAGE_BUFFER.
        index: int
            Specify the index of the binding point within the array specified by target.
        buffer: int
            The name of a buffer object to bind to the specified binding point.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER or GL_SHADER_STORAGE_BUFFER.
        GL_INVALID_VALUE is generated if index is greater than or equal to the number of target -specific
            indexed binding points.
        GL_INVALID_VALUE is generated if buffer does not have an associated data store, or if the size of
            that store is zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindBufferBase.xhtml
        """
        pass

    def bind_buffer_range(self, target: int, index: int, buffer: int, offset: POINTER(c_int), size: POINTER(c_uint32)):
        """
        Bind a range within a buffer object to an indexed buffer target

        Wrapper for glBindBufferRange

        Parameters
        ----------
        target: int
            Specify the target of the bind operation. target must be one of GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER, or GL_SHADER_STORAGE_BUFFER.
        index: int
            Specify the index of the binding point within the array specified by target.
        buffer: int
            The name of a buffer object to bind to the specified binding point.
        offset: POINTER(c_int)
            The starting offset in basic machine units into the buffer object buffer.
        size: POINTER(c_uint32)
            The amount of data in machine units that can be read from the buffer object while used as an
            indexed target.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER or GL_SHADER_STORAGE_BUFFER.
        GL_INVALID_VALUE is generated if index is greater than or equal to the number of target -specific
            indexed binding points.
        GL_INVALID_VALUE is generated if size is less than or equal to zero, or if offset + size is greater
            than the value of GL_BUFFER_SIZE.
        Additional errors may be generated if offset violates any target -specific alignmemt restrictions.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindBufferRange.xhtml
        """
        pass

    def bind_frag_data_location(self, program: int, color_number: int, name: bytes):
        """
        Bind a user-defined varying out variable to a fragment shader color number

        Wrapper for glBindFragDataLocation

        Parameters
        ----------
        program: int
            The name of the program containing varying out variable whose binding to modify
        name: bytes
            The name of the user-defined varying out variable whose binding to modify

        Raises
        ------
        GL_INVALID_VALUE is generated if colorNumber is greater than or equal to GL_MAX_DRAW_BUFFERS.
        GL_INVALID_OPERATION is generated if name starts with the reserved gl_ prefix.
        GL_INVALID_OPERATION is generated if program is not the name of a program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindFragDataLocation.xhtml
        """
        pass

    def bind_framebuffer(self, target: int, framebuffer: int):
        """
        Bind a framebuffer to a framebuffer target

        Wrapper for glBindFramebuffer

        Parameters
        ----------
        target: int
            Specifies the framebuffer target of the binding operation.
        framebuffer: int
            Specifies the name of the framebuffer object to bind.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_DRAW_FRAMEBUFFER, GL_READ_FRAMEBUFFER or
            GL_FRAMEBUFFER.
        GL_INVALID_OPERATION is generated if framebuffer is not zero or the name of a framebuffer
            previously returned from a call to glGenFramebuffers.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindFramebuffer.xhtml
        """
        pass

    def bind_renderbuffer(self, target: int, renderbuffer: int):
        """
        Bind a renderbuffer to a renderbuffer target

        Wrapper for glBindRenderbuffer

        Parameters
        ----------
        target: int
            Specifies the renderbuffer target of the binding operation. target must be GL_RENDERBUFFER.
        renderbuffer: int
            Specifies the name of the renderbuffer object to bind.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated if renderbuffer is not zero or the name of a renderbuffer
            previously returned from a call to glGenRenderbuffers.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindRenderbuffer.xhtml
        """
        pass

    def bind_vertex_array(self, array: int):
        """
        Bind a vertex array object

        Wrapper for glBindVertexArray

        Parameters
        ----------
        array: int
            Specifies the name of the vertex array to bind.

        Raises
        ------
        GL_INVALID_OPERATION is generated if array is not zero or the name of a vertex array object
            previously returned from a call to glGenVertexArrays.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindVertexArray.xhtml
        """
        pass

    def blit_framebuffer(self, src_x0: int, src_y0: int, src_x1: int, src_y1: int, dst_x0: int, dst_y0: int, dst_x1: int, dst_y1: int, mask: int, filter: int):
        """
        Copy a block of pixels from one framebuffer object to another

        Wrapper for glBlitFramebuffer

        Parameters
        ----------
        mask: int
            The bitwise OR of the flags indicating which buffers are to be copied. The allowed flags are
            GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT and GL_STENCIL_BUFFER_BIT.
        filter: int
            Specifies the interpolation to be applied if the image is stretched. Must be GL_NEAREST or
            GL_LINEAR.

        Raises
        ------
        GL_INVALID_OPERATION is generated by BlitNamedFramebuffer if readFramebuffer or drawFramebuffer is
            not zero or the name of an existing framebuffer object.
        GL_INVALID_OPERATION is generated if mask contains any of the GL_DEPTH_BUFFER_BIT or
            GL_STENCIL_BUFFER_BIT and filter is not GL_NEAREST.
        GL_INVALID_OPERATION is generated if mask contains GL_COLOR_BUFFER_BIT and any of the following
            conditions hold:
        The read buffer contains fixed-point or floating-point values and any draw buffer contains neither
            fixed-point nor floating-point values.
        The read buffer contains unsigned integer values and any draw buffer does not contain unsigned
            integer values.
        The read buffer contains signed integer values and any draw buffer does not contain signed integer
            values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlitFramebuffer.xhtml
        """
        pass

    def check_framebuffer_status(self, target: int) -> int:
        """
        Check the completeness status of a framebuffer

        Wrapper for glCheckFramebufferStatus

        Parameters
        ----------
        target: int
            Specify the target to which the framebuffer is bound for glCheckFramebufferStatus, and the target
            against which framebuffer completeness of framebuffer is checked for glCheckNamedFramebufferStatus.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_DRAW_FRAMEBUFFER, GL_READ_FRAMEBUFFER or
            GL_FRAMEBUFFER.
        GL_INVALID_OPERATION is generated by glCheckNamedFramebufferStatus if framebuffer is not zero or
            the name of an existing framebuffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCheckFramebufferStatus.xhtml
        """
        pass

    def clamp_color(self, target: int, clamp: int):
        """
        Specify whether data read via <a class="citerefentry" href="glReadPixels.xhtml"><span class="citerefentry"><span class="refentrytitle">glReadPixels</span></span></a> should be clamped

        Wrapper for glClampColor

        Parameters
        ----------
        target: int
            Target for color clamping. target must be GL_CLAMP_READ_COLOR.
        clamp: int
            Specifies whether to apply color clamping. clamp must be GL_TRUE or GL_FALSE.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_CLAMP_READ_COLOR.
        GL_INVALID_ENUM is generated if clamp is not GL_TRUE or GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClampColor.xhtml
        """
        pass

    def clear_bufferiv(self, buffer: int, drawbuffer: int, value: POINTER(c_int)):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearBufferiv

        Parameters
        ----------
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        value: POINTER(c_int)
            A pointer to the value or values to clear the buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def clear_bufferuiv(self, buffer: int, drawbuffer: int, value: POINTER(c_uint)):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearBufferuiv

        Parameters
        ----------
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        value: POINTER(c_uint)
            A pointer to the value or values to clear the buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def clear_bufferfv(self, buffer: int, drawbuffer: int, value: POINTER(c_float)):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearBufferfv

        Parameters
        ----------
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        value: POINTER(c_float)
            A pointer to the value or values to clear the buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def clear_bufferfi(self, buffer: int, drawbuffer: int, depth: float, stencil: int):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearBufferfi

        Parameters
        ----------
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        depth: float
            The value to clear the depth buffer to.
        stencil: int
            The value to clear the stencil buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def color_maski(self, buf: int, red: bool, green: bool, blue: bool, alpha: bool):
        """
        Enable and disable writing of frame buffer color components

        Wrapper for glColorMaski

        Parameters
        ----------
        buf: int
            For glColorMaski, specifies the index of the draw buffer whose color mask to set.
        red, green, blue, alpha: bool
            Specify whether red, green, blue, and alpha are to be written into the frame buffer. The initial
            values are all GL_TRUE, indicating that the color components are written.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glColorMask.xhtml
        """
        pass

    def delete_framebuffers(self, n: int, framebuffers: POINTER(c_uint)):
        """
        Delete framebuffer objects

        Wrapper for glDeleteFramebuffers

        Parameters
        ----------
        n: int
            Specifies the number of framebuffer objects to be deleted.
        framebuffers: POINTER(c_uint)
            A pointer to an array containing n framebuffer objects to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteFramebuffers.xhtml
        """
        pass

    def delete_renderbuffers(self, n: int, renderbuffers: POINTER(c_uint)):
        """
        Delete renderbuffer objects

        Wrapper for glDeleteRenderbuffers

        Parameters
        ----------
        n: int
            Specifies the number of renderbuffer objects to be deleted.
        renderbuffers: POINTER(c_uint)
            A pointer to an array containing n renderbuffer objects to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteRenderbuffers.xhtml
        """
        pass

    def delete_vertex_arrays(self, n: int, arrays: POINTER(c_uint)):
        """
        Delete vertex array objects

        Wrapper for glDeleteVertexArrays

        Parameters
        ----------
        n: int
            Specifies the number of vertex array objects to be deleted.
        arrays: POINTER(c_uint)
            Specifies the address of an array containing the n names of the objects to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteVertexArrays.xhtml
        """
        pass

    def enablei(self, cap: int, index: int):
        """
        Enable or disable server-side GL capabilities

        Wrapper for glEnablei

        Parameters
        ----------
        cap: int
            Specifies a symbolic constant indicating a GL capability.
        index: int
            Specifies the index of the switch to disable (for glEnablei and glDisablei only).

        Raises
        ------
        GL_INVALID_ENUM is generated if cap is not one of the values listed previously.
        GL_INVALID_VALUE is generated by glEnablei and glDisablei if index is greater than or equal to the
            number of indexed capabilities for cap.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml
        """
        pass

    def disablei(self, cap: int, index: int):
        """
        Enable or disable server-side GL capabilities

        Wrapper for glDisablei

        Parameters
        ----------
        cap: int
            Specifies a symbolic constant indicating a GL capability.
        index: int
            Specifies the index of the switch to disable (for glEnablei and glDisablei only).

        Raises
        ------
        GL_INVALID_ENUM is generated if cap is not one of the values listed previously.
        GL_INVALID_VALUE is generated by glEnablei and glDisablei if index is greater than or equal to the
            number of indexed capabilities for cap.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml
        """
        pass

    def flush_mapped_buffer_range(self, target: int, offset: POINTER(c_int), length: POINTER(c_uint32)):
        """
        Indicate modifications to a range of a mapped buffer

        Wrapper for glFlushMappedBufferRange

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glFlushMappedBufferRange, which must
            be one of the buffer binding targets in the following table: Buffer Binding Target Purpose
            GL_ARRAY_BUFFER Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage
            GL_COPY_READ_BUFFER Buffer copy source GL_COPY_WRITE_BUFFER Buffer copy destination
            GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect
            command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array indices GL_PIXEL_PACK_BUFFER Pixel read
            target GL_PIXEL_UNPACK_BUFFER Texture data source GL_QUERY_BUFFER Query result buffer
            GL_SHADER_STORAGE_BUFFER Read-write storage for shaders GL_TEXTURE_BUFFER Texture data buffer
            GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer GL_UNIFORM_BUFFER Uniform block storage
        offset: POINTER(c_int)
            Specifies the start of the buffer subrange, in basic machine units.
        length: POINTER(c_uint32)
            Specifies the length of the buffer subrange, in basic machine units.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFlushMappedBufferRange if target is not one of the buffer binding
            targets listed above.
        GL_INVALID_OPERATION is generated by glFlushMappedBufferRange if zero is bound to target.
        GL_INVALID_OPERATION is generated by glFlushMappedNamedBufferRange if buffer is not the name of an
            existing buffer object.
        GL_INVALID_VALUE is generated if offset or length is negative, or if offset + length exceeds the
            size of the mapping.
        GL_INVALID_OPERATION is generated if the buffer object is not mapped, or is mapped without the
            GL_MAP_FLUSH_EXPLICIT_BIT flag.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFlushMappedBufferRange.xhtml
        """
        pass

    def framebuffer_renderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int):
        """
        Attach a renderbuffer as a logical buffer of a framebuffer object

        Wrapper for glFramebufferRenderbuffer

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer is bound for glFramebufferRenderbuffer.
        attachment: int
            Specifies the attachment point of the framebuffer.
        renderbuffertarget: int
            Specifies the renderbuffer target. Must be GL_RENDERBUFFER.
        renderbuffer: int
            Specifies the name of an existing renderbuffer object of type renderbuffertarget to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFramebufferRenderbuffer if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glFramebufferRenderbuffer if zero is bound to target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferRenderbuffer if framebuffer is not the name
            of an existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_ENUM is generated if renderbuffertarget is not GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated if renderbuffertarget is not zero or the name of an existing
            renderbuffer object of type GL_RENDERBUFFER.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferRenderbuffer.xhtml
        """
        pass

    def framebuffer_texture1_d(self, target: int, attachment: int, textarget: int, texture: int, level: int):
        """
        Attach a level of a texture object as a logical buffer of a framebuffer object

        Wrapper for glFramebufferTexture1D

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer is bound for all commands except
            glNamedFramebufferTexture.
        attachment: int
            Specifies the attachment point of the framebuffer.
        textarget: int
            For glFramebufferTexture1D, glFramebufferTexture2D and glFramebufferTexture3D, specifies what type
            of texture is expected in the texture parameter, or for cube map textures, which face is to be
            attached.
        texture: int
            Specifies the name of an existing texture object to attach.
        level: int
            Specifies the mipmap level of the texture object to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by all commands accepting a target parameter if it is not one of the
            accepted framebuffer targets.
        GL_INVALID_OPERATION is generated by all commands accepting a target parameter if zero is bound to
            that target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferTexture if framebuffer is not the name of an
            existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_VALUE is generated if texture is not zero or the name of an existing texture object.
        GL_INVALID_VALUE is generated if texture is not zero and level is not a supported texture level for
            texture.
        GL_INVALID_VALUE is generated by glFramebufferTexture3D if texture is not zero and layer is larger
            than the value of GL_MAX_3D_TEXTURE_SIZE minus one.
        GL_INVALID_OPERATION is generated by all commands accepting a textarget parameter if texture is not
            zero, and textarget and the effective target of texture are not compatible.
        GL_INVALID_OPERATION is generated by if texture is a buffer texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferTexture.xhtml
        """
        pass

    def framebuffer_texture2_d(self, target: int, attachment: int, textarget: int, texture: int, level: int):
        """
        Attach a level of a texture object as a logical buffer of a framebuffer object

        Wrapper for glFramebufferTexture2D

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer is bound for all commands except
            glNamedFramebufferTexture.
        attachment: int
            Specifies the attachment point of the framebuffer.
        textarget: int
            For glFramebufferTexture1D, glFramebufferTexture2D and glFramebufferTexture3D, specifies what type
            of texture is expected in the texture parameter, or for cube map textures, which face is to be
            attached.
        texture: int
            Specifies the name of an existing texture object to attach.
        level: int
            Specifies the mipmap level of the texture object to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by all commands accepting a target parameter if it is not one of the
            accepted framebuffer targets.
        GL_INVALID_OPERATION is generated by all commands accepting a target parameter if zero is bound to
            that target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferTexture if framebuffer is not the name of an
            existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_VALUE is generated if texture is not zero or the name of an existing texture object.
        GL_INVALID_VALUE is generated if texture is not zero and level is not a supported texture level for
            texture.
        GL_INVALID_VALUE is generated by glFramebufferTexture3D if texture is not zero and layer is larger
            than the value of GL_MAX_3D_TEXTURE_SIZE minus one.
        GL_INVALID_OPERATION is generated by all commands accepting a textarget parameter if texture is not
            zero, and textarget and the effective target of texture are not compatible.
        GL_INVALID_OPERATION is generated by if texture is a buffer texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferTexture.xhtml
        """
        pass

    def framebuffer_texture3_d(self, target: int, attachment: int, textarget: int, texture: int, level: int, layer: int):
        """
        Attach a level of a texture object as a logical buffer of a framebuffer object

        Wrapper for glFramebufferTexture3D

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer is bound for all commands except
            glNamedFramebufferTexture.
        attachment: int
            Specifies the attachment point of the framebuffer.
        textarget: int
            For glFramebufferTexture1D, glFramebufferTexture2D and glFramebufferTexture3D, specifies what type
            of texture is expected in the texture parameter, or for cube map textures, which face is to be
            attached.
        texture: int
            Specifies the name of an existing texture object to attach.
        level: int
            Specifies the mipmap level of the texture object to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by all commands accepting a target parameter if it is not one of the
            accepted framebuffer targets.
        GL_INVALID_OPERATION is generated by all commands accepting a target parameter if zero is bound to
            that target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferTexture if framebuffer is not the name of an
            existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_VALUE is generated if texture is not zero or the name of an existing texture object.
        GL_INVALID_VALUE is generated if texture is not zero and level is not a supported texture level for
            texture.
        GL_INVALID_VALUE is generated by glFramebufferTexture3D if texture is not zero and layer is larger
            than the value of GL_MAX_3D_TEXTURE_SIZE minus one.
        GL_INVALID_OPERATION is generated by all commands accepting a textarget parameter if texture is not
            zero, and textarget and the effective target of texture are not compatible.
        GL_INVALID_OPERATION is generated by if texture is a buffer texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferTexture.xhtml
        """
        pass

    def framebuffer_texture_layer(self, target: int, attachment: int, texture: int, level: int, layer: int):
        """
        Attach a single layer of a texture object as a logical buffer of a framebuffer object

        Wrapper for glFramebufferTextureLayer

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer is bound for glFramebufferTextureLayer.
        attachment: int
            Specifies the attachment point of the framebuffer.
        texture: int
            Specifies the name of an existing texture object to attach.
        level: int
            Specifies the mipmap level of the texture object to attach.
        layer: int
            Specifies the layer of the texture object to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFramebufferTexture if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glFramebufferTexture if zero is bound to target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferTexture if framebuffer is not the name of an
            existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_OPERATION is generated if texture is not zero and is not the name of an existing
            three-dimensional, two-dimensional multisample array, one- or two-dimensional array, cube map, or
            cube map array texture.
        GL_INVALID_VALUE is generated if texture is not zero and level is not a supported texture level for
            texture, as described above.
        GL_INVALID_VALUE is generated if texture is not zero and layer is larger than the value of
            GL_MAX_3D_TEXTURE_SIZE minus one (for three-dimensional texture objects), or larger than the value
            of GL_MAX_ARRAY_TEXTURE_LAYERS minus one (for array texture objects).
        GL_INVALID_VALUE is generated if texture is not zero and layer is negative.
        GL_INVALID_OPERATION is generated by if texture is a buffer texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferTextureLayer.xhtml
        """
        pass

    def generate_mipmap(self, target: int):
        """
        Generate mipmaps for a specified texture object

        Wrapper for glGenerateMipmap

        Parameters
        ----------
        target: int
            Specifies the target to which the texture object is bound for glGenerateMipmap. Must be one of
            GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_CUBE_MAP, or GL_TEXTURE_CUBE_MAP_ARRAY.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGenerateMipmap if target is not one of the accepted texture
            targets.
        GL_INVALID_OPERATION is generated by glGenerateTextureMipmap if texture is not the name of an
            existing texture object.
        GL_INVALID_OPERATION is generated if target is GL_TEXTURE_CUBE_MAP or GL_TEXTURE_CUBE_MAP_ARRAY,
            and the specified texture object is not cube complete or cube array complete, respectively.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenerateMipmap.xhtml
        """
        pass

    def gen_framebuffers(self, n: int, ids: POINTER(c_uint)):
        """
        Generate framebuffer object names

        Wrapper for glGenFramebuffers

        Parameters
        ----------
        n: int
            Specifies the number of framebuffer object names to generate.
        ids: POINTER(c_uint)
            Specifies an array in which the generated framebuffer object names are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenFramebuffers.xhtml
        """
        pass

    def gen_renderbuffers(self, n: int, renderbuffers: POINTER(c_uint)):
        """
        Generate renderbuffer object names

        Wrapper for glGenRenderbuffers

        Parameters
        ----------
        n: int
            Specifies the number of renderbuffer object names to generate.
        renderbuffers: POINTER(c_uint)
            Specifies an array in which the generated renderbuffer object names are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenRenderbuffers.xhtml
        """
        pass

    def gen_vertex_arrays(self, n: int, arrays: POINTER(c_uint)):
        """
        Generate vertex array object names

        Wrapper for glGenVertexArrays

        Parameters
        ----------
        n: int
            Specifies the number of vertex array object names to generate.
        arrays: POINTER(c_uint)
            Specifies an array in which the generated vertex array object names are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenVertexArrays.xhtml
        """
        pass

    def get_booleani_v(self, target: int, index: int, data: POINTER(c_bool)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetBooleani_v

        Parameters
        ----------
        target: int
            Specifies the parameter value to be returned for indexed versions of glGet. The symbolic constants
            in the list below are accepted.
        index: int
            Specifies the index of the particular element being queried.
        data: POINTER(c_bool)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_integeri_v(self, target: int, index: int, data: POINTER(c_int)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetIntegeri_v

        Parameters
        ----------
        target: int
            Specifies the parameter value to be returned for indexed versions of glGet. The symbolic constants
            in the list below are accepted.
        index: int
            Specifies the index of the particular element being queried.
        data: POINTER(c_int)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_frag_data_location(self, program: int, name: bytes) -> int:
        """
        Query the bindings of color numbers to user-defined varying out variables

        Wrapper for glGetFragDataLocation

        Parameters
        ----------
        program: int
            The name of the program containing varying out variable whose binding to query
        name: bytes
            The name of the user-defined varying out variable whose binding to query

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not the name of a program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetFragDataLocation.xhtml
        """
        pass

    def get_framebuffer_attachment_parameteriv(self, target: int, attachment: int, pname: int, params: POINTER(c_int)):
        """
        Retrieve information about attachments of a framebuffer object

        Wrapper for glGetFramebufferAttachmentParameteriv

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer object is bound for
            glGetFramebufferAttachmentParameteriv.
        attachment: int
            Specifies the attachment of the framebuffer object to query.
        pname: int
            Specifies the parameter of attachment to query.
        params: POINTER(c_int)
            Returns the value of parameter pname for attachment.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetFramebufferAttachmentParameteriv if target is not one of the
            accepted framebuffer targets.
        GL_INVALID_OPERATION is generated by glGetNamedFramebufferAttachmentParameteriv if framebuffer is
            not zero or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if pname is not valid for the value of
            GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE, as described above.
        GL_INVALID_OPERATION is generated if attachment is not one of the accepted framebuffer attachment
            points, as described above.
        GL_INVALID_OPERATION is generated if the value of GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE is GL_NONE
            and pname is not GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME or GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE.
        GL_INVALID_OPERATION is generated if attachment is GL_DEPTH_STENCIL_ATTACHMENT and different
            objects are bound to the depth and stencil attachment points of target.
        GL_INVALID_OPERATION is generated if attachment is GL_DEPTH_STENCIL_ATTACHMENT and pname is
            GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetFramebufferAttachmentParameter.xhtml
        """
        pass

    def get_renderbuffer_parameteriv(self, target: int, pname: int, params: POINTER(c_int)):
        """
        Query a named parameter of a renderbuffer object

        Wrapper for glGetRenderbufferParameteriv

        Parameters
        ----------
        target: int
            Specifies the target to which the renderbuffer object is bound for glGetRenderbufferParameteriv.
            target must be GL_RENDERBUFFER.
        pname: int
            Specifies the parameter of the renderbuffer object to query.
        params: POINTER(c_int)
            Returns the value of parameter pname for the renderbuffer object.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetRenderbufferParameteriv if target is not GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated by glGetRenderbufferParameteriv if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedRenderbufferParameteriv if renderbuffer is not the
            name of an existing renderbuffer object.
        GL_INVALID_ENUM is generated if pname is not one of the accepted parameter names described above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetRenderbufferParameter.xhtml
        """
        pass

    def get_stringi(self, name: int, index: int) -> POINTER(c_ubyte):
        """
        Return a string describing the current GL connection

        Wrapper for glGetStringi

        Parameters
        ----------
        name: int
            Specifies a symbolic constant, one of GL_VENDOR, GL_RENDERER, GL_VERSION, or
            GL_SHADING_LANGUAGE_VERSION. Additionally, glGetStringi accepts the GL_EXTENSIONS token.
        index: int
            For glGetStringi, specifies the index of the string to return.

        Raises
        ------
        GL_INVALID_ENUM is generated if name is not an accepted value.
        GL_INVALID_VALUE is generated by glGetStringi if index is outside the valid range for indexed state
            name.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetString.xhtml
        """
        pass

    def get_tex_parameter_iiv(self, target: int, pname: int, params: POINTER(c_int)):
        """
        Return texture parameter values

        Wrapper for glGetTexParameterIiv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexParameterfv, glGetTexParameteriv,
            glGetTexParameterIiv, and glGetTexParameterIuiv functions. GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE, GL_TEXTURE_2D_MULTISAMPLE_ARRAY,
            GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_RECTANGLE, and GL_TEXTURE_CUBE_MAP_ARRAY are
            accepted.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_int)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_tex_parameter_iuiv(self, target: int, pname: int, params: POINTER(c_uint)):
        """
        Return texture parameter values

        Wrapper for glGetTexParameterIuiv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexParameterfv, glGetTexParameteriv,
            glGetTexParameterIiv, and glGetTexParameterIuiv functions. GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE, GL_TEXTURE_2D_MULTISAMPLE_ARRAY,
            GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_RECTANGLE, and GL_TEXTURE_CUBE_MAP_ARRAY are
            accepted.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_uint)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_transform_feedback_varying(self, program: int, index: int, buf_size: int, length: POINTER(c_uint32), size: POINTER(c_uint32), type: POINTER(c_uint32), name: bytes):
        """
        Retrieve information about varying variables selected for transform feedback

        Wrapper for glGetTransformFeedbackVarying

        Parameters
        ----------
        program: int
            The name of the target program object.
        index: int
            The index of the varying variable whose information to retrieve.
        length: POINTER(c_uint32)
            The address of a variable which will receive the number of characters written into name, excluding
            the null-terminator. If length is NULL no length is returned.
        size: POINTER(c_uint32)
            The address of a variable that will receive the size of the varying.
        type: POINTER(c_uint32)
            The address of a variable that will recieve the type of the varying.
        name: bytes
            The address of a buffer into which will be written the name of the varying.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not the name of a program object.
        GL_INVALID_VALUE is generated if index is greater or equal to the value of
            GL_TRANSFORM_FEEDBACK_VARYINGS.
        GL_INVALID_OPERATION is generated program has not been linked.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTransformFeedbackVarying.xhtml
        """
        pass

    def get_uniformuiv(self, program: int, location: int, params: POINTER(c_uint)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetUniformuiv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_uint)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def get_vertex_attrib_iiv(self, index: int, pname: int, params: POINTER(c_int)):
        """
        Return a generic vertex attribute parameter

        Wrapper for glGetVertexAttribIiv

        Parameters
        ----------
        index: int
            Specifies the generic vertex attribute parameter to be queried.
        pname: int
            Specifies the symbolic name of the vertex attribute parameter to be queried. Accepted values are
            GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING, GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or GL_CURRENT_VERTEX_ATTRIB.
        params: POINTER(c_int)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pname is not GL_CURRENT_VERTEX_ATTRIB and there is no
            currently bound vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if index is 0 and pname is GL_CURRENT_VERTEX_ATTRIB.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexAttrib.xhtml
        """
        pass

    def get_vertex_attrib_iuiv(self, index: int, pname: int, params: POINTER(c_uint)):
        """
        Return a generic vertex attribute parameter

        Wrapper for glGetVertexAttribIuiv

        Parameters
        ----------
        index: int
            Specifies the generic vertex attribute parameter to be queried.
        pname: int
            Specifies the symbolic name of the vertex attribute parameter to be queried. Accepted values are
            GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING, GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or GL_CURRENT_VERTEX_ATTRIB.
        params: POINTER(c_uint)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pname is not GL_CURRENT_VERTEX_ATTRIB and there is no
            currently bound vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if index is 0 and pname is GL_CURRENT_VERTEX_ATTRIB.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexAttrib.xhtml
        """
        pass

    def is_enabledi(self, cap: int, index: int) -> bool:
        """
        Test whether a capability is enabled

        Wrapper for glIsEnabledi

        Parameters
        ----------
        cap: int
            Specifies a symbolic constant indicating a GL capability.
        index: int
            Specifies the index of the capability.

        Raises
        ------
        GL_INVALID_ENUM is generated if cap is not an accepted value.
        GL_INVALID_VALUE is generated by glIsEnabledi if index is outside the valid range for the indexed
            state cap.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsEnabled.xhtml
        """
        pass

    def is_framebuffer(self, framebuffer: int) -> bool:
        """
        Determine if a name corresponds to a framebuffer object

        Wrapper for glIsFramebuffer

        Parameters
        ----------
        framebuffer: int
            Specifies a value that may be the name of a framebuffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsFramebuffer.xhtml
        """
        pass

    def is_renderbuffer(self, renderbuffer: int) -> bool:
        """
        Determine if a name corresponds to a renderbuffer object

        Wrapper for glIsRenderbuffer

        Parameters
        ----------
        renderbuffer: int
            Specifies a value that may be the name of a renderbuffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsRenderbuffer.xhtml
        """
        pass

    def is_vertex_array(self, array: int) -> bool:
        """
        Determine if a name corresponds to a vertex array object

        Wrapper for glIsVertexArray

        Parameters
        ----------
        array: int
            Specifies a value that may be the name of a vertex array object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsVertexArray.xhtml
        """
        pass

    def map_buffer_range(self, target: int, offset: POINTER(c_int), length: POINTER(c_uint32), access: int) -> c_void_p:
        """
        Map all or part of a buffer object's data store into the client's address space

        Wrapper for glMapBufferRange

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glMapBufferRange, which must be one of
            the buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER
            Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy
            source GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute
            dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex
            array indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        offset: POINTER(c_int)
            Specifies the starting offset within the buffer of the range to be mapped.
        length: POINTER(c_uint32)
            Specifies the length of the range to be mapped.
        access: int
            Specifies a combination of access flags indicating the desired access to the mapped range.

        Raises
        ------
        GL_INVALID_ENUM is generated by glMapBufferRange if target is not one of the buffer binding targets
            listed above.
        GL_INVALID_OPERATION is generated by glMapBufferRange if zero is bound to target.
        GL_INVALID_OPERATION is generated by glMapNamedBufferRange if buffer is not the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if offset or length is negative, if $offset + length$ is greater than
            the value of GL_BUFFER_SIZE for the buffer object, or if access has any bits set other than those
            defined above.
        GL_INVALID_OPERATION is generated for any of the following conditions:
        length is zero.
        The buffer object is already in a mapped state.
        Neither GL_MAP_READ_BIT nor GL_MAP_WRITE_BIT is set.
        GL_MAP_READ_BIT is set and any of GL_MAP_INVALIDATE_RANGE_BIT, GL_MAP_INVALIDATE_BUFFER_BIT or
            GL_MAP_UNSYNCHRONIZED_BIT is set.
        GL_MAP_FLUSH_EXPLICIT_BIT is set and GL_MAP_WRITE_BIT is not set.
        Any of GL_MAP_READ_BIT, GL_MAP_WRITE_BIT, GL_MAP_PERSISTENT_BIT, or GL_MAP_COHERENT_BIT are set,
            but the same bit is not included in the buffer's storage flags.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMapBufferRange.xhtml
        """
        pass

    def renderbuffer_storage(self, target: int, internalformat: int, width: int, height: int):
        """
        Establish data storage, format and dimensions of a renderbuffer object's image

        Wrapper for glRenderbufferStorage

        Parameters
        ----------
        target: int
            Specifies a binding target of the allocation for glRenderbufferStorage function. Must be
            GL_RENDERBUFFER.
        internalformat: int
            Specifies the internal format to use for the renderbuffer object's image.
        width: int
            Specifies the width of the renderbuffer, in pixels.
        height: int
            Specifies the height of the renderbuffer, in pixels.

        Raises
        ------
        GL_INVALID_ENUM is generated by glRenderbufferStorage if target is not GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated by glNamedRenderbufferStorage if renderbuffer is not the name of
            an existing renderbuffer object.
        GL_INVALID_VALUE is generated if either of width or height is negative, or greater than the value
            of GL_MAX_RENDERBUFFER_SIZE.
        GL_INVALID_ENUM is generated if internalformat is not a color-renderable, depth-renderable, or
            stencil-renderable format.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store of the requested size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glRenderbufferStorage.xhtml
        """
        pass

    def renderbuffer_storage_multisample(self, target: int, samples: int, internalformat: int, width: int, height: int):
        """
        Establish data storage, format, dimensions and sample count of a renderbuffer object's image

        Wrapper for glRenderbufferStorageMultisample

        Parameters
        ----------
        target: int
            Specifies a binding target of the allocation for glRenderbufferStorageMultisample function. Must be
            GL_RENDERBUFFER.
        samples: int
            Specifies the number of samples to be used for the renderbuffer object's storage.
        internalformat: int
            Specifies the internal format to use for the renderbuffer object's image.
        width: int
            Specifies the width of the renderbuffer, in pixels.
        height: int
            Specifies the height of the renderbuffer, in pixels.

        Raises
        ------
        GL_INVALID_ENUM is generated by glRenderbufferStorageMultisample function if target is not
            GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated by glNamedRenderbufferStorageMultisample function if renderbuffer
            is not the name of an existing renderbuffer object.
        GL_INVALID_OPERATION is generated if samples is greater than the maximum number of samples
            supported for internalformat.
        GL_INVALID_ENUM is generated if internalformat is not a color-renderable, depth-renderable, or
            stencil-renderable format.
        GL_INVALID_OPERATION is generated if internalformat is a signed or unsigned integer format and
            samples is greater than the value of GL_MAX_INTEGER_SAMPLES
        GL_INVALID_VALUE is generated if either of width or height is negative, or greater than the value
            of GL_MAX_RENDERBUFFER_SIZE.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store of the requested size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glRenderbufferStorageMultisample.xhtml
        """
        pass

    def tex_parameter_iiv(self, target: int, pname: int, params: POINTER(c_int)):
        """
        Set texture parameters

        Wrapper for glTexParameterIiv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glTexParameter functions. Must be one of
            GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY, or
            GL_TEXTURE_RECTANGLE.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        params: POINTER(c_int)
            For the vector commands, specifies a pointer to an array where the value or values of pname are
            stored.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def tex_parameter_iuiv(self, target: int, pname: int, params: POINTER(c_uint)):
        """
        Set texture parameters

        Wrapper for glTexParameterIuiv

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glTexParameter functions. Must be one of
            GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY, or
            GL_TEXTURE_RECTANGLE.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        params: POINTER(c_uint)
            For the vector commands, specifies a pointer to an array where the value or values of pname are
            stored.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def transform_feedback_varyings(self, program: int, count: int, varyings: POINTER(c_char_p), buffer_mode: int):
        """
        Specify values to record in transform feedback buffers

        Wrapper for glTransformFeedbackVaryings

        Parameters
        ----------
        program: int
            The name of the target program object.
        count: int
            The number of varying variables used for transform feedback.
        varyings: POINTER(c_char_p)
            An array of count zero-terminated strings specifying the names of the varying variables to use for
            transform feedback.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not the name of a program object.
        GL_INVALID_VALUE is generated if bufferMode is GL_SEPARATE_ATTRIBS and count is greater than the
            implementation-dependent limit GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTransformFeedbackVaryings.xhtml
        """
        pass

    def uniform1ui(self, location: int, v0: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform1ui

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform2ui(self, location: int, v0: int, v1: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform2ui

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform3ui(self, location: int, v0: int, v1: int, v2: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform3ui

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform4ui(self, location: int, v0: int, v1: int, v2: int, v3: int):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform4ui

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2, v3: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform1uiv(self, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform1uiv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform2uiv(self, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform2uiv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform3uiv(self, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform3uiv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def uniform4uiv(self, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for the current program object

        Wrapper for glUniform4uiv

        Parameters
        ----------
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector (glUniform*v) commands, specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            For the matrix (glUniformMatrix*) commands, specifies the number of matrices that are to be
            modified. This should be 1 if the targeted uniform variable is not an array of matrices, and 1 or
            more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no current program object.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for the current
            program object and location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than glUniform1i and
            glUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniform.xhtml
        """
        pass

    def vertex_attrib_i1i(self, index: int, v0: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI1i

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i1ui(self, index: int, v0: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI1ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i2i(self, index: int, v0: int, v1: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI2i

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i2ui(self, index: int, v0: int, v1: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI2ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i3i(self, index: int, v0: int, v1: int, v2: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI3i

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i3ui(self, index: int, v0: int, v1: int, v2: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI3ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4i(self, index: int, v0: int, v1: int, v2: int, v3: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4i

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2, v3: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4ui(self, index: int, v0: int, v1: int, v2: int, v3: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2, v3: int
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i1iv(self, index: int, v: POINTER(c_int)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI1iv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i1uiv(self, index: int, v: POINTER(c_uint)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI1uiv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_uint)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i2iv(self, index: int, v: POINTER(c_int)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI2iv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i2uiv(self, index: int, v: POINTER(c_uint)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI2uiv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_uint)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i3iv(self, index: int, v: POINTER(c_int)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI3iv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i3uiv(self, index: int, v: POINTER(c_uint)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI3uiv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_uint)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4bv(self, index: int, v: POINTER(c_byte)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4bv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_byte)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4ubv(self, index: int, v: POINTER(c_ubyte)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4ubv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_ubyte)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4sv(self, index: int, v: POINTER(c_int16)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4sv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int16)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4usv(self, index: int, v: POINTER(c_ushort)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4usv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_ushort)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4iv(self, index: int, v: POINTER(c_int)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4iv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_int)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_i4uiv(self, index: int, v: POINTER(c_uint)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribI4uiv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_uint)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_ipointer(self, index: int, size: int, type: int, stride: int, pointer: c_void_p):
        """
        Define an array of generic vertex attribute data

        Wrapper for glVertexAttribIPointer

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        size: int
            Specifies the number of components per generic vertex attribute. Must be 1, 2, 3, 4. Additionally,
            the symbolic constant GL_BGRA is accepted by glVertexAttribPointer. The initial value is 4.
        type: int
            Specifies the data type of each component in the array. The symbolic constants GL_BYTE,
            GL_UNSIGNED_BYTE, GL_SHORT, GL_UNSIGNED_SHORT, GL_INT, and GL_UNSIGNED_INT are accepted by
            glVertexAttribPointer and glVertexAttribIPointer. Additionally GL_HALF_FLOAT, GL_FLOAT, GL_DOUBLE,
            GL_FIXED, GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV and GL_UNSIGNED_INT_10F_11F_11F_REV
            are accepted by glVertexAttribPointer. GL_DOUBLE is also accepted by glVertexAttribLPointer and is
            the only token accepted by the type parameter for that function. The initial value is GL_FLOAT.
        stride: int
            Specifies the byte offset between consecutive generic vertex attributes. If stride is 0, the
            generic vertex attributes are understood to be tightly packed in the array. The initial value is 0.
        pointer: c_void_p
            Specifies a offset of the first component of the first generic vertex attribute in the array in the
            data store of the buffer currently bound to the GL_ARRAY_BUFFER target. The initial value is 0.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not 1, 2, 3, 4 or (for glVertexAttribPointer), GL_BGRA.
        GL_INVALID_ENUM is generated if type is not an accepted value.
        GL_INVALID_VALUE is generated if stride is negative.
        GL_INVALID_OPERATION is generated if size is GL_BGRA and type is not GL_UNSIGNED_BYTE,
            GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV.
        GL_INVALID_OPERATION is generated if type is GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV and size is not 4 or GL_BGRA.
        GL_INVALID_OPERATION is generated if type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        GL_INVALID_OPERATION is generated by glVertexAttribPointer if size is GL_BGRA and noramlized is
            GL_FALSE.
        GL_INVALID_OPERATION is generated if zero is bound to the GL_ARRAY_BUFFER buffer object binding
            point and the pointer argument is not NULL.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribPointer.xhtml
        """
        pass

class GL31(GL30):

    MAJOR = 3
    MINOR = 1

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.copy_buffer_sub_data, 'glCopyBufferSubData',
                   None, c_uint, c_uint, POINTER(c_int), POINTER(c_int), POINTER(c_uint32))
        self._load(self.draw_arrays_instanced, 'glDrawArraysInstanced',
                   None, c_uint, c_int, c_uint32, c_uint32)
        self._load(self.draw_elements_instanced, 'glDrawElementsInstanced',
                   None, c_uint, c_uint32, c_uint, c_void_p, c_uint32)
        self._load(self.get_active_uniform_blockiv, 'glGetActiveUniformBlockiv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_active_uniform_block_name, 'glGetActiveUniformBlockName',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_active_uniform_name, 'glGetActiveUniformName',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_active_uniformsiv, 'glGetActiveUniformsiv',
                   None, c_uint, c_uint32, POINTER(c_uint), c_uint, POINTER(c_int))
        self._load(self.get_uniform_block_index, 'glGetUniformBlockIndex',
                   c_uint, c_uint, c_char_p)
        self._load(self.get_uniform_indices, 'glGetUniformIndices',
                   None, c_uint, c_uint32, POINTER(c_char_p), POINTER(c_uint))
        self._load(self.primitive_restart_index, 'glPrimitiveRestartIndex',
                   None, c_uint)
        self._load(self.tex_buffer, 'glTexBuffer',
                   None, c_uint, c_uint, c_uint)
        self._load(self.uniform_block_binding, 'glUniformBlockBinding',
                   None, c_uint, c_uint, c_uint)

    def copy_buffer_sub_data(self, read_target: int, write_target: int, read_offset: POINTER(c_int), write_offset: POINTER(c_int), size: POINTER(c_uint32)):
        """
        Copy all or part of the data store of a buffer object to the data store of another buffer object

        Wrapper for glCopyBufferSubData

        Parameters
        ----------
        size: POINTER(c_uint32)
            Specifies the size, in basic machine units, of the data to be copied from the source buffer object
            to the destination buffer object.

        Raises
        ------
        GL_INVALID_ENUM is generated by glCopyBufferSubData if readTarget or writeTarget is not one of the
            buffer binding targets listed above.
        GL_INVALID_OPERATION is generated by glCopyBufferSubData if zero is bound to readTarget or
            writeTarget.
        GL_INVALID_OPERATION is generated by glCopyNamedBufferSubData if readBuffer or writeBuffer is not
            the name of an existing buffer object.
        GL_INVALID_VALUE is generated if any of readOffset, writeOffset or size is negative, if $readOffset
            + size$ is greater than the size of the source buffer object (its value of GL_BUFFER_SIZE), or if
            $writeOffset + size$ is greater than the size of the destination buffer object.
        GL_INVALID_VALUE is generated if the source and destination are the same buffer object, and the
            ranges $[readOffset,readOffset+size)$ and $[writeOffset,writeOffset+size)$ overlap.
        GL_INVALID_OPERATION is generated if either the source or destination buffer object is mapped with
            glMapBufferRange or glMapBuffer, unless they were mapped with the GL_MAP_PERSISTENT bit set in the
            glMapBufferRange access flags.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCopyBufferSubData.xhtml
        """
        pass

    def draw_arrays_instanced(self, mode: int, first: int, count: int, primcount: int):
        """
        Draw multiple instances of a range of elements

        Wrapper for glDrawArraysInstanced

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES GL_LINES_ADJACENCY,
            GL_LINE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY and GL_PATCHES are
            accepted.
        first: int
            Specifies the starting index in the enabled arrays.
        count: int
            Specifies the number of indices to be rendered.
        primcount: int
            Specifies the number of instances of the specified range of indices to be rendered.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of the accepted values.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_VALUE is generated if count or primcount are negative.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawArraysInstanced.xhtml
        """
        pass

    def draw_elements_instanced(self, mode: int, count: int, type: int, indices: c_void_p, primcount: int):
        """
        Draw multiple instances of a set of elements

        Wrapper for glDrawElementsInstanced

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.
        primcount: int
            Specifies the number of instances of the specified range of indices to be rendered.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of GL_POINTS, GL_LINE_STRIP, GL_LINE_LOOP,
            GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, or GL_TRIANGLES.
        GL_INVALID_VALUE is generated if count or primcount are negative.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawElementsInstanced.xhtml
        """
        pass

    def get_active_uniform_blockiv(self, program: int, uniform_block_index: int, pname: int, params: POINTER(c_int)):
        """
        Query information about an active uniform block

        Wrapper for glGetActiveUniformBlockiv

        Parameters
        ----------
        program: int
            Specifies the name of a program containing the uniform block.
        pname: int
            Specifies the name of the parameter to query.
        params: POINTER(c_int)
            Specifies the address of a variable to receive the result of the query.

        Raises
        ------
        GL_INVALID_VALUE is generated if uniformBlockIndex is greater than or equal to the value of
            GL_ACTIVE_UNIFORM_BLOCKS or is not the index of an active uniform block in program.
        GL_INVALID_ENUM is generated if pname is not one of the accepted tokens.
        GL_INVALID_OPERATION is generated if program is not the name of a program object for which
            glLinkProgram has been called in the past.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveUniformBlock.xhtml
        """
        pass

    def get_active_uniform_block_name(self, program: int, uniform_block_index: int, buf_size: int, length: POINTER(c_uint32), uniform_block_name: bytes):
        """
        Retrieve the name of an active uniform block

        Wrapper for glGetActiveUniformBlockName

        Parameters
        ----------
        program: int
            Specifies the name of a program containing the uniform block.
        length: POINTER(c_uint32)
            Specifies the address of a variable to receive the number of characters that were written to
            uniformBlockName.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not the name of a program object for which
            glLinkProgram has been called in the past.
        GL_INVALID_VALUE is generated if uniformBlockIndex is greater than or equal to the value of
            GL_ACTIVE_UNIFORM_BLOCKS or is not the index of an active uniform block in program.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveUniformBlockName.xhtml
        """
        pass

    def get_active_uniform_name(self, program: int, uniform_index: int, buf_size: int, length: POINTER(c_uint32), uniform_name: bytes):
        """
        Query the name of an active uniform

        Wrapper for glGetActiveUniformName

        Parameters
        ----------
        program: int
            Specifies the program containing the active uniform index uniformIndex.
        length: POINTER(c_uint32)
            Specifies the address of a variable that will receive the number of characters that were or would
            have been written to the buffer addressed by uniformName.

        Raises
        ------
        GL_INVALID_VALUE is generated if uniformIndex is greater than or equal to the value of
            GL_ACTIVE_UNIFORMS.
        GL_INVALID_VALUE is generated if bufSize is negative.
        GL_INVALID_VALUE is generated if program is not the name of a program object for which
            glLinkProgram has been issued.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveUniformName.xhtml
        """
        pass

    def get_active_uniformsiv(self, program: int, uniform_count: int, uniform_indices: POINTER(c_uint), pname: int, params: POINTER(c_int)):
        """
        Returns information about several active uniform variables for the specified program object

        Wrapper for glGetActiveUniformsiv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        pname: int
            Specifies the property of each uniform in uniformIndices that should be written into the
            corresponding element of params.
        params: POINTER(c_int)
            Specifies the address of an array of uniformCount integers which are to receive the value of pname
            for each uniform in uniformIndices.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_VALUE is generated if uniformCount is greater than or equal to the value of
            GL_ACTIVE_UNIFORMS for program.
        GL_INVALID_ENUM is generated if pname is not an accepted token.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveUniformsiv.xhtml
        """
        pass

    def get_uniform_block_index(self, program: int, uniform_block_name: bytes) -> int:
        """
        Retrieve the index of a named uniform block

        Wrapper for glGetUniformBlockIndex

        Parameters
        ----------
        program: int
            Specifies the name of a program containing the uniform block.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not the name of a program object for which
            glLinkProgram has been called in the past.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniformBlockIndex.xhtml
        """
        pass

    def get_uniform_indices(self, program: int, uniform_count: int, uniform_names: POINTER(c_char_p), uniform_indices: POINTER(c_uint)):
        """
        Retrieve the index of a named uniform block

        Wrapper for glGetUniformIndices

        Parameters
        ----------
        program: int
            Specifies the name of a program containing uniforms whose indices to query.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not the name of a program object for which
            glLinkProgram has been called in the past.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniformIndices.xhtml
        """
        pass

    def primitive_restart_index(self, index: int):
        """
        Specify the primitive restart index

        Wrapper for glPrimitiveRestartIndex

        Parameters
        ----------
        index: int
            Specifies the value to be interpreted as the primitive restart index.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPrimitiveRestartIndex.xhtml
        """
        pass

    def tex_buffer(self, target: int, internal_format: int, buffer: int):
        """
        Attach a buffer object's data store to a buffer texture object

        Wrapper for glTexBuffer

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glTexBuffer. Must be GL_TEXTURE_BUFFER.
        buffer: int
            Specifies the name of the buffer object whose storage to attach to the active buffer texture.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexBuffer if target is not GL_TEXTURE_BUFFER.
        GL_INVALID_OPERATION is generated by glTextureBuffer if texture is not the name of an existing
            texture object.
        GL_INVALID_ENUM is generated by glTextureBuffer if the effective target of texture is not
            GL_TEXTURE_BUFFER.
        GL_INVALID_ENUM is generated if internalformat is not one of the sized internal formats described
            above.
        GL_INVALID_OPERATION is generated if buffer is not zero and is not the name of an existing buffer
            object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexBuffer.xhtml
        """
        pass

    def uniform_block_binding(self, program: int, uniform_block_index: int, uniform_block_binding: int):
        """
        Assign a binding point to an active uniform block

        Wrapper for glUniformBlockBinding

        Parameters
        ----------
        program: int
            The name of a program object containing the active uniform block whose binding to assign.

        Raises
        ------
        GL_INVALID_VALUE is generated if uniformBlockIndex is not an active uniform block index of program.
        GL_INVALID_VALUE is generated if uniformBlockBinding is greater than or equal to the value of
            GL_MAX_UNIFORM_BUFFER_BINDINGS.
        GL_INVALID_VALUE is generated if program is not the name of a program object generated by the GL.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniformBlockBinding.xhtml
        """
        pass

class GL32(GL31):

    MAJOR = 3
    MINOR = 2

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.bind_frag_data_location_indexed, 'glBindFragDataLocationIndexed',
                   None, c_uint, c_uint, c_uint, c_char_p)
        self._load(self.bind_sampler, 'glBindSampler',
                   None, c_uint, c_uint)
        self._load(self.client_wait_sync, 'glClientWaitSync',
                   c_uint, c_void_p, c_uint32, c_uint64)
        self._load(self.delete_samplers, 'glDeleteSamplers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.delete_sync, 'glDeleteSync',
                   None, c_void_p)
        self._load(self.draw_elements_base_vertex, 'glDrawElementsBaseVertex',
                   None, c_uint, c_uint32, c_uint, c_void_p, c_int)
        self._load(self.draw_elements_instanced_base_vertex, 'glDrawElementsInstancedBaseVertex',
                   None, c_uint, c_uint32, c_uint, c_void_p, c_uint32, c_int)
        self._load(self.draw_range_elements_base_vertex, 'glDrawRangeElementsBaseVertex',
                   None, c_uint, c_uint, c_uint, c_uint32, c_uint, c_void_p, c_int)
        self._load(self.fence_sync, 'glFenceSync',
                   c_void_p, c_uint, c_uint32)
        self._load(self.framebuffer_texture, 'glFramebufferTexture',
                   None, c_uint, c_uint, c_uint, c_int)
        self._load(self.gen_samplers, 'glGenSamplers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.get_integer64v, 'glGetInteger64v',
                   None, c_uint, POINTER(c_int64))
        self._load(self.get_integer64i_v, 'glGetInteger64i_v',
                   None, c_uint, c_uint, POINTER(c_int64))
        self._load(self.get_buffer_parameteri64v, 'glGetBufferParameteri64v',
                   None, c_uint, c_uint, POINTER(c_int64))
        self._load(self.get_frag_data_index, 'glGetFragDataIndex',
                   c_int, c_uint, c_char_p)
        self._load(self.get_multisamplefv, 'glGetMultisamplefv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.get_query_objecti64v, 'glGetQueryObjecti64v',
                   None, c_uint, c_uint, POINTER(c_int64))
        self._load(self.get_query_objectui64v, 'glGetQueryObjectui64v',
                   None, c_uint, c_uint, POINTER(c_uint64))
        self._load(self.get_sampler_parameterfv, 'glGetSamplerParameterfv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.get_sampler_parameteriv, 'glGetSamplerParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_sampler_parameter_iiv, 'glGetSamplerParameterIiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_sampler_parameter_iuiv, 'glGetSamplerParameterIuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.get_synciv, 'glGetSynciv',
                   None, c_void_p, c_uint, c_uint32, POINTER(c_uint32), POINTER(c_int))
        self._load(self.is_sampler, 'glIsSampler',
                   c_bool, c_uint)
        self._load(self.is_sync, 'glIsSync',
                   c_bool, c_void_p)
        self._load(self.multi_draw_elements_base_vertex, 'glMultiDrawElementsBaseVertex',
                   None, c_uint, POINTER(c_uint32), c_uint, c_uint32, POINTER(c_int))
        self._load(self.provoking_vertex, 'glProvokingVertex',
                   None, c_uint)
        self._load(self.query_counter, 'glQueryCounter',
                   None, c_uint, c_uint)
        self._load(self.sample_maski, 'glSampleMaski',
                   None, c_uint, c_uint32)
        self._load(self.sampler_parameterf, 'glSamplerParameterf',
                   None, c_uint, c_uint, c_float)
        self._load(self.sampler_parameteri, 'glSamplerParameteri',
                   None, c_uint, c_uint, c_int)
        self._load(self.sampler_parameterfv, 'glSamplerParameterfv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.sampler_parameteriv, 'glSamplerParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.sampler_parameter_iiv, 'glSamplerParameterIiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.sampler_parameter_iuiv, 'glSamplerParameterIuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.wait_sync, 'glWaitSync',
                   None, c_void_p, c_uint32, c_uint64)

    def bind_frag_data_location_indexed(self, program: int, color_number: int, index: int, name: bytes):
        """
        Bind a user-defined varying out variable to a fragment shader color number and index

        Wrapper for glBindFragDataLocationIndexed

        Parameters
        ----------
        program: int
            The name of the program containing varying out variable whose binding to modify
        index: int
            The index of the color input to bind the user-defined varying out variable to
        name: bytes
            The name of the user-defined varying out variable whose binding to modify

        Raises
        ------
        GL_INVALID_VALUE is generated if colorNumber is greater than or equal to GL_MAX_DRAW_BUFFERS.
        GL_INVALID_VALUE is generated if colorNumber is greater than or equal to
            GL_MAX_DUAL_SOURCE_DRAW_BUFFERS and index is greater than or equal to one.
        GL_INVALID_VALUE is generated if index is greater than one.
        GL_INVALID_OPERATION is generated if name starts with the reserved gl_ prefix.
        GL_INVALID_OPERATION is generated if program is not the name of a program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindFragDataLocationIndexed.xhtml
        """
        pass

    def bind_sampler(self, unit: int, sampler: int):
        """
        Bind a named sampler to a texturing target

        Wrapper for glBindSampler

        Parameters
        ----------
        unit: int
            Specifies the index of the texture unit to which the sampler is bound.
        sampler: int
            Specifies the name of a sampler.

        Raises
        ------
        GL_INVALID_VALUE is generated if unit is greater than or equal to the value of
            GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS.
        GL_INVALID_OPERATION is generated if sampler is not zero or a name previously returned from a call
            to glGenSamplers, or if such a name has been deleted by a call to glDeleteSamplers.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindSampler.xhtml
        """
        pass

    def client_wait_sync(self, sync: c_void_p, flags: int, timeout: int) -> int:
        """
        Block and wait for a sync object to become signaled

        Wrapper for glClientWaitSync

        Parameters
        ----------
        sync: c_void_p
            The sync object whose status to wait on.
        flags: int
            A bitfield controlling the command flushing behavior. flags may be GL_SYNC_FLUSH_COMMANDS_BIT.
        timeout: int
            The timeout, specified in nanoseconds, for which the implementation should wait for sync to become
            signaled.

        Raises
        ------
        GL_INVALID_VALUE is generated if sync is not the name of an existing sync object.
        GL_INVALID_VALUE is generated if flags contains any unsupported flag.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClientWaitSync.xhtml
        """
        pass

    def delete_samplers(self, n: int, samplers: POINTER(c_uint)):
        """
        Delete named sampler objects

        Wrapper for glDeleteSamplers

        Parameters
        ----------
        n: int
            Specifies the number of sampler objects to be deleted.
        samplers: POINTER(c_uint)
            Specifies an array of sampler objects to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteSamplers.xhtml
        """
        pass

    def delete_sync(self, sync: c_void_p):
        """
        Delete a sync object

        Wrapper for glDeleteSync

        Parameters
        ----------
        sync: c_void_p
            The sync object to be deleted.

        Raises
        ------
        GL_INVALID_VALUE is generated if sync is neither zero or the name of a sync object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteSync.xhtml
        """
        pass

    def draw_elements_base_vertex(self, mode: int, count: int, type: int, indices: c_void_p, basevertex: int):
        """
        Render primitives from array data with a per-element offset

        Wrapper for glDrawElementsBaseVertex

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES, GL_LINES_ADJACENCY,
            GL_LINE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY and GL_PATCHES are
            accepted.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.
        basevertex: int
            Specifies a constant that should be added to each element of indices when chosing elements from the
            enabled vertex arrays.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if count is negative.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawElementsBaseVertex.xhtml
        """
        pass

    def draw_elements_instanced_base_vertex(self, mode: int, count: int, type: int, indices: c_void_p, primcount: int, basevertex: int):
        """
        Render multiple instances of a set of primitives from array data with a per-element offset

        Wrapper for glDrawElementsInstancedBaseVertex

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES, GL_LINES_ADJACENCY,
            GL_LINE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY and GL_PATCHES are
            accepted.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.
        primcount: int
            Specifies the number of instances of the indexed geometry that should be drawn.
        basevertex: int
            Specifies a constant that should be added to each element of indices when chosing elements from the
            enabled vertex arrays.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if count or primcount is negative.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawElementsInstancedBaseVertex.xhtml
        """
        pass

    def draw_range_elements_base_vertex(self, mode: int, start: int, end: int, count: int, type: int, indices: c_void_p, basevertex: int):
        """
        Render primitives from array data with a per-element offset

        Wrapper for glDrawRangeElementsBaseVertex

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES, GL_LINES_ADJACENCY,
            GL_LINE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY and GL_PATCHES are
            accepted.
        start: int
            Specifies the minimum array index contained in indices.
        end: int
            Specifies the maximum array index contained in indices.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.
        basevertex: int
            Specifies a constant that should be added to each element of indices when chosing elements from the
            enabled vertex arrays.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if count is negative.
        GL_INVALID_VALUE is generated if end &lt; start.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawRangeElementsBaseVertex.xhtml
        """
        pass

    def fence_sync(self, condition: int, flags: int) -> c_void_p:
        """
        Create a new sync object and insert it into the GL command stream

        Wrapper for glFenceSync

        Parameters
        ----------
        condition: int
            Specifies the condition that must be met to set the sync object's state to signaled. condition must
            be GL_SYNC_GPU_COMMANDS_COMPLETE.
        flags: int
            Specifies a bitwise combination of flags controlling the behavior of the sync object. No flags are
            presently defined for this operation and flags must be zero. [1]

        Raises
        ------
        GL_INVALID_ENUM is generated if condition is not GL_SYNC_GPU_COMMANDS_COMPLETE.
        GL_INVALID_VALUE is generated if flags is not zero.
        Additionally, if glFenceSync fails, it will return zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFenceSync.xhtml
        """
        pass

    def framebuffer_texture(self, target: int, attachment: int, texture: int, level: int):
        """
        Attach a level of a texture object as a logical buffer of a framebuffer object

        Wrapper for glFramebufferTexture

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer is bound for all commands except
            glNamedFramebufferTexture.
        attachment: int
            Specifies the attachment point of the framebuffer.
        texture: int
            Specifies the name of an existing texture object to attach.
        level: int
            Specifies the mipmap level of the texture object to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by all commands accepting a target parameter if it is not one of the
            accepted framebuffer targets.
        GL_INVALID_OPERATION is generated by all commands accepting a target parameter if zero is bound to
            that target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferTexture if framebuffer is not the name of an
            existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_VALUE is generated if texture is not zero or the name of an existing texture object.
        GL_INVALID_VALUE is generated if texture is not zero and level is not a supported texture level for
            texture.
        GL_INVALID_VALUE is generated by glFramebufferTexture3D if texture is not zero and layer is larger
            than the value of GL_MAX_3D_TEXTURE_SIZE minus one.
        GL_INVALID_OPERATION is generated by all commands accepting a textarget parameter if texture is not
            zero, and textarget and the effective target of texture are not compatible.
        GL_INVALID_OPERATION is generated by if texture is a buffer texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferTexture.xhtml
        """
        pass

    def gen_samplers(self, n: int, samplers: POINTER(c_uint)):
        """
        Generate sampler object names

        Wrapper for glGenSamplers

        Parameters
        ----------
        n: int
            Specifies the number of sampler object names to generate.
        samplers: POINTER(c_uint)
            Specifies an array in which the generated sampler object names are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenSamplers.xhtml
        """
        pass

    def get_integer64v(self, pname: int, data: POINTER(c_int64)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetInteger64v

        Parameters
        ----------
        pname: int
            Specifies the parameter value to be returned for non-indexed versions of glGet. The symbolic
            constants in the list below are accepted.
        data: POINTER(c_int64)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_integer64i_v(self, target: int, index: int, data: POINTER(c_int64)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetInteger64i_v

        Parameters
        ----------
        target: int
            Specifies the parameter value to be returned for indexed versions of glGet. The symbolic constants
            in the list below are accepted.
        index: int
            Specifies the index of the particular element being queried.
        data: POINTER(c_int64)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_buffer_parameteri64v(self, target: int, value: int, data: POINTER(c_int64)):
        """
        Return parameters of a buffer object

        Wrapper for glGetBufferParameteri64v

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glGetBufferParameteriv and
            glGetBufferParameteri64v. Must be one of the buffer binding targets in the following table: Buffer
            Binding Target Purpose GL_ARRAY_BUFFER Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter
            storage GL_COPY_READ_BUFFER Buffer copy source GL_COPY_WRITE_BUFFER Buffer copy destination
            GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect
            command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array indices GL_PIXEL_PACK_BUFFER Pixel read
            target GL_PIXEL_UNPACK_BUFFER Texture data source GL_QUERY_BUFFER Query result buffer
            GL_SHADER_STORAGE_BUFFER Read-write storage for shaders GL_TEXTURE_BUFFER Texture data buffer
            GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer GL_UNIFORM_BUFFER Uniform block storage
        value: int
            Specifies the name of the buffer object parameter to query.
        data: POINTER(c_int64)
            Returns the requested parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetBufferParameter* if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glGetBufferParameter* if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferParameter* if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if pname is not one of the buffer object parameter names described
            above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferParameter.xhtml
        """
        pass

    def get_frag_data_index(self, program: int, name: bytes) -> int:
        """
        Query the bindings of color indices to user-defined varying out variables

        Wrapper for glGetFragDataIndex

        Parameters
        ----------
        program: int
            The name of the program containing varying out variable whose binding to query
        name: bytes
            The name of the user-defined varying out variable whose index to query

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not the name of a program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetFragDataIndex.xhtml
        """
        pass

    def get_multisamplefv(self, pname: int, index: int, val: POINTER(c_float)):
        """
        Retrieve the location of a sample

        Wrapper for glGetMultisamplefv

        Parameters
        ----------
        pname: int
            Specifies the sample parameter name. pname must be GL_SAMPLE_POSITION.
        index: int
            Specifies the index of the sample whose position to query.
        val: POINTER(c_float)
            Specifies the address of an array to receive the position of the sample.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not one GL_SAMPLE_POSITION.
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of GL_SAMPLES.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetMultisample.xhtml
        """
        pass

    def get_query_objecti64v(self, id: int, pname: int, params: POINTER(c_int64)):
        """
        Return parameters of a query object

        Wrapper for glGetQueryObjecti64v

        Parameters
        ----------
        id: int
            Specifies the name of a query object.
        pname: int
            Specifies the symbolic name of a query object parameter. Accepted values are GL_QUERY_RESULT or
            GL_QUERY_RESULT_AVAILABLE.
        params: POINTER(c_int64)
            If a buffer is bound to the GL_QUERY_RESULT_BUFFER target, then params is treated as an offset to a
            location within that buffer's data store to receive the result of the query. If no buffer is bound
            to GL_QUERY_RESULT_BUFFER, then params is treated as an address in client memory of a variable to
            receive the resulting data.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if id is not the name of a query object.
        GL_INVALID_OPERATION is generated if id is the name of a currently active query object.
        GL_INVALID_OPERATION is generated if a buffer is currently bound to the GL_QUERY_RESULT_BUFFER
            target and the command would cause data to be written beyond the bounds of that buffer's data
            store.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetQueryObject.xhtml
        """
        pass

    def get_query_objectui64v(self, id: int, pname: int, params: POINTER(c_uint64)):
        """
        Return parameters of a query object

        Wrapper for glGetQueryObjectui64v

        Parameters
        ----------
        id: int
            Specifies the name of a query object.
        pname: int
            Specifies the symbolic name of a query object parameter. Accepted values are GL_QUERY_RESULT or
            GL_QUERY_RESULT_AVAILABLE.
        params: POINTER(c_uint64)
            If a buffer is bound to the GL_QUERY_RESULT_BUFFER target, then params is treated as an offset to a
            location within that buffer's data store to receive the result of the query. If no buffer is bound
            to GL_QUERY_RESULT_BUFFER, then params is treated as an address in client memory of a variable to
            receive the resulting data.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if id is not the name of a query object.
        GL_INVALID_OPERATION is generated if id is the name of a currently active query object.
        GL_INVALID_OPERATION is generated if a buffer is currently bound to the GL_QUERY_RESULT_BUFFER
            target and the command would cause data to be written beyond the bounds of that buffer's data
            store.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetQueryObject.xhtml
        """
        pass

    def get_sampler_parameterfv(self, sampler: int, pname: int, params: POINTER(c_float)):
        """
        Return sampler parameter values

        Wrapper for glGetSamplerParameterfv

        Parameters
        ----------
        sampler: int
            Specifies name of the sampler object from which to retrieve parameters.
        pname: int
            Specifies the symbolic name of a sampler parameter. GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
            GL_TEXTURE_WRAP_R, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_COMPARE_MODE, and GL_TEXTURE_COMPARE_FUNC
            are accepted.
        params: POINTER(c_float)
            Returns the sampler parameters.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object returned from a
            previous call to glGenSamplers.
        GL_INVALID_ENUM is generated if pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetSamplerParameter.xhtml
        """
        pass

    def get_sampler_parameteriv(self, sampler: int, pname: int, params: POINTER(c_int)):
        """
        Return sampler parameter values

        Wrapper for glGetSamplerParameteriv

        Parameters
        ----------
        sampler: int
            Specifies name of the sampler object from which to retrieve parameters.
        pname: int
            Specifies the symbolic name of a sampler parameter. GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
            GL_TEXTURE_WRAP_R, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_COMPARE_MODE, and GL_TEXTURE_COMPARE_FUNC
            are accepted.
        params: POINTER(c_int)
            Returns the sampler parameters.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object returned from a
            previous call to glGenSamplers.
        GL_INVALID_ENUM is generated if pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetSamplerParameter.xhtml
        """
        pass

    def get_sampler_parameter_iiv(self, sampler: int, pname: int, params: POINTER(c_int)):
        """
        Return sampler parameter values

        Wrapper for glGetSamplerParameterIiv

        Parameters
        ----------
        sampler: int
            Specifies name of the sampler object from which to retrieve parameters.
        pname: int
            Specifies the symbolic name of a sampler parameter. GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
            GL_TEXTURE_WRAP_R, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_COMPARE_MODE, and GL_TEXTURE_COMPARE_FUNC
            are accepted.
        params: POINTER(c_int)
            Returns the sampler parameters.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object returned from a
            previous call to glGenSamplers.
        GL_INVALID_ENUM is generated if pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetSamplerParameter.xhtml
        """
        pass

    def get_sampler_parameter_iuiv(self, sampler: int, pname: int, params: POINTER(c_uint)):
        """
        Return sampler parameter values

        Wrapper for glGetSamplerParameterIuiv

        Parameters
        ----------
        sampler: int
            Specifies name of the sampler object from which to retrieve parameters.
        pname: int
            Specifies the symbolic name of a sampler parameter. GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
            GL_TEXTURE_WRAP_R, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_COMPARE_MODE, and GL_TEXTURE_COMPARE_FUNC
            are accepted.
        params: POINTER(c_uint)
            Returns the sampler parameters.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object returned from a
            previous call to glGenSamplers.
        GL_INVALID_ENUM is generated if pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetSamplerParameter.xhtml
        """
        pass

    def get_synciv(self, sync: c_void_p, pname: int, buf_size: int, length: POINTER(c_uint32), values: POINTER(c_int)):
        """
        Query the properties of a sync object

        Wrapper for glGetSynciv

        Parameters
        ----------
        sync: c_void_p
            Specifies the sync object whose properties to query.
        pname: int
            Specifies the parameter whose value to retrieve from the sync object specified in sync.
        length: POINTER(c_uint32)
            Specifies the address of an variable to receive the number of integers placed in values.
        values: POINTER(c_int)
            Specifies the address of an array to receive the values of the queried parameter.

        Raises
        ------
        GL_INVALID_VALUE is generated if sync is not the name of a sync object.
        GL_INVALID_ENUM is generated if pname is not one of the accepted tokens.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetSync.xhtml
        """
        pass

    def is_sampler(self, id: int) -> bool:
        """
        Determine if a name corresponds to a sampler object

        Wrapper for glIsSampler

        Parameters
        ----------
        id: int
            Specifies a value that may be the name of a sampler object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsSampler.xhtml
        """
        pass

    def is_sync(self, sync: c_void_p) -> bool:
        """
        Determine if a name corresponds to a sync object

        Wrapper for glIsSync

        Parameters
        ----------
        sync: c_void_p
            Specifies a value that may be the name of a sync object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsSync.xhtml
        """
        pass

    def multi_draw_elements_base_vertex(self, mode: int, count: POINTER(c_uint32), type: int, drawcount: int, basevertex: POINTER(c_int)):
        """
        Render multiple sets of primitives by specifying indices of array data elements and an index to apply to each index

        Wrapper for glMultiDrawElementsBaseVertex

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        count: POINTER(c_uint32)
            Points to an array of the elements counts.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        drawcount: int
            Specifies the size of the count, indices and basevertex arrays.
        basevertex: POINTER(c_int)
            Specifies a pointer to the location where the base vertices are stored.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if drawcount is negative.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMultiDrawElementsBaseVertex.xhtml
        """
        pass

    def provoking_vertex(self, provoke_mode: int):
        """
        Specifiy the vertex to be used as the source of data for flat shaded varyings

        Wrapper for glProvokingVertex

        Parameters
        ----------

        Raises
        ------
        GL_INVALID_ENUM is generated if provokeMode is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProvokingVertex.xhtml
        """
        pass

    def query_counter(self, id: int, target: int):
        """
        Record the GL time into a query object after all previous commands have reached the GL server but have not yet necessarily executed.

        Wrapper for glQueryCounter

        Parameters
        ----------
        id: int
            Specify the name of a query object into which to record the GL time.
        target: int
            Specify the counter to query. target must be GL_TIMESTAMP.

        Raises
        ------
        GL_INVALID_OPERATION is generated if id is the name of a query object that is already in use within
            a glBeginQuery / glEndQuery block.
        GL_INVALID_VALUE is generated if id is not the name of a query object returned from a previous call
            to glGenQueries.
        GL_INVALID_ENUM is generated if target is not GL_TIMESTAMP.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glQueryCounter.xhtml
        """
        pass

    def sample_maski(self, mask_number: int, mask: int):
        """
        Set the value of a sub-word of the sample mask

        Wrapper for glSampleMaski

        Parameters
        ----------
        mask: int
            Specifies the new value of the mask sub-word.

        Raises
        ------
        GL_INVALID_VALUE is generated if maskIndex is greater than or equal to the value of
            GL_MAX_SAMPLE_MASK_WORDS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSampleMaski.xhtml
        """
        pass

    def sampler_parameterf(self, sampler: int, pname: int, param: float):
        """
        Set sampler parameters

        Wrapper for glSamplerParameterf

        Parameters
        ----------
        sampler: int
            Specifies the sampler object whose parameter to modify.
        pname: int
            Specifies the symbolic name of a sampler parameter. pname can be one of the following:
            GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MAG_FILTER, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD,
            GL_TEXTURE_LOD_BIAS GL_TEXTURE_COMPARE_MODE, or GL_TEXTURE_COMPARE_FUNC.
        param: float
            For the scalar commands, specifies the value of pname.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object previously returned
            from a call to glGenSamplers.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSamplerParameter.xhtml
        """
        pass

    def sampler_parameteri(self, sampler: int, pname: int, param: int):
        """
        Set sampler parameters

        Wrapper for glSamplerParameteri

        Parameters
        ----------
        sampler: int
            Specifies the sampler object whose parameter to modify.
        pname: int
            Specifies the symbolic name of a sampler parameter. pname can be one of the following:
            GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MAG_FILTER, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD,
            GL_TEXTURE_LOD_BIAS GL_TEXTURE_COMPARE_MODE, or GL_TEXTURE_COMPARE_FUNC.
        param: int
            For the scalar commands, specifies the value of pname.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object previously returned
            from a call to glGenSamplers.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSamplerParameter.xhtml
        """
        pass

    def sampler_parameterfv(self, sampler: int, pname: int, params: POINTER(c_float)):
        """
        Set sampler parameters

        Wrapper for glSamplerParameterfv

        Parameters
        ----------
        sampler: int
            Specifies the sampler object whose parameter to modify.
        pname: int
            Specifies the symbolic name of a sampler parameter. pname can be one of the following:
            GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MAG_FILTER, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD,
            GL_TEXTURE_LOD_BIAS GL_TEXTURE_COMPARE_MODE, or GL_TEXTURE_COMPARE_FUNC.
        params: POINTER(c_float)
            For the vector commands (glSamplerParameter*v), specifies a pointer to an array where the value or
            values of pname are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object previously returned
            from a call to glGenSamplers.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSamplerParameter.xhtml
        """
        pass

    def sampler_parameteriv(self, sampler: int, pname: int, params: POINTER(c_int)):
        """
        Set sampler parameters

        Wrapper for glSamplerParameteriv

        Parameters
        ----------
        sampler: int
            Specifies the sampler object whose parameter to modify.
        pname: int
            Specifies the symbolic name of a sampler parameter. pname can be one of the following:
            GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MAG_FILTER, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD,
            GL_TEXTURE_LOD_BIAS GL_TEXTURE_COMPARE_MODE, or GL_TEXTURE_COMPARE_FUNC.
        params: POINTER(c_int)
            For the vector commands (glSamplerParameter*v), specifies a pointer to an array where the value or
            values of pname are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object previously returned
            from a call to glGenSamplers.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSamplerParameter.xhtml
        """
        pass

    def sampler_parameter_iiv(self, sampler: int, pname: int, params: POINTER(c_int)):
        """
        Set sampler parameters

        Wrapper for glSamplerParameterIiv

        Parameters
        ----------
        sampler: int
            Specifies the sampler object whose parameter to modify.
        pname: int
            Specifies the symbolic name of a sampler parameter. pname can be one of the following:
            GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MAG_FILTER, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD,
            GL_TEXTURE_LOD_BIAS GL_TEXTURE_COMPARE_MODE, or GL_TEXTURE_COMPARE_FUNC.
        params: POINTER(c_int)
            For the vector commands (glSamplerParameter*v), specifies a pointer to an array where the value or
            values of pname are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object previously returned
            from a call to glGenSamplers.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSamplerParameter.xhtml
        """
        pass

    def sampler_parameter_iuiv(self, sampler: int, pname: int, params: POINTER(c_uint)):
        """
        Set sampler parameters

        Wrapper for glSamplerParameterIuiv

        Parameters
        ----------
        sampler: int
            Specifies the sampler object whose parameter to modify.
        pname: int
            Specifies the symbolic name of a sampler parameter. pname can be one of the following:
            GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_MIN_FILTER,
            GL_TEXTURE_MAG_FILTER, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD,
            GL_TEXTURE_LOD_BIAS GL_TEXTURE_COMPARE_MODE, or GL_TEXTURE_COMPARE_FUNC.
        params: POINTER(c_uint)
            For the vector commands (glSamplerParameter*v), specifies a pointer to an array where the value or
            values of pname are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if sampler is not the name of a sampler object previously returned
            from a call to glGenSamplers.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glSamplerParameter.xhtml
        """
        pass

    def wait_sync(self, sync: c_void_p, flags: int, timeout: int):
        """
        Instruct the GL server to block until the specified sync object becomes signaled

        Wrapper for glWaitSync

        Parameters
        ----------
        sync: c_void_p
            Specifies the sync object whose status to wait on.
        flags: int
            A bitfield controlling the command flushing behavior. flags may be zero.
        timeout: int
            Specifies the timeout that the server should wait before continuing. timeout must be
            GL_TIMEOUT_IGNORED.

        Raises
        ------
        GL_INVALID_VALUE is generated if sync is not the name of a sync object.
        GL_INVALID_VALUE is generated if flags is not zero.
        GL_INVALID_VALUE is generated if timeout is not GL_TIMEOUT_IGNORED.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glWaitSync.xhtml
        """
        pass

class GL33(GL32):

    MAJOR = 3
    MINOR = 3

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.vertex_attrib_p1ui, 'glVertexAttribP1ui',
                   None, c_uint, c_uint, c_bool, c_uint)
        self._load(self.vertex_attrib_p2ui, 'glVertexAttribP2ui',
                   None, c_uint, c_uint, c_bool, c_uint)
        self._load(self.vertex_attrib_p3ui, 'glVertexAttribP3ui',
                   None, c_uint, c_uint, c_bool, c_uint)
        self._load(self.vertex_attrib_p4ui, 'glVertexAttribP4ui',
                   None, c_uint, c_uint, c_bool, c_uint)
        self._load(self.vertex_attrib_divisor, 'glVertexAttribDivisor',
                   None, c_uint, c_uint)

    def vertex_attrib_p1ui(self, index: int, type: int, normalized: bool, value: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribP1ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        type: int
            For the packed commands (glVertexAttribP*), specified the type of packing used on the data. This
            parameter must be GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, to specify signed or
            unsigned data, respectively, or GL_UNSIGNED_INT_10F_11F_11F_REV to specify floating point data.
        normalized: bool
            For the packed commands, if GL_TRUE, then the values are to be converted to floating point values
            by normalizing. Otherwise, they are converted directly to floating-point values. If type indicates
            a floating-pont format, then normalized value must be GL_FALSE.
        value: int
            For the packed commands, specifies the new packed value to be used for the specified vertex
            attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_p2ui(self, index: int, type: int, normalized: bool, value: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribP2ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        type: int
            For the packed commands (glVertexAttribP*), specified the type of packing used on the data. This
            parameter must be GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, to specify signed or
            unsigned data, respectively, or GL_UNSIGNED_INT_10F_11F_11F_REV to specify floating point data.
        normalized: bool
            For the packed commands, if GL_TRUE, then the values are to be converted to floating point values
            by normalizing. Otherwise, they are converted directly to floating-point values. If type indicates
            a floating-pont format, then normalized value must be GL_FALSE.
        value: int
            For the packed commands, specifies the new packed value to be used for the specified vertex
            attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_p3ui(self, index: int, type: int, normalized: bool, value: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribP3ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        type: int
            For the packed commands (glVertexAttribP*), specified the type of packing used on the data. This
            parameter must be GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, to specify signed or
            unsigned data, respectively, or GL_UNSIGNED_INT_10F_11F_11F_REV to specify floating point data.
        normalized: bool
            For the packed commands, if GL_TRUE, then the values are to be converted to floating point values
            by normalizing. Otherwise, they are converted directly to floating-point values. If type indicates
            a floating-pont format, then normalized value must be GL_FALSE.
        value: int
            For the packed commands, specifies the new packed value to be used for the specified vertex
            attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_p4ui(self, index: int, type: int, normalized: bool, value: int):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribP4ui

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        type: int
            For the packed commands (glVertexAttribP*), specified the type of packing used on the data. This
            parameter must be GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, to specify signed or
            unsigned data, respectively, or GL_UNSIGNED_INT_10F_11F_11F_REV to specify floating point data.
        normalized: bool
            For the packed commands, if GL_TRUE, then the values are to be converted to floating point values
            by normalizing. Otherwise, they are converted directly to floating-point values. If type indicates
            a floating-pont format, then normalized value must be GL_FALSE.
        value: int
            For the packed commands, specifies the new packed value to be used for the specified vertex
            attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_divisor(self, index: int, divisor: int):
        """
        Modify the rate at which generic vertex attributes advance during instanced rendering

        Wrapper for glVertexAttribDivisor

        Parameters
        ----------
        index: int
            Specify the index of the generic vertex attribute.
        divisor: int
            Specify the number of instances that will pass between updates of the generic attribute at slot
            index.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribDivisor.xhtml
        """
        pass

class GL40(GL33):

    MAJOR = 4
    MINOR = 0

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.begin_query_indexed, 'glBeginQueryIndexed',
                   None, c_uint, c_uint, c_uint)
        self._load(self.end_query_indexed, 'glEndQueryIndexed',
                   None, c_uint, c_uint)
        self._load(self.bind_transform_feedback, 'glBindTransformFeedback',
                   None, c_uint, c_uint)
        self._load(self.blend_equationi, 'glBlendEquationi',
                   None, c_uint, c_uint)
        self._load(self.blend_equation_separatei, 'glBlendEquationSeparatei',
                   None, c_uint, c_uint, c_uint)
        self._load(self.blend_funci, 'glBlendFunci',
                   None, c_uint, c_uint, c_uint)
        self._load(self.blend_func_separatei, 'glBlendFuncSeparatei',
                   None, c_uint, c_uint, c_uint, c_uint, c_uint)
        self._load(self.delete_transform_feedbacks, 'glDeleteTransformFeedbacks',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.draw_arrays_indirect, 'glDrawArraysIndirect',
                   None, c_uint, c_void_p)
        self._load(self.draw_elements_indirect, 'glDrawElementsIndirect',
                   None, c_uint, c_uint, c_void_p)
        self._load(self.draw_transform_feedback, 'glDrawTransformFeedback',
                   None, c_uint, c_uint)
        self._load(self.draw_transform_feedback_stream, 'glDrawTransformFeedbackStream',
                   None, c_uint, c_uint, c_uint)
        self._load(self.gen_transform_feedbacks, 'glGenTransformFeedbacks',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.get_active_subroutine_name, 'glGetActiveSubroutineName',
                   None, c_uint, c_uint, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_active_subroutine_uniformiv, 'glGetActiveSubroutineUniformiv',
                   None, c_uint, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_active_subroutine_uniform_name, 'glGetActiveSubroutineUniformName',
                   None, c_uint, c_uint, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_program_stageiv, 'glGetProgramStageiv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_query_indexediv, 'glGetQueryIndexediv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_subroutine_index, 'glGetSubroutineIndex',
                   c_uint, c_uint, c_uint, c_char_p)
        self._load(self.get_subroutine_uniform_location, 'glGetSubroutineUniformLocation',
                   c_int, c_uint, c_uint, c_char_p)
        self._load(self.get_uniformdv, 'glGetUniformdv',
                   None, c_uint, c_int, POINTER(c_double))
        self._load(self.get_uniform_subroutineuiv, 'glGetUniformSubroutineuiv',
                   None, c_uint, c_int, POINTER(c_uint))
        self._load(self.is_transform_feedback, 'glIsTransformFeedback',
                   c_bool, c_uint)
        self._load(self.min_sample_shading, 'glMinSampleShading',
                   None, c_float)
        self._load(self.patch_parameteri, 'glPatchParameteri',
                   None, c_uint, c_int)
        self._load(self.patch_parameterfv, 'glPatchParameterfv',
                   None, c_uint, POINTER(c_float))
        self._load(self.pause_transform_feedback, 'glPauseTransformFeedback',
                   None, )
        self._load(self.resume_transform_feedback, 'glResumeTransformFeedback',
                   None, )
        self._load(self.uniform_subroutinesuiv, 'glUniformSubroutinesuiv',
                   None, c_uint, c_uint32, POINTER(c_uint))

    def begin_query_indexed(self, target: int, index: int, id: int):
        """
        Delimit the boundaries of a query object on an indexed target

        Wrapper for glBeginQueryIndexed

        Parameters
        ----------
        target: int
            Specifies the target type of query object to be concluded. The symbolic constant must be one of
            GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED, GL_PRIMITIVES_GENERATED,
            GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN, or GL_TIME_ELAPSED.
        index: int
            Specifies the index of the query target upon which to end the query.
        id: int
            Specifies the name of a query object.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of the accepted tokens.
        GL_INVALID_VALUE is generated if index is greater than the query target-specific maximum.
        GL_INVALID_OPERATION is generated if glBeginQueryIndexed is executed while a query object of the
            same target is already active.
        GL_INVALID_OPERATION is generated if glEndQueryIndexed is executed when a query object of the same
            target is not active.
        GL_INVALID_OPERATION is generated if id is 0.
        GL_INVALID_OPERATION is generated if id is the name of an already active query object.
        GL_INVALID_OPERATION is generated if id refers to an existing query object whose type does not does
            not match target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginQueryIndexed.xhtml
        """
        pass

    def end_query_indexed(self, target: int, index: int):
        """
        Delimit the boundaries of a query object on an indexed target

        Wrapper for glEndQueryIndexed

        Parameters
        ----------
        target: int
            Specifies the target type of query object to be concluded. The symbolic constant must be one of
            GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED, GL_PRIMITIVES_GENERATED,
            GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN, or GL_TIME_ELAPSED.
        index: int
            Specifies the index of the query target upon which to end the query.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of the accepted tokens.
        GL_INVALID_VALUE is generated if index is greater than the query target-specific maximum.
        GL_INVALID_OPERATION is generated if glBeginQueryIndexed is executed while a query object of the
            same target is already active.
        GL_INVALID_OPERATION is generated if glEndQueryIndexed is executed when a query object of the same
            target is not active.
        GL_INVALID_OPERATION is generated if id is 0.
        GL_INVALID_OPERATION is generated if id is the name of an already active query object.
        GL_INVALID_OPERATION is generated if id refers to an existing query object whose type does not does
            not match target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBeginQueryIndexed.xhtml
        """
        pass

    def bind_transform_feedback(self, target: int, id: int):
        """
        Bind a transform feedback object

        Wrapper for glBindTransformFeedback

        Parameters
        ----------
        target: int
            Specifies the target to which to bind the transform feedback object id. target must be
            GL_TRANSFORM_FEEDBACK.
        id: int
            Specifies the name of a transform feedback object reserved by glGenTransformFeedbacks.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_TRANSFORM_FEEDBACK.
        GL_INVALID_OPERATION is generated if the transform feedback operation is active on the currently
            bound transform feedback object, and that operation is not paused.
        GL_INVALID_OPERATION is generated if id is not zero or the name of a transform feedback object
            returned from a previous call to glGenTransformFeedbacks, or if such a name has been deleted by
            glDeleteTransformFeedbacks.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindTransformFeedback.xhtml
        """
        pass

    def blend_equationi(self, buf: int, mode: int):
        """
        Specify the equation used for both the RGB blend equation and the Alpha blend equation

        Wrapper for glBlendEquationi

        Parameters
        ----------
        buf: int
            for glBlendEquationi, specifies the index of the draw buffer for which to set the blend equation.
        mode: int
            specifies how source and destination colors are combined. It must be GL_FUNC_ADD, GL_FUNC_SUBTRACT,
            GL_FUNC_REVERSE_SUBTRACT, GL_MIN, GL_MAX.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of GL_FUNC_ADD, GL_FUNC_SUBTRACT,
            GL_FUNC_REVERSE_SUBTRACT, GL_MAX, or GL_MIN.
        GL_INVALID_VALUE is generated by glBlendEquationi if buf is greater than or equal to the value of
            GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendEquation.xhtml
        """
        pass

    def blend_equation_separatei(self, buf: int, mode_rgb: int, mode_alpha: int):
        """
        Set the RGB blend equation and the alpha blend equation separately

        Wrapper for glBlendEquationSeparatei

        Parameters
        ----------
        buf: int
            for glBlendEquationSeparatei, specifies the index of the draw buffer for which to set the blend
            equations.

        Raises
        ------
        GL_INVALID_ENUM is generated if either modeRGB or modeAlpha is not one of GL_FUNC_ADD,
            GL_FUNC_SUBTRACT, GL_FUNC_REVERSE_SUBTRACT, GL_MAX, or GL_MIN.
        GL_INVALID_VALUE is generated by glBlendEquationSeparatei if buf is greater than or equal to the
            value of GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendEquationSeparate.xhtml
        """
        pass

    def blend_funci(self, buf: int, sfactor: int, dfactor: int):
        """
        Specify pixel arithmetic

        Wrapper for glBlendFunci

        Parameters
        ----------
        buf: int
            For glBlendFunci, specifies the index of the draw buffer for which to set the blend function.
        sfactor: int
            Specifies how the red, green, blue, and alpha source blending factors are computed. The initial
            value is GL_ONE.
        dfactor: int
            Specifies how the red, green, blue, and alpha destination blending factors are computed. The
            following symbolic constants are accepted: GL_ZERO, GL_ONE, GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR,
            GL_DST_COLOR, GL_ONE_MINUS_DST_COLOR, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_DST_ALPHA,
            GL_ONE_MINUS_DST_ALPHA. GL_CONSTANT_COLOR, GL_ONE_MINUS_CONSTANT_COLOR, GL_CONSTANT_ALPHA, and
            GL_ONE_MINUS_CONSTANT_ALPHA. The initial value is GL_ZERO.

        Raises
        ------
        GL_INVALID_ENUM is generated if either sfactor or dfactor is not an accepted value.
        GL_INVALID_VALUE is generated by glBlendFunci if buf is greater than or equal to the value of
            GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFunc.xhtml
        """
        pass

    def blend_func_separatei(self, buf: int, src_rgb: int, dst_rgb: int, src_alpha: int, dst_alpha: int):
        """
        Specify pixel arithmetic for RGB and alpha components separately

        Wrapper for glBlendFuncSeparatei

        Parameters
        ----------
        buf: int
            For glBlendFuncSeparatei, specifies the index of the draw buffer for which to set the blend
            functions.

        Raises
        ------
        GL_INVALID_ENUM is generated if either srcRGB or dstRGB is not an accepted value.
        GL_INVALID_VALUE is generated by glBlendFuncSeparatei if buf is greater than or equal to the value
            of GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFuncSeparate.xhtml
        """
        pass

    def delete_transform_feedbacks(self, n: int, ids: POINTER(c_uint)):
        """
        Delete transform feedback objects

        Wrapper for glDeleteTransformFeedbacks

        Parameters
        ----------
        n: int
            Specifies the number of transform feedback objects to delete.
        ids: POINTER(c_uint)
            Specifies an array of names of transform feedback objects to delete.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteTransformFeedbacks.xhtml
        """
        pass

    def draw_arrays_indirect(self, mode: int, indirect: c_void_p):
        """
        Render primitives from array data, taking parameters from memory

        Wrapper for glDrawArraysIndirect

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        indirect: c_void_p
            Specifies the address of a structure containing the draw parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            to the GL_DRAW_INDIRECT_BUFFER binding and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawArraysIndirect.xhtml
        """
        pass

    def draw_elements_indirect(self, mode: int, type: int, indirect: c_void_p):
        """
        Render indexed primitives from array data, taking parameters from memory

        Wrapper for glDrawElementsIndirect

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        type: int
            Specifies the type of data in the buffer bound to the GL_ELEMENT_ARRAY_BUFFER binding.
        indirect: c_void_p
            Specifies the address of a structure containing the draw parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_OPERATION is generated if no buffer is bound to the GL_ELEMENT_ARRAY_BUFFER binding, or
            if such a buffer's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            to the GL_DRAW_INDIRECT_BUFFER binding and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawElementsIndirect.xhtml
        """
        pass

    def draw_transform_feedback(self, mode: int, id: int):
        """
        Render primitives using a count derived from a transform feedback object

        Wrapper for glDrawTransformFeedback

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        id: int
            Specifies the name of a transform feedback object from which to retrieve a primitive count.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if id is not the name of a transform feedback object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.
        GL_INVALID_OPERATION is generated if glEndTransformFeedback has never been called while the
            transform feedback object named by id was bound.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawTransformFeedback.xhtml
        """
        pass

    def draw_transform_feedback_stream(self, mode: int, id: int, stream: int):
        """
        Render primitives using a count derived from a specifed stream of a transform feedback object

        Wrapper for glDrawTransformFeedbackStream

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        id: int
            Specifies the name of a transform feedback object from which to retrieve a primitive count.
        stream: int
            Specifies the index of the transform feedback stream from which to retrieve a primitive count.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if id is not the name of a transform feedback object.
        GL_INVALID_VALUE is generated if stream is greater than or equal to the value of
            GL_MAX_VERTEX_STREAMS.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.
        GL_INVALID_OPERATION is generated if glEndTransformFeedback has never been called while the
            transform feedback object named by id was bound.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawTransformFeedbackStream.xhtml
        """
        pass

    def gen_transform_feedbacks(self, n: int, ids: POINTER(c_uint)):
        """
        Reserve transform feedback object names

        Wrapper for glGenTransformFeedbacks

        Parameters
        ----------
        n: int
            Specifies the number of transform feedback object names to reserve.
        ids: POINTER(c_uint)
            Specifies an array of into which the reserved names will be written.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenTransformFeedbacks.xhtml
        """
        pass

    def get_active_subroutine_name(self, program: int, shadertype: int, index: int, bufsize: int, length: POINTER(c_uint32), name: bytes):
        """
        Query the name of an active shader subroutine

        Wrapper for glGetActiveSubroutineName

        Parameters
        ----------
        program: int
            Specifies the name of the program containing the subroutine.
        shadertype: int
            Specifies the shader stage from which to query the subroutine name.
        index: int
            Specifies the index of the shader subroutine uniform.
        bufsize: int
            Specifies the size of the buffer whose address is given in name.
        length: POINTER(c_uint32)
            Specifies the address of a variable which is to receive the length of the shader subroutine uniform
            name.
        name: bytes
            Specifies the address of an array into which the name of the shader subroutine uniform will be
            written.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of
            GL_ACTIVE_SUBROUTINES.
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveSubroutineName.xhtml
        """
        pass

    def get_active_subroutine_uniformiv(self, program: int, shadertype: int, index: int, pname: int, values: POINTER(c_int)):
        """
        Query a property of an active shader subroutine uniform

        Wrapper for glGetActiveSubroutineUniformiv

        Parameters
        ----------
        program: int
            Specifies the name of the program containing the subroutine.
        shadertype: int
            Specifies the shader stage from which to query for the subroutine parameter. shadertype must be one
            of GL_VERTEX_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_GEOMETRY_SHADER or
            GL_FRAGMENT_SHADER.
        index: int
            Specifies the index of the shader subroutine uniform.
        pname: int
            Specifies the parameter of the shader subroutine uniform to query. pname must be
            GL_NUM_COMPATIBLE_SUBROUTINES, GL_COMPATIBLE_SUBROUTINES, GL_UNIFORM_SIZE or
            GL_UNIFORM_NAME_LENGTH.
        values: POINTER(c_int)
            Specifies the address of a into which the queried value or values will be placed.

        Raises
        ------
        GL_INVALID_ENUM is generated if shadertype or pname is not one of the accepted values.
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of
            GL_ACTIVE_SUBROUTINES.
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveSubroutineUniform.xhtml
        """
        pass

    def get_active_subroutine_uniform_name(self, program: int, shadertype: int, index: int, bufsize: int, length: POINTER(c_uint32), name: bytes):
        """
        Query the name of an active shader subroutine uniform

        Wrapper for glGetActiveSubroutineUniformName

        Parameters
        ----------
        program: int
            Specifies the name of the program containing the subroutine.
        shadertype: int
            Specifies the shader stage from which to query for the subroutine parameter. shadertype must be one
            of GL_VERTEX_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_GEOMETRY_SHADER or
            GL_FRAGMENT_SHADER.
        index: int
            Specifies the index of the shader subroutine uniform.
        bufsize: int
            Specifies the size of the buffer whose address is given in name.
        length: POINTER(c_uint32)
            Specifies the address of a variable into which is written the number of characters copied into
            name.
        name: bytes
            Specifies the address of a buffer that will receive the name of the specified shader subroutine
            uniform.

        Raises
        ------
        GL_INVALID_ENUM is generated if shadertype or pname is not one of the accepted values.
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of
            GL_ACTIVE_SUBROUTINE_UNIFORMS.
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveSubroutineUniformName.xhtml
        """
        pass

    def get_program_stageiv(self, program: int, shadertype: int, pname: int, values: POINTER(c_int)):
        """
        Retrieve properties of a program object corresponding to a specified shader stage

        Wrapper for glGetProgramStageiv

        Parameters
        ----------
        program: int
            Specifies the name of the program containing shader stage.
        shadertype: int
            Specifies the shader stage from which to query for the subroutine parameter. shadertype must be one
            of GL_VERTEX_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_GEOMETRY_SHADER or
            GL_FRAGMENT_SHADER.
        pname: int
            Specifies the parameter of the shader to query. pname must be GL_ACTIVE_SUBROUTINE_UNIFORMS,
            GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS, GL_ACTIVE_SUBROUTINES,
            GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH, or GL_ACTIVE_SUBROUTINE_MAX_LENGTH.
        values: POINTER(c_int)
            Specifies the address of a variable into which the queried value or values will be placed.

        Raises
        ------
        GL_INVALID_ENUM is generated if shadertype or pname is not one of the accepted values.
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramStage.xhtml
        """
        pass

    def get_query_indexediv(self, target: int, index: int, pname: int, params: POINTER(c_int)):
        """
        Return parameters of an indexed query object target

        Wrapper for glGetQueryIndexediv

        Parameters
        ----------
        target: int
            Specifies a query object target. Must be GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED,
            GL_ANY_SAMPLES_PASSED_CONSERVATIVE GL_PRIMITIVES_GENERATED,
            GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN, GL_TIME_ELAPSED, or GL_TIMESTAMP.
        index: int
            Specifies the index of the query object target.
        pname: int
            Specifies the symbolic name of a query object target parameter. Accepted values are
            GL_CURRENT_QUERY or GL_QUERY_COUNTER_BITS.
        params: POINTER(c_int)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_ENUM is generated if target or pname is not an accepted value.
        GL_INVALID_VALUE is generated if index is greater than or equal to the target -specific maximum.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetQueryIndexed.xhtml
        """
        pass

    def get_subroutine_index(self, program: int, shadertype: int, name: bytes) -> int:
        """
        Retrieve the index of a subroutine uniform of a given shader stage within a program

        Wrapper for glGetSubroutineIndex

        Parameters
        ----------
        program: int
            Specifies the name of the program containing shader stage.
        shadertype: int
            Specifies the shader stage from which to query for subroutine uniform index. shadertype must be one
            of GL_VERTEX_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_GEOMETRY_SHADER or
            GL_FRAGMENT_SHADER.
        name: bytes
            Specifies the name of the subroutine uniform whose index to query.

        Raises
        ------
        GL_INVALID_ENUM is generated if shadertype or pname is not one of the accepted values.
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetSubroutineIndex.xhtml
        """
        pass

    def get_subroutine_uniform_location(self, program: int, shadertype: int, name: bytes) -> int:
        """
        Retrieve the location of a subroutine uniform of a given shader stage within a program

        Wrapper for glGetSubroutineUniformLocation

        Parameters
        ----------
        program: int
            Specifies the name of the program containing shader stage.
        shadertype: int
            Specifies the shader stage from which to query for subroutine uniform index. shadertype must be one
            of GL_VERTEX_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_GEOMETRY_SHADER or
            GL_FRAGMENT_SHADER.
        name: bytes
            Specifies the name of the subroutine uniform whose index to query.

        Raises
        ------
        GL_INVALID_ENUM is generated if shadertype or pname is not one of the accepted values.
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetSubroutineUniformLocation.xhtml
        """
        pass

    def get_uniformdv(self, program: int, location: int, params: POINTER(c_double)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetUniformdv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_double)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def get_uniform_subroutineuiv(self, shadertype: int, location: int, values: POINTER(c_uint)):
        """
        Retrieve the value of a subroutine uniform of a given shader stage of the current program

        Wrapper for glGetUniformSubroutineuiv

        Parameters
        ----------
        shadertype: int
            Specifies the shader stage from which to query for subroutine uniform index. shadertype must be one
            of GL_VERTEX_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_GEOMETRY_SHADER or
            GL_FRAGMENT_SHADER.
        location: int
            Specifies the location of the subroutine uniform.
        values: POINTER(c_uint)
            Specifies the address of a variable to receive the value or values of the subroutine uniform.

        Raises
        ------
        GL_INVALID_ENUM is generated if shadertype is not one of the accepted values.
        GL_INVALID_VALUE is generated if location is greater than or equal to the value of
            GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS for the shader currently in use at shader stage shadertype.
        GL_INVALID_OPERATION is generated if no program is active.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniformSubroutine.xhtml
        """
        pass

    def is_transform_feedback(self, id: int) -> bool:
        """
        Determine if a name corresponds to a transform feedback object

        Wrapper for glIsTransformFeedback

        Parameters
        ----------
        id: int
            Specifies a value that may be the name of a transform feedback object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsTransformFeedback.xhtml
        """
        pass

    def min_sample_shading(self, value: float):
        """
        Specifies minimum rate at which sample shaing takes place

        Wrapper for glMinSampleShading

        Parameters
        ----------
        value: float
            Specifies the rate at which samples are shaded within each covered pixel.

        Raises
        ------
        None.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMinSampleShading.xhtml
        """
        pass

    def patch_parameteri(self, pname: int, value: int):
        """
        Specifies the parameters for patch primitives

        Wrapper for glPatchParameteri

        Parameters
        ----------
        pname: int
            Specifies the name of the parameter to set. The symbolc constants GL_PATCH_VERTICES,
            GL_PATCH_DEFAULT_OUTER_LEVEL, and GL_PATCH_DEFAULT_INNER_LEVEL are accepted.
        value: int
            Specifies the new value for the parameter given by pname.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated if pname is GL_PATCH_VERTICES and value is less than or equal to
            zero, or greater than the value of GL_MAX_PATCH_VERTICES.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPatchParameter.xhtml
        """
        pass

    def patch_parameterfv(self, pname: int, values: POINTER(c_float)):
        """
        Specifies the parameters for patch primitives

        Wrapper for glPatchParameterfv

        Parameters
        ----------
        pname: int
            Specifies the name of the parameter to set. The symbolc constants GL_PATCH_VERTICES,
            GL_PATCH_DEFAULT_OUTER_LEVEL, and GL_PATCH_DEFAULT_INNER_LEVEL are accepted.
        values: POINTER(c_float)
            Specifies the address of an array containing the new values for the parameter given by pname.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated if pname is GL_PATCH_VERTICES and value is less than or equal to
            zero, or greater than the value of GL_MAX_PATCH_VERTICES.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPatchParameter.xhtml
        """
        pass

    def pause_transform_feedback(self):
        """
        Pause transform feedback operations

        Wrapper for glPauseTransformFeedback

        Raises
        ------
        GL_INVALID_OPERATION is generated if the currently bound transform feedback object is not active or
            is paused.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPauseTransformFeedback.xhtml
        """
        pass

    def resume_transform_feedback(self):
        """
        Resume transform feedback operations

        Wrapper for glResumeTransformFeedback

        Raises
        ------
        GL_INVALID_OPERATION is generated if the currently bound transform feedback object is not active or
            is not paused.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glResumeTransformFeedback.xhtml
        """
        pass

    def uniform_subroutinesuiv(self, shadertype: int, count: int, indices: POINTER(c_uint)):
        """
        Load active subroutine uniforms

        Wrapper for glUniformSubroutinesuiv

        Parameters
        ----------
        shadertype: int
            Specifies the shader stage from which to query for subroutine uniform index. shadertype must be one
            of GL_VERTEX_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_GEOMETRY_SHADER or
            GL_FRAGMENT_SHADER.
        count: int
            Specifies the number of uniform indices stored in indices.
        indices: POINTER(c_uint)
            Specifies the address of an array holding the indices to load into the shader subroutine variables.

        Raises
        ------
        GL_INVALID_OPERATION is generated if no program object is current.
        GL_INVALID_VALUE is generated if count is not equal to the value of
            GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS for the shader stage shadertype of the current program.
        GL_INVALID_VALUE is generated if any value in indices is geater than or equal to the value of
            GL_ACTIVE_SUBROUTINES for the shader stage shadertype of the current program.
        GL_INVALID_ENUM is generated if shadertype is not one of the accepted values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUniformSubroutines.xhtml
        """
        pass

class GL41(GL40):

    MAJOR = 4
    MINOR = 1

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.active_shader_program, 'glActiveShaderProgram',
                   None, c_uint, c_uint)
        self._load(self.bind_program_pipeline, 'glBindProgramPipeline',
                   None, c_uint)
        self._load(self.clear_depthf, 'glClearDepthf',
                   None, c_float)
        self._load(self.create_shader_programv, 'glCreateShaderProgramv',
                   c_uint, c_uint, c_uint32, POINTER(c_char_p))
        self._load(self.delete_program_pipelines, 'glDeleteProgramPipelines',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.depth_rangef, 'glDepthRangef',
                   None, c_float, c_float)
        self._load(self.depth_range_arrayv, 'glDepthRangeArrayv',
                   None, c_uint, c_uint32, POINTER(c_double))
        self._load(self.depth_range_indexed, 'glDepthRangeIndexed',
                   None, c_uint, c_double, c_double)
        self._load(self.gen_program_pipelines, 'glGenProgramPipelines',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.get_floati_v, 'glGetFloati_v',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.get_doublei_v, 'glGetDoublei_v',
                   None, c_uint, c_uint, POINTER(c_double))
        self._load(self.get_program_binary, 'glGetProgramBinary',
                   None, c_uint, c_uint32, POINTER(c_uint32), POINTER(c_uint32), c_void_p)
        self._load(self.get_program_pipelineiv, 'glGetProgramPipelineiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_program_pipeline_info_log, 'glGetProgramPipelineInfoLog',
                   None, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_shader_precision_format, 'glGetShaderPrecisionFormat',
                   None, c_uint, c_uint, POINTER(c_int), POINTER(c_int))
        self._load(self.get_vertex_attrib_ldv, 'glGetVertexAttribLdv',
                   None, c_uint, c_uint, POINTER(c_double))
        self._load(self.is_program_pipeline, 'glIsProgramPipeline',
                   c_bool, c_uint)
        self._load(self.program_binary, 'glProgramBinary',
                   None, c_uint, c_uint, c_void_p, c_uint32)
        self._load(self.program_parameteri, 'glProgramParameteri',
                   None, c_uint, c_uint, c_int)
        self._load(self.program_uniform1f, 'glProgramUniform1f',
                   None, c_uint, c_int, c_float)
        self._load(self.program_uniform2f, 'glProgramUniform2f',
                   None, c_uint, c_int, c_float, c_float)
        self._load(self.program_uniform3f, 'glProgramUniform3f',
                   None, c_uint, c_int, c_float, c_float, c_float)
        self._load(self.program_uniform4f, 'glProgramUniform4f',
                   None, c_uint, c_int, c_float, c_float, c_float, c_float)
        self._load(self.program_uniform1i, 'glProgramUniform1i',
                   None, c_uint, c_int, c_int)
        self._load(self.program_uniform2i, 'glProgramUniform2i',
                   None, c_uint, c_int, c_int, c_int)
        self._load(self.program_uniform3i, 'glProgramUniform3i',
                   None, c_uint, c_int, c_int, c_int, c_int)
        self._load(self.program_uniform4i, 'glProgramUniform4i',
                   None, c_uint, c_int, c_int, c_int, c_int, c_int)
        self._load(self.program_uniform1ui, 'glProgramUniform1ui',
                   None, c_uint, c_int, c_uint)
        self._load(self.program_uniform2ui, 'glProgramUniform2ui',
                   None, c_uint, c_int, c_int, c_uint)
        self._load(self.program_uniform3ui, 'glProgramUniform3ui',
                   None, c_uint, c_int, c_int, c_int, c_uint)
        self._load(self.program_uniform4ui, 'glProgramUniform4ui',
                   None, c_uint, c_int, c_int, c_int, c_int, c_uint)
        self._load(self.program_uniform1fv, 'glProgramUniform1fv',
                   None, c_uint, c_int, c_uint32, POINTER(c_float))
        self._load(self.program_uniform2fv, 'glProgramUniform2fv',
                   None, c_uint, c_int, c_uint32, POINTER(c_float))
        self._load(self.program_uniform3fv, 'glProgramUniform3fv',
                   None, c_uint, c_int, c_uint32, POINTER(c_float))
        self._load(self.program_uniform4fv, 'glProgramUniform4fv',
                   None, c_uint, c_int, c_uint32, POINTER(c_float))
        self._load(self.program_uniform1iv, 'glProgramUniform1iv',
                   None, c_uint, c_int, c_uint32, POINTER(c_int))
        self._load(self.program_uniform2iv, 'glProgramUniform2iv',
                   None, c_uint, c_int, c_uint32, POINTER(c_int))
        self._load(self.program_uniform3iv, 'glProgramUniform3iv',
                   None, c_uint, c_int, c_uint32, POINTER(c_int))
        self._load(self.program_uniform4iv, 'glProgramUniform4iv',
                   None, c_uint, c_int, c_uint32, POINTER(c_int))
        self._load(self.program_uniform1uiv, 'glProgramUniform1uiv',
                   None, c_uint, c_int, c_uint32, POINTER(c_uint))
        self._load(self.program_uniform2uiv, 'glProgramUniform2uiv',
                   None, c_uint, c_int, c_uint32, POINTER(c_uint))
        self._load(self.program_uniform3uiv, 'glProgramUniform3uiv',
                   None, c_uint, c_int, c_uint32, POINTER(c_uint))
        self._load(self.program_uniform4uiv, 'glProgramUniform4uiv',
                   None, c_uint, c_int, c_uint32, POINTER(c_uint))
        self._load(self.program_uniform_matrix2fv, 'glProgramUniformMatrix2fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix3fv, 'glProgramUniformMatrix3fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix4fv, 'glProgramUniformMatrix4fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix2x3fv, 'glProgramUniformMatrix2x3fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix3x2fv, 'glProgramUniformMatrix3x2fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix2x4fv, 'glProgramUniformMatrix2x4fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix4x2fv, 'glProgramUniformMatrix4x2fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix3x4fv, 'glProgramUniformMatrix3x4fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.program_uniform_matrix4x3fv, 'glProgramUniformMatrix4x3fv',
                   None, c_uint, c_int, c_uint32, c_bool, POINTER(c_float))
        self._load(self.release_shader_compiler, 'glReleaseShaderCompiler',
                   None, )
        self._load(self.scissor_arrayv, 'glScissorArrayv',
                   None, c_uint, c_uint32, POINTER(c_int))
        self._load(self.scissor_indexed, 'glScissorIndexed',
                   None, c_uint, c_int, c_int, c_uint32, c_uint32)
        self._load(self.scissor_indexedv, 'glScissorIndexedv',
                   None, c_uint, POINTER(c_int))
        self._load(self.shader_binary, 'glShaderBinary',
                   None, c_uint32, POINTER(c_uint), c_uint, c_void_p, c_uint32)
        self._load(self.use_program_stages, 'glUseProgramStages',
                   None, c_uint, c_uint32, c_uint)
        self._load(self.validate_program_pipeline, 'glValidateProgramPipeline',
                   None, c_uint)
        self._load(self.vertex_attrib_l1d, 'glVertexAttribL1d',
                   None, c_uint, c_double)
        self._load(self.vertex_attrib_l2d, 'glVertexAttribL2d',
                   None, c_uint, c_double, c_double)
        self._load(self.vertex_attrib_l3d, 'glVertexAttribL3d',
                   None, c_uint, c_double, c_double, c_double)
        self._load(self.vertex_attrib_l4d, 'glVertexAttribL4d',
                   None, c_uint, c_double, c_double, c_double, c_double)
        self._load(self.vertex_attrib_l1dv, 'glVertexAttribL1dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib_l2dv, 'glVertexAttribL2dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib_l3dv, 'glVertexAttribL3dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib_l4dv, 'glVertexAttribL4dv',
                   None, c_uint, POINTER(c_double))
        self._load(self.vertex_attrib_lpointer, 'glVertexAttribLPointer',
                   None, c_uint, c_int, c_uint, c_uint32, c_void_p)
        self._load(self.viewport_arrayv, 'glViewportArrayv',
                   None, c_uint, c_uint32, POINTER(c_float))
        self._load(self.viewport_indexedf, 'glViewportIndexedf',
                   None, c_uint, c_float, c_float, c_float, c_float)
        self._load(self.viewport_indexedfv, 'glViewportIndexedfv',
                   None, c_uint, POINTER(c_float))

    def active_shader_program(self, pipeline: int, program: int):
        """
        Set the active program object for a program pipeline object

        Wrapper for glActiveShaderProgram

        Parameters
        ----------
        pipeline: int
            Specifies the program pipeline object to set the active program object for.
        program: int
            Specifies the program object to set as the active program pipeline object pipeline.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pipeline is not a name previously returned from a call to
            glGenProgramPipelines or if such a name has been deleted by a call to glDeleteProgramPipelines.
        GL_INVALID_OPERATION is generated if program refers to a program object that has not been
            successfully linked.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glActiveShaderProgram.xhtml
        """
        pass

    def bind_program_pipeline(self, pipeline: int):
        """
        Bind a program pipeline to the current context

        Wrapper for glBindProgramPipeline

        Parameters
        ----------
        pipeline: int
            Specifies the name of the pipeline object to bind to the context.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pipeline is not zero or a name previously returned from a call
            to glGenProgramPipelines or if such a name has been deleted by a call to glDeleteProgramPipelines.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindProgramPipeline.xhtml
        """
        pass

    def clear_depthf(self, depth: float):
        """
        Specify the clear value for the depth buffer

        Wrapper for glClearDepthf

        Parameters
        ----------
        depth: float
            Specifies the depth value used when the depth buffer is cleared. The initial value is 1.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearDepth.xhtml
        """
        pass

    def create_shader_programv(self, type: int, count: int, strings: POINTER(c_char_p)) -> int:
        """
        Create a stand-alone program from an array of null-terminated source code strings

        Wrapper for glCreateShaderProgramv

        Parameters
        ----------
        type: int
            Specifies the type of shader to create.
        count: int
            Specifies the number of source code strings in the array strings.
        strings: POINTER(c_char_p)
            Specifies the address of an array of pointers to source code strings from which to create the
            program object.

        Raises
        ------
        GL_INVALID_ENUM is generated if type is not an accepted shader type.
        GL_INVALID_VALUE is generated if count is negative.
        Other errors are generated if the supplied shader code fails to compile and link, as described for
            the commands in the pseudocode sequence above, but all such errors are generated without any side
            effects of executing those commands.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateShaderProgram.xhtml
        """
        pass

    def delete_program_pipelines(self, n: int, pipelines: POINTER(c_uint)):
        """
        Delete program pipeline objects

        Wrapper for glDeleteProgramPipelines

        Parameters
        ----------
        n: int
            Specifies the number of program pipeline objects to delete.
        pipelines: POINTER(c_uint)
            Specifies an array of names of program pipeline objects to delete.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteProgramPipelines.xhtml
        """
        pass

    def depth_rangef(self, near_val: float, far_val: float):
        """
        Specify mapping of depth values from normalized device coordinates to window coordinates

        Wrapper for glDepthRangef

        Parameters
        ----------

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthRange.xhtml
        """
        pass

    def depth_range_arrayv(self, first: int, count: int, v: POINTER(c_double)):
        """
        Specify mapping of depth values from normalized device coordinates to window coordinates for a specified set of viewports

        Wrapper for glDepthRangeArrayv

        Parameters
        ----------
        first: int
            Specifies the index of the first viewport whose depth range to update.
        count: int
            Specifies the number of viewports whose depth range to update.
        v: POINTER(c_double)
            Specifies the address of an array containing the near and far values for the depth range of each
            modified viewport.

        Raises
        ------
        GL_INVALID_VALUE is generated if first is greater than or equal to the value of GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if first + count is greater than or equal to the value of
            GL_MAX_VIEWPORTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthRangeArray.xhtml
        """
        pass

    def depth_range_indexed(self, index: int, near_val: float, far_val: float):
        """
        Specify mapping of depth values from normalized device coordinates to window coordinates for a specified viewport

        Wrapper for glDepthRangeIndexed

        Parameters
        ----------
        index: int
            Specifies the index of the viewport whose depth range to update.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of GL_MAX_VIEWPORTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthRangeIndexed.xhtml
        """
        pass

    def gen_program_pipelines(self, n: int, pipelines: POINTER(c_uint)):
        """
        Reserve program pipeline object names

        Wrapper for glGenProgramPipelines

        Parameters
        ----------
        n: int
            Specifies the number of program pipeline object names to reserve.
        pipelines: POINTER(c_uint)
            Specifies an array of into which the reserved names will be written.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenProgramPipelines.xhtml
        """
        pass

    def get_floati_v(self, target: int, index: int, data: POINTER(c_float)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetFloati_v

        Parameters
        ----------
        target: int
            Specifies the parameter value to be returned for indexed versions of glGet. The symbolic constants
            in the list below are accepted.
        index: int
            Specifies the index of the particular element being queried.
        data: POINTER(c_float)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_doublei_v(self, target: int, index: int, data: POINTER(c_double)):
        """
        Return the value or values of a selected parameter

        Wrapper for glGetDoublei_v

        Parameters
        ----------
        target: int
            Specifies the parameter value to be returned for indexed versions of glGet. The symbolic constants
            in the list below are accepted.
        index: int
            Specifies the index of the particular element being queried.
        data: POINTER(c_double)
            Returns the value or values of the specified parameter.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_VALUE is generated on any of glGetBooleani_v, glGetIntegeri_v, or glGetInteger64i_v if
            index is outside of the valid range for the indexed state target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml
        """
        pass

    def get_program_binary(self, program: int, bufsize: int, length: POINTER(c_uint32), binary_format: POINTER(c_uint32), binary: c_void_p):
        """
        Return a binary representation of a program object's compiled and linked executable source

        Wrapper for glGetProgramBinary

        Parameters
        ----------
        program: int
            Specifies the name of a program object whose binary representation to retrieve.
        length: POINTER(c_uint32)
            Specifies the address of a variable to receive the number of bytes written into binary.
        binary: c_void_p
            Specifies the address an array into which the GL will return program 's binary representation.

        Raises
        ------
        GL_INVALID_OPERATION is generated if bufSize is less than the size of GL_PROGRAM_BINARY_LENGTH for
            program.
        GL_INVALID_OPERATION is generated if GL_LINK_STATUS for the program object is false.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramBinary.xhtml
        """
        pass

    def get_program_pipelineiv(self, pipeline: int, pname: int, params: POINTER(c_int)):
        """
        Retrieve properties of a program pipeline object

        Wrapper for glGetProgramPipelineiv

        Parameters
        ----------
        pipeline: int
            Specifies the name of a program pipeline object whose parameter retrieve.
        pname: int
            Specifies the name of the parameter to retrieve.
        params: POINTER(c_int)
            Specifies the address of a variable into which will be written the value or values of pname for
            pipeline.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pipeline is not zero or a name previously returned from a call
            to glGenProgramPipelines or if such a name has been deleted by a call to glDeleteProgramPipelines.
        GL_INVALID_ENUM is generated if pname is not one of the accepted values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramPipeline.xhtml
        """
        pass

    def get_program_pipeline_info_log(self, pipeline: int, buf_size: int, length: POINTER(c_uint32), info_log: bytes):
        """
        Retrieve the info log string from a program pipeline object

        Wrapper for glGetProgramPipelineInfoLog

        Parameters
        ----------
        pipeline: int
            Specifies the name of a program pipeline object from which to retrieve the info log.
        length: POINTER(c_uint32)
            Specifies the address of a variable into which will be written the number of characters written
            into infoLog.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pipeline is not a name previously returned from a call to
            glGenProgramPipelines or if such a name has been deleted by a call to glDeleteProgramPipelines.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramPipelineInfoLog.xhtml
        """
        pass

    def get_shader_precision_format(self, shader_type: int, precision_type: int, range: POINTER(c_int), precision: POINTER(c_int)):
        """
        Retrieve the range and precision for numeric formats supported by the shader compiler

        Wrapper for glGetShaderPrecisionFormat

        Parameters
        ----------
        range: POINTER(c_int)
            Specifies the address of array of two integers into which encodings of the implementation's numeric
            range are returned.
        precision: POINTER(c_int)
            Specifies the address of an integer into which the numeric precision of the implementation is
            written.

        Raises
        ------
        GL_INVALID_ENUM is generated if shaderType or precisionType is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShaderPrecisionFormat.xhtml
        """
        pass

    def get_vertex_attrib_ldv(self, index: int, pname: int, params: POINTER(c_double)):
        """
        Return a generic vertex attribute parameter

        Wrapper for glGetVertexAttribLdv

        Parameters
        ----------
        index: int
            Specifies the generic vertex attribute parameter to be queried.
        pname: int
            Specifies the symbolic name of the vertex attribute parameter to be queried. Accepted values are
            GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING, GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or GL_CURRENT_VERTEX_ATTRIB.
        params: POINTER(c_double)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pname is not GL_CURRENT_VERTEX_ATTRIB and there is no
            currently bound vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_OPERATION is generated if index is 0 and pname is GL_CURRENT_VERTEX_ATTRIB.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexAttrib.xhtml
        """
        pass

    def is_program_pipeline(self, pipeline: int) -> bool:
        """
        Determine if a name corresponds to a program pipeline object

        Wrapper for glIsProgramPipeline

        Parameters
        ----------
        pipeline: int
            Specifies a value that may be the name of a program pipeline object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glIsProgramPipeline.xhtml
        """
        pass

    def program_binary(self, program: int, binary_format: int, binary: c_void_p, length: int):
        """
        Load a program object with a program binary

        Wrapper for glProgramBinary

        Parameters
        ----------
        program: int
            Specifies the name of a program object into which to load a program binary.
        binary: c_void_p
            Specifies the address an array containing the binary to be loaded into program.
        length: int
            Specifies the number of bytes contained in binary.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not the name of an existing program object.
        GL_INVALID_ENUM is generated if binaryFormat is not a value recognized by the implementation.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramBinary.xhtml
        """
        pass

    def program_parameteri(self, program: int, pname: int, value: int):
        """
        Specify a parameter for a program object

        Wrapper for glProgramParameteri

        Parameters
        ----------
        program: int
            Specifies the name of a program object whose parameter to modify.
        pname: int
            Specifies the name of the parameter to modify.
        value: int
            Specifies the new value of the parameter specified by pname for program.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program is not the name of an existing program object.
        GL_INVALID_ENUM is generated if pname is not one of the accepted values.
        GL_INVALID_VALUE is generated if value is not a valid value for the parameter named by pname.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramParameter.xhtml
        """
        pass

    def program_uniform1f(self, program: int, location: int, v0: float):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform1f

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform2f(self, program: int, location: int, v0: float, v1: float):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform2f

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform3f(self, program: int, location: int, v0: float, v1: float, v2: float):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform3f

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform4f(self, program: int, location: int, v0: float, v1: float, v2: float, v3: float):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform4f

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2, v3: float
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform1i(self, program: int, location: int, v0: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform1i

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform2i(self, program: int, location: int, v0: int, v1: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform2i

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform3i(self, program: int, location: int, v0: int, v1: int, v2: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform3i

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform4i(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform4i

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2, v3: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform1ui(self, program: int, location: int, v0: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform1ui

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform2ui(self, program: int, location: int, v0: int, v1: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform2ui

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform3ui(self, program: int, location: int, v0: int, v1: int, v2: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform3ui

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform4ui(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform4ui

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        v0, v1, v2, v3: int
            For the scalar commands, specifies the new values to be used for the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform1fv(self, program: int, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform1fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform2fv(self, program: int, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform2fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform3fv(self, program: int, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform3fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform4fv(self, program: int, location: int, count: int, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform4fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform1iv(self, program: int, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform1iv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform2iv(self, program: int, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform2iv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform3iv(self, program: int, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform3iv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform4iv(self, program: int, location: int, count: int, value: POINTER(c_int)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform4iv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_int)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform1uiv(self, program: int, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform1uiv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform2uiv(self, program: int, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform2uiv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform3uiv(self, program: int, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform3uiv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform4uiv(self, program: int, location: int, count: int, value: POINTER(c_uint)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniform4uiv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        value: POINTER(c_uint)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix2fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix2fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix3fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix3fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix4fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix4fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix2x3fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix2x3fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix3x2fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix3x2fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix2x4fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix2x4fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix4x2fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix4x2fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix3x4fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix3x4fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def program_uniform_matrix4x3fv(self, program: int, location: int, count: int, transpose: bool, value: POINTER(c_float)):
        """
        Specify the value of a uniform variable for a specified program object

        Wrapper for glProgramUniformMatrix4x3fv

        Parameters
        ----------
        program: int
            Specifies the handle of the program containing the uniform variable to be modified.
        location: int
            Specifies the location of the uniform variable to be modified.
        count: int
            For the vector commands (glProgramUniform*v), specifies the number of elements that are to be
            modified. This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is
            an array. For the matrix commands (glProgramUniformMatrix*), specifies the number of matrices that
            are to be modified. This should be 1 if the targeted uniform variable is not an array of matrices,
            and 1 or more if it is an array of matrices.
        transpose: bool
            For the matrix commands, specifies whether to transpose the matrix as the values are loaded into
            the uniform variable.
        value: POINTER(c_float)
            For the vector and matrix commands, specifies a pointer to an array of count values that will be
            used to update the specified uniform variable.

        Raises
        ------
        GL_INVALID_OPERATION is generated if program does not refer to a program object owned by the GL.
        GL_INVALID_OPERATION is generated if the size of the uniform variable declared in the shader does
            not match the size indicated by the glProgramUniform command.
        GL_INVALID_OPERATION is generated if one of the signed or unsigned integer variants of this
            function is used to load a uniform variable of type float, vec2, vec3, vec4, or an array of these,
            or if one of the floating-point variants of this function is used to load a uniform variable of
            type int, ivec2, ivec3, ivec4, unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the signed integer variants of this function is used to
            load a uniform variable of type unsigned int, uvec2, uvec3, uvec4, or an array of these.
        GL_INVALID_OPERATION is generated if one of the unsigned integer variants of this function is used
            to load a uniform variable of type int, ivec2, ivec3, ivec4, or an array of these.
        GL_INVALID_OPERATION is generated if location is an invalid uniform location for program and
            location is not equal to -1.
        GL_INVALID_VALUE is generated if count is less than 0.
        GL_INVALID_OPERATION is generated if count is greater than 1 and the indicated uniform variable is
            not an array variable.
        GL_INVALID_OPERATION is generated if a sampler is loaded using a command other than
            glProgramUniform1i and glProgramUniform1iv.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glProgramUniform.xhtml
        """
        pass

    def release_shader_compiler(self):
        """
        Release resources consumed by the implementation's shader compiler

        Wrapper for glReleaseShaderCompiler

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glReleaseShaderCompiler.xhtml
        """
        pass

    def scissor_arrayv(self, first: int, count: int, v: POINTER(c_int)):
        """
        Define the scissor box for multiple viewports

        Wrapper for glScissorArrayv

        Parameters
        ----------
        first: int
            Specifies the index of the first viewport whose scissor box to modify.
        count: int
            Specifies the number of scissor boxes to modify.
        v: POINTER(c_int)
            Specifies the address of an array containing the left, bottom, width and height of each scissor
            box, in that order.

        Raises
        ------
        GL_INVALID_VALUE is generated if first is greater than or equal to the value of GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if first + count is greater than or equal to the value of
            GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if any width or height specified in the array v is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glScissorArray.xhtml
        """
        pass

    def scissor_indexed(self, index: int, left: int, bottom: int, width: int, height: int):
        """
        Define the scissor box for a specific viewport

        Wrapper for glScissorIndexed

        Parameters
        ----------
        index: int
            Specifies the index of the viewport whose scissor box to modify.
        left, bottom: int
            Specify the coordinate of the bottom left corner of the scissor box, in pixels.
        width, height: int
            Specify ths dimensions of the scissor box, in pixels.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if any width or height specified in the array v is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glScissorIndexed.xhtml
        """
        pass

    def scissor_indexedv(self, index: int, v: POINTER(c_int)):
        """
        Define the scissor box for a specific viewport

        Wrapper for glScissorIndexedv

        Parameters
        ----------
        index: int
            Specifies the index of the viewport whose scissor box to modify.
        v: POINTER(c_int)
            For glScissorIndexedv, specifies the address of an array containing the left, bottom, width and
            height of each scissor box, in that order.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if any width or height specified in the array v is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glScissorIndexed.xhtml
        """
        pass

    def shader_binary(self, count: int, shaders: POINTER(c_uint), binary_format: int, binary: c_void_p, length: int):
        """
        Load pre-compiled shader binaries

        Wrapper for glShaderBinary

        Parameters
        ----------
        count: int
            Specifies the number of shader object handles contained in shaders.
        shaders: POINTER(c_uint)
            Specifies the address of an array of shader handles into which to load pre-compiled shader
            binaries.
        binary: c_void_p
            Specifies the address of an array of bytes containing pre-compiled binary shader code.
        length: int
            Specifies the length of the array whose address is given in binary.

        Raises
        ------
        GL_INVALID_OPERATION is generated if more than one of the handles in shaders refers to the same
            shader object.
        GL_INVALID_ENUM is generated if binaryFormat is not an accepted value.
        GL_INVALID_VALUE is generated if the data pointed to by binary does not match the format specified
            by binaryFormat.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glShaderBinary.xhtml
        """
        pass

    def use_program_stages(self, pipeline: int, stages: int, program: int):
        """
        Bind stages of a program object to a program pipeline

        Wrapper for glUseProgramStages

        Parameters
        ----------
        pipeline: int
            Specifies the program pipeline object to which to bind stages from program.
        stages: int
            Specifies a set of program stages to bind to the program pipeline object.
        program: int
            Specifies the program object containing the shader executables to use in pipeline.

        Raises
        ------
        GL_INVALID_VALUE is generated if shaders contains set bits that are not recognized, and is not the
            reserved value GL_ALL_SHADER_BITS.
        GL_INVALID_OPERATION is generated if program refers to a program object that was not linked with
            its GL_PROGRAM_SEPARABLE status set.
        GL_INVALID_OPERATION is generated if program refers to a program object that has not been
            successfully linked.
        GL_INVALID_OPERATION is generated if pipeline is not a name previously returned from a call to
            glGenProgramPipelines or if such a name has been deleted by a call to glDeleteProgramPipelines.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUseProgramStages.xhtml
        """
        pass

    def validate_program_pipeline(self, pipeline: int):
        """
        Validate a program pipeline object against current GL state

        Wrapper for glValidateProgramPipeline

        Parameters
        ----------
        pipeline: int
            Specifies the name of a program pipeline object to validate.

        Raises
        ------
        GL_INVALID_OPERATION is generated if pipeline is not a name previously returned from a call to
            glGenProgramPipelines or if such a name has been deleted by a call to glDeleteProgramPipelines.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glValidateProgramPipeline.xhtml
        """
        pass

    def vertex_attrib_l1d(self, index: int, v0: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL1d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_l2d(self, index: int, v0: float, v1: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL2d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_l3d(self, index: int, v0: float, v1: float, v2: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL3d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_l4d(self, index: int, v0: float, v1: float, v2: float, v3: float):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL4d

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v0, v1, v2, v3: float
            For the scalar commands, specifies the new values to be used for the specified vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_l1dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL1dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_l2dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL2dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_l3dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL3dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_l4dv(self, index: int, v: POINTER(c_double)):
        """
        Specifies the value of a generic vertex attribute

        Wrapper for glVertexAttribL4dv

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        v: POINTER(c_double)
            For the vector commands (glVertexAttrib*v), specifies a pointer to an array of values to be used
            for the generic vertex attribute.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM is generated if glVertexAttribP* is used with a type other than
            GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV, or GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_ENUM is generated if glVertexAttribL is used with a type other than GL_DOUBLE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttrib.xhtml
        """
        pass

    def vertex_attrib_lpointer(self, index: int, size: int, type: int, stride: int, pointer: c_void_p):
        """
        Define an array of generic vertex attribute data

        Wrapper for glVertexAttribLPointer

        Parameters
        ----------
        index: int
            Specifies the index of the generic vertex attribute to be modified.
        size: int
            Specifies the number of components per generic vertex attribute. Must be 1, 2, 3, 4. Additionally,
            the symbolic constant GL_BGRA is accepted by glVertexAttribPointer. The initial value is 4.
        type: int
            Specifies the data type of each component in the array. The symbolic constants GL_BYTE,
            GL_UNSIGNED_BYTE, GL_SHORT, GL_UNSIGNED_SHORT, GL_INT, and GL_UNSIGNED_INT are accepted by
            glVertexAttribPointer and glVertexAttribIPointer. Additionally GL_HALF_FLOAT, GL_FLOAT, GL_DOUBLE,
            GL_FIXED, GL_INT_2_10_10_10_REV, GL_UNSIGNED_INT_2_10_10_10_REV and GL_UNSIGNED_INT_10F_11F_11F_REV
            are accepted by glVertexAttribPointer. GL_DOUBLE is also accepted by glVertexAttribLPointer and is
            the only token accepted by the type parameter for that function. The initial value is GL_FLOAT.
        stride: int
            Specifies the byte offset between consecutive generic vertex attributes. If stride is 0, the
            generic vertex attributes are understood to be tightly packed in the array. The initial value is 0.
        pointer: c_void_p
            Specifies a offset of the first component of the first generic vertex attribute in the array in the
            data store of the buffer currently bound to the GL_ARRAY_BUFFER target. The initial value is 0.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not 1, 2, 3, 4 or (for glVertexAttribPointer), GL_BGRA.
        GL_INVALID_ENUM is generated if type is not an accepted value.
        GL_INVALID_VALUE is generated if stride is negative.
        GL_INVALID_OPERATION is generated if size is GL_BGRA and type is not GL_UNSIGNED_BYTE,
            GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV.
        GL_INVALID_OPERATION is generated if type is GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV and size is not 4 or GL_BGRA.
        GL_INVALID_OPERATION is generated if type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        GL_INVALID_OPERATION is generated by glVertexAttribPointer if size is GL_BGRA and noramlized is
            GL_FALSE.
        GL_INVALID_OPERATION is generated if zero is bound to the GL_ARRAY_BUFFER buffer object binding
            point and the pointer argument is not NULL.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribPointer.xhtml
        """
        pass

    def viewport_arrayv(self, first: int, count: int, v: POINTER(c_float)):
        """
        Set multiple viewports

        Wrapper for glViewportArrayv

        Parameters
        ----------
        first: int
            Specify the first viewport to set.
        count: int
            Specify the number of viewports to set.
        v: POINTER(c_float)
            Specify the address of an array containing the viewport parameters.

        Raises
        ------
        GL_INVALID_VALUE is generated if first is greater than or equal to the value of GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if first + count is greater than or equal to the value of
            GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if either width or height is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glViewportArray.xhtml
        """
        pass

    def viewport_indexedf(self, index: int, x: float, y: float, w: float, h: float):
        """
        Set a specified viewport

        Wrapper for glViewportIndexedf

        Parameters
        ----------
        index: int
            Specify the first viewport to set.
        x, y: float
            For glViewportIndexedf, specifies the lower left corner of the viewport rectangle, in pixels. The
            initial value is (0,0).

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if either width or height is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glViewportIndexed.xhtml
        """
        pass

    def viewport_indexedfv(self, index: int, v: POINTER(c_float)):
        """
        Set a specified viewport

        Wrapper for glViewportIndexedfv

        Parameters
        ----------
        index: int
            Specify the first viewport to set.
        v: POINTER(c_float)
            For glViewportIndexedfv, specifies the address of an array containing the viewport parameters.

        Raises
        ------
        GL_INVALID_VALUE is generated if index is greater than or equal to the value of GL_MAX_VIEWPORTS.
        GL_INVALID_VALUE is generated if either width or height is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glViewportIndexed.xhtml
        """
        pass

class GL42(GL41):

    MAJOR = 4
    MINOR = 2

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.bind_image_texture, 'glBindImageTexture',
                   None, c_uint, c_uint, c_int, c_bool, c_int, c_uint, c_uint)
        self._load(self.draw_arrays_instanced_base_instance, 'glDrawArraysInstancedBaseInstance',
                   None, c_uint, c_int, c_uint32, c_uint32, c_uint)
        self._load(self.draw_elements_instanced_base_instance, 'glDrawElementsInstancedBaseInstance',
                   None, c_uint, c_uint32, c_uint, c_void_p, c_uint32, c_uint)
        self._load(self.draw_elements_instanced_base_vertex_base_instance, 'glDrawElementsInstancedBaseVertexBaseInstance',
                   None, c_uint, c_uint32, c_uint, c_void_p, c_uint32, c_int, c_uint)
        self._load(self.draw_transform_feedback_instanced, 'glDrawTransformFeedbackInstanced',
                   None, c_uint, c_uint, c_uint32)
        self._load(self.draw_transform_feedback_stream_instanced, 'glDrawTransformFeedbackStreamInstanced',
                   None, c_uint, c_uint, c_uint, c_uint32)
        self._load(self.get_active_atomic_counter_bufferiv, 'glGetActiveAtomicCounterBufferiv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_internalformativ, 'glGetInternalformativ',
                   None, c_uint, c_uint, c_uint, c_uint32, POINTER(c_int))
        self._load(self.memory_barrier, 'glMemoryBarrier',
                   None, c_uint32)

    def bind_image_texture(self, unit: int, texture: int, level: int, layered: bool, layer: int, access: int, format: int):
        """
        Bind a level of a texture to an image unit

        Wrapper for glBindImageTexture

        Parameters
        ----------
        unit: int
            Specifies the index of the image unit to which to bind the texture
        texture: int
            Specifies the name of the texture to bind to the image unit.
        level: int
            Specifies the level of the texture that is to be bound.
        layered: bool
            Specifies whether a layered texture binding is to be established.
        layer: int
            If layered is GL_FALSE, specifies the layer of texture to be bound to the image unit. Ignored
            otherwise.
        access: int
            Specifies a token indicating the type of access that will be performed on the image.
        format: int
            Specifies the format that the elements of the image will be treated as for the purposes of
            formatted stores.

        Raises
        ------
        GL_INVALID_VALUE is generated if unit greater than or equal to the value of GL_MAX_IMAGE_UNITS.
        GL_INVALID_VALUE is generated if texture is not the name of an existing texture object.
        GL_INVALID_VALUE is generated if level or layer is less than zero.
        GL_INVALID_ENUM is generated if access or format is not one of the supported tokens.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindImageTexture.xhtml
        """
        pass

    def draw_arrays_instanced_base_instance(self, mode: int, first: int, count: int, primcount: int, baseinstance: int):
        """
        Draw multiple instances of a range of elements with offset applied to instanced attributes

        Wrapper for glDrawArraysInstancedBaseInstance

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES GL_LINES_ADJACENCY,
            GL_LINE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY and GL_PATCHES are
            accepted.
        first: int
            Specifies the starting index in the enabled arrays.
        count: int
            Specifies the number of indices to be rendered.
        primcount: int
            Specifies the number of instances of the specified range of indices to be rendered.
        baseinstance: int
            Specifies the base instance for use in fetching instanced vertex attributes.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of the accepted values.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_VALUE is generated if count or primcount are negative.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawArraysInstancedBaseInstance.xhtml
        """
        pass

    def draw_elements_instanced_base_instance(self, mode: int, count: int, type: int, indices: c_void_p, primcount: int, baseinstance: int):
        """
        Draw multiple instances of a set of elements with offset applied to instanced attributes

        Wrapper for glDrawElementsInstancedBaseInstance

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES
            are accepted.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.
        primcount: int
            Specifies the number of instances of the specified range of indices to be rendered.
        baseinstance: int
            Specifies the base instance for use in fetching instanced vertex attributes.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of GL_POINTS, GL_LINE_STRIP, GL_LINE_LOOP,
            GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, or GL_TRIANGLES.
        GL_INVALID_VALUE is generated if count or primcount are negative.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawElementsInstancedBaseInstance.xhtml
        """
        pass

    def draw_elements_instanced_base_vertex_base_instance(self, mode: int, count: int, type: int, indices: c_void_p, primcount: int, basevertex: int, baseinstance: int):
        """
        Render multiple instances of a set of primitives from array data with a per-element offset

        Wrapper for glDrawElementsInstancedBaseVertexBaseInstance

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES, GL_LINES_ADJACENCY,
            GL_LINE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY and GL_PATCHES are
            accepted.
        count: int
            Specifies the number of elements to be rendered.
        type: int
            Specifies the type of the values in indices. Must be one of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or
            GL_UNSIGNED_INT.
        indices: c_void_p
            Specifies a pointer to the location where the indices are stored.
        primcount: int
            Specifies the number of instances of the indexed geometry that should be drawn.
        basevertex: int
            Specifies a constant that should be added to each element of indices when chosing elements from the
            enabled vertex arrays.
        baseinstance: int
            Specifies the base instance for use in fetching instanced vertex attributes.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if count or primcount is negative.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            the element array and the buffer object's data store is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawElementsInstancedBaseVertexBaseInstance.xhtml
        """
        pass

    def draw_transform_feedback_instanced(self, mode: int, id: int, primcount: int):
        """
        Render multiple instances of primitives using a count derived from a transform feedback object

        Wrapper for glDrawTransformFeedbackInstanced

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        id: int
            Specifies the name of a transform feedback object from which to retrieve a primitive count.
        primcount: int
            Specifies the number of instances of the geometry to render.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if id is not the name of a transform feedback object.
        GL_INVALID_VALUE is generated if stream is greater than or equal to the value of
            GL_MAX_VERTEX_STREAMS.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.
        GL_INVALID_OPERATION is generated if glEndTransformFeedback has never been called while the
            transform feedback object named by id was bound.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawTransformFeedbackInstanced.xhtml
        """
        pass

    def draw_transform_feedback_stream_instanced(self, mode: int, id: int, stream: int, primcount: int):
        """
        Render multiple instances of primitives using a count derived from a specifed stream of a transform feedback object

        Wrapper for glDrawTransformFeedbackStreamInstanced

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        id: int
            Specifies the name of a transform feedback object from which to retrieve a primitive count.
        stream: int
            Specifies the index of the transform feedback stream from which to retrieve a primitive count.
        primcount: int
            Specifies the number of instances of the geometry to render.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if id is not the name of a transform feedback object.
        GL_INVALID_VALUE is generated if stream is greater than or equal to the value of
            GL_MAX_VERTEX_STREAMS.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array and
            the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.
        GL_INVALID_OPERATION is generated if glEndTransformFeedback has never been called while the
            transform feedback object named by id was bound.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawTransformFeedbackStreamInstanced.xhtml
        """
        pass

    def get_active_atomic_counter_bufferiv(self, program: int, buffer_index: int, pname: int, params: POINTER(c_int)):
        """
        Retrieve information about the set of active atomic counter buffers for a program

        Wrapper for glGetActiveAtomicCounterBufferiv

        Parameters
        ----------
        program: int
            The name of a program object from which to retrieve information.
        pname: int
            Specifies which parameter of the atomic counter buffer to retrieve.
        params: POINTER(c_int)
            Specifies the address of a variable into which to write the retrieved information.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not the name of a program object for which
            glLinkProgram has been called in the past.
        GL_INVALID_VALUE is generated if bufferIndex is greater than or equal to the value of
            GL_ACTIVE_ATOMIC_COUNTER_BUFFERS for program.
        GL_INVALID_ENUM is generated if pname is not one of the accepted tokens.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetActiveAtomicCounterBufferiv.xhtml
        """
        pass

    def get_internalformativ(self, target: int, internalformat: int, pname: int, buf_size: int, params: POINTER(c_int)):
        """
        Retrieve information about implementation-dependent support for internal formats

        Wrapper for glGetInternalformativ

        Parameters
        ----------
        target: int
            Indicates the usage of the internal format. target must be GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY,
            GL_TEXTURE_RECTANGLE, GL_TEXTURE_BUFFER, GL_RENDERBUFFER, GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY.
        internalformat: int
            Specifies the internal format about which to retrieve information.
        pname: int
            Specifies the type of information to query.
        params: POINTER(c_int)
            Specifies the address of a variable into which to write the retrieved information.

        Raises
        ------
        GL_INVALID_VALUE is generated if bufSize is negative.
        GL_INVALID_ENUM is generated if pname is not GL_SAMPLES or GL_NUM_SAMPLE_COUNTS.
        GL_INVALID_ENUM is generated if internalformat is not color-, depth-, or stencil-renderable.
        GL_INVALID_ENUM is generated if target is not one of GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY or GL_RENDERBUFFER.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetInternalformat.xhtml
        """
        pass

    def memory_barrier(self, barriers: int):
        """
        Defines a barrier ordering memory transactions

        Wrapper for glMemoryBarrier

        Parameters
        ----------
        barriers: int
            Specifies the barriers to insert. For glMemoryBarrier, must be a bitwise combination of any of
            GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT, GL_ELEMENT_ARRAY_BARRIER_BIT, GL_UNIFORM_BARRIER_BIT,
            GL_TEXTURE_FETCH_BARRIER_BIT, GL_SHADER_IMAGE_ACCESS_BARRIER_BIT, GL_COMMAND_BARRIER_BIT,
            GL_PIXEL_BUFFER_BARRIER_BIT, GL_TEXTURE_UPDATE_BARRIER_BIT, GL_BUFFER_UPDATE_BARRIER_BIT,
            GL_FRAMEBUFFER_BARRIER_BIT, GL_TRANSFORM_FEEDBACK_BARRIER_BIT, GL_ATOMIC_COUNTER_BARRIER_BIT, or
            GL_SHADER_STORAGE_BARRIER_BIT. For glMemoryBarrier, must be a bitwise combination of any of
            GL_ATOMIC_COUNTER_BARRIER_BIT, or GL_FRAMEBUFFER_BARRIER_BIT, GL_SHADER_IMAGE_ACCESS_BARRIER_BIT,
            GL_SHADER_STORAGE_BARRIER_BIT. GL_TEXTURE_FETCH_BARRIER_BIT, or GL_UNIFORM_BARRIER_BIT. If the
            special value GL_ALL_BARRIER_BITS is specified, all supported barriers for the corresponding
            command will be inserted.

        Raises
        ------
        GL_INVALID_VALUE is generated if barriers is not the special value GL_ALL_BARRIER_BITS, and has any
            bits set other than those described above for glMemoryBarrier or glMemoryBarrierByRegion
            respectively.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMemoryBarrier.xhtml
        """
        pass

class GL43(GL42):

    MAJOR = 4
    MINOR = 3

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.bind_vertex_buffer, 'glBindVertexBuffer',
                   None, c_uint, c_uint, POINTER(c_int), POINTER(c_int))
        self._load(self.clear_buffer_data, 'glClearBufferData',
                   None, c_uint, c_uint, c_uint, c_uint, c_void_p)
        self._load(self.clear_buffer_sub_data, 'glClearBufferSubData',
                   None, c_uint, c_uint, POINTER(c_int), POINTER(c_uint32), c_uint, c_uint, c_void_p)
        self._load(self.copy_image_sub_data, 'glCopyImageSubData',
                   None, c_uint, c_uint, c_int, c_int, c_int, c_int, c_uint, c_uint, c_int, c_int, c_int, c_int, c_uint32, c_uint32, c_uint32)
        self._load(self.debug_message_callback, 'glDebugMessageCallback',
                   None, c_void_p, c_void_p)
        self._load(self.debug_message_control, 'glDebugMessageControl',
                   None, c_uint, c_uint, c_uint, c_uint32, POINTER(c_uint), c_bool)
        self._load(self.debug_message_insert, 'glDebugMessageInsert',
                   None, c_uint, c_uint, c_uint, c_uint, c_uint32, c_char_p)
        self._load(self.dispatch_compute, 'glDispatchCompute',
                   None, c_uint, c_uint, c_uint)
        self._load(self.dispatch_compute_indirect, 'glDispatchComputeIndirect',
                   None, POINTER(c_int))
        self._load(self.framebuffer_parameteri, 'glFramebufferParameteri',
                   None, c_uint, c_uint, c_int)
        self._load(self.get_debug_message_log, 'glGetDebugMessageLog',
                   c_uint, c_uint, c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint), POINTER(c_uint32), POINTER(c_uint32), c_char_p)
        self._load(self.get_framebuffer_parameteriv, 'glGetFramebufferParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_internalformati64v, 'glGetInternalformati64v',
                   None, c_uint, c_uint, c_uint, c_uint32, POINTER(c_int64))
        self._load(self.get_object_label, 'glGetObjectLabel',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_object_ptr_label, 'glGetObjectPtrLabel',
                   None, c_void_p, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.get_pointerv, 'glGetPointerv',
                   None, c_uint, POINTER(c_void_p))
        self._load(self.get_program_interfaceiv, 'glGetProgramInterfaceiv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_program_resourceiv, 'glGetProgramResourceiv',
                   None, c_uint, c_uint, c_uint, c_uint32, POINTER(c_uint32), c_uint32, POINTER(c_uint32), POINTER(c_int))
        self._load(self.get_program_resource_index, 'glGetProgramResourceIndex',
                   c_uint, c_uint, c_uint, c_char_p)
        self._load(self.get_program_resource_location, 'glGetProgramResourceLocation',
                   c_int, c_uint, c_uint, c_char_p)
        self._load(self.get_program_resource_location_index, 'glGetProgramResourceLocationIndex',
                   c_int, c_uint, c_uint, c_char_p)
        self._load(self.get_program_resource_name, 'glGetProgramResourceName',
                   None, c_uint, c_uint, c_uint, c_uint32, POINTER(c_uint32), c_char_p)
        self._load(self.invalidate_buffer_data, 'glInvalidateBufferData',
                   None, c_uint)
        self._load(self.invalidate_buffer_sub_data, 'glInvalidateBufferSubData',
                   None, c_uint, POINTER(c_int), POINTER(c_uint32))
        self._load(self.invalidate_framebuffer, 'glInvalidateFramebuffer',
                   None, c_uint, c_uint32, POINTER(c_uint32))
        self._load(self.invalidate_sub_framebuffer, 'glInvalidateSubFramebuffer',
                   None, c_uint, c_uint32, POINTER(c_uint32), c_int, c_int, c_int, c_int)
        self._load(self.invalidate_tex_image, 'glInvalidateTexImage',
                   None, c_uint, c_int)
        self._load(self.invalidate_tex_sub_image, 'glInvalidateTexSubImage',
                   None, c_uint, c_int, c_int, c_int, c_int, c_uint32, c_uint32, c_uint32)
        self._load(self.multi_draw_arrays_indirect, 'glMultiDrawArraysIndirect',
                   None, c_uint, c_void_p, c_uint32, c_uint32)
        self._load(self.multi_draw_elements_indirect, 'glMultiDrawElementsIndirect',
                   None, c_uint, c_uint, c_void_p, c_uint32, c_uint32)
        self._load(self.object_label, 'glObjectLabel',
                   None, c_uint, c_uint, c_uint32, c_char_p)
        self._load(self.object_ptr_label, 'glObjectPtrLabel',
                   None, c_void_p, c_uint32, c_char_p)
        self._load(self.pop_debug_group, 'glPopDebugGroup',
                   None, )
        self._load(self.push_debug_group, 'glPushDebugGroup',
                   None, c_uint, c_uint, c_uint32, c_char_p)
        self._load(self.shader_storage_block_binding, 'glShaderStorageBlockBinding',
                   None, c_uint, c_uint, c_uint)
        self._load(self.tex_buffer_range, 'glTexBufferRange',
                   None, c_uint, c_uint, c_uint, POINTER(c_int), POINTER(c_uint32))
        self._load(self.texture_view, 'glTextureView',
                   None, c_uint, c_uint, c_uint, c_uint, c_uint, c_uint, c_uint, c_uint)
        self._load(self.vertex_attrib_binding, 'glVertexAttribBinding',
                   None, c_uint, c_uint)
        self._load(self.vertex_attrib_format, 'glVertexAttribFormat',
                   None, c_uint, c_int, c_uint, c_bool, c_uint)
        self._load(self.vertex_attrib_iformat, 'glVertexAttribIFormat',
                   None, c_uint, c_int, c_uint, c_uint)
        self._load(self.vertex_attrib_lformat, 'glVertexAttribLFormat',
                   None, c_uint, c_int, c_uint, c_uint)
        self._load(self.vertex_binding_divisor, 'glVertexBindingDivisor',
                   None, c_uint, c_uint)

    def bind_vertex_buffer(self, bindingindex: int, buffer: int, offset: POINTER(c_int), stride: POINTER(c_int)):
        """
        Bind a buffer to a vertex buffer bind point

        Wrapper for glBindVertexBuffer

        Parameters
        ----------
        bindingindex: int
            The index of the vertex buffer binding point to which to bind the buffer.
        buffer: int
            The name of a buffer to bind to the vertex buffer binding point.
        offset: POINTER(c_int)
            The offset of the first element of the buffer.
        stride: POINTER(c_int)
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glBindVertexBuffer if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayVertexBuffer if vaobj is not the name of an
            existing vertex array object.
        GL_INVALID_VALUE is generated if bindingindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.
        GL_INVALID_VALUE is generated if offset or stride is less than zero, or if stride is greater than
            the value of GL_MAX_VERTEX_ATTRIB_STRIDE.
        GL_INVALID_VALUE is generated if buffer is not zero or the name of an existing buffer object (as
            returned by glGenBuffers or glCreateBuffers).

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindVertexBuffer.xhtml
        """
        pass

    def clear_buffer_data(self, target: int, internalformat: int, format: int, type: int, data: c_void_p):
        """
        Fill a buffer object's data store with a fixed value

        Wrapper for glClearBufferData

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glClearBufferData, which must must be
            one of the buffer binding targets in the following table: Buffer Binding Target Purpose
            GL_ARRAY_BUFFER Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage
            GL_COPY_READ_BUFFER Buffer copy source GL_COPY_WRITE_BUFFER Buffer copy destination
            GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect
            command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array indices GL_PIXEL_PACK_BUFFER Pixel read
            target GL_PIXEL_UNPACK_BUFFER Texture data source GL_QUERY_BUFFER Query result buffer
            GL_SHADER_STORAGE_BUFFER Read-write storage for shaders GL_TEXTURE_BUFFER Texture data buffer
            GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer GL_UNIFORM_BUFFER Uniform block storage
        internalformat: int
            The internal format with which the data will be stored in the buffer object.
        format: int
            The format of the data in memory addressed by data.
        type: int
            The type of the data in memory addressed by data.
        data: c_void_p
            The address of a memory location storing the data to be replicated into the buffer's data store.

        Raises
        ------
        GL_INVALID_ENUM is generated by glClearBufferData if target is not one of the generic buffer
            binding targets.
        GL_INVALID_VALUE is generated by glClearBufferData if no buffer is bound target.
        GL_INVALID_OPERATION is generated by glClearNamedBufferData if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if internalformat is not one of the valid sized internal formats
            listed in the table above.
        GL_INVALID_OPERATION is generated if any part of the specified range of the buffer object is mapped
            with glMapBufferRange or glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set
            in the glMapBufferRange access flags.
        GL_INVALID_VALUE is generated if format is not a valid format, or type is not a valid type.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBufferData.xhtml
        """
        pass

    def clear_buffer_sub_data(self, target: int, internalformat: int, offset: POINTER(c_int), size: POINTER(c_uint32), format: int, type: int, data: c_void_p):
        """
        Fill all or part of buffer object's data store with a fixed value

        Wrapper for glClearBufferSubData

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glClearBufferSubData, which must be
            one of the buffer binding targets in the following table: Buffer Binding Target Purpose
            GL_ARRAY_BUFFER Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage
            GL_COPY_READ_BUFFER Buffer copy source GL_COPY_WRITE_BUFFER Buffer copy destination
            GL_DISPATCH_INDIRECT_BUFFER Indirect compute dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect
            command arguments GL_ELEMENT_ARRAY_BUFFER Vertex array indices GL_PIXEL_PACK_BUFFER Pixel read
            target GL_PIXEL_UNPACK_BUFFER Texture data source GL_QUERY_BUFFER Query result buffer
            GL_SHADER_STORAGE_BUFFER Read-write storage for shaders GL_TEXTURE_BUFFER Texture data buffer
            GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer GL_UNIFORM_BUFFER Uniform block storage
        internalformat: int
            The internal format with which the data will be stored in the buffer object.
        offset: POINTER(c_int)
            The offset in basic machine units into the buffer object's data store at which to start filling.
        size: POINTER(c_uint32)
            The size in basic machine units of the range of the data store to fill.
        format: int
            The format of the data in memory addressed by data.
        type: int
            The type of the data in memory addressed by data.
        data: c_void_p
            The address of a memory location storing the data to be replicated into the buffer's data store.

        Raises
        ------
        GL_INVALID_ENUM is generated by glClearBufferSubData if target is not one of the generic buffer
            binding targets.
        GL_INVALID_VALUE is generated by glClearBufferSubData if no buffer is bound to target.
        GL_INVALID_OPERATION is generated by glClearNamedBufferSubData if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if internalformat is not one of the valid sized internal formats
            listed in the table above.
        GL_INVALID_VALUE is generated if offset or range are not multiples of the number of basic machine
            units per-element for the internal format specified by internalformat. This value may be computed
            by multiplying the number of components for internalformat from the table by the size of the base
            type from the table.
        GL_INVALID_VALUE is generated if offset or size is negative, or if $offset + size$ is greater than
            the value of GL_BUFFER_SIZE for the buffer object.
        GL_INVALID_OPERATION is generated if any part of the specified range of the buffer object is mapped
            with glMapBufferRange or glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set
            in the glMapBufferRange access flags.
        GL_INVALID_VALUE is generated if format is not a valid format, or type is not a valid type.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBufferSubData.xhtml
        """
        pass

    def copy_image_sub_data(self, src_name: int, src_target: int, src_level: int, src_x: int, src_y: int, src_z: int, dst_name: int, dst_target: int, dst_level: int, dst_x: int, dst_y: int, dst_z: int, src_width: int, src_height: int, src_depth: int):
        """
        Perform a raw data copy between two images

        Wrapper for glCopyImageSubData

        Parameters
        ----------

        Raises
        ------
        GL_INVALID_OPERATION is generated if the texel size of the uncompressed image is not equal to the
            block size of the compressed image.
        GL_INVALID_ENUM is generated if either target parameter is not GL_RENDERBUFFER, a valid non-proxy
            texture target other than GL_TEXTURE_BUFFER, or is one of the cubemap face selectors.
        GL_INVALID_ENUM is generated if target does not match the type of the object.
        GL_INVALID_OPERATION is generated if either object is a texture and the texture is not complete.
        GL_INVALID_OPERATION is generated if the source and destination internal formats are not
            compatible, or if the number of samples do not match.
        GL_INVALID_VALUE is generated if either name does not correspond to a valid renderbuffer or texture
            object according to the corresponding target parameter.
        GL_INVALID_VALUE is generated if the specified level of either the source or destination is not a
            valid level for the corresponding image.
        GL_INVALID_VALUE is generated if the dimensions of the either subregion exceeds the boundaries of
            the corresponding image object, or if the image format is compressed and the dimensions of the
            subregion fail to meet the alignment constraints of the format.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCopyImageSubData.xhtml
        """
        pass

    def debug_message_callback(self, callback: c_void_p, user_param: c_void_p):
        """
        Specify a callback to receive debugging messages from the GL

        Wrapper for glDebugMessageCallback

        Parameters
        ----------
        callback: c_void_p
            The address of a callback function that will be called when a debug message is generated.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDebugMessageCallback.xhtml
        """
        pass

    def debug_message_control(self, source: int, type: int, severity: int, count: int, ids: POINTER(c_uint), enabled: bool):
        """
        Control the reporting of debug messages in a debug context

        Wrapper for glDebugMessageControl

        Parameters
        ----------
        source: int
            The source of debug messages to enable or disable.
        type: int
            The type of debug messages to enable or disable.
        severity: int
            The severity of debug messages to enable or disable.
        count: int
            The length of the array ids.
        ids: POINTER(c_uint)
            The address of an array of unsigned integers contianing the ids of the messages to enable or
            disable.
        enabled: bool
            A Boolean flag determining whether the selected messages should be enabled or disabled.

        Raises
        ------
        GL_INVALID_VALUE is generated if count is negative.
        GL_INVALID_ENUM is generated if any of source, type or severity is not one of the accepted
            interface types.
        GL_INVALID_OPERATION is generated if count is non-zero and either source or type is GL_DONT_CARE or
            if severity is not GL_DONT_CARE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDebugMessageControl.xhtml
        """
        pass

    def debug_message_insert(self, source: int, type: int, id: int, severity: int, length: int, message: bytes):
        """
        Inject an application-supplied message into the debug message queue

        Wrapper for glDebugMessageInsert

        Parameters
        ----------
        source: int
            The source of the debug message to insert.
        type: int
            The type of the debug message insert.
        id: int
            The user-supplied identifier of the message to insert.
        severity: int
            The severity of the debug messages to insert.
        length: int
            The length string contained in the character array whose address is given by message.
        message: bytes
            The address of a character array containing the message to insert.

        Raises
        ------
        GL_INVALID_ENUM is generated if any of source, type or severity is not one of the accepted
            interface types.
        GL_INVALID_VALUE is generated if the length of the message is greater than the value of
            GL_MAX_DEBUG_MESSAGE_LENGTH.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDebugMessageInsert.xhtml
        """
        pass

    def dispatch_compute(self, num_groups_x: int, num_groups_y: int, num_groups_z: int):
        """
        Launch one or more compute work groups

        Wrapper for glDispatchCompute

        Parameters
        ----------
        num_groups_x: int
            The number of work groups to be launched in the X dimension.
        num_groups_y: int
            The number of work groups to be launched in the Y dimension.
        num_groups_z: int
            The number of work groups to be launched in the Z dimension.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no active program for the compute shader stage.
        GL_INVALID_VALUE is generated if any of num_groups_x, num_groups_y, or num_groups_z is greater than
            or equal to the maximum work-group count for the corresponding dimension.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDispatchCompute.xhtml
        """
        pass

    def dispatch_compute_indirect(self, indirect: POINTER(c_int)):
        """
        Launch one or more compute work groups using parameters stored in a buffer

        Wrapper for glDispatchComputeIndirect

        Parameters
        ----------
        indirect: POINTER(c_int)
            The offset into the buffer object currently bound to the GL_DISPATCH_INDIRECT_BUFFER buffer target
            at which the dispatch parameters are stored.

        Raises
        ------
        GL_INVALID_OPERATION is generated if there is no active program for the compute shader stage.
        GL_INVALID_VALUE is generated if indirect is less than zero or not a multiple of four.
        GL_INVALID_OPERATION is generated if no buffer is bound to the GL_DISPATCH_INDIRECT_BUFFER target
            or if the command would source data beyond the end of the buffer object's data store.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDispatchComputeIndirect.xhtml
        """
        pass

    def framebuffer_parameteri(self, target: int, pname: int, param: int):
        """
        Set a named parameter of a framebuffer object

        Wrapper for glFramebufferParameteri

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer is bound for glFramebufferParameteri.
        pname: int
            Specifies the framebuffer parameter to be modified.
        param: int
            The new value for the parameter named pname.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFramebufferParameteri if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glFramebufferParameteri if the default framebuffer is bound to
            target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferParameteri if framebuffer is not the name of
            an existing framebuffer object.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_WIDTH and param is less than zero
            or greater than the value of GL_MAX_FRAMEBUFFER_WIDTH.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_HEIGHT and param is less than zero
            or greater than the value of GL_MAX_FRAMEBUFFER_HEIGHT.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_LAYERS and param is less than zero
            or greater than the value of GL_MAX_FRAMEBUFFER_LAYERS.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_SAMPLES and param is less than
            zero or greater than the value of GL_MAX_FRAMEBUFFER_SAMPLES.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferParameteri.xhtml
        """
        pass

    def get_debug_message_log(self, count: int, buf_size: int, sources: POINTER(c_uint32), types: POINTER(c_uint32), ids: POINTER(c_uint), severities: POINTER(c_uint32), lengths: POINTER(c_uint32), message_log: bytes) -> int:
        """
        Retrieve messages from the debug message log

        Wrapper for glGetDebugMessageLog

        Parameters
        ----------
        count: int
            The number of debug messages to retrieve from the log.
        sources: POINTER(c_uint32)
            The address of an array of variables to receive the sources of the retrieved messages.
        types: POINTER(c_uint32)
            The address of an array of variables to receive the types of the retrieved messages.
        ids: POINTER(c_uint)
            The address of an array of unsigned integers to receive the ids of the retrieved messages.
        severities: POINTER(c_uint32)
            The address of an array of variables to receive the severites of the retrieved messages.
        lengths: POINTER(c_uint32)
            The address of an array of variables to receive the lengths of the received messages.

        Raises
        ------
        GL_INVALID_VALUE is generated if count or bufSize is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetDebugMessageLog.xhtml
        """
        pass

    def get_framebuffer_parameteriv(self, target: int, pname: int, params: POINTER(c_int)):
        """
        Query a named parameter of a framebuffer object

        Wrapper for glGetFramebufferParameteriv

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer object is bound for glGetFramebufferParameteriv.
        pname: int
            Specifies the parameter of the framebuffer object to query.
        params: POINTER(c_int)
            Returns the value of parameter pname for the framebuffer object.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetFramebufferParameteriv if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glGetNamedFramebufferAttachmentParameteriv if framebuffer is
            not zero or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if pname is not one of the accepted parameter names.
        GL_INVALID_OPERATION is generated if a default framebuffer is queried, and pname is not one of
            GL_DOUBLEBUFFER, GL_IMPLEMENTATION_COLOR_READ_FORMAT, GL_IMPLEMENTATION_COLOR_READ_TYPE,
            GL_SAMPLES, GL_SAMPLE_BUFFERS or GL_STEREO.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetFramebufferParameter.xhtml
        """
        pass

    def get_internalformati64v(self, target: int, internalformat: int, pname: int, buf_size: int, params: POINTER(c_int64)):
        """
        Retrieve information about implementation-dependent support for internal formats

        Wrapper for glGetInternalformati64v

        Parameters
        ----------
        target: int
            Indicates the usage of the internal format. target must be GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY,
            GL_TEXTURE_RECTANGLE, GL_TEXTURE_BUFFER, GL_RENDERBUFFER, GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY.
        internalformat: int
            Specifies the internal format about which to retrieve information.
        pname: int
            Specifies the type of information to query.
        params: POINTER(c_int64)
            Specifies the address of a variable into which to write the retrieved information.

        Raises
        ------
        GL_INVALID_VALUE is generated if bufSize is negative.
        GL_INVALID_ENUM is generated if pname is not GL_SAMPLES or GL_NUM_SAMPLE_COUNTS.
        GL_INVALID_ENUM is generated if internalformat is not color-, depth-, or stencil-renderable.
        GL_INVALID_ENUM is generated if target is not one of GL_TEXTURE_2D_MULTISAMPLE,
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY or GL_RENDERBUFFER.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetInternalformat.xhtml
        """
        pass

    def get_object_label(self, identifier: int, name: int, bif_size: int, length: POINTER(c_uint32), label: bytes):
        """
        Retrieve the label of a named object identified within a namespace

        Wrapper for glGetObjectLabel

        Parameters
        ----------
        identifier: int
            The namespace from which the name of the object is allocated.
        name: int
            The name of the object whose label to retrieve.
        length: POINTER(c_uint32)
            The address of a variable to receive the length of the object label.
        label: bytes
            The address of a string that will receive the object label.

        Raises
        ------
        GL_INVALID_ENUM is generated if identifier is not one of the accepted object types.
        GL_INVALID_OPERATION is generated if name is not the name of an existing object of the type
            specified by identifier.
        GL_INVALID_VALUE is generated if bufSize is zero.
        If not NULL, length and label should be addresses to which the client has write access, otherwise
            undefined behavior, including process termination may occur.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetObjectLabel.xhtml
        """
        pass

    def get_object_ptr_label(self, ptr: c_void_p, bif_size: int, length: POINTER(c_uint32), label: bytes):
        """
        Retrieve the label of a sync object identified by a pointer

        Wrapper for glGetObjectPtrLabel

        Parameters
        ----------
        ptr: c_void_p
            The name of the sync object whose label to retrieve.
        length: POINTER(c_uint32)
            The address of a variable to receive the length of the object label.
        label: bytes
            The address of a string that will receive the object label.

        Raises
        ------
        GL_INVALID_ENUM is generated if identifier is not one of the accepted object types.
        GL_INVALID_VALUE is generated if ptr is not the name of an existing sync object.
        GL_INVALID_VALUE is generated if bufSize is zero.
        If not NULL, length and label should be addresses to which the client has write access, otherwise
            undefined behavior, including process termination may occur.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetObjectPtrLabel.xhtml
        """
        pass

    def get_pointerv(self, pname: int, params: POINTER(c_void_p)):
        """
        Return the address of the specified pointer

        Wrapper for glGetPointerv

        Parameters
        ----------
        pname: int
            Specifies the pointer to be returned. Must be one of GL_DEBUG_CALLBACK_FUNCTION or
            GL_DEBUG_CALLBACK_USER_PARAM.
        params: POINTER(c_void_p)
            Returns the pointer value specified by pname.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetPointerv.xhtml
        """
        pass

    def get_program_interfaceiv(self, program: int, program_interface: int, pname: int, params: POINTER(c_int)):
        """
        Query a property of an interface in a program

        Wrapper for glGetProgramInterfaceiv

        Parameters
        ----------
        program: int
            The name of a program object whose interface to query.
        pname: int
            The name of the parameter within programInterface to query.
        params: POINTER(c_int)
            The address of a variable to retrieve the value of pname for the program interface.

        Raises
        ------
        GL_INVALID_ENUM is generated if identifier is not one of the accepted object types.
        GL_INVALID_VALUE is generated if program is not the name of an existing sync object.
        GL_INVALID_VALUE is generated if bufSize is zero.
        GL_INVALID_OPERATION is generated if pname is GL_MAX_NAME_LENGTH and programInterface is
            GL_ATOMIC_COUNTER_BUFFER or GL_TRANSFORM_FEEDBACK_BUFFER, since active atomic counter and transform
            feedback buffer resources are not assigned name strings.
        GL_INVALID_OPERATION error is generated if pname is GL_MAX_NUM_ACTIVE_VARIABLES and
            programInterface is not GL_UNIFORM_BLOCK, GL_SHADER_STORAGE_BLOCK, GL_ATOMIC_COUNTER_BUFFER, or
            GL_TRANSFORM_FEEDBACK_BUFFER.
        If not NULL, length and label should be addresses to which the client has write access, otherwise
            undefined behavior, including process termination may occur.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramInterface.xhtml
        """
        pass

    def get_program_resourceiv(self, program: int, program_interface: int, index: int, prop_count: int, props: POINTER(c_uint32), buf_size: int, length: POINTER(c_uint32), params: POINTER(c_int)):
        """
        Retrieve values for multiple properties of a single active resource within a program object

        Wrapper for glGetProgramResourceiv

        Parameters
        ----------
        program: int
            The name of a program object whose resources to query.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.
        GL_INVALID_VALUE is generated if propCount is zero.
        GL_INVALID_ENUM is generated if programInterface is not one of the accepted interface types.
        GL_INVLALID_ENUM is generated if any value in props is not one of the accepted tokens for the
            interface programInterface

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramResource.xhtml
        """
        pass

    def get_program_resource_index(self, program: int, program_interface: int, name: bytes) -> int:
        """
        Query the index of a named resource within a program

        Wrapper for glGetProgramResourceIndex

        Parameters
        ----------
        program: int
            The name of a program object whose resources to query.
        name: bytes
            The name of the resource to query the index of.

        Raises
        ------
        GL_INVALID_ENUM is generated if programInterface is not one of the accepted interface types.
        GL_INVALID_ENUM is generated if programInterface is GL_ATOMIC_COUNTER_BUFFER or
            GL_TRANSFORM_FEEDBACK_BUFFER, since active atomic counter and transform feedback buffer resources
            are not assigned name strings.
        Although not an error, GL_INVALID_INDEX is returned if name is not the name of a resource within
            the interface identified by programInterface.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramResourceIndex.xhtml
        """
        pass

    def get_program_resource_location(self, program: int, program_interface: int, name: bytes) -> int:
        """
        Query the location of a named resource within a program

        Wrapper for glGetProgramResourceLocation

        Parameters
        ----------
        program: int
            The name of a program object whose resources to query.
        name: bytes
            The name of the resource to query the location of.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.
        GL_INVALID_ENUM is generated if programInterface is not one of the accepted interface types.
        GL_INVALID_OPERATION is generated if program has not been linked successfully.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramResourceLocation.xhtml
        """
        pass

    def get_program_resource_location_index(self, program: int, program_interface: int, name: bytes) -> int:
        """
        Query the fragment color index of a named variable within a program

        Wrapper for glGetProgramResourceLocationIndex

        Parameters
        ----------
        program: int
            The name of a program object whose resources to query.
        name: bytes
            The name of the resource to query the location of.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not the name of an existing program object.
        GL_INVALID_ENUM is generated if programInterface is not one of the accepted interface types.
        GL_INVALID_OPERATION is generated if program has not been linked successfully.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramResourceLocationIndex.xhtml
        """
        pass

    def get_program_resource_name(self, program: int, program_interface: int, index: int, buf_size: int, length: POINTER(c_uint32), name: bytes):
        """
        Query the name of an indexed resource within a program

        Wrapper for glGetProgramResourceName

        Parameters
        ----------
        program: int
            The name of a program object whose resources to query.
        index: int
            The index of the resource within programInterface of program.
        length: POINTER(c_uint32)
            The address of a variable which will receive the length of the resource name.
        name: bytes
            The address of a character array into which will be written the name of the resource.

        Raises
        ------
        GL_INVALID_ENUM is generated if programInterface is not one of the accepted interface types.
        GL_INVALID_VALUE is generated if progam is not the name of an existing program.
        GL_INVALID_VALUE is generated if index is greater than or equal to the number of entries in the
            active resource list for programInterface.
        GL_INVALID_ENUM is generated if programInterface is GL_ATOMIC_COUNTER_BUFFER or
            GL_TRANSFORM_FEEDBACK_BUFFER, since active atomic counter and transform feedback buffer resources
            are not assigned name strings.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramResourceName.xhtml
        """
        pass

    def invalidate_buffer_data(self, buffer: int):
        """
        Invalidate the content of a buffer object's data store

        Wrapper for glInvalidateBufferData

        Parameters
        ----------
        buffer: int
            The name of a buffer object whose data store to invalidate.

        Raises
        ------
        GL_INVALID_VALUE is generated if buffer is not the name of an existing buffer object.
        GL_INVALID_OPERATION is generated if any part of buffer is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateBufferData.xhtml
        """
        pass

    def invalidate_buffer_sub_data(self, buffer: int, offset: POINTER(c_int), length: POINTER(c_uint32)):
        """
        Invalidate a region of a buffer object's data store

        Wrapper for glInvalidateBufferSubData

        Parameters
        ----------
        buffer: int
            The name of a buffer object, a subrange of whose data store to invalidate.
        offset: POINTER(c_int)
            The offset within the buffer's data store of the start of the range to be invalidated.
        length: POINTER(c_uint32)
            The length of the range within the buffer's data store to be invalidated.

        Raises
        ------
        GL_INVALID_VALUE is generated if offset or length is negative, or if offset + length is greater
            than the value of GL_BUFFER_SIZE for buffer.
        GL_INVALID_VALUE is generated if buffer is not the name of an existing buffer object.
        GL_INVALID_OPERATION is generated if any part of buffer is currently mapped.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateBufferSubData.xhtml
        """
        pass

    def invalidate_framebuffer(self, target: int, num_attachments: int, attachments: POINTER(c_uint32)):
        """
        Invalidate the content of some or all of a framebuffer's attachments

        Wrapper for glInvalidateFramebuffer

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer object is attached for glInvalidateFramebuffer.
        attachments: POINTER(c_uint32)
            Specifies a pointer to an array identifying the attachments to be invalidated.

        Raises
        ------
        GL_INVALID_ENUM is generated by glInvalidateFramebuffer if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glInvalidateNamedFramebufferData if framebuffer is not zero or
            the name of an existing framebuffer object.
        GL_INVALID_VALUE is generated if numAttachments is negative.
        GL_INVALID_ENUM is generated if any element of attachments is not one of the accepted framebuffer
            attachment points, as described above.
        GL_INVALID_OPERATION is generated if element of attachments is GL_COLOR_ATTACHMENT m where m is
            greater than or equal to the value of GL_MAX_COLOR_ATTACHMENTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateFramebuffer.xhtml
        """
        pass

    def invalidate_sub_framebuffer(self, target: int, num_attachments: int, attachments: POINTER(c_uint32), x: int, y: int, width: int, height: int):
        """
        Invalidate the content of a region of some or all of a framebuffer's attachments

        Wrapper for glInvalidateSubFramebuffer

        Parameters
        ----------
        target: int
            Specifies the target to which the framebuffer object is attached for glInvalidateSubFramebuffer.
        attachments: POINTER(c_uint32)
            Specifies a pointer to an array identifying the attachments to be invalidated.
        x: int
            Specifies the X offset of the region to be invalidated.
        y: int
            Specifies the Y offset of the region to be invalidated.
        width: int
            Specifies the width of the region to be invalidated.
        height: int
            Specifies the height of the region to be invalidated.

        Raises
        ------
        GL_INVALID_ENUM by glInvalidateSubFramebuffer if target is not one of the accepted framebuffer
            targets.
        GL_INVALID_OPERATION by glInvalidateNamedFramebufferSubData if framebuffer is not zero of the name
            of an existing framebuffer object.
        GL_INVALID_VALUE is generated if numAttachments, width or height is negative.
        GL_INVALID_ENUM is generated if any element of attachments is not one of the accepted framebuffer
            attachment points, as described above.
        GL_INVALID_OPERATION is generated if element of attachments is GL_COLOR_ATTACHMENT m where m is
            greater than or equal to the value of GL_MAX_COLOR_ATTACHMENTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateSubFramebuffer.xhtml
        """
        pass

    def invalidate_tex_image(self, texture: int, level: int):
        """
        Invalidate the entirety a texture image

        Wrapper for glInvalidateTexImage

        Parameters
        ----------
        texture: int
            The name of a texture object to invalidate.
        level: int
            The level of detail of the texture object to invalidate.

        Raises
        ------
        GL_INVALID_VALUE is generated if level is less than zero or if it is greater or equal to the base 2
            logarithm of the maximum texture width, height, or depth.
        GL_INVALID_VALUE is generated if the target of texture is any of GL_TEXTURE_RECTANGLE,
            GL_TEXTURE_BUFFER, GL_TEXTURE_2D_MULTISAMPLE, or GL_TEXTURE_2D_MULTISAMPLE_ARRAY and level is not
            zero.
        GL_INVALID_VALUE is generated if texture is not the name of an existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateTexImage.xhtml
        """
        pass

    def invalidate_tex_sub_image(self, texture: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int):
        """
        Invalidate a region of a texture image

        Wrapper for glInvalidateTexSubImage

        Parameters
        ----------
        texture: int
            The name of a texture object a subregion of which to invalidate.
        level: int
            The level of detail of the texture object within which the region resides.
        xoffset: int
            The X offset of the region to be invalidated.
        yoffset: int
            The Y offset of the region to be invalidated.
        zoffset: int
            The Z offset of the region to be invalidated.
        width: int
            The width of the region to be invalidated.
        height: int
            The height of the region to be invalidated.
        depth: int
            The depth of the region to be invalidated.

        Raises
        ------
        GL_INVALID_VALUE is generated if xoffset, yoffset or zoffset is less than zero, or if any of them
            is greater than the size of the image in the corresponding dimension.
        GL_INVALID_VALUE is generated if level is less than zero or if it is greater or equal to the base 2
            logarithm of the maximum texture width, height, or depth.
        GL_INVALID_VALUE is generated if the target of texture is any of GL_TEXTURE_RECTANGLE,
            GL_TEXTURE_BUFFER, GL_TEXTURE_2D_MULTISAMPLE, or GL_TEXTURE_2D_MULTISAMPLE_ARRAY and level is not
            zero.
        GL_INVALID_VALUE is generated if texture is not the name of an existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateTexSubImage.xhtml
        """
        pass

    def multi_draw_arrays_indirect(self, mode: int, indirect: c_void_p, drawcount: int, stride: int):
        """
        Render multiple sets of primitives from array data, taking parameters from memory

        Wrapper for glMultiDrawArraysIndirect

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        indirect: c_void_p
            Specifies the address of an array of structures containing the draw parameters.
        drawcount: int
            Specifies the the number of elements in the array of draw parameter structures.
        stride: int
            Specifies the distance in basic machine units between elements of the draw parameter array.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if stride is not a multiple of four.
        GL_INVALID_VALUE is generated if drawcount is negative.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            to the GL_DRAW_INDIRECT_BUFFER binding and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMultiDrawArraysIndirect.xhtml
        """
        pass

    def multi_draw_elements_indirect(self, mode: int, type: int, indirect: c_void_p, drawcount: int, stride: int):
        """
        Render indexed primitives from array data, taking parameters from memory

        Wrapper for glMultiDrawElementsIndirect

        Parameters
        ----------
        mode: int
            Specifies what kind of primitives to render. Symbolic constants GL_POINTS, GL_LINE_STRIP,
            GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP,
            GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY, and GL_PATCHES
            are accepted.
        type: int
            Specifies the type of data in the buffer bound to the GL_ELEMENT_ARRAY_BUFFER binding.
        indirect: c_void_p
            Specifies the address of a structure containing an array of draw parameters.
        drawcount: int
            Specifies the number of elements in the array addressed by indirect.
        stride: int
            Specifies the distance in basic machine units between elements of the draw parameter array.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not an accepted value.
        GL_INVALID_VALUE is generated if stride is not a multiple of four.
        GL_INVALID_VALUE is generated if drawcount is negative.
        GL_INVALID_OPERATION is generated if no buffer is bound to the GL_ELEMENT_ARRAY_BUFFER binding, or
            if such a buffer's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to an enabled array or
            to the GL_DRAW_INDIRECT_BUFFER binding and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a geometry shader is active and mode is incompatible with the
            input primitive type of the geometry shader in the currently installed program object.
        GL_INVALID_OPERATION is generated if mode is GL_PATCHES and no tessellation control shader is
            active.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMultiDrawElementsIndirect.xhtml
        """
        pass

    def object_label(self, identifier: int, name: int, length: int, label: bytes):
        """
        Label a named object identified within a namespace

        Wrapper for glObjectLabel

        Parameters
        ----------
        identifier: int
            The namespace from which the name of the object is allocated.
        name: int
            The name of the object to label.
        length: int
            The length of the label to be used for the object.
        label: bytes
            The address of a string containing the label to assign to the object.

        Raises
        ------
        GL_INVALID_ENUM is generated if identifier is not one of the accepted object types.
        GL_INVALID_OPERATION is generated if name is not the name of an existing object of the type
            specified by identifier.
        GL_INVALID_VALUE is generated if the number of characters in label, excluding the null terminator
            when length is negative, is greater than the value of GL_MAX_LABEL_LENGTH.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glObjectLabel.xhtml
        """
        pass

    def object_ptr_label(self, ptr: c_void_p, length: int, label: bytes):
        """
        Label a a sync object identified by a pointer

        Wrapper for glObjectPtrLabel

        Parameters
        ----------
        ptr: c_void_p
            A pointer identifying a sync object.
        length: int
            The length of the label to be used for the object.
        label: bytes
            The address of a string containing the label to assign to the object.

        Raises
        ------
        GL_INVALID_VALUE is generated if ptr is not a valid sync object.
        GL_INVALID_VALUE is generated if the number of characters in label, excluding the null terminator
            when length is negative, is greater than the value of GL_MAX_LABEL_LENGTH.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glObjectPtrLabel.xhtml
        """
        pass

    def pop_debug_group(self):
        """
        Pop the active debug group

        Wrapper for glPopDebugGroup

        Raises
        ------
        GL_STACK_UNDERFLOW is generated if an attempt is made to pop the default debug group from the
            stack.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPopDebugGroup.xhtml
        """
        pass

    def push_debug_group(self, source: int, id: int, length: int, message: bytes):
        """
        Push a named debug group into the command stream

        Wrapper for glPushDebugGroup

        Parameters
        ----------
        source: int
            The source of the debug message.
        id: int
            The identifier of the message.
        length: int
            The length of the message to be sent to the debug output stream.
        message: bytes
            The a string containing the message to be sent to the debug output stream.

        Raises
        ------
        GL_INVALID_ENUM is generated if the value of source is neither GL_DEBUG_SOURCE_APPLICATION nor
            GL_DEBUG_SOURCE_THIRD_PARTY.
        GL_INVALID_VALUE is generated if length is negative and the number of characters in message,
            excluding the null-terminator, is not less than the value of GL_MAX_DEBUG_MESSAGE_LENGTH.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glPushDebugGroup.xhtml
        """
        pass

    def shader_storage_block_binding(self, program: int, storage_block_index: int, storage_block_binding: int):
        """
        Change an active shader storage block binding

        Wrapper for glShaderStorageBlockBinding

        Parameters
        ----------
        program: int
            The name of the program containing the block whose binding to change.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not the name of either a program or shader object.
        GL_INVALID_OPERATION is generated if program is the name of a shader object.
        GL_INVALID_VALUE is generated if storageBlockIndex is not an active shader storage block index in
            program, or if storageBlockBinding is greater than or equal to the value of
            MAX_SHADER_STORAGE_BUFFER_BINDINGS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glShaderStorageBlockBinding.xhtml
        """
        pass

    def tex_buffer_range(self, target: int, internal_format: int, buffer: int, offset: POINTER(c_int), size: POINTER(c_uint32)):
        """
        Attach a range of a buffer object's data store to a buffer texture object

        Wrapper for glTexBufferRange

        Parameters
        ----------
        target: int
            Specifies the target to which the texture object is bound for glTexBufferRange. Must be
            GL_TEXTURE_BUFFER.
        buffer: int
            Specifies the name of the buffer object whose storage to attach to the active buffer texture.
        offset: POINTER(c_int)
            Specifies the offset of the start of the range of the buffer's data store to attach.
        size: POINTER(c_uint32)
            Specifies the size of the range of the buffer's data store to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexBufferRange if target is not GL_TEXTURE_BUFFER.
        GL_INVALID_OPERATION is generated by glTextureBufferRange if texture is not the name of an existing
            texture object.
        GL_INVALID_ENUM is generated by glTextureBufferRange if the effective target of texture is not
            GL_TEXTURE_BUFFER.
        GL_INVALID_ENUM is generated if internalformat is not one of the sized internal formats described
            above.
        GL_INVALID_OPERATION is generated if buffer is not zero and is not the name of an existing buffer
            object.
        GL_INVALID_VALUE is generated if offset is negative, if size is less than or equal to zero, or if
            offset + size is greater than the value of GL_BUFFER_SIZE for buffer.
        GL_INVALID_VALUE is generated if offset is not an integer multiple of the value of
            GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexBufferRange.xhtml
        """
        pass

    def texture_view(self, texture: int, target: int, origtexture: int, internalformat: int, minlevel: int, numlevels: int, minlayer: int, numlayers: int):
        """
        Initialize a texture as a data alias of another texture's data store

        Wrapper for glTextureView

        Parameters
        ----------
        texture: int
            Specifies the texture object to be initialized as a view.
        target: int
            Specifies the target to be used for the newly initialized texture.
        origtexture: int
            Specifies the name of a texture object of which to make a view.
        minlevel: int
            Specifies lowest level of detail of the view.
        numlevels: int
            Specifies the number of levels of detail to include in the view.
        minlayer: int
            Specifies the index of the first layer to include in the view.
        numlayers: int
            Specifies the number of layers to include in the view.

        Raises
        ------
        GL_INVALID_VALUE is generated if minlayer or minlevel are larger than the greatest layer or level
            of origtexture.
        GL_INVALID_OPERATION is generated if target is not compatible with the target of origtexture.
        GL_INVALID_OPERATION is generated if the dimensions of origtexture are greater than the maximum
            supported dimensions for target.
        GL_INVALID_OPERATION is generated if internalformat is not compatible with the internal format of
            origtexture.
        GL_INVALID_OPERATION is generated if texture has already been bound or otherwise given a target.
        GL_INVALID_OPERATION is generated if the value of GL_TEXTURE_IMMUTABLE_FORMAT for origtexture is
            not GL_TRUE.
        GL_INVALID_OPERATION is generated if origtexture is not the name of an existing texture object.
        GL_INVALID_VALUE is generaged if target is GL_TEXTURE_CUBE_MAP and numlayers is not 6, or if target
            is GL_TEXTURE_CUBE_MAP_ARRAY and numlayers is not an integer multiple of 6.
        GL_INVALID_VALUE is generated if target is GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D,
            GL_TEXTURE_RECTANGLE, or GL_TEXTURE_2D_MULTISAMPLE and numlayers does not equal 1.
        GL_INVALID_VALUE is generated if texture zero or is not the name of a texture previously returned
            from a successful call to glGenTextures.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTextureView.xhtml
        """
        pass

    def vertex_attrib_binding(self, attribindex: int, bindingindex: int):
        """
        Associate a vertex attribute and a vertex buffer binding for a vertex array object

        Wrapper for glVertexAttribBinding

        Parameters
        ----------
        attribindex: int
            The index of the attribute to associate with a vertex buffer binding.
        bindingindex: int
            The index of the vertex buffer binding with which to associate the generic vertex attribute.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glVertexAttribBinding if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribBinding if vaobj is not the name of an
            existing vertex array object.
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if bindingindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribBinding.xhtml
        """
        pass

    def vertex_attrib_format(self, attribindex: int, size: int, type: int, normalized: bool, relativeoffset: int):
        """
        Specify the organization of vertex arrays

        Wrapper for glVertexAttribFormat

        Parameters
        ----------
        attribindex: int
            The generic vertex attribute array being described.
        size: int
            The number of values per vertex that are stored in the array.
        type: int
            The type of the data stored in the array.
        normalized: bool
            Specifies whether fixed-point data values should be normalized (GL_TRUE) or converted directly as
            fixed-point values (GL_FALSE) when they are accessed. This parameter is ignored if type is
            GL_FIXED.
        relativeoffset: int
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not one of the accepted values.
        GL_INVALID_VALUE is generated if relativeoffset is greater than the value of
            GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET.
        GL_INVALID_ENUM is generated if type is not one of the accepted tokens.
        GL_INVALID_ENUM is generated by glVertexAttribIFormat, glVertexAttribLFormat,
            glVertexArrayAttribIFormat and glVertexArrayAttribLFormat if type is
            GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_OPERATION is generated by glVertexAttribFormat, glVertexAttribIFormat and
            glVertexAttribLFormat if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribFormat, glVertexArrayAttribIFormat and
            glVertexArrayAttribLFormat if vaobj is not the name of an existing vertex array object.
        GL_INVALID_OPERATION is generated under any of the following conditions:
        size is GL_BGRA and type is not GL_UNSIGNED_BYTE, GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV.
        type is GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, and size is neither 4 nor GL_BGRA.
        type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        size is GL_BGRA and normalized is GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribFormat.xhtml
        """
        pass

    def vertex_attrib_iformat(self, attribindex: int, size: int, type: int, relativeoffset: int):
        """
        Specify the organization of vertex arrays

        Wrapper for glVertexAttribIFormat

        Parameters
        ----------
        attribindex: int
            The generic vertex attribute array being described.
        size: int
            The number of values per vertex that are stored in the array.
        type: int
            The type of the data stored in the array.
        relativeoffset: int
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not one of the accepted values.
        GL_INVALID_VALUE is generated if relativeoffset is greater than the value of
            GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET.
        GL_INVALID_ENUM is generated if type is not one of the accepted tokens.
        GL_INVALID_ENUM is generated by glVertexAttribIFormat, glVertexAttribLFormat,
            glVertexArrayAttribIFormat and glVertexArrayAttribLFormat if type is
            GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_OPERATION is generated by glVertexAttribFormat, glVertexAttribIFormat and
            glVertexAttribLFormat if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribFormat, glVertexArrayAttribIFormat and
            glVertexArrayAttribLFormat if vaobj is not the name of an existing vertex array object.
        GL_INVALID_OPERATION is generated under any of the following conditions:
        size is GL_BGRA and type is not GL_UNSIGNED_BYTE, GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV.
        type is GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, and size is neither 4 nor GL_BGRA.
        type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        size is GL_BGRA and normalized is GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribFormat.xhtml
        """
        pass

    def vertex_attrib_lformat(self, attribindex: int, size: int, type: int, relativeoffset: int):
        """
        Specify the organization of vertex arrays

        Wrapper for glVertexAttribLFormat

        Parameters
        ----------
        attribindex: int
            The generic vertex attribute array being described.
        size: int
            The number of values per vertex that are stored in the array.
        type: int
            The type of the data stored in the array.
        relativeoffset: int
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not one of the accepted values.
        GL_INVALID_VALUE is generated if relativeoffset is greater than the value of
            GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET.
        GL_INVALID_ENUM is generated if type is not one of the accepted tokens.
        GL_INVALID_ENUM is generated by glVertexAttribIFormat, glVertexAttribLFormat,
            glVertexArrayAttribIFormat and glVertexArrayAttribLFormat if type is
            GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_OPERATION is generated by glVertexAttribFormat, glVertexAttribIFormat and
            glVertexAttribLFormat if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribFormat, glVertexArrayAttribIFormat and
            glVertexArrayAttribLFormat if vaobj is not the name of an existing vertex array object.
        GL_INVALID_OPERATION is generated under any of the following conditions:
        size is GL_BGRA and type is not GL_UNSIGNED_BYTE, GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV.
        type is GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, and size is neither 4 nor GL_BGRA.
        type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        size is GL_BGRA and normalized is GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribFormat.xhtml
        """
        pass

    def vertex_binding_divisor(self, bindingindex: int, divisor: int):
        """
        Modify the rate at which generic vertex attributes advance

        Wrapper for glVertexBindingDivisor

        Parameters
        ----------
        bindingindex: int
            The index of the binding whose divisor to modify.
        divisor: int
            The new value for the instance step rate to apply.

        Raises
        ------
        GL_INVALID_VALUE is generated if bindingindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.
        GL_INVALID_OPERATION by glVertexBindingDivisor is generated if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayBindingDivisor if vaobj is not the name of an
            existing vertex array object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexBindingDivisor.xhtml
        """
        pass

class GL44(GL43):

    MAJOR = 4
    MINOR = 4

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.bind_buffers_base, 'glBindBuffersBase',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint))
        self._load(self.bind_buffers_range, 'glBindBuffersRange',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint), POINTER(POINTER(c_int)), POINTER(POINTER(c_int)))
        self._load(self.bind_image_textures, 'glBindImageTextures',
                   None, c_uint, c_uint32, POINTER(c_uint))
        self._load(self.bind_samplers, 'glBindSamplers',
                   None, c_uint, c_uint32, POINTER(c_uint))
        self._load(self.bind_textures, 'glBindTextures',
                   None, c_uint, c_uint32, POINTER(c_uint))
        self._load(self.bind_vertex_buffers, 'glBindVertexBuffers',
                   None, c_uint, c_uint32, POINTER(c_uint), POINTER(POINTER(c_int)), POINTER(c_uint32))
        self._load(self.buffer_storage, 'glBufferStorage',
                   None, c_uint, POINTER(c_uint32), c_void_p, c_uint32)
        self._load(self.clear_tex_image, 'glClearTexImage',
                   None, c_uint, c_int, c_uint, c_uint, c_void_p)
        self._load(self.clear_tex_sub_image, 'glClearTexSubImage',
                   None, c_uint, c_int, c_int, c_int, c_int, c_uint32, c_uint32, c_uint32, c_uint, c_uint, c_void_p)

    def bind_buffers_base(self, target: int, first: int, count: int, buffers: POINTER(c_uint)):
        """
        Bind one or more buffer objects to a sequence of indexed buffer targets

        Wrapper for glBindBuffersBase

        Parameters
        ----------
        target: int
            Specify the target of the bind operation. target must be one of GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER or GL_SHADER_STORAGE_BUFFER.
        count: int
            Specify the number of contiguous binding points to which to bind buffers.
        buffers: POINTER(c_uint)
            A pointer to an array of names of buffer objects to bind to the targets on the specified binding
            point, or NULL.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER or GL_SHADER_STORAGE_BUFFER.
        GL_INVALID_OPERATION is generated if first + count is greater than the number of target-specific
            indexed binding points.
        GL_INVALID_OPERATION is generated if any value in buffers is not zero or the name of an existing
            buffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindBuffersBase.xhtml
        """
        pass

    def bind_buffers_range(self, target: int, first: int, count: int, buffers: POINTER(c_uint), offsets: POINTER(POINTER(c_int)), sizes: POINTER(POINTER(c_int))):
        """
        Bind ranges of one or more buffer objects to a sequence of indexed buffer targets

        Wrapper for glBindBuffersRange

        Parameters
        ----------
        target: int
            Specify the target of the bind operation. target must be one of GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER or GL_SHADER_STORAGE_BUFFER.
        count: int
            Specify the number of contiguous binding points to which to bind buffers.
        buffers: POINTER(c_uint)
            A pointer to an array of names of buffer objects to bind to the targets on the specified binding
            point, or NULL.
        offsets: POINTER(POINTER(c_int))
            A pointer to an array of offsets into the corresponding buffer in buffers to bind, or NULL if
            buffers is NULL.
        sizes: POINTER(POINTER(c_int))
            A pointer to an array of sizes of the corresponding buffer in buffers to bind, or NULL if buffers
            is NULL.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_ATOMIC_COUNTER_BUFFER,
            GL_TRANSFORM_FEEDBACK_BUFFER, GL_UNIFORM_BUFFER or GL_SHADER_STORAGE_BUFFER.
        GL_INVALID_OPERATION is generated if first + count is greater than the number of target-specific
            indexed binding points.
        GL_INVALID_OPERATION is generated if any value in buffers is not zero or the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated by if any value in offsets is less than zero or if any value in sizes
            is less than zero.
        GL_INVALID_VALUE is generated if any pair of values in offsets and sizes does not respectively
            satisfy the constraints described for those parameters for the specified target.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindBuffersRange.xhtml
        """
        pass

    def bind_image_textures(self, first: int, count: int, textures: POINTER(c_uint)):
        """
        Bind one or more named texture images to a sequence of consecutive image units

        Wrapper for glBindImageTextures

        Parameters
        ----------
        first: int
            Specifies the first image unit to which a texture is to be bound.
        count: int
            Specifies the number of textures to bind.
        textures: POINTER(c_uint)
            Specifies the address of an array of names of existing texture objects.

        Raises
        ------
        GL_INVALID_OPERATION is generated if first + count is greater than the number of image units
            supported by the implementation.
        GL_INVALID_OPERATION is generated if any value in textures is not zero or the name of an existing
            texture object.
        GL_INVALID_OPERATION error is generated if the internal format of the level zero texture image of
            any texture in textures is not supported.
        GL_INVALID_OPERATION error is generated if the width, height, or depth of the level zero texture
            image of any texture in textures is zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindImageTextures.xhtml
        """
        pass

    def bind_samplers(self, first: int, count: int, samplers: POINTER(c_uint)):
        """
        Bind one or more named sampler objects to a sequence of consecutive sampler units

        Wrapper for glBindSamplers

        Parameters
        ----------
        first: int
            Specifies the first sampler unit to which a sampler object is to be bound.
        count: int
            Specifies the number of samplers to bind.
        samplers: POINTER(c_uint)
            Specifies the address of an array of names of existing sampler objects.

        Raises
        ------
        GL_INVALID_OPERATION is generated if first + count is greater than the number of sampler units
            supported by the implementation.
        GL_INVALID_OPERATION is generated if any value in samplers is not zero or the name of an existing
            sampler object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindSamplers.xhtml
        """
        pass

    def bind_textures(self, first: int, count: int, textures: POINTER(c_uint)):
        """
        Bind one or more named textures to a sequence of consecutive texture units

        Wrapper for glBindTextures

        Parameters
        ----------
        first: int
            Specifies the first texture unit to which a texture is to be bound.
        count: int
            Specifies the number of textures to bind.
        textures: POINTER(c_uint)
            Specifies the address of an array of names of existing texture objects.

        Raises
        ------
        GL_INVALID_OPERATION is generated if first + count is greater than the number of texture image
            units supported by the implementation.
        GL_INVALID_OPERATION is generated if any value in textures is not zero or the name of an existing
            texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindTextures.xhtml
        """
        pass

    def bind_vertex_buffers(self, first: int, count: int, buffers: POINTER(c_uint), offsets: POINTER(POINTER(c_int)), strides: POINTER(c_uint32)):
        """
        Attach multiple buffer objects to a vertex array object

        Wrapper for glBindVertexBuffers

        Parameters
        ----------
        first: int
            Specifies the first vertex buffer binding point to which a buffer object is to be bound.
        count: int
            Specifies the number of buffers to bind.
        buffers: POINTER(c_uint)
            Specifies the address of an array of strides to associate with the binding points.
        offsets: POINTER(POINTER(c_int))
            Specifies the address of an array of offsets to associate with the binding points.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glBindVertexBuffers if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayVertexBuffers if vaobj is not the name of the
            vertex array object.
        GL_INVALID_OPERATION is generated if $first + count$ is greater than the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.
        GL_INVALID_OPERATION is generated if any value in buffers is not zero or the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if any value in offsets or strides is negative, or if a value is
            stride is greater than the value of GL_MAX_VERTEX_ATTRIB_STRIDE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindVertexBuffers.xhtml
        """
        pass

    def buffer_storage(self, target: int, size: POINTER(c_uint32), data: c_void_p, flags: int):
        """
        Creates and initializes a buffer object's immutable data store

        Wrapper for glBufferStorage

        Parameters
        ----------
        target: int
            Specifies the target to which the buffer object is bound for glBufferStorage, which must be one of
            the buffer binding targets in the following table: Buffer Binding Target Purpose GL_ARRAY_BUFFER
            Vertex attributes GL_ATOMIC_COUNTER_BUFFER Atomic counter storage GL_COPY_READ_BUFFER Buffer copy
            source GL_COPY_WRITE_BUFFER Buffer copy destination GL_DISPATCH_INDIRECT_BUFFER Indirect compute
            dispatch commands GL_DRAW_INDIRECT_BUFFER Indirect command arguments GL_ELEMENT_ARRAY_BUFFER Vertex
            array indices GL_PIXEL_PACK_BUFFER Pixel read target GL_PIXEL_UNPACK_BUFFER Texture data source
            GL_QUERY_BUFFER Query result buffer GL_SHADER_STORAGE_BUFFER Read-write storage for shaders
            GL_TEXTURE_BUFFER Texture data buffer GL_TRANSFORM_FEEDBACK_BUFFER Transform feedback buffer
            GL_UNIFORM_BUFFER Uniform block storage
        size: POINTER(c_uint32)
            Specifies the size in bytes of the buffer object's new data store.
        data: c_void_p
            Specifies a pointer to data that will be copied into the data store for initialization, or NULL if
            no data is to be copied.
        flags: int
            Specifies the intended usage of the buffer's data store. Must be a bitwise combination of the
            following flags. GL_DYNAMIC_STORAGE_BIT, GL_MAP_READ_BIT GL_MAP_WRITE_BIT, GL_MAP_PERSISTENT_BIT,
            GL_MAP_COHERENT_BIT, and GL_CLIENT_STORAGE_BIT.

        Raises
        ------
        GL_INVALID_ENUM is generated by glBufferStorage if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glNamedBufferStorage if buffer is not the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if size is less than or equal to zero.
        GL_INVALID_OPERATION is generated by glBufferStorage if the reserved buffer object name 0 is bound
            to target.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store with the properties
            requested in flags.
        GL_INVALID_VALUE is generated if flags has any bits set other than those defined above.
        GL_INVALID_VALUE error is generated if flags contains GL_MAP_PERSISTENT_BIT but does not contain at
            least one of GL_MAP_READ_BIT or GL_MAP_WRITE_BIT.
        GL_INVALID_VALUE is generated if flags contains GL_MAP_COHERENT_BIT, but does not also contain
            GL_MAP_PERSISTENT_BIT.
        GL_INVALID_OPERATION is generated by glBufferStorage if the GL_BUFFER_IMMUTABLE_STORAGE flag of the
            buffer bound to target is GL_TRUE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBufferStorage.xhtml
        """
        pass

    def clear_tex_image(self, texture: int, level: int, format: int, type: int, data: c_void_p):
        """
        Fills all a texture image with a constant value

        Wrapper for glClearTexImage

        Parameters
        ----------
        texture: int
            The name of an existing texture object containing the image to be cleared.
        level: int
            The level of texture containing the region to be cleared.
        format: int
            The format of the data whose address in memory is given by data.
        type: int
            The type of the data whose address in memory is given by data.
        data: c_void_p
            The address in memory of the data to be used to clear the specified region.

        Raises
        ------
        GL_INVALID_OPERATION is generated if texture is zero or not the name of an existing texture object.
        GL_INVALID_OPERATION is generated if texture is a buffer texture.
        GL_INVALID_OPERATION is generated if texture has a compressed internal format.
        GL_INVALID_OPERATION is generated if the base internal format is GL_DEPTH_COMPONENT and format is
            not GL_DEPTH_COMPONENT.
        GL_INVALID_OPERATION is generated if the base internal format is GL_DEPTH_STENCIL and format is not
            GL_DEPTH_STENCIL.
        GL_INVALID_OPERATION is generated if the base internal format is GL_STENCIL_INDEX and format is not
            GL_STENCIL_INDEX.
        GL_INVALID_OPERATION is generated if the base internal format is GL_RGBA and format is
            GL_DEPTH_COMPONENT, GL_STENCIL_INDEX, or GL_DEPTH_STENCIL.
        GL_INVALID_OPERATION is generated if the internal format is integer and format does not specify
            integer data.
        GL_INVALID_OPERATION is generated if the internal format is not integer and format specifies
            integer data.
        GL_INVALID_OPERATION is generated if the image array identified by level has not previously been
            defined by a call to glTexImage* or glTexStorage*.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearTexImage.xhtml
        """
        pass

    def clear_tex_sub_image(self, texture: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, type: int, data: c_void_p):
        """
        Fills all or part of a texture image with a constant value

        Wrapper for glClearTexSubImage

        Parameters
        ----------
        texture: int
            The name of an existing texture object containing the image to be cleared.
        level: int
            The level of texture containing the region to be cleared.
        xoffset: int
            The coordinate of the left edge of the region to be cleared.
        yoffset: int
            The coordinate of the lower edge of the region to be cleared.
        zoffset: int
            The coordinate of the front of the region to be cleared.
        width: int
            The width of the region to be cleared.
        height: int
            The height of the region to be cleared.
        depth: int
            The depth of the region to be cleared.
        format: int
            The format of the data whose address in memory is given by data.
        type: int
            The type of the data whose address in memory is given by data.
        data: c_void_p
            The address in memory of the data to be used to clear the specified region.

        Raises
        ------
        GL_INVALID_OPERATION is generated if texture is zero or not the name of an existing texture object.
        GL_INVALID_OPERATION is generated if texture is a buffer texture.
        GL_INVALID_OPERATION is generated if texture has a compressed internal format.
        GL_INVALID_OPERATION is generated if the base internal format is GL_DEPTH_COMPONENT and format is
            not GL_DEPTH_COMPONENT.
        GL_INVALID_OPERATION is generated if the base internal format is GL_DEPTH_STENCIL and format is not
            GL_DEPTH_STENCIL.
        GL_INVALID_OPERATION is generated if the base internal format is GL_STENCIL_INDEX and format is not
            GL_STENCIL_INDEX.
        GL_INVALID_OPERATION is generated if the base internal format is GL_RGBA and format is
            GL_DEPTH_COMPONENT, GL_STENCIL_INDEX, or GL_DEPTH_STENCIL.
        GL_INVALID_OPERATION is generated if the internal format is integer and format does not specify
            integer data.
        GL_INVALID_OPERATION is generated if the internal format is not integer and format specifies
            integer data.
        GL_INVALID_OPERATION error is generated if the xoffset, yoffset, zoffset, width, height, and depth
            parameters (or combinations thereof) specify a region that falls outside the defined texture image
            array (including border, if any).

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearTexSubImage.xhtml
        """
        pass

class GL45(GL44):

    MAJOR = 4
    MINOR = 5

    def __init__(self, glfw: GLFW):
        super().__init__(glfw)

        self._load(self.bind_texture_unit, 'glBindTextureUnit',
                   None, c_uint, c_uint)
        self._load(self.vertex_array_vertex_buffer, 'glVertexArrayVertexBuffer',
                   None, c_uint, c_uint, c_uint, POINTER(c_int), c_uint32)
        self._load(self.vertex_array_vertex_buffers, 'glVertexArrayVertexBuffers',
                   None, c_uint, c_uint, c_uint32, POINTER(c_uint), POINTER(POINTER(c_int)), POINTER(c_uint32))
        self._load(self.blit_named_framebuffer, 'glBlitNamedFramebuffer',
                   None, c_uint, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint32, c_uint)
        self._load(self.named_buffer_data, 'glNamedBufferData',
                   None, c_uint, c_uint32, c_void_p, c_uint)
        self._load(self.named_buffer_storage, 'glNamedBufferStorage',
                   None, c_uint, c_uint32, c_void_p, c_uint32)
        self._load(self.named_buffer_sub_data, 'glNamedBufferSubData',
                   None, c_uint, POINTER(c_int), c_uint32, c_void_p)
        self._load(self.check_named_framebuffer_status, 'glCheckNamedFramebufferStatus',
                   c_uint, c_uint, c_uint)
        self._load(self.clear_named_framebufferiv, 'glClearNamedFramebufferiv',
                   None, c_uint, c_uint, c_int, POINTER(c_int))
        self._load(self.clear_named_framebufferuiv, 'glClearNamedFramebufferuiv',
                   None, c_uint, c_uint, c_int, POINTER(c_uint))
        self._load(self.clear_named_framebufferfv, 'glClearNamedFramebufferfv',
                   None, c_uint, c_uint, c_int, POINTER(c_float))
        self._load(self.clear_named_framebufferfi, 'glClearNamedFramebufferfi',
                   None, c_uint, c_uint, c_int, c_float, c_int)
        self._load(self.clear_named_buffer_data, 'glClearNamedBufferData',
                   None, c_uint, c_uint, c_uint, c_uint, c_void_p)
        self._load(self.clear_named_buffer_sub_data, 'glClearNamedBufferSubData',
                   None, c_uint, c_uint, POINTER(c_int), c_uint32, c_uint, c_uint, c_void_p)
        self._load(self.clip_control, 'glClipControl',
                   None, c_uint, c_uint)
        self._load(self.copy_named_buffer_sub_data, 'glCopyNamedBufferSubData',
                   None, c_uint, c_uint, POINTER(c_int), POINTER(c_int), c_uint32)
        self._load(self.create_buffers, 'glCreateBuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.create_framebuffers, 'glCreateFramebuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.create_program_pipelines, 'glCreateProgramPipelines',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.create_queries, 'glCreateQueries',
                   None, c_uint, c_uint32, POINTER(c_uint))
        self._load(self.create_renderbuffers, 'glCreateRenderbuffers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.create_samplers, 'glCreateSamplers',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.create_textures, 'glCreateTextures',
                   None, c_uint, c_uint32, POINTER(c_uint))
        self._load(self.create_transform_feedbacks, 'glCreateTransformFeedbacks',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.create_vertex_arrays, 'glCreateVertexArrays',
                   None, c_uint32, POINTER(c_uint))
        self._load(self.named_framebuffer_draw_buffer, 'glNamedFramebufferDrawBuffer',
                   None, c_uint, c_uint)
        self._load(self.named_framebuffer_draw_buffers, 'glNamedFramebufferDrawBuffers',
                   None, c_uint, c_uint32, POINTER(c_uint32))
        self._load(self.enable_vertex_array_attrib, 'glEnableVertexArrayAttrib',
                   None, c_uint, c_uint)
        self._load(self.disable_vertex_array_attrib, 'glDisableVertexArrayAttrib',
                   None, c_uint, c_uint)
        self._load(self.flush_mapped_named_buffer_range, 'glFlushMappedNamedBufferRange',
                   None, c_uint, POINTER(c_int), c_uint32)
        self._load(self.named_framebuffer_parameteri, 'glNamedFramebufferParameteri',
                   None, c_uint, c_uint, c_int)
        self._load(self.named_framebuffer_renderbuffer, 'glNamedFramebufferRenderbuffer',
                   None, c_uint, c_uint, c_uint, c_uint)
        self._load(self.named_framebuffer_texture, 'glNamedFramebufferTexture',
                   None, c_uint, c_uint, c_uint, c_int)
        self._load(self.named_framebuffer_texture_layer, 'glNamedFramebufferTextureLayer',
                   None, c_uint, c_uint, c_uint, c_int, c_int)
        self._load(self.generate_texture_mipmap, 'glGenerateTextureMipmap',
                   None, c_uint)
        self._load(self.get_named_buffer_parameteriv, 'glGetNamedBufferParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_named_buffer_parameteri64v, 'glGetNamedBufferParameteri64v',
                   None, c_uint, c_uint, POINTER(c_int64))
        self._load(self.get_named_buffer_pointerv, 'glGetNamedBufferPointerv',
                   None, c_uint, c_uint, POINTER(c_void_p))
        self._load(self.get_named_buffer_sub_data, 'glGetNamedBufferSubData',
                   None, c_uint, POINTER(c_int), c_uint32, c_void_p)
        self._load(self.getn_compressed_tex_image, 'glGetnCompressedTexImage',
                   None, c_uint, c_int, c_uint32, c_void_p)
        self._load(self.get_compressed_texture_image, 'glGetCompressedTextureImage',
                   None, c_uint, c_int, c_uint32, c_void_p)
        self._load(self.get_compressed_texture_sub_image, 'glGetCompressedTextureSubImage',
                   None, c_uint, c_int, c_int, c_int, c_int, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p)
        self._load(self.get_named_framebuffer_attachment_parameteriv, 'glGetNamedFramebufferAttachmentParameteriv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_named_framebuffer_parameteriv, 'glGetNamedFramebufferParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_graphics_reset_status, 'glGetGraphicsResetStatus',
                   c_uint, )
        self._load(self.get_named_renderbuffer_parameteriv, 'glGetNamedRenderbufferParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.getn_tex_image, 'glGetnTexImage',
                   None, c_uint, c_int, c_uint, c_uint, c_uint32, c_void_p)
        self._load(self.get_texture_image, 'glGetTextureImage',
                   None, c_uint, c_int, c_uint, c_uint, c_uint32, c_void_p)
        self._load(self.get_texture_level_parameterfv, 'glGetTextureLevelParameterfv',
                   None, c_uint, c_int, c_uint, POINTER(c_float))
        self._load(self.get_texture_level_parameteriv, 'glGetTextureLevelParameteriv',
                   None, c_uint, c_int, c_uint, POINTER(c_int))
        self._load(self.get_texture_parameterfv, 'glGetTextureParameterfv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.get_texture_parameteriv, 'glGetTextureParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_texture_parameter_iiv, 'glGetTextureParameterIiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_texture_parameter_iuiv, 'glGetTextureParameterIuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.get_texture_sub_image, 'glGetTextureSubImage',
                   None, c_uint, c_int, c_int, c_int, c_int, c_uint32, c_uint32, c_uint32, c_uint, c_uint, c_uint32, c_void_p)
        self._load(self.get_transform_feedbackiv, 'glGetTransformFeedbackiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_transform_feedbacki_v, 'glGetTransformFeedbacki_v',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_transform_feedbacki64_v, 'glGetTransformFeedbacki64_v',
                   None, c_uint, c_uint, c_uint, POINTER(c_int64))
        self._load(self.getn_uniformfv, 'glGetnUniformfv',
                   None, c_uint, c_int, c_uint32, POINTER(c_float))
        self._load(self.getn_uniformiv, 'glGetnUniformiv',
                   None, c_uint, c_int, c_uint32, POINTER(c_int))
        self._load(self.getn_uniformuiv, 'glGetnUniformuiv',
                   None, c_uint, c_int, c_uint32, POINTER(c_uint))
        self._load(self.getn_uniformdv, 'glGetnUniformdv',
                   None, c_uint, c_int, c_uint32, POINTER(c_double))
        self._load(self.get_vertex_array_indexed64iv, 'glGetVertexArrayIndexed64iv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int64))
        self._load(self.get_vertex_array_indexediv, 'glGetVertexArrayIndexediv',
                   None, c_uint, c_uint, c_uint, POINTER(c_int))
        self._load(self.get_vertex_arrayiv, 'glGetVertexArrayiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.invalidate_named_framebuffer_data, 'glInvalidateNamedFramebufferData',
                   None, c_uint, c_uint32, POINTER(c_uint32))
        self._load(self.invalidate_named_framebuffer_sub_data, 'glInvalidateNamedFramebufferSubData',
                   None, c_uint, c_uint32, POINTER(c_uint32), c_int, c_int, c_uint32, c_uint32)
        self._load(self.map_named_buffer, 'glMapNamedBuffer',
                   c_void_p, c_uint, c_uint)
        self._load(self.map_named_buffer_range, 'glMapNamedBufferRange',
                   c_void_p, c_uint, POINTER(c_int), c_uint32, c_uint32)
        self._load(self.memory_barrier_by_region, 'glMemoryBarrierByRegion',
                   None, c_uint32)
        self._load(self.named_framebuffer_read_buffer, 'glNamedFramebufferReadBuffer',
                   None, c_uint, c_uint)
        self._load(self.readn_pixels, 'glReadnPixels',
                   None, c_int, c_int, c_uint32, c_uint32, c_uint, c_uint, c_uint32, c_void_p)
        self._load(self.named_renderbuffer_storage, 'glNamedRenderbufferStorage',
                   None, c_uint, c_uint, c_uint32, c_uint32)
        self._load(self.named_renderbuffer_storage_multisample, 'glNamedRenderbufferStorageMultisample',
                   None, c_uint, c_uint32, c_uint, c_uint32, c_uint32)
        self._load(self.texture_buffer, 'glTextureBuffer',
                   None, c_uint, c_uint, c_uint)
        self._load(self.texture_buffer_range, 'glTextureBufferRange',
                   None, c_uint, c_uint, c_uint, POINTER(c_int), c_uint32)
        self._load(self.texture_parameterf, 'glTextureParameterf',
                   None, c_uint, c_uint, c_float)
        self._load(self.texture_parameteri, 'glTextureParameteri',
                   None, c_uint, c_uint, c_int)
        self._load(self.texture_parameterfv, 'glTextureParameterfv',
                   None, c_uint, c_uint, POINTER(c_float))
        self._load(self.texture_parameteriv, 'glTextureParameteriv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.texture_parameter_iiv, 'glTextureParameterIiv',
                   None, c_uint, c_uint, POINTER(c_int))
        self._load(self.texture_parameter_iuiv, 'glTextureParameterIuiv',
                   None, c_uint, c_uint, POINTER(c_uint))
        self._load(self.texture_barrier, 'glTextureBarrier',
                   None, )
        self._load(self.transform_feedback_buffer_base, 'glTransformFeedbackBufferBase',
                   None, c_uint, c_uint, c_uint)
        self._load(self.transform_feedback_buffer_range, 'glTransformFeedbackBufferRange',
                   None, c_uint, c_uint, c_uint, POINTER(c_int), c_uint32)
        self._load(self.unmap_named_buffer, 'glUnmapNamedBuffer',
                   c_bool, c_uint)
        self._load(self.vertex_array_element_buffer, 'glVertexArrayElementBuffer',
                   None, c_uint, c_uint)
        self._load(self.vertex_array_attrib_binding, 'glVertexArrayAttribBinding',
                   None, c_uint, c_uint, c_uint)
        self._load(self.vertex_array_attrib_format, 'glVertexArrayAttribFormat',
                   None, c_uint, c_uint, c_int, c_uint, c_bool, c_uint)
        self._load(self.vertex_array_attrib_iformat, 'glVertexArrayAttribIFormat',
                   None, c_uint, c_uint, c_int, c_uint, c_uint)
        self._load(self.vertex_array_attrib_lformat, 'glVertexArrayAttribLFormat',
                   None, c_uint, c_uint, c_int, c_uint, c_uint)
        self._load(self.vertex_array_binding_divisor, 'glVertexArrayBindingDivisor',
                   None, c_uint, c_uint, c_uint)

    def bind_texture_unit(self, unit: int, texture: int):
        """
        Bind an existing texture object to the specified texture unit 

        Wrapper for glBindTextureUnit

        Parameters
        ----------
        unit: int
            Specifies the texture unit, to which the texture object should be bound to.
        texture: int
            Specifies the name of a texture.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if texture is not zero or the name of an existing texture
            object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindTextureUnit.xhtml
        """
        pass

    def vertex_array_vertex_buffer(self, vaobj: int, bindingindex: int, buffer: int, offset: POINTER(c_int), stride: int):
        """
        Bind a buffer to a vertex buffer bind point

        Wrapper for glVertexArrayVertexBuffer

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object to be used by glVertexArrayVertexBuffer function.
        bindingindex: int
            The index of the vertex buffer binding point to which to bind the buffer.
        buffer: int
            The name of a buffer to bind to the vertex buffer binding point.
        offset: POINTER(c_int)
            The offset of the first element of the buffer.
        stride: int
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glBindVertexBuffer if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayVertexBuffer if vaobj is not the name of an
            existing vertex array object.
        GL_INVALID_VALUE is generated if bindingindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.
        GL_INVALID_VALUE is generated if offset or stride is less than zero, or if stride is greater than
            the value of GL_MAX_VERTEX_ATTRIB_STRIDE.
        GL_INVALID_VALUE is generated if buffer is not zero or the name of an existing buffer object (as
            returned by glGenBuffers or glCreateBuffers).

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindVertexBuffer.xhtml
        """
        pass

    def vertex_array_vertex_buffers(self, vaobj: int, first: int, count: int, buffers: POINTER(c_uint), offsets: POINTER(POINTER(c_int)), strides: POINTER(c_uint32)):
        """
        Attach multiple buffer objects to a vertex array object

        Wrapper for glVertexArrayVertexBuffers

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glVertexArrayVertexBuffers.
        first: int
            Specifies the first vertex buffer binding point to which a buffer object is to be bound.
        count: int
            Specifies the number of buffers to bind.
        buffers: POINTER(c_uint)
            Specifies the address of an array of strides to associate with the binding points.
        offsets: POINTER(POINTER(c_int))
            Specifies the address of an array of offsets to associate with the binding points.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glBindVertexBuffers if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayVertexBuffers if vaobj is not the name of the
            vertex array object.
        GL_INVALID_OPERATION is generated if $first + count$ is greater than the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.
        GL_INVALID_OPERATION is generated if any value in buffers is not zero or the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if any value in offsets or strides is negative, or if a value is
            stride is greater than the value of GL_MAX_VERTEX_ATTRIB_STRIDE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBindVertexBuffers.xhtml
        """
        pass

    def blit_named_framebuffer(self, read_framebuffer: int, draw_framebuffer: int, src_x0: int, src_y0: int, src_x1: int, src_y1: int, dst_x0: int, dst_y0: int, dst_x1: int, dst_y1: int, mask: int, filter: int):
        """
        Copy a block of pixels from one framebuffer object to another

        Wrapper for glBlitNamedFramebuffer

        Parameters
        ----------
        mask: int
            The bitwise OR of the flags indicating which buffers are to be copied. The allowed flags are
            GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT and GL_STENCIL_BUFFER_BIT.
        filter: int
            Specifies the interpolation to be applied if the image is stretched. Must be GL_NEAREST or
            GL_LINEAR.

        Raises
        ------
        GL_INVALID_OPERATION is generated by BlitNamedFramebuffer if readFramebuffer or drawFramebuffer is
            not zero or the name of an existing framebuffer object.
        GL_INVALID_OPERATION is generated if mask contains any of the GL_DEPTH_BUFFER_BIT or
            GL_STENCIL_BUFFER_BIT and filter is not GL_NEAREST.
        GL_INVALID_OPERATION is generated if mask contains GL_COLOR_BUFFER_BIT and any of the following
            conditions hold:
        The read buffer contains fixed-point or floating-point values and any draw buffer contains neither
            fixed-point nor floating-point values.
        The read buffer contains unsigned integer values and any draw buffer does not contain unsigned
            integer values.
        The read buffer contains signed integer values and any draw buffer does not contain signed integer
            values.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlitFramebuffer.xhtml
        """
        pass

    def named_buffer_data(self, buffer: int, size: int, data: c_void_p, usage: int):
        """
        Creates and initializes a buffer object's data store

        Wrapper for glNamedBufferData

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glNamedBufferData function.
        size: int
            Specifies the size in bytes of the buffer object's new data store.
        data: c_void_p
            Specifies a pointer to data that will be copied into the data store for initialization, or NULL if
            no data is to be copied.
        usage: int
            Specifies the expected usage pattern of the data store. The symbolic constant must be
            GL_STREAM_DRAW, GL_STREAM_READ, GL_STREAM_COPY, GL_STATIC_DRAW, GL_STATIC_READ, GL_STATIC_COPY,
            GL_DYNAMIC_DRAW, GL_DYNAMIC_READ, or GL_DYNAMIC_COPY.

        Raises
        ------
        GL_INVALID_ENUM is generated by glBufferData if target is not one of the accepted buffer targets.
        GL_INVALID_ENUM is generated if usage is not GL_STREAM_DRAW, GL_STREAM_READ, GL_STREAM_COPY,
            GL_STATIC_DRAW, GL_STATIC_READ, GL_STATIC_COPY, GL_DYNAMIC_DRAW, GL_DYNAMIC_READ, or
            GL_DYNAMIC_COPY.
        GL_INVALID_VALUE is generated if size is negative.
        GL_INVALID_OPERATION is generated by glBufferData if the reserved buffer object name 0 is bound to
            target.
        GL_INVALID_OPERATION is generated by glNamedBufferData if buffer is not the name of an existing
            buffer object.
        GL_INVALID_OPERATION is generated if the GL_BUFFER_IMMUTABLE_STORAGE flag of the buffer object is
            GL_TRUE.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store with the specified size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBufferData.xhtml
        """
        pass

    def named_buffer_storage(self, buffer: int, size: int, data: c_void_p, flags: int):
        """
        Creates and initializes a buffer object's immutable data store

        Wrapper for glNamedBufferStorage

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glNamedBufferStorage function.
        size: int
            Specifies the size in bytes of the buffer object's new data store.
        data: c_void_p
            Specifies a pointer to data that will be copied into the data store for initialization, or NULL if
            no data is to be copied.
        flags: int
            Specifies the intended usage of the buffer's data store. Must be a bitwise combination of the
            following flags. GL_DYNAMIC_STORAGE_BIT, GL_MAP_READ_BIT GL_MAP_WRITE_BIT, GL_MAP_PERSISTENT_BIT,
            GL_MAP_COHERENT_BIT, and GL_CLIENT_STORAGE_BIT.

        Raises
        ------
        GL_INVALID_ENUM is generated by glBufferStorage if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glNamedBufferStorage if buffer is not the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if size is less than or equal to zero.
        GL_INVALID_OPERATION is generated by glBufferStorage if the reserved buffer object name 0 is bound
            to target.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store with the properties
            requested in flags.
        GL_INVALID_VALUE is generated if flags has any bits set other than those defined above.
        GL_INVALID_VALUE error is generated if flags contains GL_MAP_PERSISTENT_BIT but does not contain at
            least one of GL_MAP_READ_BIT or GL_MAP_WRITE_BIT.
        GL_INVALID_VALUE is generated if flags contains GL_MAP_COHERENT_BIT, but does not also contain
            GL_MAP_PERSISTENT_BIT.
        GL_INVALID_OPERATION is generated by glBufferStorage if the GL_BUFFER_IMMUTABLE_STORAGE flag of the
            buffer bound to target is GL_TRUE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBufferStorage.xhtml
        """
        pass

    def named_buffer_sub_data(self, buffer: int, offset: POINTER(c_int), size: int, data: c_void_p):
        """
        Updates a subset of a buffer object's data store

        Wrapper for glNamedBufferSubData

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glNamedBufferSubData.
        offset: POINTER(c_int)
            Specifies the offset into the buffer object's data store where data replacement will begin,
            measured in bytes.
        size: int
            Specifies the size in bytes of the data store region being replaced.
        data: c_void_p
            Specifies a pointer to the new data that will be copied into the data store.

        Raises
        ------
        GL_INVALID_ENUM is generated by glBufferSubData if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glBufferSubData if zero is bound to target.
        GL_INVALID_OPERATION is generated by glNamedBufferSubData if buffer is not the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if offset or size is negative, or if $offset + size$ is greater than
            the value of GL_BUFFER_SIZE for the specified buffer object.
        GL_INVALID_OPERATION is generated if any part of the specified range of the buffer object is mapped
            with glMapBufferRange or glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set
            in the glMapBufferRange access flags.
        GL_INVALID_OPERATION is generated if the value of the GL_BUFFER_IMMUTABLE_STORAGE flag of the
            buffer object is GL_TRUE and the value of GL_BUFFER_STORAGE_FLAGS for the buffer object does not
            have the GL_DYNAMIC_STORAGE_BIT bit set.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBufferSubData.xhtml
        """
        pass

    def check_named_framebuffer_status(self, framebuffer: int, target: int) -> int:
        """
        Check the completeness status of a framebuffer

        Wrapper for glCheckNamedFramebufferStatus

        Parameters
        ----------
        target: int
            Specify the target to which the framebuffer is bound for glCheckFramebufferStatus, and the target
            against which framebuffer completeness of framebuffer is checked for glCheckNamedFramebufferStatus.
        framebuffer: int
            Specifies the name of the framebuffer object for glCheckNamedFramebufferStatus

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not GL_DRAW_FRAMEBUFFER, GL_READ_FRAMEBUFFER or
            GL_FRAMEBUFFER.
        GL_INVALID_OPERATION is generated by glCheckNamedFramebufferStatus if framebuffer is not zero or
            the name of an existing framebuffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCheckFramebufferStatus.xhtml
        """
        pass

    def clear_named_framebufferiv(self, framebuffer: int, buffer: int, drawbuffer: int, value: POINTER(c_int)):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearNamedFramebufferiv

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glClearNamedFramebuffer*.
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        value: POINTER(c_int)
            A pointer to the value or values to clear the buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def clear_named_framebufferuiv(self, framebuffer: int, buffer: int, drawbuffer: int, value: POINTER(c_uint)):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearNamedFramebufferuiv

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glClearNamedFramebuffer*.
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        value: POINTER(c_uint)
            A pointer to the value or values to clear the buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def clear_named_framebufferfv(self, framebuffer: int, buffer: int, drawbuffer: int, value: POINTER(c_float)):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearNamedFramebufferfv

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glClearNamedFramebuffer*.
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        value: POINTER(c_float)
            A pointer to the value or values to clear the buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def clear_named_framebufferfi(self, framebuffer: int, buffer: int, drawbuffer: int, depth: float, stencil: int):
        """
        Clear individual buffers of a framebuffer

        Wrapper for glClearNamedFramebufferfi

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glClearNamedFramebuffer*.
        buffer: int
            Specify the buffer to clear.
        drawbuffer: int
            Specify a particular draw buffer to clear.
        depth: float
            The value to clear the depth buffer to.
        stencil: int
            The value to clear the stencil buffer to.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glClearNamedFramebuffer* if framebuffer is not zero or the
            name of an existing framebuffer object.
        GL_INVALID_ENUM is generated by glClearBufferiv and glClearNamedFramebufferiv buffer is not
            GL_COLOR or GL_STENCIL.
        GL_INVALID_ENUM is generated by glClearBufferuiv and glClearNamedFramebufferuiv buffer is not
            GL_COLOR.
        GL_INVALID_ENUM is generated by glClearBufferfv and glClearNamedFramebufferfv buffer is not
            GL_COLOR or GL_DEPTH.
        GL_INVALID_ENUM is generated by glClearBufferfi and glClearNamedFramebufferfi buffer is not
            GL_DEPTH_STENCIL.
        GL_INVALID_VALUE is generated if buffer is GL_COLOR drawbuffer is negative, or greater than the
            value of GL_MAX_DRAW_BUFFERS minus one.
        GL_INVALID_VALUE is generated if buffer is GL_DEPTH, GL_STENCIL or GL_DEPTH_STENCIL and drawbuffer
            is not zero.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBuffer.xhtml
        """
        pass

    def clear_named_buffer_data(self, buffer: int, internalformat: int, format: int, type: int, data: c_void_p):
        """
        Fill a buffer object's data store with a fixed value

        Wrapper for glClearNamedBufferData

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glClearNamedBufferData.
        internalformat: int
            The internal format with which the data will be stored in the buffer object.
        format: int
            The format of the data in memory addressed by data.
        type: int
            The type of the data in memory addressed by data.
        data: c_void_p
            The address of a memory location storing the data to be replicated into the buffer's data store.

        Raises
        ------
        GL_INVALID_ENUM is generated by glClearBufferData if target is not one of the generic buffer
            binding targets.
        GL_INVALID_VALUE is generated by glClearBufferData if no buffer is bound target.
        GL_INVALID_OPERATION is generated by glClearNamedBufferData if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if internalformat is not one of the valid sized internal formats
            listed in the table above.
        GL_INVALID_OPERATION is generated if any part of the specified range of the buffer object is mapped
            with glMapBufferRange or glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set
            in the glMapBufferRange access flags.
        GL_INVALID_VALUE is generated if format is not a valid format, or type is not a valid type.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBufferData.xhtml
        """
        pass

    def clear_named_buffer_sub_data(self, buffer: int, internalformat: int, offset: POINTER(c_int), size: int, format: int, type: int, data: c_void_p):
        """
        Fill all or part of buffer object's data store with a fixed value

        Wrapper for glClearNamedBufferSubData

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glClearNamedBufferSubData.
        internalformat: int
            The internal format with which the data will be stored in the buffer object.
        offset: POINTER(c_int)
            The offset in basic machine units into the buffer object's data store at which to start filling.
        size: int
            The size in basic machine units of the range of the data store to fill.
        format: int
            The format of the data in memory addressed by data.
        type: int
            The type of the data in memory addressed by data.
        data: c_void_p
            The address of a memory location storing the data to be replicated into the buffer's data store.

        Raises
        ------
        GL_INVALID_ENUM is generated by glClearBufferSubData if target is not one of the generic buffer
            binding targets.
        GL_INVALID_VALUE is generated by glClearBufferSubData if no buffer is bound to target.
        GL_INVALID_OPERATION is generated by glClearNamedBufferSubData if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if internalformat is not one of the valid sized internal formats
            listed in the table above.
        GL_INVALID_VALUE is generated if offset or range are not multiples of the number of basic machine
            units per-element for the internal format specified by internalformat. This value may be computed
            by multiplying the number of components for internalformat from the table by the size of the base
            type from the table.
        GL_INVALID_VALUE is generated if offset or size is negative, or if $offset + size$ is greater than
            the value of GL_BUFFER_SIZE for the buffer object.
        GL_INVALID_OPERATION is generated if any part of the specified range of the buffer object is mapped
            with glMapBufferRange or glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set
            in the glMapBufferRange access flags.
        GL_INVALID_VALUE is generated if format is not a valid format, or type is not a valid type.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearBufferSubData.xhtml
        """
        pass

    def clip_control(self, origin: int, depth: int):
        """
        Control clip coordinate to window coordinate behavior

        Wrapper for glClipControl

        Parameters
        ----------
        origin: int
            Specifies the clip control origin. Must be one of GL_LOWER_LEFT or GL_UPPER_LEFT.
        depth: int
            Specifies the clip control depth mode. Must be one of GL_NEGATIVE_ONE_TO_ONE or GL_ZERO_TO_ONE.

        Raises
        ------
        An GL_INVALID_ENUM error is generated if origin is not GL_LOWER_LEFT or GL_UPPER_LEFT.
        An GL_INVALID_ENUM error is generated if depth is not GL_NEGATIVE_ONE_TO_ONE or GL_ZERO_TO_ONE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClipControl.xhtml
        """
        pass

    def copy_named_buffer_sub_data(self, read_buffer: int, write_buffer: int, read_offset: POINTER(c_int), write_offset: POINTER(c_int), size: int):
        """
        Copy all or part of the data store of a buffer object to the data store of another buffer object

        Wrapper for glCopyNamedBufferSubData

        Parameters
        ----------
        size: int
            Specifies the size, in basic machine units, of the data to be copied from the source buffer object
            to the destination buffer object.

        Raises
        ------
        GL_INVALID_ENUM is generated by glCopyBufferSubData if readTarget or writeTarget is not one of the
            buffer binding targets listed above.
        GL_INVALID_OPERATION is generated by glCopyBufferSubData if zero is bound to readTarget or
            writeTarget.
        GL_INVALID_OPERATION is generated by glCopyNamedBufferSubData if readBuffer or writeBuffer is not
            the name of an existing buffer object.
        GL_INVALID_VALUE is generated if any of readOffset, writeOffset or size is negative, if $readOffset
            + size$ is greater than the size of the source buffer object (its value of GL_BUFFER_SIZE), or if
            $writeOffset + size$ is greater than the size of the destination buffer object.
        GL_INVALID_VALUE is generated if the source and destination are the same buffer object, and the
            ranges $[readOffset,readOffset+size)$ and $[writeOffset,writeOffset+size)$ overlap.
        GL_INVALID_OPERATION is generated if either the source or destination buffer object is mapped with
            glMapBufferRange or glMapBuffer, unless they were mapped with the GL_MAP_PERSISTENT bit set in the
            glMapBufferRange access flags.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCopyBufferSubData.xhtml
        """
        pass

    def create_buffers(self, n: int, buffers: POINTER(c_uint)):
        """
        Create buffer objects

        Wrapper for glCreateBuffers

        Parameters
        ----------
        n: int
            Specifies the number of buffer objects to create.
        buffers: POINTER(c_uint)
            Specifies an array in which names of the new buffer objects are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateBuffers.xhtml
        """
        pass

    def create_framebuffers(self, n: int, ids: POINTER(c_uint)):
        """
        Create framebuffer objects

        Wrapper for glCreateFramebuffers

        Parameters
        ----------
        n: int
            Number of framebuffer objects to create.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateFramebuffers.xhtml
        """
        pass

    def create_program_pipelines(self, n: int, pipelines: POINTER(c_uint)):
        """
        Create program pipeline objects

        Wrapper for glCreateProgramPipelines

        Parameters
        ----------
        n: int
            Number of program pipeline objects to create.
        pipelines: POINTER(c_uint)
            Specifies an array in which names of the new program pipeline objects are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateProgramPipelines.xhtml
        """
        pass

    def create_queries(self, target: int, n: int, ids: POINTER(c_uint)):
        """
        Create query objects

        Wrapper for glCreateQueries

        Parameters
        ----------
        target: int
            Specifies the target of each created query object.
        n: int
            Number of query objects to create.
        ids: POINTER(c_uint)
            Specifies an array in which names of the new query objects are stored.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not an accepted value.
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateQueries.xhtml
        """
        pass

    def create_renderbuffers(self, n: int, renderbuffers: POINTER(c_uint)):
        """
        Create renderbuffer objects

        Wrapper for glCreateRenderbuffers

        Parameters
        ----------
        n: int
            Number of renderbuffer objects to create.
        renderbuffers: POINTER(c_uint)
            Specifies an array in which names of the new renderbuffer objects are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateRenderbuffers.xhtml
        """
        pass

    def create_samplers(self, n: int, samplers: POINTER(c_uint)):
        """
        Create sampler objects

        Wrapper for glCreateSamplers

        Parameters
        ----------
        n: int
            Number of sampler objects to create.
        samplers: POINTER(c_uint)
            Specifies an array in which names of the new sampler objects are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateSamplers.xhtml
        """
        pass

    def create_textures(self, target: int, n: int, textures: POINTER(c_uint)):
        """
        Create texture objects

        Wrapper for glCreateTextures

        Parameters
        ----------
        target: int
            Specifies the effective texture target of each created texture.
        n: int
            Number of texture objects to create.
        textures: POINTER(c_uint)
            Specifies an array in which names of the new texture objects are stored.

        Raises
        ------
        GL_INVALID_ENUM is generated if target is not one of the allowable values.
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateTextures.xhtml
        """
        pass

    def create_transform_feedbacks(self, n: int, ids: POINTER(c_uint)):
        """
        Create transform feedback objects

        Wrapper for glCreateTransformFeedbacks

        Parameters
        ----------
        n: int
            Number of transform feedback objects to create.
        ids: POINTER(c_uint)
            Specifies an array in which names of the new transform feedback objects are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateTransformFeedbacks.xhtml
        """
        pass

    def create_vertex_arrays(self, n: int, arrays: POINTER(c_uint)):
        """
        Create vertex array objects

        Wrapper for glCreateVertexArrays

        Parameters
        ----------
        n: int
            Number of vertex array objects to create.
        arrays: POINTER(c_uint)
            Specifies an array in which names of the new vertex array objects are stored.

        Raises
        ------
        GL_INVALID_VALUE is generated if n is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateVertexArrays.xhtml
        """
        pass

    def named_framebuffer_draw_buffer(self, framebuffer: int, buf: int):
        """
        Specify which color buffers are to be drawn into

        Wrapper for glNamedFramebufferDrawBuffer

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glNamedFramebufferDrawBuffer function. Must be
            zero or the name of a framebuffer object.
        buf: int
            For default framebuffer, the argument specifies up to four color buffers to be drawn into. Symbolic
            constants GL_NONE, GL_FRONT_LEFT, GL_FRONT_RIGHT, GL_BACK_LEFT, GL_BACK_RIGHT, GL_FRONT, GL_BACK,
            GL_LEFT, GL_RIGHT, and GL_FRONT_AND_BACK are accepted. The initial value is GL_FRONT for
            single-buffered contexts, and GL_BACK for double-buffered contexts. For framebuffer objects,
            GL_COLOR_ATTACHMENT$m$ and GL_NONE enums are accepted, where $m$ is a value between 0 and
            GL_MAX_COLOR_ATTACHMENTS.

        Raises
        ------
        GL_INVALID_OPERATION error is generated by glNamedFramebufferDrawBuffer if framebuffer is not zero
            or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if buf is not an accepted value.
        GL_INVALID_OPERATION is generated if the default framebuffer is affected and none of the buffers
            indicated by buf exists.
        GL_INVALID_OPERATION is generated if a framebuffer object is affected and buf is not equal to
            GL_NONE or GL_COLOR_ATTACHMENT$m$, where $m$ is a value between 0 and GL_MAX_COLOR_ATTACHMENTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawBuffer.xhtml
        """
        pass

    def named_framebuffer_draw_buffers(self, framebuffer: int, n: int, bufs: POINTER(c_uint32)):
        """
        Specifies a list of color buffers to be drawn into

        Wrapper for glNamedFramebufferDrawBuffers

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glNamedFramebufferDrawBuffers.
        n: int
            Specifies the number of buffers in bufs.
        bufs: POINTER(c_uint32)
            Points to an array of symbolic constants specifying the buffers into which fragment colors or data
            values will be written.
        n: int
            The fragment shader output value is written into the n th color attachment of the current
            framebuffer. n may range from zero to the value of GL_MAX_COLOR_ATTACHMENTS.

        Raises
        ------
        GL_INVALID_OPERATION error is generated by glNamedFramebufferDrawBuffers if framebuffer is not zero
            or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if one of the values in bufs is not an accepted value.
        GL_INVALID_ENUM is generated if the API call refers to the default framebuffer and one or more of
            the values in bufs is one of the GL_COLOR_ATTACHMENT n tokens.
        GL_INVALID_ENUM is generated if the API call refers to a framebuffer object and one or more of the
            values in bufs is anything other than GL_NONE or one of the GL_COLOR_ATTACHMENT n tokens.
        GL_INVALID_ENUM is generated if n is less than 0.
        GL_INVALID_OPERATION is generated if a symbolic constant other than GL_NONE appears more than once
            in bufs.
        GL_INVALID_OPERATION is generated if any of the entries in bufs (other than GL_NONE) indicates a
            color buffer that does not exist in the current GL context.
        GL_INVALID_OPERATION is generated if any value in bufs is GL_BACK, and n is not one.
        GL_INVALID_VALUE is generated if n is greater than GL_MAX_DRAW_BUFFERS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawBuffers.xhtml
        """
        pass

    def enable_vertex_array_attrib(self, vaobj: int, index: int):
        """
        Enable or disable a generic vertex attribute array

        Wrapper for glEnableVertexArrayAttrib

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glDisableVertexArrayAttrib and
            glEnableVertexArrayAttrib functions.
        index: int
            Specifies the index of the generic vertex attribute to be enabled or disabled.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glEnableVertexAttribArray and glDisableVertexAttribArray if no
            vertex array object is bound.
        GL_INVALID_OPERATION is generated by glEnableVertexArrayAttrib and glDisableVertexArrayAttrib if
            vaobj is not the name of an existing vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnableVertexAttribArray.xhtml
        """
        pass

    def disable_vertex_array_attrib(self, vaobj: int, index: int):
        """
        Enable or disable a generic vertex attribute array

        Wrapper for glDisableVertexArrayAttrib

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glDisableVertexArrayAttrib and
            glEnableVertexArrayAttrib functions.
        index: int
            Specifies the index of the generic vertex attribute to be enabled or disabled.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glEnableVertexAttribArray and glDisableVertexAttribArray if no
            vertex array object is bound.
        GL_INVALID_OPERATION is generated by glEnableVertexArrayAttrib and glDisableVertexArrayAttrib if
            vaobj is not the name of an existing vertex array object.
        GL_INVALID_VALUE is generated if index is greater than or equal to GL_MAX_VERTEX_ATTRIBS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnableVertexAttribArray.xhtml
        """
        pass

    def flush_mapped_named_buffer_range(self, buffer: int, offset: POINTER(c_int), length: int):
        """
        Indicate modifications to a range of a mapped buffer

        Wrapper for glFlushMappedNamedBufferRange

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glFlushMappedNamedBufferRange.
        offset: POINTER(c_int)
            Specifies the start of the buffer subrange, in basic machine units.
        length: int
            Specifies the length of the buffer subrange, in basic machine units.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFlushMappedBufferRange if target is not one of the buffer binding
            targets listed above.
        GL_INVALID_OPERATION is generated by glFlushMappedBufferRange if zero is bound to target.
        GL_INVALID_OPERATION is generated by glFlushMappedNamedBufferRange if buffer is not the name of an
            existing buffer object.
        GL_INVALID_VALUE is generated if offset or length is negative, or if offset + length exceeds the
            size of the mapping.
        GL_INVALID_OPERATION is generated if the buffer object is not mapped, or is mapped without the
            GL_MAP_FLUSH_EXPLICIT_BIT flag.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFlushMappedBufferRange.xhtml
        """
        pass

    def named_framebuffer_parameteri(self, framebuffer: int, pname: int, param: int):
        """
        Set a named parameter of a framebuffer object

        Wrapper for glNamedFramebufferParameteri

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glNamedFramebufferParameteri.
        pname: int
            Specifies the framebuffer parameter to be modified.
        param: int
            The new value for the parameter named pname.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFramebufferParameteri if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glFramebufferParameteri if the default framebuffer is bound to
            target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferParameteri if framebuffer is not the name of
            an existing framebuffer object.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_WIDTH and param is less than zero
            or greater than the value of GL_MAX_FRAMEBUFFER_WIDTH.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_HEIGHT and param is less than zero
            or greater than the value of GL_MAX_FRAMEBUFFER_HEIGHT.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_LAYERS and param is less than zero
            or greater than the value of GL_MAX_FRAMEBUFFER_LAYERS.
        GL_INVALID_VALUE is generated if pname is GL_FRAMEBUFFER_DEFAULT_SAMPLES and param is less than
            zero or greater than the value of GL_MAX_FRAMEBUFFER_SAMPLES.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferParameteri.xhtml
        """
        pass

    def named_framebuffer_renderbuffer(self, framebuffer: int, attachment: int, renderbuffertarget: int, renderbuffer: int):
        """
        Attach a renderbuffer as a logical buffer of a framebuffer object

        Wrapper for glNamedFramebufferRenderbuffer

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glNamedFramebufferRenderbuffer.
        attachment: int
            Specifies the attachment point of the framebuffer.
        renderbuffertarget: int
            Specifies the renderbuffer target. Must be GL_RENDERBUFFER.
        renderbuffer: int
            Specifies the name of an existing renderbuffer object of type renderbuffertarget to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFramebufferRenderbuffer if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glFramebufferRenderbuffer if zero is bound to target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferRenderbuffer if framebuffer is not the name
            of an existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_ENUM is generated if renderbuffertarget is not GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated if renderbuffertarget is not zero or the name of an existing
            renderbuffer object of type GL_RENDERBUFFER.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferRenderbuffer.xhtml
        """
        pass

    def named_framebuffer_texture(self, framebuffer: int, attachment: int, texture: int, level: int):
        """
        Attach a level of a texture object as a logical buffer of a framebuffer object

        Wrapper for glNamedFramebufferTexture

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glNamedFramebufferTexture.
        attachment: int
            Specifies the attachment point of the framebuffer.
        texture: int
            Specifies the name of an existing texture object to attach.
        level: int
            Specifies the mipmap level of the texture object to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by all commands accepting a target parameter if it is not one of the
            accepted framebuffer targets.
        GL_INVALID_OPERATION is generated by all commands accepting a target parameter if zero is bound to
            that target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferTexture if framebuffer is not the name of an
            existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_VALUE is generated if texture is not zero or the name of an existing texture object.
        GL_INVALID_VALUE is generated if texture is not zero and level is not a supported texture level for
            texture.
        GL_INVALID_VALUE is generated by glFramebufferTexture3D if texture is not zero and layer is larger
            than the value of GL_MAX_3D_TEXTURE_SIZE minus one.
        GL_INVALID_OPERATION is generated by all commands accepting a textarget parameter if texture is not
            zero, and textarget and the effective target of texture are not compatible.
        GL_INVALID_OPERATION is generated by if texture is a buffer texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferTexture.xhtml
        """
        pass

    def named_framebuffer_texture_layer(self, framebuffer: int, attachment: int, texture: int, level: int, layer: int):
        """
        Attach a single layer of a texture object as a logical buffer of a framebuffer object

        Wrapper for glNamedFramebufferTextureLayer

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glNamedFramebufferTextureLayer.
        attachment: int
            Specifies the attachment point of the framebuffer.
        texture: int
            Specifies the name of an existing texture object to attach.
        level: int
            Specifies the mipmap level of the texture object to attach.
        layer: int
            Specifies the layer of the texture object to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by glFramebufferTexture if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glFramebufferTexture if zero is bound to target.
        GL_INVALID_OPERATION is generated by glNamedFramebufferTexture if framebuffer is not the name of an
            existing framebuffer object.
        GL_INVALID_ENUM is generated if attachment is not one of the accepted attachment points.
        GL_INVALID_OPERATION is generated if texture is not zero and is not the name of an existing
            three-dimensional, two-dimensional multisample array, one- or two-dimensional array, cube map, or
            cube map array texture.
        GL_INVALID_VALUE is generated if texture is not zero and level is not a supported texture level for
            texture, as described above.
        GL_INVALID_VALUE is generated if texture is not zero and layer is larger than the value of
            GL_MAX_3D_TEXTURE_SIZE minus one (for three-dimensional texture objects), or larger than the value
            of GL_MAX_ARRAY_TEXTURE_LAYERS minus one (for array texture objects).
        GL_INVALID_VALUE is generated if texture is not zero and layer is negative.
        GL_INVALID_OPERATION is generated by if texture is a buffer texture.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glFramebufferTextureLayer.xhtml
        """
        pass

    def generate_texture_mipmap(self, texture: int):
        """
        Generate mipmaps for a specified texture object

        Wrapper for glGenerateTextureMipmap

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGenerateTextureMipmap.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGenerateMipmap if target is not one of the accepted texture
            targets.
        GL_INVALID_OPERATION is generated by glGenerateTextureMipmap if texture is not the name of an
            existing texture object.
        GL_INVALID_OPERATION is generated if target is GL_TEXTURE_CUBE_MAP or GL_TEXTURE_CUBE_MAP_ARRAY,
            and the specified texture object is not cube complete or cube array complete, respectively.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGenerateMipmap.xhtml
        """
        pass

    def get_named_buffer_parameteriv(self, buffer: int, pname: int, params: POINTER(c_int)):
        """
        Return parameters of a buffer object

        Wrapper for glGetNamedBufferParameteriv

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glGetNamedBufferParameteriv and
            glGetNamedBufferParameteri64v.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetBufferParameter* if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glGetBufferParameter* if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferParameter* if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if pname is not one of the buffer object parameter names described
            above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferParameter.xhtml
        """
        pass

    def get_named_buffer_parameteri64v(self, buffer: int, pname: int, params: POINTER(c_int64)):
        """
        Return parameters of a buffer object

        Wrapper for glGetNamedBufferParameteri64v

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glGetNamedBufferParameteriv and
            glGetNamedBufferParameteri64v.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetBufferParameter* if target is not one of the accepted buffer
            targets.
        GL_INVALID_OPERATION is generated by glGetBufferParameter* if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferParameter* if buffer is not the name of an
            existing buffer object.
        GL_INVALID_ENUM is generated if pname is not one of the buffer object parameter names described
            above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferParameter.xhtml
        """
        pass

    def get_named_buffer_pointerv(self, buffer: int, pname: int, params: POINTER(c_void_p)):
        """
        Return the pointer to a mapped buffer object's data store

        Wrapper for glGetNamedBufferPointerv

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glGetNamedBufferPointerv.
        pname: int
            Specifies the name of the pointer to be returned. Must be GL_BUFFER_MAP_POINTER.
        params: POINTER(c_void_p)
            Returns the pointer value specified by pname.

        Raises
        ------
        GL_INVALID_ENUM is generated if by glGetBufferPointerv if target is not one of the accepted buffer
            targets, or if pname is not GL_BUFFER_MAP_POINTER.
        GL_INVALID_OPERATION is generated by glGetBufferPointerv if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferPointerv if buffer is not the name of an
            existing buffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferPointerv.xhtml
        """
        pass

    def get_named_buffer_sub_data(self, buffer: int, offset: POINTER(c_int), size: int, data: c_void_p):
        """
        Returns a subset of a buffer object's data store

        Wrapper for glGetNamedBufferSubData

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glGetNamedBufferSubData.
        offset: POINTER(c_int)
            Specifies the offset into the buffer object's data store from which data will be returned, measured
            in bytes.
        size: int
            Specifies the size in bytes of the data store region being returned.
        data: c_void_p
            Specifies a pointer to the location where buffer object data is returned.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetBufferSubData if target is not one of the generic buffer
            binding targets.
        GL_INVALID_OPERATION is generated by glGetBufferSubData if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedBufferSubData if buffer is not the name of an
            existing buffer object.
        GL_INVALID_VALUE is generated if offset or size is negative, or if $offset + size$ is greater than
            the value of GL_BUFFER_SIZE for the buffer object.
        GL_INVALID_OPERATION is generated if the buffer object is mapped with glMapBufferRange or
            glMapBuffer, unless it was mapped with the GL_MAP_PERSISTENT_BIT bit set in the glMapBufferRange
            access flags.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetBufferSubData.xhtml
        """
        pass

    def getn_compressed_tex_image(self, target: int, level: int, buf_size: int, pixels: c_void_p):
        """
        Return a compressed texture image

        Wrapper for glGetnCompressedTexImage

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetCompressedTexImage and
            glGetnCompressedTexImage functions. GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D,
            GL_TEXTURE_2D_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_CUBE_MAP_POSITIVE_X,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Z, and GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, GL_TEXTURE_RECTANGLE are
            accepted.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level
            $n$ is the $n$-th mipmap reduction image.
        pixels: c_void_p
            Returns the compressed texture image.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glGetCompressedTextureImage if texture is not the name of an
            existing texture object.
        GL_INVALID_VALUE is generated if level is less than zero or greater than the maximum number of LODs
            permitted by the implementation.
        GL_INVALID_OPERATION is generated if glGetCompressedTexImage, glGetnCompressedTexImage, and
            glGetCompressedTextureImage is used to retrieve a texture that is in an uncompressed internal
            format.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target, the buffer storage was not initialized with glBufferStorage using
            GL_MAP_PERSISTENT_BIT flag, and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and the data would be packed to the buffer object such that the memory
            writes required would exceed the data store size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetCompressedTexImage.xhtml
        """
        pass

    def get_compressed_texture_image(self, texture: int, level: int, buf_size: int, pixels: c_void_p):
        """
        Return a compressed texture image

        Wrapper for glGetCompressedTextureImage

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGetCompressedTextureImage function.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level
            $n$ is the $n$-th mipmap reduction image.
        pixels: c_void_p
            Returns the compressed texture image.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glGetCompressedTextureImage if texture is not the name of an
            existing texture object.
        GL_INVALID_VALUE is generated if level is less than zero or greater than the maximum number of LODs
            permitted by the implementation.
        GL_INVALID_OPERATION is generated if glGetCompressedTexImage, glGetnCompressedTexImage, and
            glGetCompressedTextureImage is used to retrieve a texture that is in an uncompressed internal
            format.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target, the buffer storage was not initialized with glBufferStorage using
            GL_MAP_PERSISTENT_BIT flag, and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and the data would be packed to the buffer object such that the memory
            writes required would exceed the data store size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetCompressedTexImage.xhtml
        """
        pass

    def get_compressed_texture_sub_image(self, texture: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, buf_size: int, pixels: c_void_p):
        """
        Retrieve a sub-region of a compressed texture image from a compressed texture object

        Wrapper for glGetCompressedTextureSubImage

        Parameters
        ----------
        texture: int
            Specifies the name of the source texture object. Must be GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY
            or GL_TEXTURE_RECTANGLE. In specific, buffer and multisample textures are not permitted.
        level: int
            Specifies the level-of-detail number. Level 0 is the base image level. Level $n$ is the $n$th
            mipmap reduction image.
        xoffset: int
            Specifies a texel offset in the x direction within the texture array.
        yoffset: int
            Specifies a texel offset in the y direction within the texture array.
        zoffset: int
            Specifies a texel offset in the z direction within the texture array.
        width: int
            Specifies the width of the texture subimage. Must be a multiple of the compressed block's width,
            unless the offset is zero and the size equals the texture image size.
        height: int
            Specifies the height of the texture subimage. Must be a multiple of the compressed block's height,
            unless the offset is zero and the size equals the texture image size.
        depth: int
            Specifies the depth of the texture subimage. Must be a multiple of the compressed block's depth,
            unless the offset is zero and the size equals the texture image size.
        pixels: c_void_p
            Returns the texture subimage. Should be a pointer to an array of the type specified by type.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if texture is the name of a buffer or multisample texture.
        GL_INVALID_OPERATION error is generated if the buffer size required to store the requested data is
            greater than bufSize.
        GL_INVALID_OPERATION error is generated if the texture compression format is not based on
            fixed-size blocks.
        GL_INVALID_VALUE error is generated if texture is not the name of an existing texture object.
        GL_INVALID_VALUE is generated if xoffset, yoffset or zoffset are negative.
        GL_INVALID_VALUE is generated if xoffset + width is greater than the texture's width, yoffset +
            height is greater than the texture's height, or zoffset + depth is greater than the texture's
            depth.
        GL_INVALID_VALUE error is generated if the effective target is GL_TEXTURE_1D and either yoffset is
            not zero, or height is not one.
        GL_INVALID_VALUE error is generated if the effective target is GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D or GL_TEXTURE_RECTANGLE and either zoffset is not zero, or depth is not one.
        GL_INVALID_VALUE error is generated if xoffset, yoffset or zoffset is not a multiple of the
            compressed block width, height or depth respectively.
        GL_INVALID_VALUE error is generated if width, height or depth is not a multiple of the compressed
            block width, height or depth respectively, unless the offset is zero and the size equals the
            texture image size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetCompressedTextureSubImage.xhtml
        """
        pass

    def get_named_framebuffer_attachment_parameteriv(self, framebuffer: int, attachment: int, pname: int, params: POINTER(c_int)):
        """
        Retrieve information about attachments of a framebuffer object

        Wrapper for glGetNamedFramebufferAttachmentParameteriv

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glGetNamedFramebufferAttachmentParameteriv.
        attachment: int
            Specifies the attachment of the framebuffer object to query.
        pname: int
            Specifies the parameter of attachment to query.
        params: POINTER(c_int)
            Returns the value of parameter pname for attachment.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetFramebufferAttachmentParameteriv if target is not one of the
            accepted framebuffer targets.
        GL_INVALID_OPERATION is generated by glGetNamedFramebufferAttachmentParameteriv if framebuffer is
            not zero or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if pname is not valid for the value of
            GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE, as described above.
        GL_INVALID_OPERATION is generated if attachment is not one of the accepted framebuffer attachment
            points, as described above.
        GL_INVALID_OPERATION is generated if the value of GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE is GL_NONE
            and pname is not GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME or GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE.
        GL_INVALID_OPERATION is generated if attachment is GL_DEPTH_STENCIL_ATTACHMENT and different
            objects are bound to the depth and stencil attachment points of target.
        GL_INVALID_OPERATION is generated if attachment is GL_DEPTH_STENCIL_ATTACHMENT and pname is
            GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetFramebufferAttachmentParameter.xhtml
        """
        pass

    def get_named_framebuffer_parameteriv(self, framebuffer: int, pname: int, param: POINTER(c_int)):
        """
        Query a named parameter of a framebuffer object

        Wrapper for glGetNamedFramebufferParameteriv

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glGetNamedFramebufferParameteriv.
        pname: int
            Specifies the parameter of the framebuffer object to query.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetFramebufferParameteriv if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glGetNamedFramebufferAttachmentParameteriv if framebuffer is
            not zero or the name of an existing framebuffer object.
        GL_INVALID_ENUM is generated if pname is not one of the accepted parameter names.
        GL_INVALID_OPERATION is generated if a default framebuffer is queried, and pname is not one of
            GL_DOUBLEBUFFER, GL_IMPLEMENTATION_COLOR_READ_FORMAT, GL_IMPLEMENTATION_COLOR_READ_TYPE,
            GL_SAMPLES, GL_SAMPLE_BUFFERS or GL_STEREO.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetFramebufferParameter.xhtml
        """
        pass

    def get_graphics_reset_status(self) -> int:
        """
        Check if the rendering context has not been lost due to software or hardware issues

        Wrapper for glGetGraphicsResetStatus

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetGraphicsResetStatus.xhtml
        """
        pass

    def get_named_renderbuffer_parameteriv(self, renderbuffer: int, pname: int, params: POINTER(c_int)):
        """
        Query a named parameter of a renderbuffer object

        Wrapper for glGetNamedRenderbufferParameteriv

        Parameters
        ----------
        renderbuffer: int
            Specifies the name of the renderbuffer object for glGetNamedRenderbufferParameteriv.
        pname: int
            Specifies the parameter of the renderbuffer object to query.
        params: POINTER(c_int)
            Returns the value of parameter pname for the renderbuffer object.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetRenderbufferParameteriv if target is not GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated by glGetRenderbufferParameteriv if zero is bound to target.
        GL_INVALID_OPERATION is generated by glGetNamedRenderbufferParameteriv if renderbuffer is not the
            name of an existing renderbuffer object.
        GL_INVALID_ENUM is generated if pname is not one of the accepted parameter names described above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetRenderbufferParameter.xhtml
        """
        pass

    def getn_tex_image(self, target: int, level: int, format: int, type: int, buf_size: int, pixels: c_void_p):
        """
        Return a texture image

        Wrapper for glGetnTexImage

        Parameters
        ----------
        target: int
            Specifies the target to which the texture is bound for glGetTexImage and glGetnTexImage functions.
            GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_RECTANGLE, GL_TEXTURE_CUBE_MAP_POSITIVE_X, GL_TEXTURE_CUBE_MAP_NEGATIVE_X,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, GL_TEXTURE_CUBE_MAP_POSITIVE_Z,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, and GL_TEXTURE_CUBE_MAP_ARRAY are acceptable.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n
            is the n th mipmap reduction image.
        format: int
            Specifies a pixel format for the returned data. The supported formats are GL_STENCIL_INDEX,
            GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL, GL_RED, GL_GREEN, GL_BLUE, GL_RG, GL_RGB, GL_RGBA, GL_BGR,
            GL_BGRA, GL_RED_INTEGER, GL_GREEN_INTEGER, GL_BLUE_INTEGER, GL_RG_INTEGER, GL_RGB_INTEGER,
            GL_RGBA_INTEGER, GL_BGR_INTEGER, GL_BGRA_INTEGER.
        type: int
            Specifies a pixel type for the returned data. The supported types are GL_UNSIGNED_BYTE, GL_BYTE,
            GL_UNSIGNED_SHORT, GL_SHORT, GL_UNSIGNED_INT, GL_INT, GL_HALF_FLOAT, GL_FLOAT,
            GL_UNSIGNED_BYTE_3_3_2, GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5,
            GL_UNSIGNED_SHORT_5_6_5_REV, GL_UNSIGNED_SHORT_4_4_4_4, GL_UNSIGNED_SHORT_4_4_4_4_REV,
            GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV, GL_UNSIGNED_INT_8_8_8_8,
            GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, GL_UNSIGNED_INT_2_10_10_10_REV,
            GL_UNSIGNED_INT_24_8, GL_UNSIGNED_INT_10F_11F_11F_REV, GL_UNSIGNED_INT_5_9_9_9_REV, and
            GL_FLOAT_32_UNSIGNED_INT_24_8_REV.
        pixels: c_void_p
            Returns the texture image. Should be a pointer to an array of the type specified by type.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetTexImage and glGetnTexImage functions if target is not an
            accepted value. These include:
        GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_RECTANGLE, GL_TEXTURE_CUBE_MAP_POSITIVE_X,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Z, and GL_TEXTURE_CUBE_MAP_NEGATIVE_Z for glGetTexImage and
            glGetnTexImage functions.
        GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_RECTANGLE, and GL_TEXTURE_CUBE_MAP for glGetTextureImage
            function.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml
        """
        pass

    def get_texture_image(self, texture: int, level: int, format: int, type: int, buf_size: int, pixels: c_void_p):
        """
        Return a texture image

        Wrapper for glGetTextureImage

        Parameters
        ----------
        texture: int
            Specifies the texture object name.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n
            is the n th mipmap reduction image.
        format: int
            Specifies a pixel format for the returned data. The supported formats are GL_STENCIL_INDEX,
            GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL, GL_RED, GL_GREEN, GL_BLUE, GL_RG, GL_RGB, GL_RGBA, GL_BGR,
            GL_BGRA, GL_RED_INTEGER, GL_GREEN_INTEGER, GL_BLUE_INTEGER, GL_RG_INTEGER, GL_RGB_INTEGER,
            GL_RGBA_INTEGER, GL_BGR_INTEGER, GL_BGRA_INTEGER.
        type: int
            Specifies a pixel type for the returned data. The supported types are GL_UNSIGNED_BYTE, GL_BYTE,
            GL_UNSIGNED_SHORT, GL_SHORT, GL_UNSIGNED_INT, GL_INT, GL_HALF_FLOAT, GL_FLOAT,
            GL_UNSIGNED_BYTE_3_3_2, GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5,
            GL_UNSIGNED_SHORT_5_6_5_REV, GL_UNSIGNED_SHORT_4_4_4_4, GL_UNSIGNED_SHORT_4_4_4_4_REV,
            GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV, GL_UNSIGNED_INT_8_8_8_8,
            GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, GL_UNSIGNED_INT_2_10_10_10_REV,
            GL_UNSIGNED_INT_24_8, GL_UNSIGNED_INT_10F_11F_11F_REV, GL_UNSIGNED_INT_5_9_9_9_REV, and
            GL_FLOAT_32_UNSIGNED_INT_24_8_REV.
        pixels: c_void_p
            Returns the texture image. Should be a pointer to an array of the type specified by type.

        Raises
        ------
        GL_INVALID_ENUM is generated by glGetTexImage and glGetnTexImage functions if target is not an
            accepted value. These include:
        GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_RECTANGLE, GL_TEXTURE_CUBE_MAP_POSITIVE_X,
            GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
            GL_TEXTURE_CUBE_MAP_POSITIVE_Z, and GL_TEXTURE_CUBE_MAP_NEGATIVE_Z for glGetTexImage and
            glGetnTexImage functions.
        GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY,
            GL_TEXTURE_CUBE_MAP_ARRAY, GL_TEXTURE_RECTANGLE, and GL_TEXTURE_CUBE_MAP for glGetTextureImage
            function.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml
        """
        pass

    def get_texture_level_parameterfv(self, texture: int, level: int, pname: int, params: POINTER(c_float)):
        """
        Return texture parameter values for a specific level of detail

        Wrapper for glGetTextureLevelParameterfv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGetTextureLevelParameterfv and glGetTextureLevelParameteriv
            functions.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n
            is the n th mipmap reduction image.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_TEXTURE_WIDTH, GL_TEXTURE_HEIGHT,
            GL_TEXTURE_DEPTH, GL_TEXTURE_INTERNAL_FORMAT, GL_TEXTURE_RED_SIZE, GL_TEXTURE_GREEN_SIZE,
            GL_TEXTURE_BLUE_SIZE, GL_TEXTURE_ALPHA_SIZE, GL_TEXTURE_DEPTH_SIZE, GL_TEXTURE_COMPRESSED,
            GL_TEXTURE_COMPRESSED_IMAGE_SIZE, and GL_TEXTURE_BUFFER_OFFSET are accepted.
        params: POINTER(c_float)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glGetTextureLevelParameterfv and glGetTextureLevelParameteriv
            functions if texture is not the name of an existing texture object.
        GL_INVALID_ENUM is generated by glGetTexLevelParameterfv and glGetTexLevelParameteriv functions if
            target or pname is not an accepted value.
        GL_INVALID_VALUE is generated if level is less than 0.
        GL_INVALID_VALUE may be generated if level is greater than log 2 max, where max is the returned
            value of GL_MAX_TEXTURE_SIZE.
        GL_INVALID_VALUE is generated if target is GL_TEXTURE_BUFFER and level is not zero.
        GL_INVALID_OPERATION is generated if GL_TEXTURE_COMPRESSED_IMAGE_SIZE is queried on texture images
            with an uncompressed internal format or on proxy targets.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexLevelParameter.xhtml
        """
        pass

    def get_texture_level_parameteriv(self, texture: int, level: int, pname: int, params: POINTER(c_int)):
        """
        Return texture parameter values for a specific level of detail

        Wrapper for glGetTextureLevelParameteriv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGetTextureLevelParameterfv and glGetTextureLevelParameteriv
            functions.
        level: int
            Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n
            is the n th mipmap reduction image.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_TEXTURE_WIDTH, GL_TEXTURE_HEIGHT,
            GL_TEXTURE_DEPTH, GL_TEXTURE_INTERNAL_FORMAT, GL_TEXTURE_RED_SIZE, GL_TEXTURE_GREEN_SIZE,
            GL_TEXTURE_BLUE_SIZE, GL_TEXTURE_ALPHA_SIZE, GL_TEXTURE_DEPTH_SIZE, GL_TEXTURE_COMPRESSED,
            GL_TEXTURE_COMPRESSED_IMAGE_SIZE, and GL_TEXTURE_BUFFER_OFFSET are accepted.
        params: POINTER(c_int)
            Returns the requested data.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glGetTextureLevelParameterfv and glGetTextureLevelParameteriv
            functions if texture is not the name of an existing texture object.
        GL_INVALID_ENUM is generated by glGetTexLevelParameterfv and glGetTexLevelParameteriv functions if
            target or pname is not an accepted value.
        GL_INVALID_VALUE is generated if level is less than 0.
        GL_INVALID_VALUE may be generated if level is greater than log 2 max, where max is the returned
            value of GL_MAX_TEXTURE_SIZE.
        GL_INVALID_VALUE is generated if target is GL_TEXTURE_BUFFER and level is not zero.
        GL_INVALID_OPERATION is generated if GL_TEXTURE_COMPRESSED_IMAGE_SIZE is queried on texture images
            with an uncompressed internal format or on proxy targets.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexLevelParameter.xhtml
        """
        pass

    def get_texture_parameterfv(self, texture: int, pname: int, params: POINTER(c_float)):
        """
        Return texture parameter values

        Wrapper for glGetTextureParameterfv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGetTextureParameterfv, glGetTextureParameteriv,
            glGetTextureParameterIiv, and glGetTextureParameterIuiv functions.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_float)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_texture_parameteriv(self, texture: int, pname: int, params: POINTER(c_int)):
        """
        Return texture parameter values

        Wrapper for glGetTextureParameteriv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGetTextureParameterfv, glGetTextureParameteriv,
            glGetTextureParameterIiv, and glGetTextureParameterIuiv functions.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_int)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_texture_parameter_iiv(self, texture: int, pname: int, params: POINTER(c_int)):
        """
        Return texture parameter values

        Wrapper for glGetTextureParameterIiv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGetTextureParameterfv, glGetTextureParameteriv,
            glGetTextureParameterIiv, and glGetTextureParameterIuiv functions.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_int)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_texture_parameter_iuiv(self, texture: int, pname: int, params: POINTER(c_uint)):
        """
        Return texture parameter values

        Wrapper for glGetTextureParameterIuiv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glGetTextureParameterfv, glGetTextureParameteriv,
            glGetTextureParameterIiv, and glGetTextureParameterIuiv functions.
        pname: int
            Specifies the symbolic name of a texture parameter. GL_DEPTH_STENCIL_TEXTURE_MODE,
            GL_IMAGE_FORMAT_COMPATIBILITY_TYPE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_BORDER_COLOR,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_TEXTURE_IMMUTABLE_FORMAT,
            GL_TEXTURE_IMMUTABLE_LEVELS, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MAX_LEVEL,
            GL_TEXTURE_MAX_LOD, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_SWIZZLE_RGBA,
            GL_TEXTURE_TARGET, GL_TEXTURE_VIEW_MIN_LAYER, GL_TEXTURE_VIEW_MIN_LEVEL,
            GL_TEXTURE_VIEW_NUM_LAYERS, GL_TEXTURE_VIEW_NUM_LEVELS, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, and
            GL_TEXTURE_WRAP_R are accepted.
        params: POINTER(c_uint)
            Returns the texture parameters.

        Raises
        ------
        GL_INVALID_ENUM is generated if pname is not an accepted value.
        GL_INVALID_ENUM error is generated by glGetTexParameter if the effective target is not one of the
            accepted texture targets.
        GL_INVALID_OPERATION is generated by glGetTextureParameter* if texture is not the name of an
            existing texture object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml
        """
        pass

    def get_texture_sub_image(self, texture: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, type: int, buf_size: int, pixels: c_void_p):
        """
        Retrieve a sub-region of a texture image from a texture object

        Wrapper for glGetTextureSubImage

        Parameters
        ----------
        texture: int
            Specifies the name of the source texture object. Must be GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_ARRAY
            or GL_TEXTURE_RECTANGLE. In specific, buffer and multisample textures are not permitted.
        level: int
            Specifies the level-of-detail number. Level 0 is the base image level. Level $n$ is the $n$th
            mipmap reduction image.
        xoffset: int
            Specifies a texel offset in the x direction within the texture array.
        yoffset: int
            Specifies a texel offset in the y direction within the texture array.
        zoffset: int
            Specifies a texel offset in the z direction within the texture array.
        width: int
            Specifies the width of the texture subimage.
        height: int
            Specifies the height of the texture subimage.
        depth: int
            Specifies the depth of the texture subimage.
        format: int
            Specifies the format of the pixel data. The following symbolic values are accepted: GL_RED, GL_RG,
            GL_RGB, GL_BGR, GL_RGBA, GL_BGRA, GL_DEPTH_COMPONENT and GL_STENCIL_INDEX.
        type: int
            Specifies the data type of the pixel data. The following symbolic values are accepted:
            GL_UNSIGNED_BYTE, GL_BYTE, GL_UNSIGNED_SHORT, GL_SHORT, GL_UNSIGNED_INT, GL_INT, GL_FLOAT,
            GL_UNSIGNED_BYTE_3_3_2, GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5,
            GL_UNSIGNED_SHORT_5_6_5_REV, GL_UNSIGNED_SHORT_4_4_4_4, GL_UNSIGNED_SHORT_4_4_4_4_REV,
            GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV, GL_UNSIGNED_INT_8_8_8_8,
            GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, and GL_UNSIGNED_INT_2_10_10_10_REV.
        pixels: c_void_p
            Returns the texture subimage. Should be a pointer to an array of the type specified by type.

        Raises
        ------
        GL_INVALID_VALUE error is generated if texture is not the name of an existing texture object.
        GL_INVALID_OPERATION error is generated if texture is the name of a buffer or multisample texture.
        GL_INVALID_VALUE is generated if xoffset, yoffset or zoffset are negative.
        GL_INVALID_VALUE is generated if xoffset + width is greater than the texture's width, yoffset +
            height is greater than the texture's height, or zoffset + depth is greater than the texture's
            depth.
        GL_INVALID_VALUE error is generated if the effective target is GL_TEXTURE_1D and either yoffset is
            not zero, or height is not one.
        GL_INVALID_VALUE error is generated if the effective target is GL_TEXTURE_1D, GL_TEXTURE_1D_ARRAY,
            GL_TEXTURE_2D or GL_TEXTURE_RECTANGLE and either zoffset is not zero, or depth is not one.
        GL_INVALID_OPERATION error is generated if the buffer size required to store the requested data is
            greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTextureSubImage.xhtml
        """
        pass

    def get_transform_feedbackiv(self, xfb: int, pname: int, param: POINTER(c_int)):
        """
        Query the state of a transform feedback object.

        Wrapper for glGetTransformFeedbackiv

        Parameters
        ----------
        xfb: int
            The name of an existing transform feedback object, or zero for the default transform feedback
            object.
        pname: int
            Property to use for the query. Must be one of the values: GL_TRANSFORM_FEEDBACK_BUFFER_BINDING,
            GL_TRANSFORM_FEEDBACK_BUFFER_START, GL_TRANSFORM_FEEDBACK_BUFFER_SIZE,
            GL_TRANSFORM_FEEDBACK_PAUSED, GL_TRANSFORM_FEEDBACK_ACTIVE.
        param: POINTER(c_int)
            The address of a buffer into which will be written the requested state information.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if xfb is not zero or the name of an existing transform
            feedback object.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbackiv if pname is not
            GL_TRANSFORM_FEEDBACK_PAUSED or GL_TRANSFORM_FEEDBACK_ACTIVE.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbacki_v if pname is not
            GL_TRANSFORM_FEEDBACK_BUFFER_BINDING.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbacki64_v if pname is not
            GL_TRANSFORM_FEEDBACK_BUFFER_START or GL_TRANSFORM_FEEDBACK_BUFFER_SIZE.
        GL_INVALID_VALUE error is generated by glGetTransformFeedbacki_v and glGetTransformFeedbacki64_v if
            index is greater than or equal to the number of binding points for transform feedback (the value of
            GL_MAX_TRANSFORM_FEEDBACK_BUFFERS).

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTransformFeedback.xhtml
        """
        pass

    def get_transform_feedbacki_v(self, xfb: int, pname: int, index: int, param: POINTER(c_int)):
        """
        Query the state of a transform feedback object.

        Wrapper for glGetTransformFeedbacki_v

        Parameters
        ----------
        xfb: int
            The name of an existing transform feedback object, or zero for the default transform feedback
            object.
        pname: int
            Property to use for the query. Must be one of the values: GL_TRANSFORM_FEEDBACK_BUFFER_BINDING,
            GL_TRANSFORM_FEEDBACK_BUFFER_START, GL_TRANSFORM_FEEDBACK_BUFFER_SIZE,
            GL_TRANSFORM_FEEDBACK_PAUSED, GL_TRANSFORM_FEEDBACK_ACTIVE.
        index: int
            Index of the transform feedback stream (for indexed state).
        param: POINTER(c_int)
            The address of a buffer into which will be written the requested state information.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if xfb is not zero or the name of an existing transform
            feedback object.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbackiv if pname is not
            GL_TRANSFORM_FEEDBACK_PAUSED or GL_TRANSFORM_FEEDBACK_ACTIVE.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbacki_v if pname is not
            GL_TRANSFORM_FEEDBACK_BUFFER_BINDING.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbacki64_v if pname is not
            GL_TRANSFORM_FEEDBACK_BUFFER_START or GL_TRANSFORM_FEEDBACK_BUFFER_SIZE.
        GL_INVALID_VALUE error is generated by glGetTransformFeedbacki_v and glGetTransformFeedbacki64_v if
            index is greater than or equal to the number of binding points for transform feedback (the value of
            GL_MAX_TRANSFORM_FEEDBACK_BUFFERS).

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTransformFeedback.xhtml
        """
        pass

    def get_transform_feedbacki64_v(self, xfb: int, pname: int, index: int, param: POINTER(c_int64)):
        """
        Query the state of a transform feedback object.

        Wrapper for glGetTransformFeedbacki64_v

        Parameters
        ----------
        xfb: int
            The name of an existing transform feedback object, or zero for the default transform feedback
            object.
        pname: int
            Property to use for the query. Must be one of the values: GL_TRANSFORM_FEEDBACK_BUFFER_BINDING,
            GL_TRANSFORM_FEEDBACK_BUFFER_START, GL_TRANSFORM_FEEDBACK_BUFFER_SIZE,
            GL_TRANSFORM_FEEDBACK_PAUSED, GL_TRANSFORM_FEEDBACK_ACTIVE.
        index: int
            Index of the transform feedback stream (for indexed state).
        param: POINTER(c_int64)
            The address of a buffer into which will be written the requested state information.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if xfb is not zero or the name of an existing transform
            feedback object.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbackiv if pname is not
            GL_TRANSFORM_FEEDBACK_PAUSED or GL_TRANSFORM_FEEDBACK_ACTIVE.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbacki_v if pname is not
            GL_TRANSFORM_FEEDBACK_BUFFER_BINDING.
        GL_INVALID_ENUM error is generated by glGetTransformFeedbacki64_v if pname is not
            GL_TRANSFORM_FEEDBACK_BUFFER_START or GL_TRANSFORM_FEEDBACK_BUFFER_SIZE.
        GL_INVALID_VALUE error is generated by glGetTransformFeedbacki_v and glGetTransformFeedbacki64_v if
            index is greater than or equal to the number of binding points for transform feedback (the value of
            GL_MAX_TRANSFORM_FEEDBACK_BUFFERS).

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTransformFeedback.xhtml
        """
        pass

    def getn_uniformfv(self, program: int, location: int, buf_size: int, params: POINTER(c_float)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetnUniformfv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_float)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def getn_uniformiv(self, program: int, location: int, buf_size: int, params: POINTER(c_int)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetnUniformiv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_int)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def getn_uniformuiv(self, program: int, location: int, buf_size: int, params: POINTER(c_uint)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetnUniformuiv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_uint)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def getn_uniformdv(self, program: int, location: int, buf_size: int, params: POINTER(c_double)):
        """
        Returns the value of a uniform variable

        Wrapper for glGetnUniformdv

        Parameters
        ----------
        program: int
            Specifies the program object to be queried.
        location: int
            Specifies the location of the uniform variable to be queried.
        params: POINTER(c_double)
            Returns the value of the specified uniform variable.

        Raises
        ------
        GL_INVALID_VALUE is generated if program is not a value generated by OpenGL.
        GL_INVALID_OPERATION is generated if program is not a program object.
        GL_INVALID_OPERATION is generated if program has not been successfully linked.
        GL_INVALID_OPERATION is generated if location does not correspond to a valid uniform variable
            location for the specified program object.
        GL_INVALID_OPERATION is generated by glGetnUniform if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetUniform.xhtml
        """
        pass

    def get_vertex_array_indexed64iv(self, vaobj: int, index: int, pname: int, param: POINTER(c_int64)):
        """
        Retrieve parameters of an attribute of a vertex array object

        Wrapper for glGetVertexArrayIndexed64iv

        Parameters
        ----------
        vaobj: int
            Specifies the name of a vertex array object.
        index: int
            Specifies the index of the vertex array object attribute. Must be a number between 0 and
            (GL_MAX_VERTEX_ATTRIBS - 1).
        pname: int
            Specifies the property to be used for the query. For glGetVertexArrayIndexediv, it must be one of
            the following values: GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_LONG, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or
            GL_VERTEX_ATTRIB_RELATIVE_OFFSET. For glGetVertexArrayIndexed64v, it must be equal to
            GL_VERTEX_BINDING_OFFSET.
        param: POINTER(c_int64)
            Returns the requested value.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if vaobj is not the name of an existing vertex array
            object.
        GL_INVALID_VALUE error is generated if index is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM error is generated if pname is not one of the valid values. For more details,
            please see above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexArrayIndexed.xhtml
        """
        pass

    def get_vertex_array_indexediv(self, vaobj: int, index: int, pname: int, param: POINTER(c_int)):
        """
        Retrieve parameters of an attribute of a vertex array object

        Wrapper for glGetVertexArrayIndexediv

        Parameters
        ----------
        vaobj: int
            Specifies the name of a vertex array object.
        index: int
            Specifies the index of the vertex array object attribute. Must be a number between 0 and
            (GL_MAX_VERTEX_ATTRIBS - 1).
        pname: int
            Specifies the property to be used for the query. For glGetVertexArrayIndexediv, it must be one of
            the following values: GL_VERTEX_ATTRIB_ARRAY_ENABLED, GL_VERTEX_ATTRIB_ARRAY_SIZE,
            GL_VERTEX_ATTRIB_ARRAY_STRIDE, GL_VERTEX_ATTRIB_ARRAY_TYPE, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED,
            GL_VERTEX_ATTRIB_ARRAY_INTEGER, GL_VERTEX_ATTRIB_ARRAY_LONG, GL_VERTEX_ATTRIB_ARRAY_DIVISOR, or
            GL_VERTEX_ATTRIB_RELATIVE_OFFSET. For glGetVertexArrayIndexed64v, it must be equal to
            GL_VERTEX_BINDING_OFFSET.
        param: POINTER(c_int)
            Returns the requested value.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if vaobj is not the name of an existing vertex array
            object.
        GL_INVALID_VALUE error is generated if index is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_ENUM error is generated if pname is not one of the valid values. For more details,
            please see above.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexArrayIndexed.xhtml
        """
        pass

    def get_vertex_arrayiv(self, vaobj: int, pname: int, param: POINTER(c_int)):
        """
        Retrieve parameters of a vertex array object

        Wrapper for glGetVertexArrayiv

        Parameters
        ----------
        vaobj: int
            specifies the name of the vertex array object to use for the query.
        pname: int
            Name of the property to use for the query. Must be GL_ELEMENT_ARRAY_BUFFER_BINDING.
        param: POINTER(c_int)
            Returns the requested value.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if vaobj is not the name of an existing vertex array
            object.
        GL_INVALID_ENUM error is generated if pname is not GL_ELEMENT_ARRAY_BUFFER_BINDING.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetVertexArrayiv.xhtml
        """
        pass

    def invalidate_named_framebuffer_data(self, framebuffer: int, num_attachments: int, attachments: POINTER(c_uint32)):
        """
        Invalidate the content of some or all of a framebuffer's attachments

        Wrapper for glInvalidateNamedFramebufferData

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glInvalidateNamedFramebufferData.
        attachments: POINTER(c_uint32)
            Specifies a pointer to an array identifying the attachments to be invalidated.

        Raises
        ------
        GL_INVALID_ENUM is generated by glInvalidateFramebuffer if target is not one of the accepted
            framebuffer targets.
        GL_INVALID_OPERATION is generated by glInvalidateNamedFramebufferData if framebuffer is not zero or
            the name of an existing framebuffer object.
        GL_INVALID_VALUE is generated if numAttachments is negative.
        GL_INVALID_ENUM is generated if any element of attachments is not one of the accepted framebuffer
            attachment points, as described above.
        GL_INVALID_OPERATION is generated if element of attachments is GL_COLOR_ATTACHMENT m where m is
            greater than or equal to the value of GL_MAX_COLOR_ATTACHMENTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateFramebuffer.xhtml
        """
        pass

    def invalidate_named_framebuffer_sub_data(self, framebuffer: int, num_attachments: int, attachments: POINTER(c_uint32), x: int, y: int, width: int, height: int):
        """
        Invalidate the content of a region of some or all of a framebuffer's attachments

        Wrapper for glInvalidateNamedFramebufferSubData

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glInvalidateNamedFramebufferSubData.
        attachments: POINTER(c_uint32)
            Specifies a pointer to an array identifying the attachments to be invalidated.
        x: int
            Specifies the X offset of the region to be invalidated.
        y: int
            Specifies the Y offset of the region to be invalidated.
        width: int
            Specifies the width of the region to be invalidated.
        height: int
            Specifies the height of the region to be invalidated.

        Raises
        ------
        GL_INVALID_ENUM by glInvalidateSubFramebuffer if target is not one of the accepted framebuffer
            targets.
        GL_INVALID_OPERATION by glInvalidateNamedFramebufferSubData if framebuffer is not zero of the name
            of an existing framebuffer object.
        GL_INVALID_VALUE is generated if numAttachments, width or height is negative.
        GL_INVALID_ENUM is generated if any element of attachments is not one of the accepted framebuffer
            attachment points, as described above.
        GL_INVALID_OPERATION is generated if element of attachments is GL_COLOR_ATTACHMENT m where m is
            greater than or equal to the value of GL_MAX_COLOR_ATTACHMENTS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glInvalidateSubFramebuffer.xhtml
        """
        pass

    def map_named_buffer(self, buffer: int, access: int) -> c_void_p:
        """
        Map all of a buffer object's data store into the client's address space

        Wrapper for glMapNamedBuffer

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glMapNamedBuffer.
        access: int
            Specifies the access policy for glMapBuffer and glMapNamedBuffer, indicating whether it will be
            possible to read from, write to, or both read from and write to the buffer object's mapped data
            store. The symbolic constant must be GL_READ_ONLY, GL_WRITE_ONLY, or GL_READ_WRITE.

        Raises
        ------
        GL_INVALID_ENUM is generated by glMapBuffer if target is not one of the buffer binding targets
            listed above.
        GL_INVALID_OPERATION is generated by glMapBuffer if zero is bound to target.
        GL_INVALID_OPERATION is generated by glMapNamedBuffer if buffer is not the name of an existing
            buffer object.
        GL_INVALID_ENUM is generated if access is not GL_READ_ONLY, GL_WRITE_ONLY, or GL_READ_WRITE.
        GL_OUT_OF_MEMORY is generated if the GL is unable to map the buffer object's data store. This may
            occur for a variety of system-specific reasons, such as the absence of sufficient remaining virtual
            memory.
        GL_INVALID_OPERATION is generated if the buffer object is in a mapped state.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMapBuffer.xhtml
        """
        pass

    def map_named_buffer_range(self, buffer: int, offset: POINTER(c_int), length: int, access: int) -> c_void_p:
        """
        Map all or part of a buffer object's data store into the client's address space

        Wrapper for glMapNamedBufferRange

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glMapNamedBufferRange.
        offset: POINTER(c_int)
            Specifies the starting offset within the buffer of the range to be mapped.
        length: int
            Specifies the length of the range to be mapped.
        access: int
            Specifies a combination of access flags indicating the desired access to the mapped range.

        Raises
        ------
        GL_INVALID_ENUM is generated by glMapBufferRange if target is not one of the buffer binding targets
            listed above.
        GL_INVALID_OPERATION is generated by glMapBufferRange if zero is bound to target.
        GL_INVALID_OPERATION is generated by glMapNamedBufferRange if buffer is not the name of an existing
            buffer object.
        GL_INVALID_VALUE is generated if offset or length is negative, if $offset + length$ is greater than
            the value of GL_BUFFER_SIZE for the buffer object, or if access has any bits set other than those
            defined above.
        GL_INVALID_OPERATION is generated for any of the following conditions:
        length is zero.
        The buffer object is already in a mapped state.
        Neither GL_MAP_READ_BIT nor GL_MAP_WRITE_BIT is set.
        GL_MAP_READ_BIT is set and any of GL_MAP_INVALIDATE_RANGE_BIT, GL_MAP_INVALIDATE_BUFFER_BIT or
            GL_MAP_UNSYNCHRONIZED_BIT is set.
        GL_MAP_FLUSH_EXPLICIT_BIT is set and GL_MAP_WRITE_BIT is not set.
        Any of GL_MAP_READ_BIT, GL_MAP_WRITE_BIT, GL_MAP_PERSISTENT_BIT, or GL_MAP_COHERENT_BIT are set,
            but the same bit is not included in the buffer's storage flags.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMapBufferRange.xhtml
        """
        pass

    def memory_barrier_by_region(self, barriers: int):
        """
        Defines a barrier ordering memory transactions

        Wrapper for glMemoryBarrierByRegion

        Parameters
        ----------
        barriers: int
            Specifies the barriers to insert. For glMemoryBarrier, must be a bitwise combination of any of
            GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT, GL_ELEMENT_ARRAY_BARRIER_BIT, GL_UNIFORM_BARRIER_BIT,
            GL_TEXTURE_FETCH_BARRIER_BIT, GL_SHADER_IMAGE_ACCESS_BARRIER_BIT, GL_COMMAND_BARRIER_BIT,
            GL_PIXEL_BUFFER_BARRIER_BIT, GL_TEXTURE_UPDATE_BARRIER_BIT, GL_BUFFER_UPDATE_BARRIER_BIT,
            GL_FRAMEBUFFER_BARRIER_BIT, GL_TRANSFORM_FEEDBACK_BARRIER_BIT, GL_ATOMIC_COUNTER_BARRIER_BIT, or
            GL_SHADER_STORAGE_BARRIER_BIT. For glMemoryBarrier, must be a bitwise combination of any of
            GL_ATOMIC_COUNTER_BARRIER_BIT, or GL_FRAMEBUFFER_BARRIER_BIT, GL_SHADER_IMAGE_ACCESS_BARRIER_BIT,
            GL_SHADER_STORAGE_BARRIER_BIT. GL_TEXTURE_FETCH_BARRIER_BIT, or GL_UNIFORM_BARRIER_BIT. If the
            special value GL_ALL_BARRIER_BITS is specified, all supported barriers for the corresponding
            command will be inserted.

        Raises
        ------
        GL_INVALID_VALUE is generated if barriers is not the special value GL_ALL_BARRIER_BITS, and has any
            bits set other than those described above for glMemoryBarrier or glMemoryBarrierByRegion
            respectively.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glMemoryBarrier.xhtml
        """
        pass

    def named_framebuffer_read_buffer(self, framebuffer: int, mode: int):
        """
        Select a color buffer source for pixels

        Wrapper for glNamedFramebufferReadBuffer

        Parameters
        ----------
        framebuffer: int
            Specifies the name of the framebuffer object for glNamedFramebufferReadBuffer function.
        mode: int
            Specifies a color buffer. Accepted values are GL_FRONT_LEFT, GL_FRONT_RIGHT, GL_BACK_LEFT,
            GL_BACK_RIGHT, GL_FRONT, GL_BACK, GL_LEFT, GL_RIGHT, and the constants GL_COLOR_ATTACHMENT i.

        Raises
        ------
        GL_INVALID_ENUM is generated if mode is not one of the twelve (or more) accepted values.
        GL_INVALID_OPERATION is generated if mode specifies a buffer that does not exist.
        GL_INVALID_OPERATION is generated by glNamedFramebufferReadBuffer if framebuffer is not zero or the
            name of an existing framebuffer object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glReadBuffer.xhtml
        """
        pass

    def readn_pixels(self, x: int, y: int, width: int, height: int, format: int, type: int, buf_size: int, data: c_void_p):
        """
        Read a block of pixels from the frame buffer

        Wrapper for glReadnPixels

        Parameters
        ----------
        x, y: int
            Specify the window coordinates of the first pixel that is read from the frame buffer. This location
            is the lower left corner of a rectangular block of pixels.
        width, height: int
            Specify the dimensions of the pixel rectangle. width and height of one correspond to a single
            pixel.
        format: int
            Specifies the format of the pixel data. The following symbolic values are accepted:
            GL_STENCIL_INDEX, GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL, GL_RED, GL_GREEN, GL_BLUE, GL_RGB, GL_BGR,
            GL_RGBA, and GL_BGRA.
        type: int
            Specifies the data type of the pixel data. Must be one of GL_UNSIGNED_BYTE, GL_BYTE,
            GL_UNSIGNED_SHORT, GL_SHORT, GL_UNSIGNED_INT, GL_INT, GL_HALF_FLOAT, GL_FLOAT,
            GL_UNSIGNED_BYTE_3_3_2, GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5,
            GL_UNSIGNED_SHORT_5_6_5_REV, GL_UNSIGNED_SHORT_4_4_4_4, GL_UNSIGNED_SHORT_4_4_4_4_REV,
            GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV, GL_UNSIGNED_INT_8_8_8_8,
            GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, GL_UNSIGNED_INT_2_10_10_10_REV,
            GL_UNSIGNED_INT_24_8, GL_UNSIGNED_INT_10F_11F_11F_REV, GL_UNSIGNED_INT_5_9_9_9_REV, or
            GL_FLOAT_32_UNSIGNED_INT_24_8_REV.
        data: c_void_p
            Returns the pixel data.

        Raises
        ------
        GL_INVALID_ENUM is generated if format or type is not an accepted value.
        GL_INVALID_VALUE is generated if either width or height is negative.
        GL_INVALID_OPERATION is generated if format is GL_STENCIL_INDEX and there is no stencil buffer.
        GL_INVALID_OPERATION is generated if format is GL_DEPTH_COMPONENT and there is no depth buffer.
        GL_INVALID_OPERATION is generated if format is GL_DEPTH_STENCIL and there is no depth buffer or if
            there is no stencil buffer.
        GL_INVALID_ENUM is generated if format is GL_DEPTH_STENCIL and type is not GL_UNSIGNED_INT_24_8 or
            GL_FLOAT_32_UNSIGNED_INT_24_8_REV.
        GL_INVALID_OPERATION is generated if type is one of GL_UNSIGNED_BYTE_3_3_2,
            GL_UNSIGNED_BYTE_2_3_3_REV, GL_UNSIGNED_SHORT_5_6_5, or GL_UNSIGNED_SHORT_5_6_5_REV and format is
            not GL_RGB.
        GL_INVALID_OPERATION is generated if type is one of GL_UNSIGNED_SHORT_4_4_4_4,
            GL_UNSIGNED_SHORT_4_4_4_4_REV, GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_1_5_5_5_REV,
            GL_UNSIGNED_INT_8_8_8_8, GL_UNSIGNED_INT_8_8_8_8_REV, GL_UNSIGNED_INT_10_10_10_2, or
            GL_UNSIGNED_INT_2_10_10_10_REV and format is neither GL_RGBA nor GL_BGRA.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and the buffer object's data store is currently mapped.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and the data would be packed to the buffer object such that the memory
            writes required would exceed the data store size.
        GL_INVALID_OPERATION is generated if a non-zero buffer object name is bound to the
            GL_PIXEL_PACK_BUFFER target and data is not evenly divisible into the number of bytes needed to
            store in memory a datum indicated by type.
        GL_INVALID_OPERATION is generated if GL_READ_FRAMEBUFFER_BINDING is non-zero, the read framebuffer
            is complete, and the value of GL_SAMPLE_BUFFERS for the read framebuffer is greater than zero.
        GL_INVALID_OPERATION is generated by glReadnPixels if the buffer size required to store the
            requested data is greater than bufSize.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glReadPixels.xhtml
        """
        pass

    def named_renderbuffer_storage(self, renderbuffer: int, internalformat: int, width: int, height: int):
        """
        Establish data storage, format and dimensions of a renderbuffer object's image

        Wrapper for glNamedRenderbufferStorage

        Parameters
        ----------
        renderbuffer: int
            Specifies the name of the renderbuffer object for glNamedRenderbufferStorage function.
        internalformat: int
            Specifies the internal format to use for the renderbuffer object's image.
        width: int
            Specifies the width of the renderbuffer, in pixels.
        height: int
            Specifies the height of the renderbuffer, in pixels.

        Raises
        ------
        GL_INVALID_ENUM is generated by glRenderbufferStorage if target is not GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated by glNamedRenderbufferStorage if renderbuffer is not the name of
            an existing renderbuffer object.
        GL_INVALID_VALUE is generated if either of width or height is negative, or greater than the value
            of GL_MAX_RENDERBUFFER_SIZE.
        GL_INVALID_ENUM is generated if internalformat is not a color-renderable, depth-renderable, or
            stencil-renderable format.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store of the requested size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glRenderbufferStorage.xhtml
        """
        pass

    def named_renderbuffer_storage_multisample(self, renderbuffer: int, samples: int, internalformat: int, width: int, height: int):
        """
        Establish data storage, format, dimensions and sample count of a renderbuffer object's image

        Wrapper for glNamedRenderbufferStorageMultisample

        Parameters
        ----------
        renderbuffer: int
            Specifies the name of the renderbuffer object for glNamedRenderbufferStorageMultisample function.
        samples: int
            Specifies the number of samples to be used for the renderbuffer object's storage.
        internalformat: int
            Specifies the internal format to use for the renderbuffer object's image.
        width: int
            Specifies the width of the renderbuffer, in pixels.
        height: int
            Specifies the height of the renderbuffer, in pixels.

        Raises
        ------
        GL_INVALID_ENUM is generated by glRenderbufferStorageMultisample function if target is not
            GL_RENDERBUFFER.
        GL_INVALID_OPERATION is generated by glNamedRenderbufferStorageMultisample function if renderbuffer
            is not the name of an existing renderbuffer object.
        GL_INVALID_OPERATION is generated if samples is greater than the maximum number of samples
            supported for internalformat.
        GL_INVALID_ENUM is generated if internalformat is not a color-renderable, depth-renderable, or
            stencil-renderable format.
        GL_INVALID_OPERATION is generated if internalformat is a signed or unsigned integer format and
            samples is greater than the value of GL_MAX_INTEGER_SAMPLES
        GL_INVALID_VALUE is generated if either of width or height is negative, or greater than the value
            of GL_MAX_RENDERBUFFER_SIZE.
        GL_OUT_OF_MEMORY is generated if the GL is unable to create a data store of the requested size.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glRenderbufferStorageMultisample.xhtml
        """
        pass

    def texture_buffer(self, texture: int, internalformat: int, buffer: int):
        """
        Attach a buffer object's data store to a buffer texture object

        Wrapper for glTextureBuffer

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureBuffer.
        buffer: int
            Specifies the name of the buffer object whose storage to attach to the active buffer texture.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexBuffer if target is not GL_TEXTURE_BUFFER.
        GL_INVALID_OPERATION is generated by glTextureBuffer if texture is not the name of an existing
            texture object.
        GL_INVALID_ENUM is generated by glTextureBuffer if the effective target of texture is not
            GL_TEXTURE_BUFFER.
        GL_INVALID_ENUM is generated if internalformat is not one of the sized internal formats described
            above.
        GL_INVALID_OPERATION is generated if buffer is not zero and is not the name of an existing buffer
            object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexBuffer.xhtml
        """
        pass

    def texture_buffer_range(self, texture: int, internalformat: int, buffer: int, offset: POINTER(c_int), size: int):
        """
        Attach a range of a buffer object's data store to a buffer texture object

        Wrapper for glTextureBufferRange

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureBufferRange.
        buffer: int
            Specifies the name of the buffer object whose storage to attach to the active buffer texture.
        offset: POINTER(c_int)
            Specifies the offset of the start of the range of the buffer's data store to attach.
        size: int
            Specifies the size of the range of the buffer's data store to attach.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexBufferRange if target is not GL_TEXTURE_BUFFER.
        GL_INVALID_OPERATION is generated by glTextureBufferRange if texture is not the name of an existing
            texture object.
        GL_INVALID_ENUM is generated by glTextureBufferRange if the effective target of texture is not
            GL_TEXTURE_BUFFER.
        GL_INVALID_ENUM is generated if internalformat is not one of the sized internal formats described
            above.
        GL_INVALID_OPERATION is generated if buffer is not zero and is not the name of an existing buffer
            object.
        GL_INVALID_VALUE is generated if offset is negative, if size is less than or equal to zero, or if
            offset + size is greater than the value of GL_BUFFER_SIZE for buffer.
        GL_INVALID_VALUE is generated if offset is not an integer multiple of the value of
            GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexBufferRange.xhtml
        """
        pass

    def texture_parameterf(self, texture: int, pname: int, param: float):
        """
        Set texture parameters

        Wrapper for glTextureParameterf

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureParameter functions.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        param: float
            For the scalar commands, specifies the value of pname.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def texture_parameteri(self, texture: int, pname: int, param: int):
        """
        Set texture parameters

        Wrapper for glTextureParameteri

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureParameter functions.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        param: int
            For the scalar commands, specifies the value of pname.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def texture_parameterfv(self, texture: int, pname: int, paramtexture: POINTER(c_float)):
        """
        Set texture parameters

        Wrapper for glTextureParameterfv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureParameter functions.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def texture_parameteriv(self, texture: int, pname: int, param: POINTER(c_int)):
        """
        Set texture parameters

        Wrapper for glTextureParameteriv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureParameter functions.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        param: POINTER(c_int)
            For the scalar commands, specifies the value of pname.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def texture_parameter_iiv(self, texture: int, pname: int, params: POINTER(c_int)):
        """
        Set texture parameters

        Wrapper for glTextureParameterIiv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureParameter functions.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        params: POINTER(c_int)
            For the vector commands, specifies a pointer to an array where the value or values of pname are
            stored.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def texture_parameter_iuiv(self, texture: int, pname: int, params: POINTER(c_uint)):
        """
        Set texture parameters

        Wrapper for glTextureParameterIuiv

        Parameters
        ----------
        texture: int
            Specifies the texture object name for glTextureParameter functions.
        pname: int
            Specifies the symbolic name of a single-valued texture parameter. pname can be one of the
            following: GL_DEPTH_STENCIL_TEXTURE_MODE, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_COMPARE_FUNC,
            GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_LOD_BIAS, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER,
            GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_SWIZZLE_R,
            GL_TEXTURE_SWIZZLE_G, GL_TEXTURE_SWIZZLE_B, GL_TEXTURE_SWIZZLE_A, GL_TEXTURE_WRAP_S,
            GL_TEXTURE_WRAP_T, or GL_TEXTURE_WRAP_R. For the vector commands (glTexParameter*v), pname can also
            be one of GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA.
        params: POINTER(c_uint)
            For the vector commands, specifies a pointer to an array where the value or values of pname are
            stored.

        Raises
        ------
        GL_INVALID_ENUM is generated by glTexParameter if target is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if pname is not one of the accepted defined values.
        GL_INVALID_ENUM is generated if params should have a defined constant value (based on the value of
            pname) and does not.
        GL_INVALID_ENUM is generated if glTexParameter{if} or glTextureParameter{if} is called for a
            non-scalar parameter (pname GL_TEXTURE_BORDER_COLOR or GL_TEXTURE_SWIZZLE_RGBA).
        GL_INVALID_ENUM is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname is any of the sampler states.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and either of pnames
            GL_TEXTURE_WRAP_S or GL_TEXTURE_WRAP_T is set to either GL_MIRROR_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT
            or GL_REPEAT.
        GL_INVALID_ENUM is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_MIN_FILTER is set to a value other than GL_NEAREST or GL_LINEAR (no mipmap filtering is
            permitted).
        GL_INVALID_OPERATION is generated if the effective target is either GL_TEXTURE_2D_MULTISAMPLE or
            GL_TEXTURE_2D_MULTISAMPLE_ARRAY, and pname GL_TEXTURE_BASE_LEVEL is set to a value other than zero.
        GL_INVALID_OPERATION is generated by glTextureParameter if texture is not the name of an existing
            texture object.
        GL_INVALID_OPERATION is generated if the effective target is GL_TEXTURE_RECTANGLE and pname
            GL_TEXTURE_BASE_LEVEL is set to any value other than zero.
        GL_INVALID_VALUE is generated if pname is GL_TEXTURE_BASE_LEVEL or GL_TEXTURE_MAX_LEVEL, and param
            or params is negative.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml
        """
        pass

    def texture_barrier(self):
        """
        Controls the ordering of reads and writes to rendered fragments across drawing commands

        Wrapper for glTextureBarrier

        Raises
        ------
        None.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTextureBarrier.xhtml
        """
        pass

    def transform_feedback_buffer_base(self, xfb: int, index: int, buffer: int):
        """
        Bind a buffer object to a transform feedback buffer object

        Wrapper for glTransformFeedbackBufferBase

        Parameters
        ----------
        xfb: int
            Name of the transform feedback buffer object.
        index: int
            Index of the binding point within xfb.
        buffer: int
            Name of the buffer object to bind to the specified binding point.

        Raises
        ------
        GL_INVALID_OPERATION is generated if xfb is not the name of an existing transform feedback object.
        GL_INVALID_VALUE is generated if in buffer is not zero or the name of an existing buffer object.
        GL_INVALID_VALUE is generated if index is greater than or equal to the number of transform feedback
            buffer binding points (the value of GL_TRANSFORM_FEEDBACK_BUFFER_BINDING).

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTransformFeedbackBufferBase.xhtml
        """
        pass

    def transform_feedback_buffer_range(self, xfb: int, index: int, buffer: int, offset: POINTER(c_int), size: int):
        """
        Bind a range within a buffer object to a transform feedback buffer object

        Wrapper for glTransformFeedbackBufferRange

        Parameters
        ----------
        xfb: int
            Name of the transform feedback buffer object.
        index: int
            Index of the binding point within xfb.
        buffer: int
            Name of the buffer object to bind to the specified binding point.
        offset: POINTER(c_int)
            The starting offset in basic machine units into the buffer object.
        size: int
            The amount of data in basic machine units that can be read from or written to the buffer object
            while used as an indexed target.

        Raises
        ------
        GL_INVALID_OPERATION is generated if xfb is not the name of an existing transform feedback object.
        GL_INVALID_VALUE is generated if in buffer is not zero or the name of an existing buffer object.
        GL_INVALID_VALUE is generated if index is greater than or equal to the number of transform feedback
            buffer binding points (the value of GL_TRANSFORM_FEEDBACK_BUFFER_BINDING).
        GL_INVALID_VALUE is generated if offset is negative.
        GL_INVALID_VALUE is generated if buffer is non-zero and either size is less than or equal to zero,
            or offset + size is greater than the value of GL_BUFFER_SIZE for buffer.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glTransformFeedbackBufferRange.xhtml
        """
        pass

    def unmap_named_buffer(self, buffer: int) -> bool:
        """
        Release the mapping of a buffer object's data store into the client's address space

        Wrapper for glUnmapNamedBuffer

        Parameters
        ----------
        buffer: int
            Specifies the name of the buffer object for glUnmapNamedBuffer.

        Raises
        ------
        GL_INVALID_ENUM is generated by glUnmapBuffer if target is not one of the buffer binding targets
            listed above.
        GL_INVALID_OPERATION is generated by glUnmapBuffer if zero is bound to target.
        GL_INVALID_OPERATION is generated by glUnmapNamedBuffer if buffer is not the name of an existing
            buffer object.
        GL_INVALID_OPERATION is generated if the buffer object is not in a mapped state.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glUnmapBuffer.xhtml
        """
        pass

    def vertex_array_element_buffer(self, vaobj: int, buffer: int):
        """
        Configures element array buffer binding of a vertex array object

        Wrapper for glVertexArrayElementBuffer

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object.
        buffer: int
            Specifies the name of the buffer object to use for the element array buffer binding.

        Raises
        ------
        GL_INVALID_OPERATION error is generated if vaobj is not the name of an existing vertex array
            object.
        GL_INVALID_OPERATION error is generated if buffer is not zero or the name of an existing buffer
            object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexArrayElementBuffer.xhtml
        """
        pass

    def vertex_array_attrib_binding(self, vaobj: int, attribindex: int, bindingindex: int):
        """
        Associate a vertex attribute and a vertex buffer binding for a vertex array object

        Wrapper for glVertexArrayAttribBinding

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glVertexArrayAttribBinding.
        attribindex: int
            The index of the attribute to associate with a vertex buffer binding.
        bindingindex: int
            The index of the vertex buffer binding with which to associate the generic vertex attribute.

        Raises
        ------
        GL_INVALID_OPERATION is generated by glVertexAttribBinding if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribBinding if vaobj is not the name of an
            existing vertex array object.
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if bindingindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribBinding.xhtml
        """
        pass

    def vertex_array_attrib_format(self, vaobj: int, attribindex: int, size: int, type: int, normalized: bool, relativeoffset: int):
        """
        Specify the organization of vertex arrays

        Wrapper for glVertexArrayAttribFormat

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glVertexArrayAttrib{I, L}Format functions.
        attribindex: int
            The generic vertex attribute array being described.
        size: int
            The number of values per vertex that are stored in the array.
        type: int
            The type of the data stored in the array.
        normalized: bool
            Specifies whether fixed-point data values should be normalized (GL_TRUE) or converted directly as
            fixed-point values (GL_FALSE) when they are accessed. This parameter is ignored if type is
            GL_FIXED.
        relativeoffset: int
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not one of the accepted values.
        GL_INVALID_VALUE is generated if relativeoffset is greater than the value of
            GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET.
        GL_INVALID_ENUM is generated if type is not one of the accepted tokens.
        GL_INVALID_ENUM is generated by glVertexAttribIFormat, glVertexAttribLFormat,
            glVertexArrayAttribIFormat and glVertexArrayAttribLFormat if type is
            GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_OPERATION is generated by glVertexAttribFormat, glVertexAttribIFormat and
            glVertexAttribLFormat if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribFormat, glVertexArrayAttribIFormat and
            glVertexArrayAttribLFormat if vaobj is not the name of an existing vertex array object.
        GL_INVALID_OPERATION is generated under any of the following conditions:
        size is GL_BGRA and type is not GL_UNSIGNED_BYTE, GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV.
        type is GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, and size is neither 4 nor GL_BGRA.
        type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        size is GL_BGRA and normalized is GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribFormat.xhtml
        """
        pass

    def vertex_array_attrib_iformat(self, vaobj: int, attribindex: int, size: int, type: int, relativeoffset: int):
        """
        Specify the organization of vertex arrays

        Wrapper for glVertexArrayAttribIFormat

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glVertexArrayAttrib{I, L}Format functions.
        attribindex: int
            The generic vertex attribute array being described.
        size: int
            The number of values per vertex that are stored in the array.
        type: int
            The type of the data stored in the array.
        relativeoffset: int
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not one of the accepted values.
        GL_INVALID_VALUE is generated if relativeoffset is greater than the value of
            GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET.
        GL_INVALID_ENUM is generated if type is not one of the accepted tokens.
        GL_INVALID_ENUM is generated by glVertexAttribIFormat, glVertexAttribLFormat,
            glVertexArrayAttribIFormat and glVertexArrayAttribLFormat if type is
            GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_OPERATION is generated by glVertexAttribFormat, glVertexAttribIFormat and
            glVertexAttribLFormat if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribFormat, glVertexArrayAttribIFormat and
            glVertexArrayAttribLFormat if vaobj is not the name of an existing vertex array object.
        GL_INVALID_OPERATION is generated under any of the following conditions:
        size is GL_BGRA and type is not GL_UNSIGNED_BYTE, GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV.
        type is GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, and size is neither 4 nor GL_BGRA.
        type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        size is GL_BGRA and normalized is GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribFormat.xhtml
        """
        pass

    def vertex_array_attrib_lformat(self, vaobj: int, attribindex: int, size: int, type: int, relativeoffset: int):
        """
        Specify the organization of vertex arrays

        Wrapper for glVertexArrayAttribLFormat

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glVertexArrayAttrib{I, L}Format functions.
        attribindex: int
            The generic vertex attribute array being described.
        size: int
            The number of values per vertex that are stored in the array.
        type: int
            The type of the data stored in the array.
        relativeoffset: int
            The distance between elements within the buffer.

        Raises
        ------
        GL_INVALID_VALUE is generated if attribindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIBS.
        GL_INVALID_VALUE is generated if size is not one of the accepted values.
        GL_INVALID_VALUE is generated if relativeoffset is greater than the value of
            GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET.
        GL_INVALID_ENUM is generated if type is not one of the accepted tokens.
        GL_INVALID_ENUM is generated by glVertexAttribIFormat, glVertexAttribLFormat,
            glVertexArrayAttribIFormat and glVertexArrayAttribLFormat if type is
            GL_UNSIGNED_INT_10F_11F_11F_REV.
        GL_INVALID_OPERATION is generated by glVertexAttribFormat, glVertexAttribIFormat and
            glVertexAttribLFormat if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayAttribFormat, glVertexArrayAttribIFormat and
            glVertexArrayAttribLFormat if vaobj is not the name of an existing vertex array object.
        GL_INVALID_OPERATION is generated under any of the following conditions:
        size is GL_BGRA and type is not GL_UNSIGNED_BYTE, GL_INT_2_10_10_10_REV or
            GL_UNSIGNED_INT_2_10_10_10_REV.
        type is GL_INT_2_10_10_10_REV or GL_UNSIGNED_INT_2_10_10_10_REV, and size is neither 4 nor GL_BGRA.
        type is GL_UNSIGNED_INT_10F_11F_11F_REV and size is not 3.
        size is GL_BGRA and normalized is GL_FALSE.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexAttribFormat.xhtml
        """
        pass

    def vertex_array_binding_divisor(self, vaobj: int, bindingindex: int, divisor: int):
        """
        Modify the rate at which generic vertex attributes advance

        Wrapper for glVertexArrayBindingDivisor

        Parameters
        ----------
        vaobj: int
            Specifies the name of the vertex array object for glVertexArrayBindingDivisor function.
        bindingindex: int
            The index of the binding whose divisor to modify.
        divisor: int
            The new value for the instance step rate to apply.

        Raises
        ------
        GL_INVALID_VALUE is generated if bindingindex is greater than or equal to the value of
            GL_MAX_VERTEX_ATTRIB_BINDINGS.
        GL_INVALID_OPERATION by glVertexBindingDivisor is generated if no vertex array object is bound.
        GL_INVALID_OPERATION is generated by glVertexArrayBindingDivisor if vaobj is not the name of an
            existing vertex array object.

        Notes
        -----
        https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glVertexBindingDivisor.xhtml
        """
        pass


GL_ANY = Union[GL20, GL21, GL30, GL31, GL32, GL33, GL40, GL41, GL42, GL43, GL44, GL45]