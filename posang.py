# From https://code.google.com/p/agpy/source/browse/trunk/agpy/posang.py
# now at
# https://github.com/keflavich/agpy/tree/master/agpy
# Changes by Bryan Miller:
#   2014jul22 - default system=radec
#   2014jul22 - changed to ra2-ra1 so that sign matches posang.pro
#  RA1 = 66.15593384
#  DC1 = 33.95988843
#  RA2 = 66.15646079
#  DC2 = 33.96100069
#  print posang.posang(RA1,DC1,RA2,DC2)
#  21.4522920312

from astropy.coordinates import SkyCoord
from numpy import pi,arctan2,sin,cos,tan
# from astropy import units as u

def posang(l1,b1,l2,b2,system='radec',units='degrees',**kwargs):
    """
    Return the position angle between two points assuming a rectilinear
    coordinate system (I think; at the very least I am making no corrections
    for wcs).

    INPUT:
    longitude1, latitude1, longitude2, latitude2

    """

    if system.lower() == 'galactic':
        pos1 = SkyCoord(l1,b1,unit=('deg','deg'),frame='galactic')
        pos2 = SkyCoord(l2,b2,unit=('deg','deg'),frame='galactic')
    elif system.lower() in ('radec','fk5','icrs'):
        pos1 = SkyCoord(l1,b1,unit=('deg','deg'),frame='icrs')
        pos2 = SkyCoord(l2,b2,unit=('deg','deg'),frame='icrs')

    ra1,dec1 = pos1.icrs.ra.deg,pos1.icrs.dec.deg
    ra2,dec2 = pos2.icrs.ra.deg,pos2.icrs.dec.deg

    radiff = (ra2-ra1)/180.*pi

    angle = arctan2( sin(radiff) , cos(dec1*pi/180.)*tan(dec2*pi/180.) - sin(dec1*pi/180.)*cos(radiff) ) 

    if units == 'degrees':
        return angle/pi*180.
    elif units == 'radians':
        return angle
    else:
        raise ValueError("Invalid units: %s" % units)

if __name__ == "__main__":

    RA1 = 66.15593384
    DC1 = 33.95988843
    RA2 = 66.15646079
    DC2 = 33.96100069
    print (posang(RA1,DC1,RA2,DC2))
    assert posang(RA1,DC1,RA2,DC2), 21.4522920312

    print (posang(RA1,DC1,RA2,DC2,system='galactic'))

