import open3d as o3d
import numpy as np

def visualize(mesh):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(mesh)
    vis.run()
    vis.destroy_window()

def main():
    mesh = o3d.io.read_triangle_mesh("Input.obj")
    # 2. Get rotation matrix using Euler angles (e.g., 90 degrees / pi/2 around X)
    R = mesh.get_rotation_matrix_from_xyz((np.pi *1.5, 0, 0))

    # 3. Apply rotation around the geometric center
    mesh.rotate(R, center=mesh.get_center())
    o3d.io.write_triangle_mesh("copy_of_Input.obj",mesh)
    visualize(mesh)

main()