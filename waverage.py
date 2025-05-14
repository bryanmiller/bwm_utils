import numpy as np


def waverage(x, errx):
    # Weighted average
    # Bryan Miller
    # 2014-06-10
    # References: http://en.wikipedia.org/wiki/Weighted_arithmetic_mean
    # http://stats.stackexchange.com/questions/47325/bias-correction-in-weighted-variance

    ax = np.array(x)
    asigx = np.array(errx)
    if 0.0 in asigx:
        raise Exception("Zero in error array.")

    w = 1./asigx**2
    xw = ax*w
    sumw = np.sum(w)
    sumwsq = np.sum((w**2))
    sumxw = np.sum(xw)
    
    # Weighted average
    mean = sumxw/sumw
    # Standard deviation of the mean (weighted)
    stdev_mean = 1./np.sqrt(sumw)
    # Unbiased estimator of the weighted population variance
    if len(ax) > 1:
        stdev_pop = np.sqrt(sumw*(np.sum(w*(x-mean)**2))/(sumw**2 - sumwsq))
    else:
        stdev_pop = np.nan
    # Variance in the weighted mean (account for error underestimate)
    # var_wmean = np.sqrt(stddev_mean*(np.sum(w*(x-mean)**2))/(len(ax) - 1.))

    return [mean, stdev_mean, stdev_pop]
    