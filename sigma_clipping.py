# Routines for cleaning averages, e.g. sigma clipping

from waverage import waverage
import numpy as np


def avsigclip(x, errx, n_sig=3., i_err=2, n_iter=4, verbose=False):
    """Average with sigma clipping
        n_sig: number of sigma to clip
        i_err: index to use for the sigma comparison, 1 for stdev_mean, 2 for stdev_pop
        n_iter: max number of iterations
    """
    l_x = np.array(x) if type(x) is not np.ndarray else x
    l_errx = np.array(errx) if type(errx) is not np.ndarray else errx

    avg = waverage(l_x, l_errx)
    avg_prev = avg[0] * 0.1
    if verbose:
        print(x)

    diff_limit = 0.01
    ii = 0
    while avg[0] - avg_prev > diff_limit * avg[0] and ii < n_iter:
        if verbose:
            print(avg[0], avg[i_err])
        avg_prev = avg[0]
        jj = np.where(np.abs(l_x - avg[0]) < n_sig * avg[i_err])[0]
        if verbose:
            print(jj)
            print(l_x[jj])
        if len(jj) > 2:
            avg = waverage(l_x[jj], l_errx[jj])
        ii += 1

    return avg




