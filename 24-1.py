text='mark ，帅哥，18，183 帅，mark'
print(text.replace('18','19'))
print(text)


import re
text='今天是：11/28/2018'
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))
print(text)



import re
text='今天是：11/28/2018'
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2',text))
print(text)