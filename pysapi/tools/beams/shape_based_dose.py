import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from scipy.sparse import csr_matrix, lil_matrix, hstack, vstack
from ..geometry import rotation_matrix, proj_iso_plane  # , make_fluence_maps
from time import time
# from scipy.signal import convolve2d
from scipy.ndimage import convolve
from scipy.ndimage.interpolation import rotate

#  commissioning data and fit fxns

pdd_data = {
    "6X": {
        "buildup": [-0.00015749459237802087, 0.018456397544299074, -0.88448139491242872, 22.163062813849965,
                    -312.23926598651917, 2449.7961711094094, 1749.682558831852],
        "split": 18.75,
        "falloff": [-2.8264719677060061e-07, 0.00024313850219755478, -0.036093426359969094, -28.230918530108855,
                    11245.762396352433]
    },
    "15X": {
        "buildup": [-2.7723087151505166e-06, 0.00055879347539751413, -0.053759468984408219, 3.0197899077600456,
                    -101.31274784968605, 1888.8581630228164, 1293.1597039077351],
        "split": 32.8125,
        "falloff": [-1.9597228831831153e-11, 2.693437995470181e-08, -1.4915457123262073e-05, 0.0042146835045338083,
                    -0.58755541834481695, -2.688095323220637, 17061.029792989608]
    },
    # "15X": {
    #     "buildup": [-2.781688925124089e-06, 0.0005606841739703134, -0.054105297895991306, 3.0520358074793372,
    #                 -102.57441264586714, 1907.2660184066269, 1267.6475603080792],
    #     "split": 32.8125,
    #     "falloff": [-2.8839890418852902e-11, 3.887703303176435e-08, -2.0889148193952867e-05, 0.0056726958756894907,
    #                 -0.7677552995266792, 7.7496351540534905, 16882.372184793865]
    # },
    "15X_old": {
        "buildup": [-1.6507633296164477e-06, 0.00028630426498036006, -0.02888629114824896, 1.7451265889913861,
                    -61.497244761739545, 1171.9987395979024, 1674.4131730133356],
        "split": 28.125,
        "falloff": [-2.954626231433345e-07, 0.00024567974262585063, -0.052934868220503181, -18.176864694198056,
                    11639.846648127208]
    }
}

kernel_data = {
    "15X": [0.00028964017385020818, 0.00011667873579437889, 0.0024779599104120744, 6.4674171413250718,
            18.237437627703674, 1.5545102702143783],

    # (f1,f2,f3,s1,s2,r3)
    #               {
    #     'f2':.2,#.32,
    #     'f3':0.0,#.0052, # ODDS ARE THIS FACTOR IS WRONG
    #     'sig1': 1.0,#1.1,  # calibrated with 2 mm kernel
    #     'sig2': 2.0,#2.9,
    # },
    # "6X":{
    #     'calib_beam_size_mm': 2.0, # calibrated with 2 mm kernel
    #     'f2':.09,
    #     'f3':.0043,
    #     'sig1':.8,
    #     'sig2':1.9,
    # },
}


