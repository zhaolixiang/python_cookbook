import sys

class safesub(dict):
    def __missing__(self, key):
        return '{'+key+'}'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name='mark'
n=10
print(sub('Hello {name}'))
print(sub('You have {n} messages'))
print(sub('You favorite color is {color}'))
