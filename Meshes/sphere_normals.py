import numpy as np
import sys
import vtk
import ply_writer

from vtk.util import numpy_support as vn

def calc_density(normals, r=0.1):
    density = np.zeros(normals.shape[0])
    for i, n in enumerate(normals):
        density[i] = np.sum((normals[:, 0] - n[0])**2 \
                + (normals[:, 1] - n[1])**2 \
                + (normals[:, 2] - n[2])**2 <= r**2)
    return density

def map_to_colours(density):
    init = 255.0
    end = 256**3 - 1.0

    d_init = density.min()
    d_end = density.max()

    color_map = ((end - init)/(d_end - d_init) * (density - d_init) + init).astype('int32')

    r = (color_map / 256**2) % 256
    g = (color_map / 256) % 256
    b = color_map % 256

    output = np.zeros((r.shape[0], 3), dtype='uint8')

    output[:, 0] = r
    output[:, 1] = g
    output[:, 2] = b

    return output

def read_normals(mesh_file):
    stl = vtk.vtkSTLReader()
    stl.SetFileName(mesh_file)
    stl.Update()

    normals = vtk.vtkPolyDataNormals()
    normals.SetInput(stl.GetOutput())
    normals.Update()
    output = normals.GetOutput()

    a_normals = vn.vtk_to_numpy(output.GetPointData().GetArray("Normals"))
    return a_normals / np.linalg.norm(a_normals)

def main():
    normals = read_normals(sys.argv[1])
    normals_density = calc_density(normals)
    colour_mapped_normals = map_to_colours(normals_density)
    print colour_mapped_normals
    writer = ply_writer.PlyWriter(sys.argv[2])
    writer.from_faces_vertices_list([], normals,
                                    colour_mapped_normals)

if __name__ == '__main__':
    main()
