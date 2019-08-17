import re
line='abc def ; ghi, jkl,mno, pkr'
#分隔符：分号，都逗号，空格符，前后可以跟着任意数量的额外空格
result=re.split(r'\s*[;,\s]\s*',line)
print(result)




import re
line='abc def ; ghi, jkl,mno, pkr'
result=re.split(r'\s*(;|,|\s)\s*',line)
print(result)