import sys
# sys.path.append("D:\\TPS\\va\\Main\\Bin\\Release64") # Dev
sys.path.append("C:\\Program Files (x86)\\Varian\\RTM\\15.5\\esapi\\API") # Prod
sys.path.append("C:\\Program Files (x86)\\Varian\\RTM\\15.5\\ExternalBeam") # Prod

import clr  # pip install pythonnet
clr.AddReference('System.Windows')
clr.AddReference('System.Linq')
clr.AddReference('System.Collections')
#clr.AddReference('System.Reflection')
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

SAFE_MODE = True  # if True all array copies are verified

class lot:
    '''a custom collection container for pysapi'''
    def __init__(self, some_collectable):
        self.collection = some_collectable

    def FirstOrDefault(self,fxn):
        result = list(filter(fxn,self.collection))
        if len(result) == 0:
            return None
        else:
            return result[0]
    
    def Select(self, fxn):
        '''returns a new lot of objects where fxn(object) == True'''
        if callable(fxn):
            return lot(list(filter(fxn,self.collection)))
        else:
            raise TypeError('fxn is not callable')
        
    def __getitem__(self,key):
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
    return lambda self,key=None: lot(getattr(self,attr)) if key is None else lot(getattr(self,attr))[key]


def lotify(T):
    '''adds lot accessors to IEnumerable children'''
    # TODO: add recursion
    ienum_t = System.Type.GetType('System.Collections.IEnumerable')
    t = System.Type.GetType(T.__module__+'.'+T.__name__+','+T.__module__)
    for p in t.GetProperties():
        # look for IEnumerable types
        if ienum_t.IsAssignableFrom(p.PropertyType) \
        and p.PropertyType.IsGenericType \
        and len(p.PropertyType.GetGenericArguments()) == 1:
            # add the lot accessor to the parent object
            setattr(T,p.Name+"Lot",lot_lambda(p.Name))


def check_arrays(a, b):
    '''array copy verification'''
    assert len(a) == len(b), "Arrays are different size!"
    assert any(A == B for A,B in zip(a, b)), "Arrays have different values!"


def to_ndarray(src,dtype):
    '''converts a blitable .NET array of type dtype to a numpy array of type dtype'''
    src_hndl = GCHandle.Alloc(src, GCHandleType.Pinned)
    try:
        src_ptr = src_hndl.AddrOfPinnedObject().ToInt64()
        dest = np.fromstring(string_at(src_ptr, len(src)*sizeof(dtype)),dtype=dtype)
    finally:
        if src_hndl.IsAllocated: src_hndl.Free()
    if SAFE_MODE:
        check_arrays(src, dest)
    return dest


def dose_to_nparray(dose):
    '''returns a 3D numpy.ndarray of floats indexed like [z,y,x]'''

    dose_shape = (dose.ZSize,dose.YSize,dose.XSize)
    dose_array = np.zeros(dose_shape)

    _buffer = Array.CreateInstance(Int32, dose.XSize, dose.YSize)
    for z in range(dose.ZSize):
        dose.GetVoxels(z,_buffer)
        dose_array[z,:,:] = to_ndarray(_buffer,dtype=c_int32).reshape((dose.XSize,dose.YSize)).T  # transposed to [y,x] ordering
        
    scale = float(dose.VoxelToDoseValue(1).Dose - dose.VoxelToDoseValue(0).Dose)  # maps int to float
    offset = float(dose.VoxelToDoseValue(0).Dose)/scale  # minimum dose value stored as int (zero if coming from Eclipse plan)
    return scale*dose_array.astype(float)+offset

