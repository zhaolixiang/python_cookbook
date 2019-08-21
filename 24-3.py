import re
text='今天是：11/28/2018,昨天是11/27/2018'
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
new_text,n=datepat.subn(r'\3-\1-\2',text)
print(text)
print(new_text)
print(n)