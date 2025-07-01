import sys
import os
import pythoncom

ESAPI_PATH = os.environ.get('ESAPI_PATH')

if ESAPI_PATH is not None:
    # optionally set ESAPI_PATH env var with location of DLLs
    sys.path.append(ESAPI_PATH)
else:
    # do some soul searching
    rpaths = [os.path.join("esapi", "API"), "ExternalBeam"]
    base = os.path.join("Program Files (x86)", "Varian", "RTM")
    drives = ["C:", "D:"]  # Could potentially list local drives, but Eclispe should be on C or D
    searched_paths = []
    # Add paths that exist
    paths = []
    version = 0
    release = 0
    for drive in drives:
        drive_path = os.path.join(drive, os.sep, base)
        searched_paths += [os.path.join(drive_path, '%version', i) for i in rpaths]
        if not os.path.exists(drive_path):
            continue
        # Only load up the latest version and release of the software, regardless of the drive
        for ver in os.listdir(drive_path):
            if os.path.isdir(os.path.join(drive_path, ver)):
                if ver.find('.') != -1:
                    new_version, new_release = ver.split('.')
                    new_version, new_release = int(new_version), int(new_release)
                    if new_version > version:
                        release = -1
                    if new_version >= version:
                        version = new_version
                        if new_release > release:
                            release = new_release
                            """
                            Only update the path if those locations actually exist
                            """
                            if min([os.path.exists(os.path.join(drive, os.sep, base, ver, rp)) for rp in rpaths]):
                                paths = [os.path.join(drive, os.sep, base, ver, rp) for rp in rpaths]

    if len(paths) < 2:
        raise Exception("Did not find required library paths!  Searched for:\n %s" % (",\n".join(searched_paths)))
    if len(paths) > 2:
        print("WARNING: Found multiple possible VMS dll locations:\n %s" % (",\n".join(paths)))

    for p in paths:
        sys.path.append(p)

import clr  # pip install git+https://github.com/VarianAPIs/pythonnet

import typing

if typing.TYPE_CHECKING:
    from .stubs.VMS.TPS.Common.Model.Types import *
    from .stubs.VMS.TPS.Common.Model.API import *

    from .stubs import System
    from .stubs.System.Collections.Generic import Dictionary

    # for numpy array interfacing
    # from .stubs.System.Windows import Point
    from .stubs.System import Array, Int32, Double
    # from .stubs.System.Runtime.InteropServices import GCHandle, GCHandleType  # TODO: these are missing from type stubs

else:
    # enforce single thread apartment mode:
    pythoncom.CoInitialize()
    
    clr.AddReference('System.Windows')
    # clr.AddReference('System.Linq')
    # clr.AddReference('System.Collections')
    clr.AddReference('VMS.TPS.Common.Model.API')
    # clr.AddReference('VMS.TPS.Common.Model')

    # the bad stuff
    import System
    from System.Collections.Generic import Dictionary 
    # import System.Reflection

    # the good stuff
    from VMS.TPS.Common.Model.Types import *
    from VMS.TPS.Common.Model.API import *

    # for numpy array interfacing
    from System.Windows import Point
    from System import Array, Int32, Double
    from System.Runtime.InteropServices import GCHandle, GCHandleType

# the python
import numpy as np
from ctypes import string_at, sizeof, c_int32, c_bool, c_double
from scipy.ndimage.morphology import binary_dilation, binary_erosion

from .Lot import Lot

SAFE_MODE = False  # if True all C# to Numpy array copies are verified

def lot_lambda(attr):
    '''returns a lambda that wraps attr in a lot'''
    return lambda self, key=None: Lot(getattr(self, attr)) if key is None else Lot(getattr(self, attr))[key]


def lotify(T):
    '''adds lot accessors to IEnumerable children'''
    # TODO: add recursion
    ienum_t = System.Type.GetType('System.Collections.IEnumerable')
    t = System.Type.GetType(T.__module__ + '.' + T.__name__ + ',' + T.__module__)
    for p in t.GetProperties():
        # look for IEnumerable types
        if ienum_t.IsAssignableFrom(p.PropertyType) \
                and p.PropertyType.IsGenericType \
                and len(p.PropertyType.GetGenericArguments()) == 1:
            # Monkeypatch the lot accessor onto the parent object
            setattr(T, p.Name + "Lot", lot_lambda(p.Name))


