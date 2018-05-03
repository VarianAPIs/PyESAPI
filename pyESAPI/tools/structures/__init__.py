from .dvh import *
from .ovh import *
from .dth import *

def voxel_size(v_pts):
    vx = v_pts[1,0,0,0]-v_pts[0,0,0,0]
    vy = v_pts[0,1,0,1]-v_pts[0,0,0,1]
    vz = v_pts[0,0,1,2]-v_pts[0,0,0,2]

    return vx, vy, vz

def voxel_volume(v_pts):
    """Returns the volume of voxel elements in mm^3
    
    Args:
        v_pts: a 4D numpy array of uniform grid voxel location points (x,y,z) for each voxel

    Returns:
        vox_vol: volume of the voxel @ (0,0,0)
    """
    vx,vy,vz = voxel_size(v_pts)

    return vx*vy*vz