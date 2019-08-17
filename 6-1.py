from collections import OrderedDict

d=OrderedDict()
d['a']=1
d['b']=2
d['c']=3
d['d']=4

#根据插入删除输出
for key in d:
    print(key,d[key])