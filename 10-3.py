s='HelloWorld'
a=slice(2,5)
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(str(i)+":"+s[i])
