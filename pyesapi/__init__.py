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
from scipy.ndimage.morphology import binary_dilation

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
                pre_buffer.CopyTo(row_buffer, 0)

            # save data
            mask_array[x, y, :] = to_ndarray(row_buffer, dtype)

            # add step for next point
            start_x = VVector.op_Addition(start_x, y_step)

    return mask_array


def make_segment_mask_for_grid(structure, dose_or_image):
    '''returns a 3D numpy.ndarray of bools matching dose or image grid indexed like [z,x,y]'''
    assert dose_or_image is not None, "A dose or image object is required to generate a mask."
    return make_segment_mask_for_structure(dose_or_image, structure)


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
