from collections import Counter
words1=[
'a','b','c','d','e','f',
'a','b','c','d','e','f',
'a','b','c',
'a','b',
'a'
]

words2=[
'a','b','c','d','e','f',
'a','b','c',
'a','b',
'a'
]
one=Counter(words1)
two=Counter(words2)
print(one)
print(two)

three=one+two
print(three)

four=one-two
print(four)