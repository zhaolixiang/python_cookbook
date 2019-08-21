s='{name} has {n} messages.'
name='mark'
class safesub(dict):
    def __missing__(self, key):
        return '{'+key+'}'
print(s.format_map(safesub(vars())))
