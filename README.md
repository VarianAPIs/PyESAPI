## Links
* [Developer Workshop 2018 Material](tree/master/examples/DeveloperWorkshop2018)

## Quickstart

* Install [Anaconda3](https://www.anaconda.com/download/?lang=en-us) for "Just Me" (unless you know what you are doing)
  * Use defaults (don't add anaconda to path, but do set ananconda as your default python installation)
* Optionally install google chrome browser (for better Jupyter Notebook experience) and set it as your default browser
* Launch Anaconda Prompt
* Execute the command `pip install pythonnet`
* Execute the command `jupyter notebook`
* Create a new notebook and start with example below to test basic functionality

## Example
Below is taken from [example.py](https://github.com/VarianPremiumDeveloper/PyESAPI/blob/master/examples/example.py) in [examples](https://github.com/VarianPremiumDeveloper/PyESAPI/blob/master/examples) folder.

```python
import sys
sys.path.append(r'C:\Users\Varian\source\repos\vmspy')  # path to vmspy repo
import pyesapi
pyesapi.SAFE_MODE = False # bypass C# to Numpy array verification (faster)
from matplotlib import pyplot as plt
import numpy as np
from time import time
import atexit
#load app only once
app = pyesapi.CustomScriptExecutable.CreateApplication('python_demo')  # script name is used for logging
# setup clean exit
atexit.register(app.Dispose)


# In[2]:

patient = app.OpenPatientById('001')


# In[10]:

# shortcut for patient.Courses.ElementAt(0).PlanSetups.FirstOrDefault(lambda x: x.Id == '1 IMRT Prost' )
plan = patient.CoursesLot(0).PlanSetupsLot('1 IMRT Prost')

# normal indexing works too
structures = patient.StructureSetsLot()[0].StructuresLot()

# lot.Select takes a function and returns a lot
fem_heads = structures.Select(lambda s: 'fem' in s.Id)
print("Fem Heads:",[(f.Id,f.Volume) for f in fem_heads])

# python.NET treats IEnumerables as an iterable anyway
import pandas as pd
print(
    "Patients:\n",
    pd.DataFrame(
        [(p.Id, p.LastName) for p in app.PatientSummaries],
        columns = ['Id', 'Last Name']
    )[3:13]
)  

body1 = patient.StructureSetsLot()[0].StructuresLot('body')
body = structures['body']  # another shortcut for FirstOrDefault on Id field
assert body == body1  # same object

voxels = plan.Dose.np_voxel_locations()  # a PyESAPI extension!
#voxels = plan.StructureSet.Image.np_voxel_locations()  # a PyESAPI extension!


# In[11]:

# let's grab some structure masks using PyESAPI extension method
# this is actually a little slow, but worth the wait... (better impemented in c++ and added to ESAPI)
structures_of_interest = ['PTV 8100','bladder','rectum','body']
masks = {}
tic = time()
for s in structures:
    if s.Id in structures_of_interest:
        print("Creating mask for {} at Dose grid resolution...            ".format(s.Id),end='\r')
        masks[s.Id] = plan.Dose.np_structure_mask(s)  # PyESAPI extension!
        #print("Creating mask for {} at CT Image resolution...            ".format(s.Id),end='\r')
        #masks[s.Id] = plan.StructureSet.Image.np_structure_mask(s)  # PyESAPI extension!
print("Creating structure masks took {:0.2f} s                   ".format(time()-tic))

tic = time()
dose = plan.Dose.np_array_like()  # PyESAPI extension! (Dose at Dose grid resolution, default)
#dose = plan.Dose.np_array_like(plan.StructureSet.Image)  # PyESAPI extension! (Dose at CT Image resolution)
print("Extracting dose took {:0.2f} s".format(time()-tic))


# In[12]:

# run some verification based on Structure.IsPointInsideSegment(VVector) ...
# this is very slow!
for sId in structures_of_interest:
    print("Verifying {} mask...".format(sId))
    pyesapi.validate_structure_mask(structures[sId],masks[sId],voxels)


# In[13]:

# plot a dose slice ...
assert plan.DoseValuePresentation == pyesapi.DoseValuePresentation.Relative, "dose not in relative units"
slice_idx = 39
slice_z_mm = voxels[0,0,slice_idx][2]  # a 3D array of 3D points of locations for each voxel
print(dose.shape)
plt.imshow(dose[:,:,slice_idx].T,interpolation=None,cmap='jet')  # indexed as [x,y,z], transpose needed for imshow
plt.axis('off')
plt.colorbar()
plt.title("Rx Relative Dose (Z = {:.1f})".format(slice_z_mm))
plt.show()


# In[14]:

# plot masked dose ...
all_masks = np.zeros_like(masks['body'])
for k,mask in masks.items():
    if k == 'body':
        continue
    all_masks = np.logical_or(all_masks,mask)

plt.imshow((dose*all_masks)[:,:,slice_idx].T,interpolation=None,cmap='jet')  # mask is indexed same as dose grid
plt.axis('off')
plt.colorbar()
plt.title("")
plt.show()


# In[15]:

# let's compute some DVH "by hand" and compare to Eclipse

plt.figure(figsize=(10,7))
for sId in ['PTV 8100','bladder','rectum','body']:
    mask_idx = np.where(masks[sId])
    tot_vox = np.ones_like(dose)[mask_idx].sum()
    hist,bins = np.histogram(dose[mask_idx].flatten(),bins=1000,range=(0,dose.max()))

    plt.plot(bins[:-1],100.-hist.cumsum()*100.0/tot_vox,label=sId)
    dvh = plan.GetDVHCumulativeData(
        structures[sId],
        pyesapi.DoseValuePresentation.Relative,
        pyesapi.VolumePresentation.Relative,
        .01
    )
    pts = np.array([[p.DoseValue.Dose,p.Volume] for p in dvh.CurveData])
    plt.plot(pts[:,0],pts[:,1],'k--',alpha=.33)

plt.legend(loc=0)
plt.title("Mask-Calculated DVH vs. Eclipse DVH (gray dashed lines)")
plt.show()


# In[16]:

# to exit cleanly when done...
app.ClosePatient()

```