def compute_Dij(dose_shape, idxs_oi, pts_3d, pts_3d_shell, SAD=1000., gantry_angle=0., field_size=100.,
                beamlet_size_x=1., beamlet_size_z=5., field_buffer=20., beam_energy="6X", show_plots=False,
                anti_alias=False):
    """
    all units in mm (DICOM)
    returns a "ray-trace" Dij matrix (no scatter)
    :param SAD:
    :param gantry_angle:
    :param field_size:
    :param beamlet_size:
    :param field_buffer: added to all sides of the field
    :param beam_energy:
    :param show_plots:
    :param anti_alias:

    1)

    :return:
    """
    big_tic = time()
    # dose calc settings
    # SAD = 1000.  # mm
    # gantry_angle = 0.  # degrees

    # all geometry defined on iso-center plane as usual
    # field_size = 100.  # mm (square)
    # beamlet_size = 1.  # mm (square)
    # field_buffer = 20.  # mm (width of region beyond field - allows for scattering outside of field)

    # BUILD FLUENCE MAP ###############################################################################################

    tic = time()

    # pre-sanity check
    assert field_size % beamlet_size_x == 0, "field_size must be integer multiple of beamlet_size"
    assert field_buffer % beamlet_size_x == 0, "field_buffer must be integer multiple of beamlet_size"

    assert field_size % beamlet_size_z == 0, "field_size must be integer multiple of beamlet_size"
    assert field_buffer % beamlet_size_z == 0, "field_buffer must be integer multiple of beamlet_size"

    # some pre-calcualted variables which are re-used throughout the code
    src = [0, SAD, 0]  # source point @ 0 degrees rotation in (isocenter-shifted) DICOM ref. frame
    src_rot = np.dot(rotation_matrix([0., 0., np.radians(180. - gantry_angle)]), src)
    # print(src_rot)
    # setup fluence grid
    expanded_field_size = field_size + 2. * field_buffer  # [buffer][field][buffer]
    field_buffer_x_px = int(field_buffer / beamlet_size_x)  # number of fluence pixels in buffer region
    field_size_x_px = int(field_size / beamlet_size_x)  # number of fluence pixels in field

    field_buffer_z_px = int(field_buffer / beamlet_size_z)  # number of fluence pixels in buffer region
    field_size_z_px = int(field_size / beamlet_size_z)  # number of fluence pixels in field

    # compute BOUNDARIES of fluence map pixels (note the +1)
    x_map_boundaries = np.linspace(-expanded_field_size / 2., expanded_field_size / 2.,
                                   int(expanded_field_size / beamlet_size_x) + 1)
    z_map_boundaries = np.linspace(-expanded_field_size / 2., expanded_field_size / 2.,
                                   int(expanded_field_size / beamlet_size_z) + 1)
    # z_map_boundaries = x_map_boundaries
    x_mesh_boundaries, z_mesh_boundaries = np.meshgrid(x_map_boundaries, z_map_boundaries)

    # sanity check
    # print(x_mesh_boundaries.shape[1], 2*field_buffer_x_px + field_size_x_px + 1, "x field dimensions")
    # print(x_mesh_boundaries.shape[0], 2*field_buffer_z_px + field_size_z_px + 1, "x field dimensions")

    assert x_mesh_boundaries.shape[1] == 2 * field_buffer_x_px + field_size_x_px + 1, "error computing field dimensions"
    assert x_mesh_boundaries.shape[0] == 2 * field_buffer_z_px + field_size_z_px + 1, "error computing field dimensions"

    # compute CENTRAL POINTS of pixels on fluence map
    x_map_centers = np.linspace(-expanded_field_size / 2. + beamlet_size_x / 2,
                                expanded_field_size / 2. - beamlet_size_x / 2.,
                                int(expanded_field_size / beamlet_size_x))

    z_map_centers = np.linspace(-expanded_field_size / 2. + beamlet_size_z / 2,
                                expanded_field_size / 2. - beamlet_size_z / 2.,
                                int(expanded_field_size / beamlet_size_z))

    # z_map_centers = x_map_centers
    x_mesh_centers, z_mesh_centers = np.meshgrid(x_map_centers, z_map_centers)

    # print(len(x_map))
    # print(x_map.min(), x_map.max())

    # get point data
    # vox_size = study['{}/voxel_size'.format(ct_group)]
    # pts_3d = study['{}/voxel_coords'.format(ct_group)] - isocenter
    # try grabbing body contour instead?
    # pts_3d_shell = (study['ct/voxel_coords'.format(ct_group)] - isocenter)[np.where(study[body_shell_path])]  # shell path in full resolution?

    print(time() - tic, ' sec for init')

    # BUILD SURFACE DISTANCE MAP ######################################################################################

    tic = time()

    # rotate and project points to isocenter plane
    pts_proj = proj_iso_plane(pts_3d_shell.T, SAD, gantry_angle)
    # pick out relevant points (y dimension should always be zero)
    x = pts_proj[0]
    z = pts_proj[2]

    # optional, adds ~30 compute time to this section
    assert sum(pts_proj[1]) == 0.0, "unexpected behavior of projection operation"

    # create digitize bin boundaries at a lower resolution: make space wider by 1cm on each side (buffer zone)
    # THESE SET BOUNDARIES - indexing is not a problem here since we use matching rather than slicing on this step
    x_bins = np.linspace(-field_size / 2. - 1.5 * field_buffer, field_size / 2. + 1.5 * field_buffer, 25)
    z_bins = np.linspace(-field_size / 2. - 1.5 * field_buffer, field_size / 2. + 1.5 * field_buffer, 25)

    x_dig = np.digitize(x, x_bins)  # the binned indices along x dimension: x_bins[i-1] <= x < x_bins[i]

    # the actual limits of the projected data
    # print('x', x.min(), x.max())
    # print('z', z.min(), z.max())

    # stores distance values for each bin
    d_min = []
    # d_max = []

    # stores the point values for each bin
    p_min = []
    # p_max = []

    # for each x-bin "i" (digitize returns valid index between 1 <= i < len(x_bins))
    for i in range(1, len(x_bins)):

        # find indices of points within the current x-bin "i"
        idx_x = np.array(np.where(x_dig == i))

        # get binned indices along z dimension for the points withing x-bin "i"
        z_dig = np.digitize(z[idx_x], z_bins)  # z_bins[j-1] <= z < z_bins[j]

        # for each z-bin "j"
        for j in range(1, len(z_bins)):

            # find the indices of points within current x-bin "i" and z-bin "j"
            idx_xz = idx_x[np.where(z_dig == j)]

            # if there is more than one point in the current xz-bin "i,j"
            if len(idx_xz) > 1:
                # get the 3d coordinate for each point
                pix_pts = pts_3d_shell[idx_xz, :]

                # get the 2d coordinate for each point (on projection plane)
                pln_pts = pts_proj[:, idx_xz]

                # compute distances to source for the 3d points
                dists = np.linalg.norm(pix_pts - src_rot, axis=1)  # faster

                # save the 2d coordinates of the minimum and maximum distance points
                p_min.append(pln_pts[::2, dists.argmin()])  # only selecting x-y component
                # p_max.append(pln_pts[::2, dists.argmax()])  # only selecting x-y component

                # save the distances to the minimum and maximum 3d points
                d_min.append(dists.min())
                # d_max.append(dists.max())
        del z_dig

    del x_dig

    # cast to numpy array
    p_min = np.array(p_min)
    d_min = np.array(d_min)
    # p_max = np.array(p_max)
    # d_max = np.array(d_max)

    print(time() - tic, 'sec for surface map computation')

    if show_plots:
        # example of interpolated distance map @ fluence map resolution
        # create interpolated distance map
        d_map = griddata(p_min, d_min, (x_mesh_centers, z_mesh_centers), method='cubic')
        print(d_map.shape)
        plt.imshow(d_map, interpolation='none')
        plt.colorbar()
        print("dmap mean SSD:", d_map.mean(), " mm")
        plt.show()

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        # surf = ax.plot_surface(x_mesh,z_mesh,d_min.max()-d_map)
        ax.scatter(p_min[:, 0], p_min[:, 1], d_min)
        plt.show()

    # COMPUTE DEPTH TO EACH POINT #####################################################################################

    tic = time()

    # create dose grid (@ CT resolution for now)
    dose_test = np.zeros(dose_shape)

    # only select points inside body contour
    # idxs_oi = np.where(study[body_contour_path] > 0)
    pts_3d_oi = pts_3d[idxs_oi]  # points within body contour

    # project all points to isocenter plane
    vol_proj = proj_iso_plane(pts_3d_oi.T, SAD, gantry_angle)

    # compute physical distance between source and all points of interest
    dist_pts = np.linalg.norm(pts_3d_oi - src_rot, axis=1)

    # compute physical distance between body surface and all points of interest
    dx_map = griddata(p_min, d_min, (vol_proj[0], vol_proj[2]), method='cubic')

    dose_test[idxs_oi] = dist_pts - dx_map

    # only used for testing/validation
    # dose_test[idxs_oi] = np.divide(dist_pts,np.square(dist_pts))
    print(time() - tic, "sec for depth calculation")

    if show_plots:
        plt.imshow(dose_test[:, :, dose_test.shape[2] / 2])
        plt.colorbar()
        plt.show()
        # plt.imshow(dose_test[:,dose_test.shape[1]/2,:])
        # plt.colorbar()
        # plt.show()

    del dx_map

    # APPLY PDD #######################################################################################################

    tic = time()

    pdd_f_fxn = np.poly1d(pdd_data[beam_energy]['falloff'])
    pdd_b_fxn = np.poly1d(pdd_data[beam_energy]['buildup'])

    # make copy of distance data
    pdd_dose = dose_test.copy()

    # optional cleanup
    # nan_vals = np.where(np.isnan(pdd_dose))
    # pdd_dose[nan_vals] = 0.

    # select buildup region by index
    bu_idx = np.where(pdd_dose <= pdd_data[beam_energy]['split'])
    # select fall off region by index
    fo_idx = np.where(pdd_dose > pdd_data[beam_energy]['split'])

    # apply buildup and falloff PDD filter
    # TODO: can we narrow the indexing here rather than applying to full dose grid?
    pdd_dose[bu_idx] = pdd_b_fxn(pdd_dose[bu_idx])
    pdd_dose[fo_idx] = pdd_f_fxn(pdd_dose[fo_idx])

    # normalize by physical distance (1/square(r))
    # TESTING NO NORM
    pdd_dose[idxs_oi] = np.divide(pdd_dose[idxs_oi], np.square(dist_pts))

    # cleanup dose grid
    pdd_dose[np.where(np.isnan(pdd_dose))] = 0.0
    pdd_dose[np.where(pdd_dose < 0.0)] = 0.0

    print(time() - tic, 'sec to apply PDD')
    del bu_idx
    del fo_idx

    # BUILD SPARSE MATRIX #############################################################################################

    # here we form the "ray trace" matrix for computing dose given a fluence map
    # TODO: double check behavior of np.digitize

    # some variable shortcuts
    x_map_n = len(x_map_centers)
    z_map_n = len(z_map_centers)

    def digitize_voxel_mtx(vol_pts, x_map_bounds, z_map_bounds, x_shift=0.0, z_shift=0.0):
        # digitize the location of each vozel point on the fluence plane
        v_dig_x = np.digitize(vol_pts[0] + x_shift, x_map_bounds) - 1
        v_dig_z = np.digitize(vol_pts[2] + z_shift, z_map_bounds) - 1
        # select on valid indeces within fluence map
        v_dig_valid = np.where((0 <= v_dig_x) & (v_dig_x < x_map_n) & (0 <= v_dig_z) & (v_dig_z < z_map_n))

        tmp = pdd_dose[idxs_oi]

        # form sparse dose matrix:
        sparse_dose = tmp[v_dig_valid].flatten().copy()

        fmap_width = len(x_map_bounds) - 1  # we subtract 1 here because boundaries are of length x_map_n+1

        col_idx = v_dig_x[v_dig_valid] + fmap_width * (v_dig_z[v_dig_valid])
        row_idx = v_dig_valid[0]  # np.array(range(len(sparse_dose)))
        del tmp
        del v_dig_x
        del v_dig_z
        return csr_matrix((sparse_dose.astype(np.float32), (row_idx, col_idx)),
                          shape=(
                              len(idxs_oi[0]),
                              (x_map_boundaries.shape[0] - 1) * (z_map_boundaries.shape[0] - 1)
                          ))

    if anti_alias:
        # this averages out beamlet contributions across neighboring voxels

        d = 2.

        csr = digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries)

        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  x_shift=-beamlet_size_x / d, z_shift=-beamlet_size_z / d)
        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  x_shift=+beamlet_size_x / d, z_shift=+beamlet_size_z / d)
        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  x_shift=-beamlet_size_x / d, z_shift=+beamlet_size_z / d)
        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  x_shift=+beamlet_size_x / d, z_shift=-beamlet_size_z / d)

        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  z_shift=-beamlet_size_z / d)
        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  z_shift=+beamlet_size_z / d)
        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  x_shift=-beamlet_size_x / d)
        csr += digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries,
                                  x_shift=+beamlet_size_x / d)

        csr /= 9.
    else:
        csr = digitize_voxel_mtx(vol_proj, x_map_boundaries, z_map_boundaries)
    # print(col_idx.max())
    # print(csr.shape)
    # print(csr.nnz)

    print("total time: ", time() - big_tic, " sec")

    return csr  # , idxs_oi# v_dig_valid #, x_bins, z_bins


