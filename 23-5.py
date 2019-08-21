import re
#加入捕获组
datepat=re.compile(r'(\d+)+/(\d+)+/(\d+)')
m=datepat.match('11/27/2018')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month,day,year=m.groups()
print(month)
print(day)
print(year)

print('*'*20)

text='今天是 11/27/2018，昨天是11/26/2018'
for month,day,year in datepat.findall(text):
    print('{}-{}-{}'.format(year,month,day))

print('*'*20)

for m in datepat.finditer(text):
    print(m.groups())
