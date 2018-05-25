# Timezone classes
# Bryan Miller
# see http://docs.python.org/2/library/datetime.html
#
# Import dependencies
from datetime import timedelta, datetime, tzinfo

# UTC
class UTC(tzinfo):
    """UTC"""
    def utcoffset(self, dt):
        return timedelta(0)
    def dst(self, dt):
        # no DST
        return timedelta(0)
    def tzname(self,dt):
        return "UTC"
    
# Chilean time for 2013
class CLT(tzinfo):
    def utcoffset(self, dt):
        return  self.dst(dt) - timedelta(hours=4)
    def dst(self, dt):
        if dt.year == 2013:
            # DST starts September 8
            d = datetime(2013, 9, 8)
            self.dston = d
            # DST ends April 28
            d = datetime(2013, 4, 28)
            self.dstoff = d
            if (dt.replace(tzinfo=None) >= self.dston or
               dt.replace(tzinfo=None) < self.dstoff):
                return timedelta(hours=1)
            else:
                return timedelta(0)
        else:
            return timedelta(0)
    def tzname(self,dt):
            return "CLT"