def _g_func(r, sig):
    return np.exp(- np.square(r / sig) / 2.0) / sig / np.sqrt(2.0 * np.pi)


def _e_func(r, sig):
    return np.exp(- np.abs(r / sig)) / 2.0


def _scatt_func(r, f1, f2, f3, sig1, sig2, sig3):
    return f1 * _g_func(r, sig1) + f2 * _g_func(r, sig2) + f3 * _e_func(r, sig3)


def _scatter_kernel(x, y, popt):
    scatt_temp = _scatt_func(np.sqrt(np.square(x) + np.square(y)), *popt)
    return scatt_temp / scatt_temp.max()


# def _scatter_kernel(x, y, bx_size_x,bx_size_y,centers=None,energy='6X'):
#     """
#     :param x: grid of x locations in fluence map [mm]
#     :param y: grid of y locations in fluence map [mm]
#     :param bx_size_x: beamlet size along x dimension (i know i could just calculate it, sorry)
#     :param bx_size_y:
#     :param centers:
#     :param energy: string for kernel configuration
#     :return: 2d scatter kernel
#     """
#
#     _r = np.sqrt( np.square(x-centers[0]) + np.square(y-centers[1]) )
#     return _scatt_func(_r,kernel_data[energy]['f1'],kernel_data[energy]['f2'],kernel_data[energy]['f3'],
#                        kernel_data[energy]['sig1'],kernel_data[energy]['sig2'],kernel_data[energy]['sig3'])

