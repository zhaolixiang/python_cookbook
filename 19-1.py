from collections import ChainMap
a={'x':1,'z':3}
b={'y':2,'z':4}

c=ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))

a['z']=5
print(c['z'])