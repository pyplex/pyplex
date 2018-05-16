from pyplex import gl
from pyplex.glow import abstract
from pyplex.glow.type import Type
from pyplex.glow.buffer import ArrayBuffer
from ctypes import *

from typing import List, Optional
from ctypes import pointer, c_int


class VertexArray(abstract.BindableObject):
    def __init__(self, ctx: gl.GL30):
        self._ctx = ctx

        self._ptr = c_uint(0)
        self._ctx.gen_vertex_arrays(1, pointer(self._ptr))
        self._ptr = self._ptr.value

        max_attributes = c_int(0)
        ctx.get_integerv(gl.MAX_VERTEX_ATTRIBS, pointer(max_attributes))
        self._attributes = [None] * max_attributes.value

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def attributes(self) -> List[ArrayBuffer]:
        return self._attributes

    def attribute(self, location: int, buffer: ArrayBuffer):
        with buffer, self:
            self._attributes[location] = buffer

            buffertype = Type.from_np(buffer.shape[1:], buffer.dtype)
            self._ctx.enable_vertex_attrib_array(location)
            self._ctx.vertex_attrib_pointer(location, buffertype.count, buffertype.gl_base, False, 0, c_void_p(0))

    def bind(self):
        self._ctx.bind_vertex_array(self._ptr)

    def unbind(self):
        self._ctx.bind_vertex_array(0)

    def delete(self):
        self._ctx.delete_vertex_arrays(1, pointer(self._ptr))

    def __setitem__(self, location: int, buffer: ArrayBuffer):
        self.attribute(location, buffer)

    def __getitem__(self, location: int) -> Optional[ArrayBuffer]:
        return self._attributes[location]