def make_sh2o_Dij_template(study, template, ct_group='ct_lowres', body_shell_path='structures/body/shell',
                           dose_mask_path='structures_lowres/body/mask', dij_cutoff=1e-4):
    """
    Should create a Dij for each beam in the template, with the template containing field sizes, isocenters, and gantry angles

    Parameters
    ----------
    study
    template
    ct_group
    body_shell_path
    dose_mask_path
    trial_name
    anti_alias

    Returns
    -------

    """
    pass


def _make_csr(_group):
    m = _group['DijT_csr']
    return csr_matrix((m['data'], m['indices'], m['indptr']), shape=m['shape'])


def get_DijT(study, dose_group='dose_sh2o'):
    return _make_csr(study.h5[dose_group])


def make_maps_from_x(study, dose_group='dose_sh2o', alt_x_path=None):
    if alt_x_path is None:
        x = study['{}/x'.format(dose_group)]
    else:
        x = study[alt_x_path]

    # count beams
    n_beams = len(study['{}/beams'.format(dose_group)].keys())
    aps = x.reshape((n_beams, -1))
    N = aps.shape[1]
    beamlet_size_xz_mm = study[
        '{}/beams/{}/beamlet_size_xz_mm'.format(dose_group, 1)]  # assume at least 1 beam all same size
    xy_beamlet_ratio = beamlet_size_xz_mm[1] / beamlet_size_xz_mm[0]
    n_flu_x = int(np.sqrt(N / xy_beamlet_ratio))
    n_flu_y = int(xy_beamlet_ratio * n_flu_x)

    assert n_flu_y * n_flu_x == N, "wrong xy_beamlet_ratio"
    print(n_flu_x, n_flu_y)
    print(n_beams)

    for beam_number in range(1, n_beams + 1):
        # we also compute JAW information, however, it's probably not much different from the original tps plan
        flu = aps[(beam_number - 1)].reshape(n_flu_y, n_flu_x)
        idx = np.where(flu.sum(0) > 0)
        x_idx_min = idx[0][0] - 1
        x_idx_max = idx[0][-1] + 1
        x_midpoint = float(n_flu_x) / 2.0
        x_1 = (x_idx_min - x_midpoint) * beamlet_size_xz_mm[0]
        x_2 = (x_idx_max - x_midpoint) * beamlet_size_xz_mm[0]
        # print("x:", x_idx_min, x_idx_max, x_midpoint)
        # print("x1mm:", x_1)
        # print("x2mm:", x_2)

        idx = np.where(flu.sum(1) > 0)
        y_idx_min = idx[0][0] - 1
        y_idx_max = idx[0][-1] + 1
        y_midpoint = float(n_flu_y) / 2.0
        y_1 = (y_idx_min - y_midpoint) * beamlet_size_xz_mm[1]
        y_2 = (y_idx_max - y_midpoint) * beamlet_size_xz_mm[1]
        # print("y", y_idx_min, y_idx_max, y_midpoint)
        # print("y1mm:", y_1)
        # print("y2mm:", y_2)

        study.create_dataset('{}/beams/{}/{}'.format(dose_group, beam_number, 'jaw_x1'), x_1, compression=None)  # mm
        study.create_dataset('{}/beams/{}/{}'.format(dose_group, beam_number, 'jaw_x2'), x_2, compression=None)
        study.create_dataset('{}/beams/{}/{}'.format(dose_group, beam_number, 'jaw_y1'), y_1, compression=None)
        study.create_dataset('{}/beams/{}/{}'.format(dose_group, beam_number, 'jaw_y2'), y_2, compression=None)
        study.create_dataset('{}/beams/{}/map'.format(dose_group, beam_number), flu.T)


