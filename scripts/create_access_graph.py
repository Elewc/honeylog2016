import sys
from datetime import datetime as dt

f = open(sys.argv[1]).readlines()


time_dict = {}
for i in f:
    timestamp = i.split('\t')[0]
    tdatetime = dt.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    ymd = tdatetime.strftime('%m/%d/%Y')
    if not ymd in time_dict:
        time_dict[ymd] = 1
    time_dict[ymd] += 1

for x in sorted(time_dict.items(), key=lambda x: x[0]):
    print("%s,%d" % (x[0], x[1]))
