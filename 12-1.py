from operator import itemgetter
rows=[
{'name':'mark','age':18,'uid':'110'},
{'name':'miaomiao','age':28,'uid':'150'},
{'name':'miaomiao','age':8,'uid':'150'},
{'name':'xiaohei','age':38,'uid':'130'},
]

rows_by_name=sorted(rows,key=itemgetter('name'))
rows_by_uid=sorted(rows,key=itemgetter('uid'))
print(rows_by_name)
print(rows_by_uid)


#itemgetter还支持多个键
rows_by_name_age=sorted(rows,key=itemgetter('name','age'))
print(rows_by_name_age)

#itemgetter同样适用min、max
print(min(rows,key=itemgetter('uid')))
print(max(rows,key=itemgetter('age')))
