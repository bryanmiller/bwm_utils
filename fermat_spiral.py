# Generates x,y points in a Fermat spiral
# Bryan Miller
# theta = 137.508*np.pi/180., golden angle
# b = number of spirals
# a = scale factor, default gives positions in degrees

import numpy as np

# Calculate points in a Fermat spiral
def fermat(n_point,a=0.03,b=1.0,theta=2.399963):
    # local variable with the correct type
    l_npt = int(n_point)
    l_a = float(a)
    l_b = float(b)
    l_theta = float(theta)

    x = np.zeros(n_point)
    y = np.zeros(n_point)

    for ii in range(l_npt):
        l_ii = float(ii)
        x[ii] = l_a*np.sqrt(l_ii)*np.cos(l_b*l_ii*l_theta)
        y[ii] = l_a*np.sqrt(l_ii)*np.sin(l_b*l_ii*l_theta)

    return x,y

# Determine scale factor needed to produce a given offset in n_point points
def fermat_scale(n_point,offset,b=1.0,theta=2.399963):
    # local variable with the correct type
    l_npt = float(n_point)
    l_offset = float(offset)
    l_b = float(b)
    l_theta = float(theta)

    a = l_offset/(np.sqrt(l_npt*(np.cos(l_b*l_npt*l_theta)**2 + np.sin(l_b*l_npt*l_theta)**2)))

    return a
