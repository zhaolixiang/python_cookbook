from collections import deque

q=deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
q.appendleft(5)
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)