import unicodedata
str1='\u00f1'
str2='n\u0303'

t1=unicodedata.normalize('NFC',str1)
t2=unicodedata.normalize('NFC',str2)

print(t1)
print(t2)

print(t1==t2)

print(len(t1))
print(len(t2))

print('*'*10)

t3=unicodedata.normalize('NFD',str1)
t4=unicodedata.normalize('NFD',str2)
print(t3)
print(t4)

print(t3==t4)

print(len(t3))
print(len(t4))