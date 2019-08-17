a={
    'x':1,
    'y':2,
    'z':3
}
b={
    'w':10,
    'x':11,
    'y':2
}

#找出 在两个字典中读存在的键
print(a.keys() & b.keys())

#找出 存在a却不存在b的键
print(a.keys() -b.keys())

#找出两个字典中，键和值都同时相等的数据
print(a.items() & b.items())