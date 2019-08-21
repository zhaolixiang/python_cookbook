s='{name} has {n} messages.'
name='mark'
n=10

print(s.format_map(vars()))
print(vars())