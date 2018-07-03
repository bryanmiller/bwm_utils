#!/usr/bin/env python

from __future__ import print_function
import numpy as np
from scipy import spatial

def find_nearest(a, a0):
    # https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    "Element in nd array `a` closest to the scalar value `a0`"
    idx = np.abs(a - a0).argmin()
    # idx = np.sum(np.square(np.abs(a-a0)),1).argmin()
    return a[idx], idx

def find_nearest_vector(a, pt):
  # idx = np.array([np.linalg.norm(x+y) for (x,y) in a-pt]).argmin()
  dist, idx = spatial.KDTree(a).query(pt)
  return a[idx], idx


if __name__=='__main__':

    x = np.random.uniform(size=10)
    print(x)

    near, inear = find_nearest(x,0.5)
    print(near,x[inear])

    near, inear = find_nearest(-x,-0.5)
    print(near)

    A = np.random.uniform(size=(10,2))
    print(A)

    near, inear = find_nearest_vector(A,[0.5,0.5])
    print(near,inear)