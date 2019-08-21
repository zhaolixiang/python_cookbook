s = ' hello    world     \n'
print(s.strip())

s = ' hello    world     \n'
print(s.replace(' ',''))


import re
s = ' hello    world     \n'
print(re.sub('\s+',' ',s))
