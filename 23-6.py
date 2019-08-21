import re
#加入捕获组
datepat=re.compile(r'(\d+)+/(\d+)+/(\d+)')
m=datepat.match('11/27/2018xxxx')
print(m)


import re
#加入捕获组
datepat=re.compile(r'(\d+)+/(\d+)+/(\d+)$')
m1=datepat.match('11/27/2018xxxx')
m2=datepat.match('11/27/2018')
print(m1)
print(m2)

