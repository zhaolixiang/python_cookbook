#将序列分解为单独的变量
m=(1,2)
x,y=m
print("x=",x)
print("y=",y)

print("*"*30)

data=["mark",18,"超级帅",(1992,5,4)]
name,age,feature,birthday=data
print("name=",name)
print("age=",age)
print("feature=",feature)
print("birthday=",birthday)
print("*"*30)


name,age,feature,(year,mon,day)=data
print("name=",name)
print("age=",age)
print("feature=",feature)
print("year=",year)
print("mon=",mon)
print("day=",day)