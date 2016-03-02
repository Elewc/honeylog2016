import GeoIP
import sys

gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
f = open(sys.argv[1], 'r').readlines()
cc = {}
for i in f:
    code = gi.country_code_by_addr(i.strip())
    if not code in cc:
        cc[code] = 1
    cc[code] += 1

#print(cc)
#print(sorted(cc.items(), key=lambda x:x[1]))

for i in sorted(cc.items(), key=lambda x: x[1], reverse=True):
    print(i[0], i[1])