def to_ndarray(src, dtype):
    '''converts a blitable .NET array of type dtype to a numpy array of type dtype'''
    src_hndl = GCHandle.Alloc(src, GCHandleType.Pinned)
    try:
        src_ptr = src_hndl.AddrOfPinnedObject().ToInt64()
        dest = np.frombuffer(string_at(src_ptr, len(src) * sizeof(dtype)), dtype=dtype)
    finally:
        if src_hndl.IsAllocated:
            src_hndl.Free()
    if SAFE_MODE:
        check_arrays(src, dest)
    return dest


def image_to_nparray(image_like):
    '''returns a 3D numpy.ndarray of floats indexed like [x,y,z]'''
    _shape = (image_like.XSize, image_like.YSize, image_like.ZSize)
    _array = np.zeros(_shape)

    _buffer = Array.CreateInstance(Int32, image_like.XSize, image_like.YSize)
    for z in range(image_like.ZSize):
        image_like.GetVoxels(z, _buffer)
        _array[:, :, z] = to_ndarray(_buffer, dtype=c_int32).reshape((image_like.XSize, image_like.YSize))

    return _array


def dose_to_nparray(dose):
    '''returns a 3D numpy.ndarray of floats indexed like [x,y,z]'''
    dose_array = image_to_nparray(dose)

    scale = float(dose.VoxelToDoseValue(1).Dose - dose.VoxelToDoseValue(0).Dose)  # maps int to float
    offset = float(
        dose.VoxelToDoseValue(0).Dose) / scale  # minimum dose value stored as int (zero if coming from Eclipse plan)
    return scale * dose_array.astype(float) + offset


def fill_in_profiles(dose_or_image, profile_fxn, row_buffer, dtype, pre_buffer=None):
    '''fills in 3D profile data (dose or segments)'''
    mask_array = np.zeros((dose_or_image.XSize, dose_or_image.YSize, dose_or_image.ZSize))

    # note used ZSize-1 to match zero indexed loops below and compute_voxel_points_matrix(...)
    z_direction = VVector.op_Multiply(Double((dose_or_image.ZSize - 1) * dose_or_image.ZRes), dose_or_image.ZDirection)
    y_step = VVector.op_Multiply(dose_or_image.YRes, dose_or_image.YDirection)

    for x in range(dose_or_image.XSize):  # scan X dimensions
        start_x = VVector.op_Addition(dose_or_image.Origin,
                                      VVector.op_Multiply(Double(x * dose_or_image.XRes), dose_or_image.XDirection))

        for y in range(dose_or_image.YSize):  # scan Y dimension
            stop = VVector.op_Addition(start_x, z_direction)

            # get the profile along Z dimension 
            if pre_buffer is None:
                profile_fxn(start_x, stop, row_buffer)
            else:
                profile_fxn(start_x, stop, pre_buffer)
                pre_buffer.CopyTo(row_buffer, 0)  # is this really needed?

            # save data
            mask_array[x, y, :] = to_ndarray(row_buffer, dtype)

            # add step for next point
            start_x = VVector.op_Addition(start_x, y_step)

    return mask_array


