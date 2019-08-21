import unicodedata
import sys
cmb_chars=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

s='pytĥon\fis\tawesome\r\n'
remap={
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):None,
}
a=s.translate(remap)
b=unicodedata.normalize('NFD',a)
print(b)

print(b.translate(cmb_chars))