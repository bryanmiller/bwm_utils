#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from fermat_spiral import fermat
from fermat_spiral import fermat_scale
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Number of points",type=int)
    parser.add_argument("-a", help="Scale factor", default=0.00045, type=float)
    parser.add_argument("-b", help="Number of spirals", default=1.0, type=float)
    parser.add_argument("-r", help="Random sigma", default=0.0, type=float)
    parser.add_argument("-d", help="Dmax", default=0.0, type=float)
    parser.add_argument("-p", help="2nd number of points", default=0, type=int)
    args = parser.parse_args()


    # Scaling of pattern
    #a = 7.0
    #a = 0.00045
    a = args.a
    # Number of spirals? b=1 gives the most uniform pattern
    #b = 1.0
    b = args.b
    # print(a,b)
    dmax = args.d
    nnew = args.p

    # Sigma (arcsec) for normal randomization
    r = args.r

    # golden angle
    theta=137.50776*np.pi/180.
    # print(theta)

    #np = 33
    n = args.n
    # print(n)
    x,y = fermat(n,a=a,b=b,theta=theta)
    # convert from degrees to arcsec
    x = 3600.*x
    y = 3600.*y

    r = np.random.normal(0.0, r, (n,2))

    for ii in range(n):
        x[ii] = x[ii] + r[ii,0]
        y[ii] = y[ii] + r[ii,1]
        offset = 0.0
        if ii > 0:
            offset = np.sqrt((x[ii] - x[ii - 1]) ** 2 + (y[ii] - y[ii - 1]) ** 2)
        dist = np.sqrt((x[ii])**2 + (y[ii])**2)  # distance from origin
        print('{:7.2f} {:7.2f} {:7.2f} {:7.2f}'.format(x[ii], y[ii], offset, dist))

    plt.plot(x,y,'bo')
    plt.show()

    # Test scale
    if dmax == 0:
        dmax = dist
    if nnew == 0:
        nnew = n
    dmax = dist # arcsec
    anew = fermat_scale(nnew,dmax/3600.,b=b,theta=theta)
    print('a({:3d}, {:7.2f}) = {:7.3f}'.format(nnew,dmax,anew))
    x,y = fermat(nnew,a=anew,b=b,theta=theta)
    # convert from degrees to arcsec
    x = 3600.*x
    y = 3600.*y
    for ii in range(nnew):
        x[ii] = x[ii] + r[ii,0]
        y[ii] = y[ii] + r[ii,1]
        offset = 0.0
        if ii > 0:
            offset = np.sqrt((x[ii] - x[ii - 1]) ** 2 + (y[ii] - y[ii - 1]) ** 2)
        dist = np.sqrt((x[ii])**2 + (y[ii])**2)  # distance from origin
        print('{:7.2f} {:7.2f} {:7.2f} {:7.2f}'.format(x[ii], y[ii], offset, dist))
