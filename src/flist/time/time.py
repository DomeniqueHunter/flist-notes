
import re
import datetime
from dateutil.relativedelta import relativedelta

# https://miguendes.me/how-to-use-datetimetimedelta-in-python-with-examples

delta_s = "2y, 5mo, 3d ago"
 
def _parse_time(time_str):
    regex = re.compile(r'((?P<years>\d+?)y[ ,]*)?((?P<months>\d+?)mo[ ,]*)?((?P<weeks>\d+?)w[ ,]*)?((?P<days>\d+?)d[ ,]*)?((?P<hours>\d+?)h[ ,]*)?((?P<minutes>\d+?)m[ ,]*)?((?P<seconds>\d+?)s[ ,]*)? ago')
    parts = regex.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    detailed = False
    for name, param in parts.items():
        if param:
            time_params[name] = int(param)
        if (name == 'hours' or name == 'minutes' or name == 'seconds') and parts[name] != None:
            detailed = True
            
    return relativedelta(**time_params), detailed


def ftime(timestamp:str) -> str:
    now = datetime.datetime.now()
    # print(timestamp)
    delta, detailed = _parse_time(timestamp)
    ts = now - delta
    if detailed:
        return str(ts.strftime('%Y-%m-%d %H:%M:%S'))
        
    return str(ts.strftime('%Y-%m-%d'))