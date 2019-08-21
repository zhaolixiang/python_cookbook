import re
num=re.compile('\d+')

str1='123'
str2='\u0661\u0662\u0663'

print(num.match(str1))
print(num.match(str2))