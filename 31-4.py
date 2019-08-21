import unicodedata

a='pytĥon is awesome\n'
b=unicodedata.normalize('NFD',a)
print(b.encode('ascii','ignore').decode('ascii'))