import unicodedata
import sys

digimap={c:ord('0')+unicodedata.digit(chr(c))
         for c in range(sys.maxunicode)
         if unicodedata.category(chr(c))=='Nd'}

print(len(digimap))

x='\u0661\u0662\u0663'
print(x.translate(digimap))