def _make_sh2o_Dij_beam(dose_shape, idxs_oi, pts_3d_ct, pts_3d_shell_ct, pysapi_beam, field_size_mm,
                        field_buffer_mm,
                        beamlet_size_x_mm, beamlet_size_z_mm):
    """ Ready for use in PySAPI """
    print("Beam: #{} ({})".format(pysapi_beam.get_BeamNumber(), pysapi_beam.Id))

    #  since each beam could have a different isocenter
    isocenter_mm = [pysapi_beam.IsocenterPosition.x, pysapi_beam.IsocenterPosition.y,
                    pysapi_beam.IsocenterPosition.z]  # already in mm
    pts_3d = pts_3d_ct - isocenter_mm
    pts_3d_shell = pts_3d_shell_ct - isocenter_mm

    gantry_angle_deg = pysapi_beam.ControlPoints[0].GantryAngle
    assert np.all([cp.GantryAngle == gantry_angle_deg for cp in pysapi_beam.ControlPoints]), "Arc beams not implemented."

    csr = compute_Dij(  # v_dig_valid, x_bins, y_bins
        dose_shape,
        idxs_oi,
        pts_3d,
        pts_3d_shell,
        SAD=pysapi_beam.TreatmentUnit.get_SourceAxisDistance(),
        gantry_angle=gantry_angle_deg,
        field_size=field_size_mm,
        field_buffer=field_buffer_mm,  # added to all sides
        beamlet_size_x=beamlet_size_x_mm,
        beamlet_size_z=beamlet_size_z_mm,
        show_plots=False,
        anti_alias=True
    )

    tic = time()
    print(time() - tic, "sec", csr.__repr__())
    return csr


