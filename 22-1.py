from fnmatch import fnmatch,fnmatchcase
print(fnmatch('mark.txt','*.txt'))
print(fnmatch('mark.txt','?ark.txt'))
print(fnmatch('mark2018.txt','?ark201[0-9].txt'))

print(fnmatchcase('mark.txt','*.TXT'))



#假设有一组街道地址，就像这样：
address=[
    '111 A 上海 SH',
    '112 B 上海 SH',
    '113 C 上海 SH',
    '124 D 北京 BJ',
    '138 E 北京 BJ',
    '145 F 北京 BJ',
]

result=[addr for addr in address if fnmatchcase(addr,'1[1-3][1-5]*BJ')]
print(result)