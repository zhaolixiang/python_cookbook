from collections import namedtuple
Subscriber=namedtuple('Subsciber',['addr','joined','age'])
sub=Subscriber("",None,0)

def dict_to_stock(s):
    return sub._replace(**s)

a={"addr":"111111@qq.com","joined":"1111-11-11","age":11}
a=dict_to_stock(a)
print(a)

b={"addr":"111111@qq.com","joined":"1111-11-11"}
b=dict_to_stock(b)
print(b)