def make_segment_mask_for_grid(structure, dose_or_image, sub_samples = None):
    '''returns a 3D numpy.ndarray of bools matching dose or image grid indexed like [z,x,y]
       sub_samples: int, number of samples along each dimension of voxel used to compute partial voxel values (default: None == center of voxel only)
    '''
    assert dose_or_image is not None, "A dose or image object is required to generate a mask."
    mask = make_segment_mask_for_structure(dose_or_image, structure)
    if sub_samples is None:
        return mask
    else:
        assert type(sub_samples) == int, "sub_samples must be an integer"
        assert sub_samples > 1, "sub_samples must be > 1"
        # compute fractional voxels at boundary

        mask_dilated = binary_dilation(mask)
        mask_eroded = binary_erosion(mask)
        mask_boundary = mask_dilated ^ mask_eroded
        nsamples = sub_samples**3
        boundary_idx = np.where(mask_boundary)

        mask_partials = np.zeros_like(mask, dtype=float)
        xRes, yRes, zRes = dose_or_image.XRes, dose_or_image.YRes, dose_or_image.ZRes
        
        for ix, iy, iz in zip(boundary_idx[0],boundary_idx[1],boundary_idx[2]):

            x = dose_or_image.Origin.x + ix * xRes
            y = dose_or_image.Origin.y + iy * yRes
            z = dose_or_image.Origin.z + iz * zRes

            f = 0
            for xf in np.linspace(-0.5*xRes,0.5*xRes,sub_samples):
                for yf in np.linspace(-0.5*yRes,0.5*yRes,sub_samples):
                    start = VVector(x + xf, y + yf, z - 0.5 * zRes)
                    stop  = VVector(x + xf, y + yf, z + 0.5 * zRes )
                    inside = System.Collections.BitArray(sub_samples)
                    structure.GetSegmentProfile(start, stop, inside)
                    for b in inside:
                        if b:
                            f += 1
            mask_partials[ix,iy,iz] = f/nsamples

        return mask_partials + mask_eroded


def make_segment_mask_for_structure(dose_or_image, structure):
    '''returns a 3D numpy.ndarray of bools matching dose or image grid indexed like [x,y,z]'''
    if (structure.HasSegment):
        pre_buffer = System.Collections.BitArray(dose_or_image.ZSize)
        row_buffer = Array.CreateInstance(bool, dose_or_image.ZSize)

        return fill_in_profiles(dose_or_image, structure.GetSegmentProfile, row_buffer, c_bool, pre_buffer)
    else:
        raise Exception("structure has no segment data")


def make_dose_for_grid(dose, image=None):
    '''returns a 3D numpy.ndarray of doubles matching dose (default) or image grid indexed like [x,y,z]'''

    if image is not None:
        row_buffer = Array.CreateInstance(Double, image.ZSize)
        dose_array = fill_in_profiles(image, dose.GetDoseProfile, row_buffer, c_double)
    else:
        # default
        dose_array = dose_to_nparray(dose)

    dose_array[np.where(np.isnan(dose_array))] = 0.0
    return dose_array


def compute_voxel_points_matrix(dose_or_image):
    ''' returns a matrix of vectors, matching the dose or image object provided, indexed like [x,y,z] wich returns a vector (x,y.z) mm'''
    origin = [dose_or_image.Origin.x, dose_or_image.Origin.y, dose_or_image.Origin.z]
    resolution = [dose_or_image.XRes, dose_or_image.YRes, dose_or_image.ZRes]
    _shape = [dose_or_image.XSize, dose_or_image.YSize, dose_or_image.ZSize]

    # create an array of points (location of each voxel)
    ax = []
    for dim in range(3):
        ax.append(np.linspace(
            start=origin[dim],
            stop=origin[dim] + (_shape[dim] - 1) * resolution[dim],
            num=_shape[dim],
            endpoint=True
        ))

    # create a matrix of 3-vectors for voxel locations
    voxel_points = np.vstack((np.meshgrid(*ax, indexing='ij'))).reshape(3, *_shape).T
    voxel_points = np.swapaxes(voxel_points, 0, 2)  # gets us to [x,y,z]
    assert np.all(origin == voxel_points[0, 0, 0])
    assert np.all(origin + (np.array(_shape) - 1) * np.array(resolution) == voxel_points[-1, -1, -1])
    return voxel_points


def set_fluence_nparray(beam, shaped_fluence, beamlet_size_mm=2.5):
    """sets optimal fluence in beam given numpy array and beamlet size (asserts square fluence, and zero collimator rotation)."""
    # assumes all fluence is square with isocenter at center of image
    # TODO: implement functionality below to remove assertions
    assert beamlet_size_mm == 2.5, "beamlet sizes of other than 2.5 mm are not implemented"
    assert shaped_fluence.shape[0] == shaped_fluence.shape[1], "non-square fluence not implemented"
    assert beam.ControlPoints[0].CollimatorAngle == 0.0, "non-zero collimator angle not implemented"

    _buffer = Array.CreateInstance(System.Single, shaped_fluence.shape[0], shaped_fluence.shape[1])

    # note: the shape -1, then divide by 2.0 gives desired center of corner beamlet (half pixel shift)
    x_origin = - float(shaped_fluence.shape[0] - 1) * beamlet_size_mm / 2.0
    y_origin = + float(shaped_fluence.shape[1] - 1) * beamlet_size_mm / 2.0

    for i in range(shaped_fluence.shape[0]):
        for j in range(shaped_fluence.shape[1]):
            _buffer[i, j] = shaped_fluence[i, j]

    fluence = Fluence(_buffer, x_origin, y_origin)
    beam.SetOptimalFluence(fluence)

