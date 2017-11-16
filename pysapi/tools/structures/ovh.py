from .. import Double
import numpy as np

def cumovh(structure_set, ptv_id, oar_id, min_mm=-10.0, max_mm=50.0, step_mm=5.0,norm=True):
    '''Compute the cumulative overlapping volume histogram (cOVH) for a target and an organ.
    Requires write accesss to patient objects.
    
    Args:
        structure_set: a pysapi.Structure object
        ptv_id: the structure id of the primary target volume (PTV) to be expaned
        oar_id: the structure id of the organ at risk (OAR) for which the OVH is to be calculated
        min_mm: the expansion in mm to start with, should be greater than -50.0 mm (default is -10.0)
        max_mm: the expansion in mm to compute up to, should be less than 50.0 mm (default is 50.0)
        step_mm: the steps in mm to take after min_mm and up to but not exceeding max_mm (default is 5.0)
    
    Returns:
        mm: an np.array of expansions in mm of the target
        volume: a np.array of the computed overlap volume of the corrisponding expansions in cm^3      
    '''
    ptv = structure_set.StructuresLot(ptv_id)
    oar = structure_set.StructuresLot(oar_id)

    try:
        overlap = structure_set.AddStructure('DOSE_REGION','temp_pysapi2')
        ovh_mm = np.arange(min_mm, max_mm, step_mm, dtype=Double)
        ovh_vol = []

        for expanded_mm in ovh_mm:
            overlap.SegmentVolume = oar.And(ptv.Margin(expanded_mm))
            ovh_vol.append(overlap.Volume)
    finally:
        structure_set.RemoveStructure(overlap)

    return ovh_mm, np.array(ovh_vol)