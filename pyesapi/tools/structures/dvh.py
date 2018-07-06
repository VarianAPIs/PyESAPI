from ... import DoseValuePresentation, VolumePresentation

def dvh_absolute(plan, sId, dose_bin_width=.1):
    '''Shortcut to compute DVH with absolue dose and relative volume values.

    Args:
        plan: a pysapi.Plan object
        sId: the structure id of interest
        dose_bin_width: width of dose bins use for DVH calc in absolute dose units (default is .1)

    Returns:
        dose: list of DVH dose values in % of Rx
        volume: list of DVH volume values
    '''
    dvh = plan.GetDVHCumulativeData(
        plan.StructureSet.StructuresLot(sId),
        DoseValuePresentation.Relative,
        VolumePresentation.AbsoluteCm3,
        dose_bin_width
    )
    return [p.DoseValue.Dose for p in dvh.CurveData], [p.Volume for p in dvh.CurveData]

def dvh_relative(plan, sId, dose_bin_width=.1):
    '''Shortcut to compute DVH with relative dose and relative volume values.

    Args:
        plan: a pysapi.Plan object
        sId: the structure id of interest
        dose_bin_width: width of dose bins use for DVH calc in relative dose units (default is .1)

    Returns:
        dose: list of DVH dose values in system's dose units (cGy or Gy)
        volume: list of DVH volume values
    '''
    dvh = plan.GetDVHCumulativeData(
        plan.StructureSet.StructuresLot(sId),
        DoseValuePresentation.Relative,
        VolumePresentation.Relative,
        dose_bin_width
    )
    return [p.DoseValue.Dose for p in dvh.CurveData], [p.Volume for p in dvh.CurveData]