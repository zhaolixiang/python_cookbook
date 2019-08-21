import re
text1='11/27/2018'
text2='Nov 27, 2018'
datepat=re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('符合模型：数字/数字/数字')
else:
    print('不符合模型：数字/数字/数字')

if datepat.match(text2):
    print('符合模型：数字/数字/数字')
else:
    print('不符合模型：数字/数字/数字')