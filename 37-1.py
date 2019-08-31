text = 'foo = 23 + 42 * 10'
import re

# tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
#          ('NUM', '42'), ('TIMES', '*'), ('NUM', 10')]
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
sm = scanner.match()
print(sm, sm.lastgroup, sm.group())

sm = scanner.match()
print(sm, sm.lastgroup, sm.group())

sm = scanner.match()
print(sm, sm.lastgroup, sm.group())

sm = scanner.match()
print(sm, sm.lastgroup, sm.group())

sm = scanner.match()
print(sm, sm.lastgroup, sm.group())
