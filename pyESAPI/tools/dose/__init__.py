from ... import ExternalBeamMachineParameters, VRect, Double, Patient

def calc_pdd(phantom: Patient,
             PHANTOM_PID='water', STRUCTURE_SET_ID='CT_1',
             MACHINE_ID='23EX_Varian', ENERGY_MODE="15X",
             FIELD_SIZE_MM=100.0, SAVE_PLAN=False, COMM_COURSE='ShapeDose'):

    assert phantom.CanModifyData(), "Please allow modifications to the phantom first..."

    try:
        course = phantom.CoursesLot(COMM_COURSE)
    except:
        course = phantom.AddCourse()
        course.Id = COMM_COURSE

    #     print("Creating Plan...")
    plan = course.AddExternalPlanSetup(phantom.StructureSetsLot('CT_1'))
    plan.Id = "{0:.1f}x{0:.1f}".format(FIELD_SIZE_MM / 10.0)
    half_field_mm = FIELD_SIZE_MM / 2.0

    #     print("Creating Field...")
    beam = plan.AddStaticBeam(
        ExternalBeamMachineParameters(MACHINE_ID, ENERGY_MODE, 500, 'STATIC', None),
        VRect[Double](-half_field_mm, -half_field_mm, half_field_mm, half_field_mm),  # x1,y1,x2,y2
        90.0, 0.0, 0.0,  # gantry at 90 deg
        plan.StructureSet.Image.UserOrigin
    )

    # adjust to 100.0 CM SSD
    new_iso = beam.IsocenterPosition
    new_iso.y += beam.SSD - 1000.0

    plan.RemoveBeam(beam)

    beam = plan.AddStaticBeam(
        ExternalBeamMachineParameters(MACHINE_ID, ENERGY_MODE, 500, 'STATIC', None),
        VRect[Double](-half_field_mm, -half_field_mm, half_field_mm, half_field_mm),  # x1,y1,x2,y2
        90.0, 0.0, 0.0,  # gantry at 90 deg
        new_iso
    )
    beam.Id = "PDD"
    assert beam.SSD == 1000.0, "SSD computed wrong"

    print("Calculating Dose...", end='\r')
    calc_result = plan.CalculateDose()
    assert calc_result.Success, "Dose calc failed"

    dose = beam.Dose.np_array_like()
    vox_pts = beam.Dose.np_voxel_locations()
    #     print("Dose grid shape:", dose.shape)

    dose_slice = dose[:, :, int(dose.shape[2] / 2.0)]
    pdd_dose = dose_slice[int(dose.shape[0] / 2.0)].copy()
    pdd_dose /= pdd_dose.max()
    pdd_depth = vox_pts[int(dose.shape[0] / 2.0), :, int(dose.shape[2] / 2.0)][:, 1].copy()
    pdd_depth -= pdd_depth[0]

    print("Done!              ", end='\r')
    return {'depth_mm': pdd_depth, 'dose_relative': pdd_dose}