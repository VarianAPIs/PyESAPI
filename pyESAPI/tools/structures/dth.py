import numpy as np
from scipy.ndimage.morphology import binary_erosion 

def _min_dist(a_pt, test_pts):
    """computes the minimum distance between a_pt and a list of test_pts"""
    assert a_pt.shape[0] == test_pts.shape[1], "dimensions of inputs are not as expected"
    return np.min(np.sqrt(np.sum(np.power(test_pts-a_pt,2),axis=1))) # swapping min and sqrt doesn't save much time
    
def distance_to_surface(structure_mask, target_mask, voxel_pts):
    """For every voxel in structure, find minimum distance to target surface.
    The target surface is calculated by removing the binary erosion of the target mask.
    
    Args:
        structure_mask: a 3D numpy array of boolean values
        target_mask: a 3D numpy array of boolean values
        voxel_pts: a 4D numpy array of voxel location points (x,y,z) for each voxel in masks

    Returns:
        a 3D numpy array of minimum distances to target_mask surface for each True voxel in structure_mask, 
        numpy.NaN otherwise.
    """
    
    # TODO: make multitreaded

    # compute surface voxels
    target_shell = np.logical_and(target_mask,np.logical_not(binary_erosion(target_mask,iterations=1)))        
    surface_pts = voxel_pts[np.where(target_shell)]

    # index voxels inside structure but outside target
    idx_outside = np.where(np.logical_and(structure_mask,np.logical_not(target_mask)))
    
    # index voxels inside structure and inside target
    idx_inside = np.where(np.logical_and(structure_mask,target_mask))
    
    structure_pts_outside = voxel_pts[idx_outside]
    structure_pts_inside = voxel_pts[idx_inside]
    
    dists_to_target = np.empty(structure_mask.shape) 
    dists_to_target[:] = np.NaN

    # only compute if there are structure voxels ouside the target
    if len(structure_pts_outside.shape) != 0:
        dists_to_target[idx_outside] = list(map(lambda pt: _min_dist(pt,surface_pts),structure_pts_outside))    
    
    # only compute if there are structure voxels inside the target
    if len(structure_pts_inside) != 0:
        # pts inside have negative dist
        dists_to_target[idx_inside] = list(map(lambda pt: - _min_dist(pt,surface_pts),structure_pts_inside))
    
    return dists_to_target