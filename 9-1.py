def dedupe(items):
    seen=set()
    for item in items:
        print(item)
        if item not in seen:
            yield item
            seen.add(item)

a=[1,2,3,1,9,1,5,10]
print(list(dedupe(a)))
