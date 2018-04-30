from pyplex import gl
from pyplex.glow.texture import Texture2D
from ctypes import *


class FrameBuffer:
    def __init__(self, ctx: gl.GL_ANY, target: gl.FrameBufferTarget = gl.FrameBufferTarget.FRAMEBUFFER):
        self._ctx = ctx
        self._target = target

        self._ptr = c_uint(0)
        self._ctx.gen_framebuffers(1, pointer(self._ptr))
        self._ptr = self._ptr.value

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def target(self) -> gl.FrameBufferTarget:
        return self._target

    def attach(self, texture: Texture2D, attachment: gl.FrameBufferAttachment):
        self._ctx.bind_framebuffer(self._target, self._ptr)
        self._ctx.framebuffer_texture_2d(self._target, attachment, texture.target, texture.ptr, 0)
        self._ctx.bind_framebuffer(self._target, 0)

    def bind(self):
        self._ctx.bind_framebuffer(self._target, self._ptr)

    def unbind(self):
        self._ctx.bind_framebuffer(self._target, 0)

    def delete(self):
        self._ctx.delete_framebuffers(1, pointer(self._ptr))

    def __enter__(self):
        self._ctx.bind_framebuffer(self._target, self._ptr)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._ctx.bind_framebuffer(self._target, 0)