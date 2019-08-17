def dedupe(items,key=None):
    seen=set()
    for item in items:
        value=item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)

a=[
    {'x':1,'y':2},
    {'x':1,'y':3},
    {'x':1,'y':4},
    {'x':1,'y':2},
    {'x':1,'y':3},
    {'x':1,'y':1},

]
print(list(dedupe(a,key=lambda d:(d['x'],d['y']))))

print(list(dedupe(a,key=lambda d:d['y'])))