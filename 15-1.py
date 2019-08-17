myList=[1,4,-5,10,-7,2,3,-1]
print([n for n in myList if n>0])
print([n for n in myList if n<0])


myList=[1,4,-5,10,-7,2,3,-1]
pos=(n for n in myList if n >0)
for x in pos:
    print(x)

values=['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False

ivals=list(filter(is_int,values))
print(ivals)



import math
myList=[1,4,-5,10,-7,2,3,-1]
print([math.sqrt(n) for n in myList if n>0])

myList=[1,4,-5,10,-7,2,3,-1]
print([n if n>0 else 0 for n in myList])
print([n if n<0 else 0 for n in myList])


from itertools import compress
address=[
'5412 N CLARK1',
'5148 N CLARK2',
'5800 E CLARK3',
'2122 N CLARK4',
'5645 M CLARK5',
'1060 W CLARK6',
]
counts=[0,3,10,4,1,7]
#构建一个列表，它相应的count值要大于5
more5=[n>5 for n in counts]
print(more5)

print(list(compress(address,more5)))