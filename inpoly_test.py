#!/usr/bin/env python

# test inpoly function
# Bryan Miller

import inpoly as ip
import numpy as np
import matplotlib.pyplot as plt

# initial variables for FOV calc, in arcsec
xend=384.6557
yend=326.1332
xstart=67.4656
ystart=8.9421
#xcorner1=13.813
#xcorner2=13.813
xcorner1=27.0
xcorner2=27.0
#ycorner1=13.813
#ycorner2=13.813
ycorner1=27.0
ycorner2=27.0
ydelta=1.1632
xdim=452.0486
ydim=335.0016

# calculate vertices
xv=np.linspace(1,9,num=9)
yv=np.linspace(1,9,num=9)

# Vertices (GMOS FOV)
# A
xv[0]=xstart
yv[0]=yend-ycorner2
# B
xv[1]=xstart+xcorner2
yv[1]=yend
# C
xv[2]=xend-xcorner1
yv[2]=yend
# D
xv[3]=xend
yv[3]=yend-ycorner2
# E
xv[7]=xstart
yv[7]=ystart+ycorner1
# F
xv[6]=xstart+xcorner2
yv[6]=ystart
# G
xv[5]=xend-xcorner1
yv[5]=ystart
# H
xv[4]=xend
yv[4]=ystart+ycorner1
# For plotting the closed polygon
xv[8]=xv[0]
yv[8]=yv[0]

# test points
binning=2
pixscale=0.0728
scale=binning*pixscale

x = np.array([xstart, 610.629*scale, 638.10*scale, (xend+xstart)/2., 2563.79*scale, 2453.90*scale, 2481.37*scale,xstart-5.])
y = np.array([ystart, 65.25*scale, 106.46*scale, (yend+ystart)/2., 2166.89*scale, 2208.1*scale, 2249.31*scale,(yend+ystart)/2.])
# result should be:
# False
# False
# True
# True
# False
# True
# False
# False

# The number of vertices is one less than the number of sides to plot
nv = len(xv)-1
#print yv
#print yv[:nv]

# xin = []
# yin = []
# xout = []
# yout = []
# for i in range(x.size):
#     inp = ip.inpoly(xv[:nv],yv[:nv],x[i],y[i])
#     if inp:
#         xin.append(x[i])
#         yin.append(y[i])
#     else:
#         xout.append(x[i])
#         yout.append(y[i])
#     print inp
#
inp = ip.inpoly(xv[:nv],yv[:nv],x,y)
iin = np.where(inp)
iio = np.where([not ii for ii in inp])

# Plot
plt.plot(xv, yv)
# plt.plot(xout,yout,color='black',linestyle='none',marker='o',label='Out')
# plt.plot(xin,yin,color='red',linestyle='none',marker='o',label='In')
plt.plot(x[iio],y[iio],color='black',linestyle='none',marker='o',label='Out')
plt.plot(x[iin],y[iin],color='red',linestyle='none',marker='o',label='In')
legend = plt.legend(loc="lower right",numpoints=1,borderpad=0.25,labelspacing=0.25)
plt.xlabel(r'X')
plt.ylabel(r'Y')
plt.show()

