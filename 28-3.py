import unicodedata
str='\ufb01'

print(str)
print(len(str))
print('*'*10)

t_nfd=unicodedata.normalize('NFD',str)
t_nfkd=unicodedata.normalize('NFKD',str)
t_nfc=unicodedata.normalize('NFC',str)
t_nfkc=unicodedata.normalize('NFKC',str)

print(t_nfd)
print(len(t_nfd))
print('*'*10)

print(t_nfkd)
print(len(t_nfkd))
print('*'*10)

print(t_nfc)
print(len(t_nfc))
print('*'*10)

print(t_nfkc)
print(len(t_nfkc))