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
                 colors: Optional[BUFFER]=None, primitive: gl.Primitive=gl.Primitive.TRIANGLES):

        self._ctx = ctx
        self._vao = VertexArray(ctx)
        self._primitive = primitive

        self._faces = faces if isinstance(faces, ElementArrayBuffer) else ElementArrayBuffer(ctx, faces.astype(np.uint16))

        self._vertices = vertices if isinstance(vertices, ArrayBuffer) else ArrayBuffer(ctx, vertices)
        self._vao[AttributeLocation.VERTICES] = self._vertices

        self._uvs = self._normals = self._tangents = self._bitangents = self._colors = None

        if uvs is not None and len(uvs) > 0:
            self._uvs = uvs if isinstance(uvs, ArrayBuffer) else ArrayBuffer(ctx, uvs)
            self._vao[AttributeLocation.UVS] = self._uvs

        if normals is not None and len(normals) > 0:
            self._normals = normals if isinstance(normals, ArrayBuffer) else ArrayBuffer(ctx, normals)
            self._vao[AttributeLocation.NORMALS] = self._normals

        if tangents is not None and len(tangents) > 0:
            self._tangents = tangents if isinstance(normals, ArrayBuffer) else ArrayBuffer(ctx, tangents)
            self._vao[AttributeLocation.TANGENTS] = self._tangents

        if bitangents is not None and len(bitangents) > 0:
            self._bitangents = bitangents if isinstance(normals, ArrayBuffer) else ArrayBuffer(ctx, bitangents)
            self._vao[AttributeLocation.BITANGENTS] = self._bitangents

        if colors is not None and len(colors) > 0:
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

    @property
    def primitive(self) -> gl.Primitive:
        return self._primitive

    def recalculate_normals(self):
        elements = self.faces.data.reshape(-1, 3)
        vertices = self.vertices.data

        face_normals = np.cross(
            vertices[elements[:, 0]] - vertices[elements[:, 1]],
            vertices[elements[:, 0]] - vertices[elements[:, 2]])

        normals = np.zeros_like(vertices)

        for element, face_normal in zip(elements, face_normals):
            normals[element] += face_normal

        normals /= np.linalg.norm(normals, axis=-1, keepdims=True)

        if self._normals:
            self._normals.data = normals
        else:
            self._normals = ArrayBuffer(self._ctx, normals)

