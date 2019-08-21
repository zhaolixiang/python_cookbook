import re
text='Mark is a handsome guy and mark is only 18 years old.'
result1=re.findall('mark',text,flags=re.IGNORECASE)
result2=re.sub('mark','python',text,flags=re.IGNORECASE)

print(result1)
print(result2)