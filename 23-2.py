import re
text1='11/27/2018'
text2='Nov 27, 2018'
if re.match(r'\d+/\d+/\d+',text1):
    print('符合模型：数字/数字/数字')
else:
    print('不符合模型：数字/数字/数字')

if re.match(r'\d+/\d+/\d+',text2):
    print('符合模型：数字/数字/数字')
else:
    print('不符合模型：数字/数字/数字')
