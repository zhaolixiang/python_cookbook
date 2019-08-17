import re
line='abc def ; ghi, jkl,mno, pkr'
result=re.split(r'\s*(?:;|,|\s)\s*',line)

print(result)