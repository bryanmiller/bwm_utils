import numpy as np

### linefit
# From linefit.f from Stan Love
# Converted to python by Bryan Miller
# Fit a line to points with uncertainties in both axes

def linefit(x,sigx,y,sigy):
    m = 0.0
    b = 0.0
    csum = 0.0
    mold = -99999.
    sigsqb = 9999.0
    sigsqm = 9999.
    n = x.size
    while abs(m-mold) > 0.1*np.sqrt(sigsqm):
        mold = m
        sigsquen = sigy**2 + (mold*sigx)**2
        sumx = np.sum(x/sigsquen)
        sumy = np.sum(y/sigsquen)
        sumxx = np.sum((x**2)/sigsquen)
        sumxy = np.sum((x*y)/sigsquen)
        sums = np.sum(1.0/sigsquen)
        csum = np.sum((y-b-m*x)**2/sigsquen)
        det = sums*sumxx - sumx**2
        b = (sumxx*sumy - sumx*sumxy)/det
        m = (sums*sumxy - sumx*sumy)/det
        sigsqb = sumxx/det
        sigsqm = sums/det
    sigb = np.sqrt(sigsqb)
    sigm = np.sqrt(sigsqm)
    chi = csum/float(n-2)
    
    return m,sigm,b,sigb,chi


    