def _calc_num_px_for_field(field_size_mm, field_buffer_mm, beamlet_size_x_mm, beamlet_size_z_mm):
    field_buffer_x_px = int(field_buffer_mm / beamlet_size_x_mm)  # number of fluence pixels in buffer region
    field_size_x_px = int(field_size_mm / beamlet_size_x_mm)  # number of fluence pixels in field
    x_map_n = 2 * field_buffer_x_px + field_size_x_px

    field_buffer_z_px = int(field_buffer_mm / beamlet_size_z_mm)  # number of fluence pixels in buffer region
    field_size_z_px = int(field_size_mm / beamlet_size_z_mm)  # number of fluence pixels in field
    z_map_n = 2 * field_buffer_z_px + field_size_z_px

    return x_map_n, z_map_n


def compute_shape_dose_influence_matrix(pysapi_plan, body_shell, pts_3d_ct, dose_mask, fluence_cutoff=5e-3,
                                        return_scatter_matrix=False):
    """ Ready for use in PySAPI """

    beam_energy = pysapi_plan.BeamsLot(0).EnergyModeDisplayName
    assert np.all([beam_energy == b.EnergyModeDisplayName for b in
                   pysapi_plan.Beams]), "Beams having different energies is not implemented."

    ## testing alternative sizes
    beamlet_size_x_mm = 2.5  # 1.0 # this is minimum leaf resolution, set to 1.0 mm
    beamlet_size_z_mm = 2.5  # 5.0 # truebeam HD is 5.0mm and 10.0mm clinac is 10.0mm
    field_buffer_mm = 20.0  # or 2 cm, needed for penumbra

    idxs_oi = np.where(dose_mask > 0)  # indexes Of Interest

    # this should happen at full resulution if possible
    pts_3d_shell_ct = pts_3d_ct[np.where(body_shell)]

    field_size_mm = 0.
    # scan control points to get max square field size
    for beam_obj in pysapi_plan.Beams:
        jaws_max_mm = np.max([np.abs([cp.get_JawPositions().get_X1() for cp in beam_obj.ControlPoints]).max(),
                              np.abs([cp.get_JawPositions().get_X2() for cp in beam_obj.ControlPoints]).max(),
                              np.abs([cp.get_JawPositions().get_X1() for cp in beam_obj.ControlPoints]).max(),
                              np.abs([cp.get_JawPositions().get_X2() for cp in beam_obj.ControlPoints]).max()])
        tst_fsize = 2. * jaws_max_mm
        if tst_fsize > field_size_mm:
            field_size_mm = tst_fsize

    # snap to nearest reasonable size (evenly divisible by beamlet size)
    field_size_mm = np.ceil(field_size_mm / beamlet_size_z_mm) * beamlet_size_z_mm

    print("common field size (mm): ", field_size_mm)
    print("assigned leaf width/beamlet size X *anisotropic* (mm): ", beamlet_size_x_mm)
    print("assigned leaf width/beamlet size Z *anisotropic* (mm): ", beamlet_size_z_mm)

    # pre-sanity check
    assert field_size_mm % beamlet_size_x_mm == 0, "field_size must be integer multiple of beamlet_size"
    assert field_buffer_mm % beamlet_size_x_mm == 0, "field_buffer must be integer multiple of beamlet_size"

    assert field_size_mm % beamlet_size_z_mm == 0, "field_size must be integer multiple of beamlet_size"
    assert field_buffer_mm % beamlet_size_z_mm == 0, "field_buffer must be integer multiple of beamlet_size"

    x_map_n, z_map_n = _calc_num_px_for_field(field_size_mm, field_buffer_mm, beamlet_size_x_mm, beamlet_size_z_mm)

    v_mtx = lil_matrix((x_map_n * z_map_n, x_map_n * z_map_n), dtype=np.float32)  # the 2D scatter kernel matrix

    print(x_map_n)
    for i in range(x_map_n):
        x_ax = (np.array(range(x_map_n)) - i) * beamlet_size_x_mm
        if i % 10 == 0:
            print("row: {}".format(i), end='\r')
        for j in range(z_map_n):
            y_ax = (np.array(range(z_map_n)) - j) * beamlet_size_z_mm
            x_m, y_m = np.meshgrid(x_ax, y_ax)
            k = _scatter_kernel(y_m, x_m, kernel_data[beam_energy])
            tmp = k.flatten()
            tmp[np.where(tmp < fluence_cutoff)] = 0.0
            v_mtx[i * z_map_n + j, :] = tmp
    print()
    print(v_mtx.__repr__())

    for itr, beam in enumerate(pysapi_plan.Beams):
        if itr == 0:
            # first beam
            full_DijT = _make_sh2o_Dij_beam(
                pts_3d_ct.shape[:3], idxs_oi, pts_3d_ct, pts_3d_shell_ct,
                beam, field_size_mm, field_buffer_mm, beamlet_size_x_mm, beamlet_size_z_mm,
            ).dot(v_mtx.T).transpose()
        else:
            full_DijT = vstack((full_DijT, _make_sh2o_Dij_beam(
                pts_3d_ct.shape[:3], idxs_oi, pts_3d_ct, pts_3d_shell_ct,
                beam, field_size_mm, field_buffer_mm, beamlet_size_x_mm, beamlet_size_z_mm,
            ).dot(v_mtx.T).transpose()))

    full_DijT = full_DijT.tocsr()

    if return_scatter_matrix:
        return full_DijT, v_mtx
    else:
        return full_DijT


