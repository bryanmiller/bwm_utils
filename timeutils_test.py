#!/usr/bin/env python

# Tests for timeutils
# Bryan Miller

from __future__ import print_function
import timeutils as tu

print( tu.dec2sex(-5.055))
print( tu.dec2sex(5.055))

print( tu.dec2sex(-65.0505))
print( tu.dec2sex(65.0505))

print( tu.dec2sex(-165.5505))
print( tu.dec2sex(165.5505))

print( tu.dec2sex(-165.5505,tohour=True))
print( tu.dec2sex(165.5505,tohour=True))

# Generates an error, value out of range
try:
    print( tu.dec2sex(-165.5505,hour=True))
except:
    pass

# Generates an error, value out of range
try:
    print( tu.dec2sex(165.5505,hour=True))
except:
    pass

print( tu.dec2sex(-165.5505,p=0))
print( tu.dec2sex(165.5505,p=0))

print( tu.dec2sex(165.5505,p=2,sep=' '))

print( tu.sex2dec('00 24 05.67',sep=' '))
print( tu.sex2dec('00 24 05.67',todegree=True,sep=' '))
