import open3d as o3d
import numpy as np

def visualize(mesh):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(mesh)
    vis.run()
    vis.destroy_window()

def main():
    mesh = o3d.io.read_triangle_mesh("results/odm_texturing/odm_textured_model_geo.obj")
    # 2. Get rotation matrix using Euler angles (e.g., 90 degrees / pi/2 around X)
    R = mesh.get_rotation_matrix_from_xyz((np.pi *1.5, 0, 0))

    # 3. Apply rotation around the geometric center
    mesh.rotate(R, center=mesh.get_center())
    pcd = mesh.sample_points_uniformly(
    number_of_points=50000
    )

    # 4. Seperate terain from objects in the scene
    plane_model, inliers = pcd.segment_plane(
    distance_threshold=0.05,
    ransac_n=3,
    num_iterations=1000
    )

    terrain = pcd.select_by_index(inliers)
    objects = pcd.select_by_index(
        inliers,
        invert=True
    )

    # 5. Isolate separate objects
    labels = np.array(
        objects.cluster_dbscan(
            eps=0.1,
            min_points=30
        )
    )
    bbox = objects.get_oriented_bounding_box()
    bbox.color = (1, 0, 0)
    dims = bbox.extent
    print("Length Width Height:", dims)
    o3d.visualization.draw_geometries(
        [objects, bbox]
    )

    # Number of clusters
    n_clusters = labels.max() + 1
    print("Clusters found:", n_clusters)

    # Measure each cluster
    for i in range(n_clusters):

        # Extract cluster
        idx = np.where(labels == i)[0]
        cluster = objects.select_by_index(idx)

        # Bounding box
        bbox = cluster.get_oriented_bounding_box()

        # Dimensions
        dims = bbox.extent

        print(f"Cluster {i}")
        print("Length Width Height:", dims)

        # Optional visualization
        bbox.color = (1, 0, 0)
        o3d.visualization.draw_geometries(
            [cluster, bbox]
        )


main()