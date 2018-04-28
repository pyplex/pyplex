from pyplex import gl
from ctypes import *

from typing import List


class CompilationError(Exception):
    pass


class Shader:

    SOURCE_EXTENSION = '.glsl'

    def __init__(self, ctx: gl.GL20, type: gl.ShaderType, *sources: str):
        self._ctx = ctx
        self._type = type

        self._paths = [source if source.endswith(Shader.SOURCE_EXTENSION) else None for source in sources]
        self._sources = [self._read(source) if path else source for (source, path) in zip(sources, self.paths)]

        self._ptr = self._ctx.create_shader(type)

        source_buffer = (c_char_p * len(self.sources))()
        length_buffer = (c_int * len(self.sources))()

        for i, source in enumerate(self.sources):
            source_buffer[i] = c_char_p(source.encode())
            length_buffer[i] = c_int(len(source))

        self._ctx.shader_source(self._ptr, len(self.sources), source_buffer, length_buffer)

        self._ctx.compile_shader(self._ptr)

        if not self._parameter(gl.ShaderParameter.COMPILE_STATUS):
            raise CompilationError(self.log())

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def type(self) -> gl.ShaderType:
        return self._type

    @property
    def paths(self) -> List[str]:
        return self._paths

    @property
    def sources(self) -> List[str]:
        return self._sources

    def log(self):
        log_length = self._parameter(gl.ShaderParameter.INFO_LOG_LENGTH)
        result = bytes(log_length - 1)
        self._ctx.get_shader_info_log(self._ptr, log_length, None, result)
        return result.decode()

    def delete(self):
        self._ctx.delete_shader(self._ptr)

    def _parameter(self, parameter: gl.ShaderParameter) -> int:
        result = c_int(0)
        self._ctx.get_shaderiv(self._ptr, parameter, pointer(result))
        return result.value

    def _read(self, path: str):
        with open(path) as source_file:
            return source_file.read()


class VertexShader(Shader):
    def __init__(self, ctx: gl.GL20, *sources: str):
        super().__init__(ctx, gl.ShaderType.VERTEX, *sources)


class FragmentShader(Shader):
    def __init__(self, ctx: gl.GL20, *sources: str):
        super().__init__(ctx, gl.ShaderType.FRAGMENT, *sources)


class GeometryShader(Shader):
    def __init__(self, ctx: gl.GL20, *sources: str):
        super().__init__(ctx, gl.ShaderType.GEOMETRY, *sources)


class TessControlShader(Shader):
    def __init__(self, ctx: gl.GL20, *sources: str):
        super().__init__(ctx, gl.ShaderType.TESS_CONTROL, *sources)


class TessEvaluationShader(Shader):
    def __init__(self, ctx: gl.GL20, *sources: str):
        super().__init__(ctx, gl.ShaderType.TESS_EVALUATION, *sources)


class ComputeShader(Shader):
    def __init__(self, ctx: gl.GL20, *sources: str):
        super().__init__(ctx, gl.ShaderType.VERTEX, *sources)