def make_sh2o_dose(study, ct_group, body_shell_path, dose_mask_path, trial_name='', fluence_obj=None,
                   mode='original', dose_group=None):
    # TODO: make this function work.

    # some per-plan settings/constants
    # ct_group = 'ct_lowres'
    # body_shell_path = 'structures/body/shell' #'/structures_lowres/block/mask'
    # dose_mask_path = 'structures_lowres/body/mask' #'/structures_lowres/block/mask'

    SAD_mm = 1000.0
    # if fluence_obj is None:
    #     f = make_fluence_maps(study, resolution=160,
    #                           minLeafPxWidth=2)  # creates .25 cm or 50 cm square pixels(for field_size = 40)
    #     #  todo: make_fluence_maps should place all needed data in rt5 study!!
    # else:
    #     f = fluence_obj

    if mode == 'original':

        # field_size_mm = 400.
        field_buffer_mm = 0.0  # (from above)

        field_size_mm = f.fieldSize * 10.

        x_px_size = f.minLeafWidth / float(f.minLeafWidth_in_px)  # usually something like .5 cm / 2.0
        y_px_size = f.fieldSize / f.resolution  # usually something like  40 cm / 160
        print("beamlet sizes (x y): ", x_px_size, y_px_size, (x_px_size - y_px_size))
        assert x_px_size == y_px_size, "non-uniform beamlet sizes not currently supported"
        # np.testing.assert_approx_equal(x_px_size,y_px_size, significant=10)

        # assure that the following dataset has been constructed by make_low_res

        ######## if you are getting errors check here #################
        # study.create_dataset('ct_lowres/voxel_coords',study['ct/voxel_coords'][::2,::2,:])
        # print("*!*!*!TODO: create 'ct_lowres/voxel_coords' as part of make_lowres tool!!!!" DONE!)

        beamlet_size_x_mm = x_px_size * 10.  # cm -> mm
        beamlet_size_z_mm = beamlet_size_x_mm

    elif mode == 'replan':  # fluence resolution is read in by what has been saved during 'make_sh2o_DijT_replan(...)'
        beamlet_size_xy_mm = study[
            '{}/beams/{}/beamlet_size_xz_mm'.format(dose_group, 1)]  # assume all same beamlet sizes

        beamlet_size_x_mm = beamlet_size_xy_mm[0]  # this is minimum leaf resolution, set to 1.0 mm
        beamlet_size_z_mm = beamlet_size_xy_mm[1]  # truebeam HD is 5.0mm and 10.0mm clinac is 10.0mm
        field_buffer_mm = study['{}/beams/{}/field_buffer_mm'.format(dose_group, 1)]  # or 2 cm

        field_size_mm = study['{}/beams/{}/field_size_mm'.format(dose_group, 1)]
        print("field size (mm): ", field_size_mm)
        print("assigned leaf width or beamlet size X *anisotropic* (mm): ", beamlet_size_x_mm)
        print("assigned leaf width or beamlet size Z *anisotropic* (mm): ", beamlet_size_z_mm)

        # pre-sanity check
        assert field_size_mm % beamlet_size_x_mm == 0, "field_size must be integer multiple of beamlet_size"
        assert field_buffer_mm % beamlet_size_x_mm == 0, "field_buffer must be integer multiple of beamlet_size"

        assert field_size_mm % beamlet_size_z_mm == 0, "field_size must be integer multiple of beamlet_size"
        assert field_buffer_mm % beamlet_size_z_mm == 0, "field_buffer must be integer multiple of beamlet_size"
    else:
        raise Exception('bad "mode" parameter')

    # used for scatter kernel to define pixel indexes in x and y(z)
    x_map_n, z_map_n = _calc_num_px_for_field(field_size_mm, field_buffer_mm, beamlet_size_x_mm, beamlet_size_z_mm)
    # x_ax = np.array(range(x_map_n))
    x_ax = (np.array(range(x_map_n)) - (x_map_n - 1.) / 2.) * beamlet_size_x_mm
    # y_ax = np.array(range(z_map_n))
    y_ax = (np.array(range(z_map_n)) - (z_map_n - 1.) / 2.) * beamlet_size_z_mm
    x_m, y_m = np.meshgrid(x_ax, y_ax)

    pts_3d_ct = study['{}/voxel_coords'.format(ct_group)]
    idxs_oi = np.where(study[dose_mask_path] > 0)

    # this should happen at full resulution if possible
    pts_3d_shell_ct = study['ct/voxel_coords'.format(ct_group)][np.where(study[body_shell_path])]

    for beam in f.mlcData:
        print("processing beam: ", beam.Number)

        csr = _make_sh2o_Dij_beam(
            study, idxs_oi, pts_3d_ct, pts_3d_shell_ct,
            beam, SAD_mm, field_size_mm, field_buffer_mm, beamlet_size_x_mm, beamlet_size_z_mm,
            # dose_group=dose_group, save_meta=True
        )

        print("COLLIMATOR ANGLE CHECK!!! ", beam.CollimatorAng)

        print("using beam energy: '{:.0f}X'".format(beam.BeamEnergy))
        # note transpose in sizes...
        ## DUE TO WIERDNESS OF CONVOLUTION FUNCTION WE NEED TO OFFSET THE KERNEL BY HALF A BIXEL:
        ## TESTING TRANSPOSE
        scat_kern = _scatter_kernel(y_m - beamlet_size_z_mm / 2., x_m - beamlet_size_x_mm / 2., kernel_data[
            "{:.0f}X".format(beam.BeamEnergy)])  # subtracting one due to nature of conv and kernel

        # convolve scatter kernel
        if mode == 'original':
            f_map_c = convolve(rotate(beam.map, -beam.CollimatorAng, reshape=False), scat_kern,
                               mode='constant')  # this ordering will give result the size that the dose matrix is shaped for
        elif mode == 'replan':
            # note no rotation
            f_map_c = convolve(study['{}/beams/{}/map'.format(dose_group, beam.Number)], scat_kern,
                               mode='constant')  # this ordering will give result the size that the dose matrix is shaped for
        else:
            raise Exception('bad "mode" parameter')

        # create dose for the beam
        spmv_dose = np.zeros_like(study['{}/hu'.format(ct_group)])

        print("dose shape {}".format(spmv_dose.shape))
        print("plan fluence shape {}, ({})".format(beam.map.shape, beam.map.flatten().shape))
        print("fluence shape {}, ({})".format(f_map_c.shape, f_map_c.flatten().shape))
        print("matrix shape {}".format(csr.shape))
        spmv_dose[idxs_oi] = csr.dot(f_map_c.flatten())

        # TODO: getting negative values?
        neg_dose_idx = np.where(spmv_dose < 0.)
        print("any negative values? : {}".format(neg_dose_idx))  # due to polynomials in PDD
        spmv_dose[neg_dose_idx] = 0.
        study.create_dataset('dose_sh2o{}/beam/{}/average'.format(trial_name, beam.Number), spmv_dose)
        study.save()
        del csr

    # now sum the dose
    # tot_dose = np.zeros_like(study['{}/density'.format(ct_group)])
    tot_dose = np.zeros_like(study['{}/hu'.format(ct_group)])
    for beam in f.mlcData:
        tot_dose += study['dose_sh2o{}/beam/{}/average'.format(trial_name, beam.Number)]

    study.create_dataset('dose_sh2o{}/gy'.format(trial_name), tot_dose)
    study.save()
