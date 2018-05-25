from __future__ import print_function
import numpy as np

# Python version of the IDL script
# Bryan Miller

def randomp(pow,n,range_x=[5.,100.]):
# NAME:
#       RANDOMP
# PURPOSE:
#       Generates an array of random numbers distributed as a power law.
# CALLING SEQUENCE:
#       RANDOMP(Pow, N, [ RANGE_X = [low,high]])'
# INPUTS:
#       Pow:  Exponent of power law.
#               The pdf of X is f_X(x) = A*x^pow, low <= x <= high
#               ASTRONOMERS PLEASE NOTE:  
#               pow is little gamma  = big gamma - 1 for stellar IMFs.
#       N:    Number of elements in generated vector.
#
# OPTIONAL INPUT KEYWORD PARAMETER:
#       RANGE_X:  2-element vector [low,high] specifying the range of 
#               output X values# the default is [5, 100].
#
# OUTPUTS:
#       X:    Vector of random numbers, distributed as a power law between
#               specified range
# PROCEDURE:  
#       "Transformation Method" for random variables is described in Bevington 
#       & Robinson, "Data Reduction & Error Analysis for Physical Sciences", 2nd
#       Edition (McGraw-Hill, 1992). p. 83.
#       Output of RANDOMU function is transformed to power-law
#       random variable.
#
# EXAMPLE:
#       Create a stellar initial mass function (IMF) with 10000 stars
#       ranging from 0.5 to 100 solar masses and a Salpeter slope.  Enter:
#
#       MASS = RANDOMP(-2.35,10000,RANGE_X=[0.5,100])
#
# NOTES:
#       Versions 5.1.1 and V5.2 of IDL have a bug in RANDOMU such that the SEED
#       value is initialized to the same value at the start of each session,
#       rather than being initialized by the system clock.    RANDOMP will be
#       affected in a similar manner.
# MODIFICATION HISTORY:
#       Written by R. S. Hill, Hughes STX, July 13, 1995
#       July 14, 1995   SEED keyword added at Landsman's suggestion.
#                    Documentation converted to standard format.  RSH
#       Converted to IDL V5.0   W. Landsman   September 1997
#       Converted to python     B. Miller     October 2014
#-

    if len(range_x) != 2:
        print ('Error - RANGE_X keyword must be a 2 element vector')
        return
        
    pow1 = pow + 1.0
    
    lo = range_x[0]
    hi = range_x[1]
    if lo > hi:
        temp=lo
        lo=hi
        hi=tmp

    r = np.random.random( n )
    if pow != -1.0:
        norm = 1.0/(hi**pow1 - lo**pow1)
        expo = np.log10(r/norm + lo**pow1)/pow1
        x = 10.0**expo
    else:
        norm = 1.0/(np.log(hi) - np.log(lo))
        x = np.exp(r/norm + np.log(lo))

    return x

