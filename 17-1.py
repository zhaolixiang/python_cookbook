from collections import namedtuple
Subscriber=namedtuple('Subsciber',['addr','joined'])
sub=Subscriber("1782980833@qq.com","2018-10-23")

print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr,joined=sub
print(addr)
print(joined)

#下面错误，因为namedtuple是不可变的
#sub.joined="2019"