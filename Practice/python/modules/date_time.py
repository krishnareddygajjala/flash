
import datetime


ctime = datetime.datetime.now()
print ctime

nextweek = ctime+datetime.timedelta(days = 7)
nw = nextweek.strftime(r"%d/%b/%Y  %H:%M:%S")
#print nextweek
print nw
previousweek = ctime-datetime.timedelta(days = 7)
pw = previousweek.strftime(r"%d/%b/%Y  %H:%M:%S")
#print previousweek
print pw
print datetime.MAXYEAR
print datetime.MINYEAR
print datetime.tzinfo()
print datetime.date.today()
print datetime.time.tzinfo()