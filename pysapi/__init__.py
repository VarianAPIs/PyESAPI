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
from ctypes import string_at, sizeof, c_int32, c_bool

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

def segment_mask_for_dose_gird(structure, dose):
    '''returns a 3D numpy.ndarray of bools matching dose grid indexed like [z,y,x]'''
    if (structure.HasSegment):
        dose_shape = (dose.ZSize,dose.YSize,dose.XSize)
        mask_array = np.zeros(dose_shape)

        pre_buffer = System.Collections.BitArray(dose.ZSize);
        row_buffer = Array.CreateInstance(bool,dose.ZSize);
        
        z_direction = VVector.op_Multiply(Double(dose.ZSize * dose.ZRes),dose.ZDirection)
        for x in range(dose.XSize): # scan X dimension
            start_x = VVector.op_Addition(dose.Origin,
                VVector.op_Multiply(Double(x * dose.XRes),dose.XDirection))
            for y in range(dose.YSize): # scan Y dimension
                # get the profile along Z dimension
                start = VVector.op_Addition(start_x,VVector.op_Multiply(Double(y * dose.YRes),dose.YDirection))
                stop = VVector.op_Addition(start,z_direction)
                structure.GetSegmentProfile(start,stop,pre_buffer)
                pre_buffer.CopyTo(row_buffer,0)
                mask_array[:,y,x] = to_ndarray(row_buffer,c_bool)
                
        return mask_array
    else:
        raise Exception("structure has no segment data")

# where the magic happens:

# add any missing objects with IEnumerable childeren
lotify(Patient)
lotify(PlanSetup)
lotify(Course)
lotify(Beam)
lotify(StructureSet)

# monkeypatch numpy array translators
Structure.asarray = segment_mask_for_dose_gird
Dose.asarray = dose_to_nparray


