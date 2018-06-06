from pyplex import gl
from pyplex.mesh import Mesh

import pyassimp

from typing import List
from enum import IntEnum


class TextureType(IntEnum):
    NONE = 0x0
    DIFFUSE = 0x1
    SPECULAR = 0x2
    AMBIENT = 0x3
    EMISSIVE = 0x4
    HEIGHT = 0x5
    NORMALS = 0x6
    SHININESS = 0x7
    OPACITY = 0x8
    DISPLACEMENT = 0x9
    LIGHTMAP = 0xA,
    REFLECTION = 0xB
    UNKNOWN = 0xC


class AssetImporter:
    def __init__(self, ctx: gl.GL_ANY, path: str):
        self._ctx = ctx
        self.scene = pyassimp.load(path)

        for i, material in enumerate(self.scene.materials):
            print("Material {}. {}".format(i, material))
            for j, (key, value) in enumerate(material.properties.items()):
                tt = TextureType(material[0].mProperties[j].contents.mSemantic)
                print("\t{:>10s}\t{}\t".format(key, value) + (str(tt) if tt else ''))
            print()

    @property
    def meshes(self) -> List[Mesh]:
        return [Mesh(self._ctx,
                     mesh.faces,
                     mesh.vertices,
                     mesh.texturecoords[0],
                     mesh.normals,
                     mesh.tangents,
                     mesh.bitangents,
                     mesh.colors)
                for mesh in self.scene.meshes]