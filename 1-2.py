#将序列分解为单独的变量
mark="mark"
m,a,r,k=mark
print(m)
print(a)
print(r)
print(k)
print("*"*30)

#有时候我们想丢弃某个值，单由于变量数量必须和要分解的对象的可分解数量相同，此时我们可以使用_来表示要丢弃的值。

mark="mark"
m,a,r,_=mark
print(m)
print(a)
print(r)
#其实_还是一个变量，指示看起来舒服点
print(_)