
from flist.time.time import ftime

# https://miguendes.me/how-to-use-datetimetimedelta-in-python-with-examples

delta_s = ["2y, 5mo, 3d ago", "1w, 2d ago", "1d, 18h ago"]

for delta in delta_s:
    ts = ftime(delta)
    print(ts, '-', delta)
