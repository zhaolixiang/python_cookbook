s='{name} has {n} messages.'

class Info:
    def __init__(self,name,n):
        self.name=name
        self.n=n

a=Info('Mark',10)
print(s.format_map(vars(a)))
print(vars(a))