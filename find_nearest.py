#!/usr/bin/env python

from __future__ import print_function
import numpy as np
from scipy import spatial
from bisect import bisect_left
import math

def find_nearest(array, value):
    # https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array/2566508
    nparray = np.asarray(array)
    idx = (np.abs(nparray - value)).argmin()
    return nparray[idx], idx

def find_nearest_sort(array,value):
    # https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array/2566508
    # faster for very large arrays
    nparray = np.sort(array)
    idx = np.searchsorted(nparray, value, side="left")
    if idx > 0 and (idx == len(nparray) or math.fabs(value - nparray[idx-1]) < math.fabs(value - nparray[idx])):
        return nparray[idx-1]
    else:
        return nparray[idx]

def find_nearest_vector(a, pt):
  # idx = np.array([np.linalg.norm(x+y) for (x,y) in a-pt]).argmin()
  dist, idx = spatial.KDTree(a).query(pt)
  return a[idx], idx

def find_closest(myList, myNumber):
    """
    Returns closest value to myNumber.
    If two numbers are equally close, return the smallest number.

    # adapted from
    # https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
    """

    sortList = sorted(myList)
    # print(sortList)

    pos = bisect_left(sortList, myNumber)
    if pos == 0:
        return sortList[0]
    if pos == len(sortList):
        return sortList[-1]
    before = sortList[pos - 1]
    after = sortList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before

if __name__=='__main__':

    x = np.random.uniform(size=10)
    print(x)

    near, inear = find_nearest(x,1.5)
    print(near,x[inear])

    near = find_nearest_sort(x,1.5)
    print(near)

    near = find_closest(x,1.5)
    print(near)

    near, inear = find_nearest(-x,-0.5)
    print(near, inear)

    A = np.random.uniform(size=(10,2))
    print(A)

    near, inear = find_nearest_vector(A,[0.5,0.5])
    print(near,inear)