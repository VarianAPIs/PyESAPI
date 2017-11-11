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

import System
import System.Collections
import System.Linq
import System.Reflection
from VMS.TPS.Common.Model.Types import *
from VMS.TPS.Common.Model.API import *

class lot:
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

lotify(Patient)
lotify(PlanSetup)
lotify(Course)
lotify(Beam)
lotify(StructureSet)

