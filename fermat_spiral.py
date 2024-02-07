# Generates x,y points in a Fermat spiral
# Bryan Miller
# theta = 137.508*np.pi/180., golden angle
# b = number of spirals
# a = scale factor, default gives positions in degrees

import numpy as np


# Calculate points in a Fermat spiral
def fermat(n_point, a=0.03, b=1.0, theta=2.399963):
    # local variable with the correct type
    l_npt = np.int16(n_point)
    l_a = np.float32(a)
    l_b = np.float32(b)
    l_theta = np.float32(theta)

    x = np.zeros(n_point)
    y = np.zeros(n_point)

    for ii in range(l_npt):
        l_ii = np.float32(ii)
        x[ii] = l_a*np.sqrt(l_ii)*np.cos(l_b*l_ii*l_theta)
        y[ii] = l_a*np.sqrt(l_ii)*np.sin(l_b*l_ii*l_theta)

    return x, y


# Determine scale factor needed to produce a given offset in n_point points
def fermat_scale(n_point, offset, b=1.0, theta=2.399963):
    # local variable with the correct type
    l_npt = np.float32(n_point)
    l_offset = np.float32(offset)
    l_b = np.float32(b)
    l_theta = np.float32(theta)

    a = l_offset / (np.sqrt(l_npt*(np.cos(l_b*l_npt*l_theta)**2 + np.sin(l_b*l_npt*l_theta)**2)))

    return a
