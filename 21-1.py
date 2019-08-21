filename='mark.txt'
url='http://www.baidu.com'

print(filename.endswith('.txt'))
print(url.startswith('https:'))


url='http://www.baidu.com'
print(url.startswith(('https:','http:')))



import re
url='http://www.baidu.com'
url2='utp://xxxxxx'
m=re.match('https:|http:|ftp',url)
m2=re.match('https:|http:|ftp',url2)
print(m)
print(m2)

