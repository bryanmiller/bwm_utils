#!/usr/bin/env python

# Bryan Miller
# 2014.06.25
# http://en.wikipedia.org/wiki/Standard_deviation

from __future__ import print_function
import math as m
import numpy as np
from waverage import waverage
from sigma_clipping import avsigclip

mean = 1.0
sigma = 0.5
sig_sigma = 0.15
n = 1

d = np.random.normal(mean, sigma, n)
s = np.random.normal(sigma, sig_sigma, n)

# Unweighted
print( 'Unweighted mean with numpy')
ave = np.mean(d)
print( 'Average = ',ave)
# stdev data (population), unbiased
if n > 1:
    print( 'Stdev data = ',m.sqrt(np.sum((d - ave)**2)/(n-1)),np.std(d,ddof=1))
# stdev mean
print( 'Stdev mean = ',m.sqrt(np.sum((d - ave)**2)/n),np.std(d,ddof=0))

# Weighted
w = waverage(d,s)
print('Weighted mean')
print(w)
print('')

# With sigma clipping
print( 'Weighted mean with sigma clipping')
w_sigclip = avsigclip(d, s, n_sig=2, verbose=False)
print(w_sigclip)
print('')

# Sigma clipping example
x = np.array([8., 9., 10., 11., 9., 8., 12., 14., 20., 35., -15.])
x_err = np.ones(len(x))
avg, std_mean, std_pop = avsigclip(x, x_err, n_sig=2, verbose=True)
print(avg, std_mean, std_pop)
# w_sigclip = avsigclip(x, x_err, n_sig=2, i_err=1)
# print(w_sigclip)