def make_contour_mask_fast(structure_set, structure_obj, image_like, super_sample=8):
    '''Generate a 3D mask from structure contours on an image-like object grid (e.g., Dose or Image).
    This function uses OpenCV to efficiently create a mask from the contours of a structure set.
    However, it does not exactly match the segment volume represented in Eclipse. For a more accurate representation,
    use the `np_mask_like` method of the structure object. Built with the help of Google Gemini and Claude.

    Args:
        structure_set (pyesapi.StructureSet): The structure set containing the contours.
        structure_obj (pyesapi.Structure): The specific structure to create a mask for.
        image_like (pyesapi.Image or pyesapi.Dose): The image-like object that defines the grid for the mask.
        super_sample (int): The intermediate super-sampling factor to increase mask accuracy. Default is 8, where 1 means no super-sampling (but fastest).
    Returns:
        np.ndarray: A 3D boolean mask where True indicates the presence of the structure.
    '''

    # Import cv2 when needed for mask generation
    try:
        import cv2
    except ImportError:
        raise ImportError("opencv-python is required for mask generation. Install with: pip install opencv-python")

    x_res = image_like.XRes
    y_res = image_like.YRes
    z_res = image_like.ZRes

    origin_x = image_like.Origin.x 
    origin_y = image_like.Origin.y
    origin_z = image_like.Origin.z
    
    nx = image_like.XSize
    ny = image_like.YSize
    nz = image_like.ZSize

    total_volume_mm3 = 0
    mask_3d = np.zeros((nz, ny, nx), dtype=bool)

    all_contrours_per_source_slice = []

    # The CT data (source) can be different from the requested mask geometry (sample), so we use the StructureSet's Image geo directly to extract contours

    # first loop over the Z slices of the structure set image and grab contours and signed areas
    for source_z_idx in range(structure_set.Image.ZSize):

        contours_on_slice = structure_obj.GetContoursOnImagePlane(source_z_idx)
        if len(contours_on_slice) == 0:
            all_contrours_per_source_slice.append(None)  # Append empty contours with zero area for each empty slice
            continue

        # Calculate total SIGNED area for the current slice z to handle holes
        total_signed_area_on_slice_mm2 = 0.0
        # For mask generation, collect all contour polygons on this slice
        slice_polygons = []      
        for contour_xyz in contours_on_slice:
            if len(contour_xyz) < 3:
                print(f"WARNING: Skipping contour with < 3 points on slice index {source_z_idx}")
                continue

             # Extract X, Y coordinates
            x = np.array([v[0] for v in contour_xyz])
            y = np.array([v[1] for v in contour_xyz])
            
            # Calculate SIGNED area using Shoelace formula
            signed_area = - 0.5 * (np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))  # sign is flipped relative to this formulation (coordinate system?)
            total_signed_area_on_slice_mm2 += signed_area
            
            # Store polygon for mask generation
            slice_polygons.append((x, y, signed_area))

        all_contrours_per_source_slice.append(slice_polygons)

    # Now, loop over the Z slices of the requested mask geometry
    for sample_z_idx in range(nz):

        sample_z_position = sample_z_idx * z_res + origin_z - z_res / 2  # Center the sample slice position

        # Find the closest Z slice in the source image index space
        source_z_idx = ((sample_z_position - structure_set.Image.Origin.z + structure_set.Image.ZRes/2)/structure_set.Image.ZRes + np.finfo(np.float64).tiny).astype(int)
        
        # Only process if this Z sample slice is within the source Z slices
        if source_z_idx < structure_set.Image.ZSize and source_z_idx >= 0:
            # Create mask for this slice
            slice_mask = np.zeros((ny, nx), dtype=bool)

            slice_polygons_list = all_contrours_per_source_slice[source_z_idx]
            if slice_polygons_list is not None:
                for x, y, signed_area in slice_polygons_list:
                    if len(x) == 0:
                        continue
                    # Convert contour to pixel coordinates using non-isotropic resolution
                    contour_pixels = np.zeros((len(x), 2), dtype=np.int32)

                    if super_sample > 1:
                        # Apply super-sampling to improve contour resolution
                        contour_pixels[:, 0] = np.round((x - origin_x + x_res/2) / x_res * super_sample) # x pixel coords
                        contour_pixels[:, 1] = np.round((y - origin_y + y_res/2) / y_res * super_sample) # y pixel coords
                        
                        # Create a temporary mask for this contour using cv2.fillPoly
                        temp_mask_hires = np.zeros((ny * super_sample, nx * super_sample), dtype=np.uint8)
                        cv2.fillPoly(temp_mask_hires, [contour_pixels], 1, lineType=cv2.LINE_8)
                        temp_mask = cv2.resize(temp_mask_hires, (nx, ny), interpolation=cv2.INTER_AREA)
                        temp_mask_bool = temp_mask.astype(bool)
                    else:
                        # Convert to pixel coordinates without super-sampling
                        contour_pixels[:, 0] = np.round((x - origin_x + x_res/2) / x_res).astype(np.int32) # x pixel coords
                        contour_pixels[:, 1] = np.round((y - origin_y + y_res/2) / y_res).astype(np.int32) # y pixel coords
                        # Create a temporary mask for this contour using cv2.fillPoly
                        temp_mask = np.zeros((ny, nx), dtype=np.uint8)
                        cv2.fillPoly(temp_mask, [contour_pixels], 1, lineType=cv2.LINE_8)
                        temp_mask_bool = temp_mask.astype(bool)
                    
                    # Add or subtract based on winding direction (signed area)
                    if signed_area > 0:  # Positive area - add to mask
                        slice_mask |= temp_mask_bool
                    else:  # Negative area - subtract from mask (hole)
                        slice_mask &= ~temp_mask_bool
            
            mask_3d[sample_z_idx] = slice_mask

    return mask_3d.T

