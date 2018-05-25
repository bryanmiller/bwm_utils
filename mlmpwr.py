#!/usr/bin/env python

# Bryan Miller

import numpy as np

def alpha(a,b,c):

    anew=1.+1./(c + np.log(b)/(b**(a-1.)-1.))

    return anew

def mlmpwr(x):
    # Maximum-likelihood method to determine the power-law slope a for
    # a differential distribution f(x,a) = x**-a (Crawford etal. 1970)
    # Bryan Miller
    # 2014 Oct 21 - from mlmpwr.pro
    
    # Make sure that the input is a numpy array
    l_x = np.array(x)
    
    m = len(l_x)
    fm = float(m)

    x1 = np.min(l_x)
    x2 = np.max(l_x)
    b = x2/x1

    s = np.sum(np.log(l_x/x1))
    c = s/fm
    #print('b = ',b,', c = ,',c)

    # Initial value for the slope
    aold = 1. + 1./c
    #print(aold)
    a = alpha(aold,b,c)
    #print,a

    # Iterate to converge
    err = 0.0001
    k = 0
    while (np.abs(a-aold) > err) and (k < 999):
        k = k+1
        aold = a
        a = alpha(aold,b,c)
        # print,a

    am1 = a - 1.
    n0 = fm*(am1)/(1.-b**(1.-a))
    siga = am1/(np.sqrt(fm*(1.-(am1**2*np.log(b)**2)/b**am1)))
    
    # Unbiased estimate of the slope
    a = (fm - 1.)*a/fm

    return n0,a,siga
