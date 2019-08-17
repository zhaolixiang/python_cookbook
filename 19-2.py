from collections import ChainMap
a={'x':1,'z':3}
b={'y':2,'z':4}

#为了防止b被直接修改，先cope一份b
c=dict(b)
print(id(c))
print(id(b))

c.update(a)

print(c['x'])
print(c['y'])
print(c['z'])