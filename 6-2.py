from collections import OrderedDict
import json

d=OrderedDict()
d['a']=1
d['b']=2
d['c']=3
d['d']=4

j=json.dumps(d)
print(j)