#!/Users/bmiller/bin/python

# test different estimates of linear fits
# Bryan Miller

from __future__ import print_function
# import subprocess
import numpy as np
# import matplotlib.pyplot as plt
from linefit import linefit 

m = 2.0
sigm = 0.05
b = -3.5
sigb = 0.05
sigy = 0.2
sigx = 0.5

x = np.arange(-5,25,1)
y = m*x + b
n = x.size

#plt.plot(x,y)
#plt.show()

ntrial = 1000

ytrial = np.zeros([n,ntrial])
for i in range(0,n):
    ytrial[i,:] = np.random.normal(m,sigm,ntrial)*x[i] + np.random.normal(b,sigb,ntrial)

# loop over ntrials
mfit = np.zeros(ntrial)
merr = np.zeros(ntrial)
bfit = np.zeros(ntrial)
berr = np.zeros(ntrial)

mlf = np.zeros(ntrial)
mlfe = np.zeros(ntrial)
blf = np.zeros(ntrial)
blfe = np.zeros(ntrial)

#print( ytrial[:,0] )

for j in range(0,ntrial):
    ye = abs(np.random.normal(0.0,sigy,n))
    linfit, cov = np.polyfit(x,ytrial[:,j],1,w=1./ye,cov=True)
    mfit[j] = linfit[0]
    bfit[j] = linfit[1]
    merr[j] = np.sqrt(cov[0,0])
    berr[j] = np.sqrt(cov[1,1])
    
    # fit line with linef
    # Velocity dispersion from PM93
#     lffile = 'tmplinef.dat'
#     output_file = open(lffile,'w')
# 
#     values = []
#     for i in range(n):
#         output_file.write(str(x[i])+' 0.3 '+str(ytrial[i,j])+' '+str(0.3)+'\n')
#     output_file.close()
# 
#     process = subprocess.Popen(['linef',lffile],\
#                 stdout=subprocess.PIPE).communicate()[0]
#     process = process.rstrip("\n")
#     values = process.split()
#     mlf[j] = float(values[1])
#     mlfe[j] = float(values[2])
#     blf[j] = float(values[3])
#     blfe[j] = float(values[4])
    
    xe = np.ones(n)*0.0
    #ye = np.ones(n)*0.1
    res = linefit(x,xe,ytrial[:,j],ye)
    mlf[j] = res[0]
    mlfe[j] = res[1]
    blf[j] = res[2]
    blfe[j] = res[3]
    
print( 'polyfit' )
print( np.mean(mfit),np.std(mfit,ddof=1) )
print( np.mean(merr),np.std(merr,ddof=1) )
print( np.mean(bfit),np.std(bfit,ddof=1) )
print( np.mean(berr),np.std(berr,ddof=1) )
print( '' )
print( 'linefit' )
print( np.mean(mlf),np.std(mlf,ddof=1) )
print( np.mean(mlfe),np.mean(mlfe)*np.sqrt(4.*n),np.std(mlfe,ddof=1) )
print( np.mean(blf),np.std(blf,ddof=1) )
print( np.mean(mlfe),np.mean(blfe)*np.sqrt(2.*n),np.std(blfe,ddof=1) )
# included are empirical factors to make the linefit errors agree more with
# the polyfit and Monte-Carlo results when the errors are small
# The best procedure in general is to Monte-Carlo the errors.




