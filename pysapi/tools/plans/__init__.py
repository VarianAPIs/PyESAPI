from ... import VolumePresentation, DoseValuePresentation
from .shape_based_dose import dose_influence_matrix

def normalize_relative(plan, target_id, percent = 95.0):
    """ Sets a plan's normalization such that 100% of Rx dose covers a percent volume of a target
    
    Args:
        plan: PlanSetup object
        target_id: Structure Id of target (must be associated with the plan's structure set)
        percent: the percentage to normalize to (default: 95.0)
    """
    plan.set_PlanNormalizationValue(100.0)  # reset first
    
    # print("\tNormalizing to D{0} = 100% Rx of".format(percent),target_id)
    dPer = plan.GetDoseAtVolume(
        plan.StructureSet.StructuresLot(target_id),
        percent,
        VolumePresentation.Relative,
        DoseValuePresentation.Relative
    )
    plan.set_PlanNormalizationValue(dPer.Dose)
