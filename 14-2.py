from collections import defaultdict

rows=[
    {'name':'mark','age':18,'uid':'110'},
    {'name':'miaomiao','age':28,'uid':'160'},
    {'name':'miaomiao2','age':28,'uid':'150'},
    {'name':'xiaohei','age':38,'uid':'130'},
]

rows_by_age=defaultdict(list)
for row in rows:
    rows_by_age[row['age']].append(row)
for a in rows_by_age[28]:
    print(a)