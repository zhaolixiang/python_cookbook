prices={
'a':1.1,
'b':2.2,
'c':3.3,
'd':4.4,
'e':5.5
}
p1={key:value for key ,value in prices.items() if value>3}
print(p1)

names={'a','b'}
p2={key:value for key,value in prices.items() if key in names}
print(p2)

#结果为：{'c': 3.3, 'd': 4.4, 'e': 5.5}
p3=dict((key,value) for key,value in prices.items() if value>3)

#结果为：{'b': 2.2, 'a': 1.1}
p4={key:prices[key] for key in prices.keys() & names}