from datetime import datetime, timedelta, date, tzinfo
import pytz

dt = datetime(2018, 3, 27, 23, 8,tzinfo=pytz.utc)
print dt
dt_plus_one_day = dt + timedelta(days=1)
print dt_plus_one_day
d = date(2005, 7, 14)
print dt.strftime("%d/%m/%y %H:%M")
print datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print datetime.now()
print datetime.utcnow()