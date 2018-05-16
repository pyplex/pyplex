import pyassimp
import os

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


class MeshLoader:
    def __init__(self, path: str):
        self.scene = pyassimp.load(path)

        # for i, mesh in enumerate(self.scene.meshes):
        #     print("Mesh {}. {}".format(i, mesh))
        #     print("{:>10s}\t{}".format("name", mesh.name))
        #     print("{:>10s}\t{}".format("material", mesh.materialindex))
        #     print("{:>10s}\t{:8s}\t{}".format("vertices", str(mesh.vertices.shape), str(mesh.vertices.dtype)))
        #     print("{:>10s}\t{:8s}\t{}".format("faces", str(mesh.faces.shape), str(mesh.faces.dtype)))
        #     print("{:>10s}\t{:8s}\t{}".format("uvs", str(mesh.texturecoords.shape), str(mesh.texturecoords.dtype)))
        #     print("{:>10s}\t{:8s}\t{}".format("normals", str(mesh.normals.shape), str(mesh.normals.dtype)))
        #     print("{:>10s}\t{:8s}\t{}".format("tangents", str(mesh.tangents.shape), str(mesh.tangents.dtype)))
        #     print("{:>10s}\t{:8s}\t{}".format("bitangents", str(mesh.bitangents.shape), str(mesh.bitangents.dtype)))
        #     print("{:>10s}\t{:8s}\t{}".format("colors", str(mesh.colors.shape), str(mesh.colors.dtype)))
        #     print()
        #
        # for i, material in enumerate(self.scene.materials):
        #     print("Material {}. {}".format(i, material))
        #     for j, (key, value) in enumerate(material.properties.items()):
        #         tt = TextureType(material[0].mProperties[j].contents.mSemantic)
        #         print("\t{:>10s}\t{}\t".format(key, value) + (str(tt) if tt else ''))
        #     print()


if __name__ == "__main__":
    MODEL = os.path.join(os.path.dirname(__file__), '../obj/sponza/sponza.obj')
    MeshLoader(MODEL)