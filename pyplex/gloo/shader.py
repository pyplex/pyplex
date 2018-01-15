from pyplex import gl
from pyplex.gloo import Object


class ShaderCompileError(Exception):
    """Shader Compile Error"""
    pass


class Shader(Object):
    def __init__(self, ctx: gl.Context, type: gl.ShaderType, source: str):
        """
        Create Shader

        Parameters
        ----------
        ctx: gl.Context
        type: gl.ShaderType
        source: str
        """
        self._ctx = ctx
        self._type = type
        self._source = source

        # Create and Compile Shader
        self._ptr = self.ctx.create_shader(type)
        self.ctx.shader_source(self._ptr, source)
        self.ctx.compile_shader(self._ptr)

        # if Shader has errors -> throw ShaderCompileError
        if not self.ctx.shader_parameter(self._ptr, gl.ShaderParameter.COMPILE_STATUS):
            raise ShaderCompileError(self.log)

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
    def ptr(self) -> gl.Shader:
        """
        Returns
        -------
        ptr: gl.Shader
            Pointer to OpenGL Shader object
        """
        return self._ptr

    @property
    def type(self) -> gl.ShaderType:
        """
        Returns
        -------
        type: gl.ShaderType
            Shader Type
        """
        return self._type

    @property
    def source(self) -> str:
        """
        Returns
        -------
        source: str
            Shader Source
        """
        return self._source

    @property
    def log(self) -> str:
        """
        Returns
        -------
        log: str
            Shader Info Log
        """
        return self.ctx.shader_info_log(self._ptr)

    def delete(self):
        self.ctx.delete_shader(self.ptr)


class VertexShader(Shader):
    def __init__(self, ctx: gl.Context, source: str):
        """
        Create Vertex Shader

        Parameters
        ----------
        ctx: gl.Context
        source: str
        """
        super().__init__(ctx, gl.ShaderType.VERTEX_SHADER, source)


class FragmentShader(Shader):
    def __init__(self, ctx: gl.Context, source: str):
        """
        Create Fragment Shader

        Parameters
        ----------
        ctx: gl.Context
        source: str
        """
        super().__init__(ctx, gl.ShaderType.FRAGMENT_SHADER, source)


class GeometryShader(Shader):
    def __init__(self, ctx: gl.Context, source: str):
        """
        Create Geometry Shader

        Parameters
        ----------
        ctx: gl.Context
        source: str
        """
        super().__init__(ctx, gl.ShaderType.GEOMETRY_SHADER, source)


class TessControlShader(Shader):
    def __init__(self, ctx: gl.Context, source: str):
        """
        Create Tessellation Control Shader

        Parameters
        ----------
        ctx: gl.Context
        source: str
        """
        super().__init__(ctx, gl.ShaderType.TESS_CONTROL_SHADER, source)


class TessEvaluationShader(Shader):
    def __init__(self, ctx: gl.Context, source: str):
        """
        Create Tessellation Evaluation Shader

        Parameters
        ----------
        ctx: gl.Context
        source: str
        """
        super().__init__(ctx, gl.ShaderType.TESS_EVALUATION_SHADER, source)


class ComputeShader(Shader):
    def __init__(self, ctx: gl.Context, source: str):
        """
        Create Compute Shader

        Parameters
        ----------
        ctx: gl.Context
        source: str
        """
        super().__init__(ctx, gl.ShaderType.COMPUTE_SHADER, source)
