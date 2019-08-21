import re
text='今天是 11/27/2018，昨天是11/26/2018'
datepat=re.compile(r'\d+/\d+/\d+')
print(datepat.findall(text))