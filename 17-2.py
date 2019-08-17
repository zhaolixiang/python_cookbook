from collections import namedtuple
Subscriber=namedtuple('Subsciber',['addr','joined'])
sub=Subscriber("1782980833@qq.com","2018-10-23")

print(sub)

sub=sub._replace(joined="2018-10-24")
print(sub)