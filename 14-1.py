from operator import itemgetter
from itertools import groupby

rows=[
    {'name':'mark','age':18,'uid':'110'},
    {'name':'miaomiao','age':28,'uid':'160'},
    {'name':'miaomiao2','age':28,'uid':'150'},
    {'name':'xiaohei','age':38,'uid':'130'},
]

#首先根据age排序
rows.sort(key=itemgetter('age'))

for age,items in groupby(rows,key=itemgetter('age')):
    print(age)
    for i in items:
        print(i)