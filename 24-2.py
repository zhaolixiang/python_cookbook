import re
from calendar import month_abbr
text='今天是：11/28/2018'
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')

def change_date(m):
    mon_name=month_abbr[int(m.group(1))]
    return '{}  {}  {}'.format(m.group(3),mon_name,m.group(2))
print(datepat.sub(change_date,text))
print(text)