import sys

# sys.path.append("D:\\TPS\\va\\Main\\Bin\\Release64") # Dev
sys.path.append("C:\\Program Files (x86)\\Varian\\RTM\\15.5\\esapi\\API")  # Prod
sys.path.append("C:\\Program Files (x86)\\Varian\\RTM\\15.5\\ExternalBeam")  # Prod

import clr  # pip install pythonnet

clr.AddReference('System.Windows')
clr.AddReference('System.Linq')
clr.AddReference('System.Collections')
clr.AddReference('VMS.TPS.Common.Model')
clr.AddReference('VMS.TPS.Common.Model.API')

# the bad stuff
import System.Collections
import System.Reflection

# the good stuff
from VMS.TPS.Common.Model.Types import *
from VMS.TPS.Common.Model.API import *

# for numpy array interfacing
from System import Array, Int32, Double
from System.Runtime.InteropServices import GCHandle, GCHandleType

# the python
import numpy as np
from ctypes import string_at, sizeof, c_int32, c_bool, c_double
from scipy.ndimage.morphology import binary_dilation

SAFE_MODE = True  # if True all C# to Numpy array copies are verified


class Lot:
    '''a custom collection container for pysapi'''

    def __init__(self, some_collectable):
        self.collection = some_collectable

    def FirstOrDefault(self, fxn):
        result = list(filter(fxn, self.collection))
        if len(result) == 0:
            return None
        else:
            return result[0]

    def Select(self, fxn):
        '''returns a new lot of objects where fxn(object) == True'''
        if callable(fxn):
            return Lot(list(filter(fxn, self.collection)))
        else:
            raise TypeError('fxn is not callable')

    def __getitem__(self, key):
        if type(key) is int or type(key) is slice:
            # this could be slow:
            return [i for i in self.collection][key]
        else:
            if callable(key):
                obj = self.FirstOrDefault(key)
            else:
                obj = self.FirstOrDefault(lambda x: x.Id == key)
            if obj == None:
                print(type(key))
                raise KeyError('not found')
            else:
                return obj


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


def check_arrays(a, b):
    '''array copy verification'''
    assert len(a) == len(b), "Arrays are different size!"
    assert any(A == B for A, B in zip(a, b)), "Arrays have different values!"


def to_ndarray(src, dtype):
    '''converts a blitable .NET array of type dtype to a numpy array of type dtype'''
    src_hndl = GCHandle.Alloc(src, GCHandleType.Pinned)
    try:
        src_ptr = src_hndl.AddrOfPinnedObject().ToInt64()
        dest = np.fromstring(string_at(src_ptr, len(src) * sizeof(dtype)), dtype=dtype)
    finally:
        if src_hndl.IsAllocated: src_hndl.Free()
    if SAFE_MODE:
        check_arrays(src, dest)
    return dest


def dose_to_nparray(dose):
    '''returns a 3D numpy.ndarray of floats indexed like [x,y,z]'''

    dose_shape = (dose.XSize, dose.YSize, dose.ZSize)
    dose_array = np.zeros(dose_shape)

    _buffer = Array.CreateInstance(Int32, dose.XSize, dose.YSize)
    for z in range(dose.ZSize):
        dose.GetVoxels(z, _buffer)
        dose_array[:, :, z] = to_ndarray(_buffer, dtype=c_int32).reshape((dose.XSize, dose.YSize))

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
    return make_segment_mask_for_structure(dose_or_image, structure)


def make_segment_mask_for_structure(dose_or_image, structure):
    '''returns a 3D numpy.ndarray of bools matching dose or image grid indexed like [x,y,z]'''
    if (structure.HasSegment):
        mask_array = np.zeros((dose_or_image.ZSize, dose_or_image.YSize, dose_or_image.XSize))

        pre_buffer = System.Collections.BitArray(dose_or_image.ZSize)
        row_buffer = Array.CreateInstance(bool, dose_or_image.ZSize)

        return fill_in_profiles(dose_or_image, structure.GetSegmentProfile, row_buffer, c_bool, pre_buffer)
    else:
        raise Exception("structure has no segment data")


def make_dose_for_grid(dose, image=None):
    '''returns a 3D numpy.ndarray of doubles matching dose (default) or image grid indexed like [x,y,z]'''

    if image is not None:
        row_buffer = Array.CreateInstance(Double, image.ZSize);
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
    assert beamlet_size_mm == 2.5, "only beamlet of other than 2.5 mm is not implemented"
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

# where the magic happens:

# add Lot accessors to objects with IEnumerable childeren
lotify(Patient)
lotify(PlanSetup)
lotify(Course)
lotify(Beam)
lotify(StructureSet)

# monkeypatch "extensions" for numpy array translators
Structure.np_mask_like = make_segment_mask_for_grid
Dose.np_array_like = make_dose_for_grid

Image.np_structure_mask = make_segment_mask_for_structure
Dose.np_structure_mask = make_segment_mask_for_structure

Image.np_voxel_locations = compute_voxel_points_matrix
Dose.np_voxel_locations = compute_voxel_points_matrix

Beam.np_set_fluence = set_fluence_nparray

# some tests

def validate_structure_mask(structure, mask, pts, margin=4):
    dilation_idx = np.where(binary_dilation(mask, iterations=margin))
    flat_pts = pts[dilation_idx]
    flat_mask = mask[dilation_idx]
    vv = VVector()

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