def fill_in_profiles(dose_or_image, profile_fxn, row_buffer, dtype, pre_buffer=None):
    mask_array = np.zeros((dose_or_image.ZSize,dose_or_image.YSize,dose_or_image.XSize))

    z_direction = VVector.op_Multiply(Double(dose_or_image.ZSize * dose_or_image.ZRes),dose_or_image.ZDirection)
    for x in range(dose_or_image.XSize): # scan X dimension
        start_x = VVector.op_Addition(dose_or_image.Origin,
            VVector.op_Multiply(Double(x * dose_or_image.XRes),dose_or_image.XDirection))
        for y in range(dose_or_image.YSize): # scan Y dimension
            # get the profile along Z dimension
            start = VVector.op_Addition(start_x,VVector.op_Multiply(Double(y * dose_or_image.YRes),dose_or_image.YDirection))
            stop = VVector.op_Addition(start,z_direction)
            if pre_buffer is None:
                profile_fxn(start,stop,row_buffer)
            else:
                profile_fxn(start,stop,pre_buffer)
                pre_buffer.CopyTo(row_buffer,0)
            mask_array[:,y,x] = to_ndarray(row_buffer,dtype)
    return mask_array


def make_segment_mask_for_gird(structure,dose_or_image):
    '''returns a 3D numpy.ndarray of bools matching dose or image grid indexed like [z,x,y]'''
    return make_segment_mask_for_structure(dose_or_image,structure)


def make_segment_mask_for_structure(dose_or_image, structure):
    '''returns a 3D numpy.ndarray of bools matching dose or image grid indexed like [z,y,x]'''
    if (structure.HasSegment):
        mask_array = np.zeros((dose_or_image.ZSize,dose_or_image.YSize,dose_or_image.XSize))

        pre_buffer = System.Collections.BitArray(dose_or_image.ZSize);
        row_buffer = Array.CreateInstance(bool,dose_or_image.ZSize);
                
        return fill_in_profiles(dose_or_image,structure.GetSegmentProfile,row_buffer,c_bool,pre_buffer)
    else:
        raise Exception("structure has no segment data")


def make_dose_for_grid(dose, image=None):
    '''returns a 3D numpy.ndarray of doubles matching dose (default) or image grid indexed like [z,y,x]'''
    
    if image is not None:
        row_buffer = Array.CreateInstance(Double,image.ZSize);                
        dose_array = fill_in_profiles(image,dose.GetDoseProfile,row_buffer,c_double)
    else:
        # default
        dose_array = dose_to_nparray(dose)

    dose_array[np.where(np.isnan(dose_array))] = 0.0
    return dose_array


def compute_voxel_points_matrix(dose_or_image):
    
    origin = [dose_or_image.Origin.x,dose_or_image.Origin.y,dose_or_image.Origin.z]
    resolution = [dose_or_image.XRes,dose_or_image.YRes,dose_or_image.ZRes]
    _shape = [dose_or_image.XSize,dose_or_image.YSize,dose_or_image.ZSize]
    
    # create an array of points (location of each voxel)
    ax = []
    for dim in range(3):
        ax.append(np.linspace(
            start = origin[dim],
            stop = origin[dim] + _shape[dim]*resolution[dim],
            num = _shape[dim]
        ))

    # create a matrix of 3-vectors for voxel locations
    voxel_points = np.vstack((np.meshgrid(*ax,indexing='ij'))).reshape(3,*_shape).T
    voxel_points = np.swapaxes(voxel_points,0,2)  # gets us to [z,y,x]
    assert np.all(origin == voxel_points[0,0,0])
    assert np.all(origin + np.array(_shape) * np.array(resolution) == voxel_points[-1,-1,-1])
    return voxel_points


# where the magic happens:

# add any missing objects with IEnumerable childeren
lotify(Patient)
lotify(PlanSetup)
lotify(Course)
lotify(Beam)
lotify(StructureSet)

# monkeypatch numpy array translators
Structure.nparray_like = make_segment_mask_for_gird
Dose.nparray_like = make_dose_for_grid

Image.mask_nparray = make_segment_mask_for_structure
Dose.mask_nparray = make_segment_mask_for_structure

Image.voxel_pts_nparray = compute_voxel_points_matrix
Dose.voxel_pts_nparray = compute_voxel_points_matrix


