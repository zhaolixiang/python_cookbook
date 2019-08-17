import re
line='abc def ; ghi, jkl,mno, pkr'
result=re.split(r'\s*(;|,|\s)\s*',line)

values=result[::2]
delimiters=result[1::2]+['']

print(values)
print(delimiters)

last=''.join(v+d for v,d in zip(values,delimiters))
print(last)