## where the magic happens ##

# add Lot accessors to objects with IEnumerable childeren
lotify(Patient)
lotify(PlanSetup)
lotify(Course)
lotify(Beam)
lotify(StructureSet)


# monkeypatch "extensions" for numpy array translators
Structure.np_mask_like = make_segment_mask_for_grid
Dose.np_array_like = make_dose_for_grid
Image.np_array_like = image_to_nparray

Image.np_structure_mask = make_segment_mask_for_structure
Dose.np_structure_mask = make_segment_mask_for_structure

Image.np_voxel_locations = compute_voxel_points_matrix
Dose.np_voxel_locations = compute_voxel_points_matrix

Beam.np_set_fluence = set_fluence_nparray

StructureSet.np_mask_for_structure_fast = make_contour_mask_fast

# fixing some pythonnet confusion
def get_editable_IonBeamParameters(beam):
    for mi in beam.GetType().GetMethods():
        if mi.ReturnType.ToString() == 'VMS.TPS.Common.Model.API.IonBeamParameters':
            return mi.Invoke(beam,[])
IonBeam.GetEditableIonBeamParameters = get_editable_IonBeamParameters


## some tests ##

def validate_structure_mask(structure, mask, pts, margin=4):
    dilation_idx = np.where(binary_dilation(mask, iterations=margin))
    flat_pts = pts[dilation_idx]
    flat_mask = mask[dilation_idx]
    vv = VVector(0. ,0. , 0.)

    def tester(pt):
        vv.x = pt[0]
        vv.y = pt[1]
        vv.z = pt[2]
        return structure.IsPointInsideSegment(vv)

    mismatch_count = 0
    for i, p in enumerate(flat_pts):
        if flat_mask[i] != tester(p):
            mismatch_count += 1

    error = mismatch_count / len(flat_mask) * 100.0
    print("mask error (%):", error)
    assert error <= 0.05, "Masking error greater than 0.05 %"


def check_arrays(a, b):
    '''array copy verification'''
    assert len(a) == len(b), "Arrays are different size!"
    assert any(A == B for A, B in zip(a, b)), "Arrays have different values!"
