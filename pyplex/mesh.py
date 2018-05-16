from pyplex import gl

from pyplex.glow.vertexarray import VertexArray
from pyplex.glow.buffer import ArrayBuffer, ElementArrayBuffer

import numpy as np
from typing import Optional, Union


BUFFER = Union[np.ndarray, ArrayBuffer]


class AttributeLocation:
    VERTICES = 0
    UVS = 1
    NORMALS = 2
    TANGENTS = 3
    BITANGENTS = 4
    COLORS = 5


class Mesh:
    def __init__(self, ctx: gl.GL_ANY, faces: Union[np.ndarray, ElementArrayBuffer], vertices: BUFFER,
                 uvs: Optional[BUFFER]=None, normals: Optional[BUFFER]=None,
                 tangents: Optional[BUFFER]=None, bitangents: Optional[BUFFER]=None,
                 colors: Optional[BUFFER]=None):

        self._vao = VertexArray(ctx)

        self._faces = faces if isinstance(faces, ElementArrayBuffer) else ElementArrayBuffer(ctx, faces)

        self._vertices = vertices if isinstance(vertices, ArrayBuffer) else ArrayBuffer(ctx, vertices)
        self._vao[AttributeLocation.VERTICES] = self._vertices

        self._uvs = self._normals = self._tangents = self._bitangents = self._colors = None

        if uvs:
            self._uvs = uvs if isinstance(uvs, ArrayBuffer) else ArrayBuffer(ctx, uvs)
            self._vao[AttributeLocation.UVS] = self._uvs

        if normals:
            self._normals = normals if isinstance(normals, ArrayBuffer) else ArrayBuffer(ctx, normals)
            self._vao[AttributeLocation.NORMALS] = self._normals

        if tangents:
            self._tangents = tangents if isinstance(normals, ArrayBuffer) else ArrayBuffer(ctx, tangents)
            self._vao[AttributeLocation.TANGENTS] = self._tangents

        if bitangents:
            self._bitangents = bitangents if isinstance(normals, ArrayBuffer) else ArrayBuffer(ctx, bitangents)
            self._vao[AttributeLocation.BITANGENTS] = self._bitangents

        if colors:
            self._colors = colors if isinstance(colors, ArrayBuffer) else ArrayBuffer(ctx, colors)
            self._vao[AttributeLocation.COLORS] = self._colors

    @property
    def vao(self):
        return self._vao

    @property
    def faces(self) -> ElementArrayBuffer:
        return self._faces

    @property
    def vertices(self) -> ArrayBuffer:
        return self._vertices

    @property
    def uvs(self) -> Optional[ArrayBuffer]:
        return None

    @property
    def normals(self) -> Optional[ArrayBuffer]:
        return None

    @property
    def tangents(self) -> Optional[ArrayBuffer]:
        return None

    @property
    def bitangents(self) -> Optional[ArrayBuffer]:
        return None

    @property
    def colors(self) -> Optional[ArrayBuffer]:
        return None
