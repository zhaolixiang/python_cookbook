import unicodedata
str='啦啦啦\ufb01我是测试\u00f1呱呱呱n\u0303'

t1=unicodedata.normalize('NFD',str)
print(str)
print(t1)

#使用combining()函数判断指定内容是否为一个组合型字符。
result=''.join(x for x in t1 if not unicodedata.combining(x))
print(result)