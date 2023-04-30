
import re
import datetime
from dateutil.relativedelta import relativedelta

# https://miguendes.me/how-to-use-datetimetimedelta-in-python-with-examples

delta_s = "2y, 5mo, 3d ago"
 
def _parse_time(time_str):
    regex = re.compile(r'((?P<years>\d+?)y[ ,]*)?((?P<months>\d+?)mo[ ,]*)?((?P<weeks>\d+?)w[ ,]*)?((?P<days>\d+?)d[ ,]*)?((?P<hours>\d+?)hr[ ,]*)?((?P<minutes>\d+?)m[ ,]*)?((?P<seconds>\d+?)s[ ,]*)? ago')
    parts = regex.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for name, param in parts.items():
        if param:
            time_params[name] = int(param)
    return relativedelta(**time_params)


def ftime(timestamp:str) -> str:
    now = datetime.datetime.now()
    ts = now - _parse_time(timestamp)
    return str(ts.strftime('%Y-%m-%d'))