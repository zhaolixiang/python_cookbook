from fractions import Fraction

a=Fraction(5,4)
b=Fraction(7,16)
print(a)
print(b)
print(a+b)
print(a*b)

c=a*b
print(c.numerator)
print(c.denominator)

print(float(c))

print(c.limit_denominator(8))

x=3.75
print(x.as_integer_ratio())
print(*x.as_integer_ratio())
y=Fraction(*x.as_integer_ratio())
print(y)