from pyplex import gl
from pyplex.glow import abstract
from pyplex.glow.texture import Texture2D, DepthTexture2D
from ctypes import *

from typing import List, Optional


class IncompleteFrameBufferError(Exception):
    pass


class FrameBuffer(abstract.BindableObject):
    def __init__(self, ctx: gl.GL_ANY, target: gl.FrameBufferTarget = gl.FrameBufferTarget.FRAMEBUFFER,
                 color: Optional[List[Texture2D]]=None,
                 depth: Optional[DepthTexture2D]=None,
                 stencil: Optional[Texture2D]=None):

        self._ctx = ctx
        self._target = target

        self._ptr = c_uint(0)
        self._ctx.gen_framebuffers(1, pointer(self._ptr))
        self._ptr = self._ptr.value

        with self:
            if color:
                for i, texture in enumerate(color):
                    self._ctx.framebuffer_texture_2d(
                        self._target, gl.FrameBufferAttachment.COLOR_0 + i, texture.target, texture.ptr, 0)
            else:
                self._ctx.draw_buffer(0)
                self._ctx.read_buffer(0)
            if depth:
                self._ctx.framebuffer_texture_2d(
                    self._target, gl.FrameBufferAttachment.DEPTH, depth.target, depth.ptr, 0)
            if stencil:
                self._ctx.framebuffer_texture_2d(
                    self._target, gl.FrameBufferAttachment.STENCIL, stencil.target, stencil.ptr, 0)

        if not self._ctx.check_framebuffer_status(self._target):
            raise IncompleteFrameBufferError()

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
