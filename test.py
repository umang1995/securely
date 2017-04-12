import json
b = []

a = dict()
a['latitude'] = 1234
a['longitude'] = 4321

b.append(a)
c = dict()
c['latitude'] = 4567
c['longitude'] = 7654

b.append(c)
d = dict()
d['latitude'] = 9876
d['longitude'] = 6789

b.append(d)

js = json.dumps(b)
print js
sj = json.loads(js)

print sj

for ts in sj:
    latitude = ts.get('latitude',None)
    longitude = ts.get('longitude',None)
    print latitude,' ' ,longitude
