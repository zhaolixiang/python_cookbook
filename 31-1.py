s='pytĥon\fis\tawesome\r\n'
print(s)

remap={
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):None,
}
a=s.translate(remap)

print(a)