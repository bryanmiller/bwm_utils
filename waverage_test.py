#!/usr/bin/env python

# Bryan Miller
# 2014.06.25
# http://en.wikipedia.org/wiki/Standard_deviation

from __future__ import print_function
import math as m
import numpy as np
from waverage import waverage

mean = 1.0
sigma = 0.5
sig_sigma = 0.15
n = 5

d = np.random.normal(mean,sigma,n)
s = np.random.normal(sigma,sig_sigma,n)

# Unweighted
print( 'Unweighted mean')
ave = np.mean(d)
print( 'Average = ',ave)
# stdev data (population), unbiased
print( 'Stdev data = ',m.sqrt(np.sum((d - ave)**2)/(n-1)),np.std(d,ddof=1))
# stdev mean
print( 'Stdev mean = ',m.sqrt(np.sum((d - ave)**2)/n),np.std(d,ddof=0))

# Weighted
w = waverage(d,s)
print( 'Weighted mean')
print( w )


