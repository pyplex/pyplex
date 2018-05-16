from pyplex.geometry.geometry import Geometry
import numpy as np
import re



def wavefront(path: str) -> Geometry:

    FLOAT = r'[-+]?(?:\d*\.?\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?'
    VERTEX_ELEM = r'(\d+)/\d*/\d*'
    NORMAL_ELEM = r'\d*/\d*/(\d+)'

    VERTEX = r'v ({0} {0} {0})'.format(FLOAT)
    ELEMENT = r'f {0} {0} {0}'.format(VERTEX_ELEM)

    NORMAL = r'vn ({0} {0} {0})'.format(FLOAT)
    NORMAL_ELEMENT = r'f {0} {0} {0}'.format(NORMAL_ELEM)

    with open(path) as obj_file:
        obj_data = obj_file.read()
        vertices = np.fromstring(' '.join(re.findall(VERTEX, obj_data)), np.float32, sep=' ').reshape(-1, 3)
        elements = np.fromstring(' '.join(' '.join(e) for e in re.findall(ELEMENT, obj_data)), np.uint32, sep=' ') - 1

        # normal_elements = np.fromstring(' '.join(' '.join(e) for e in re.findall(NORMAL_ELEMENT, obj_data)), np.uint32, sep=' ') - 1
        normals = np.fromstring(' '.join(re.findall(NORMAL, obj_data)), np.float32, sep=' ').reshape(-1, 3)

    return Geometry(vertices, elements, normals=normals)


if __name__ == "__main__":
    wavefront(r"C:\Users\Bram\Projects\pyplex\obj\suzanne.obj")