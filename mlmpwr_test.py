#!/usr/bin/env python

# Test for mlmpwr
# Bryan Miller

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from mlmpwr import mlmpwr
from randomp import randomp

# a = 4 # shape
# samples = 1000
# s = np.random.power(a, samples)
# # Display the histogram of the samples, along with the probability density function:
# count, bins, ignored = plt.hist(s, bins=30)
# x = np.linspace(0, 1, 100)
# y = a*x**(a-1.)
# normed_y = samples*np.diff(bins)[0]*y
# plt.plot(x, normed_y)
# plt.show()

a = -2.35
samples = 1000
s = randomp(a,samples,range_x=[0.5,100.])
count, bins, ignored = plt.hist(s, bins=30,log=True)
x = np.linspace(0.5, 100, 100)
y = x**(a)
normed_y = samples*np.diff(bins)[0]*y
plt.plot(x, normed_y,color='green')
plt.ylim(0,samples)

# MLM slope determination
res = mlmpwr(s)
print(res)

y2 = res[0]*x**(-res[1])
normed_y2 = samples*np.diff(bins)[0]*x**(-res[1])
plt.plot(x, y2,color='red')
plt.plot(x, normed_y2,color='blue')

plt.show()
