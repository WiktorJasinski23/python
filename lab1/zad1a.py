#!/usr/bin/env python3.7

# import math
# import math
from math import sqrt
# from cmath import sqrt as csqrt

print('Podaj wspolczynniki')
print('a=', end='')
a = float(input())
print('b=', end='')
b = float(input())
print('c=', end='')
c = float(input())

delta = b*b - 4*a*c
epsilon = pow(10, -10)
if delta > 0 + epsilon:
    x1 = (b - sqrt(delta))/(2*a)
    x2 = (b + sqrt(delta))/(2*a)
    print(x1, x2)
elif 0 + epsilon > delta > 0 - epsilon:
    x = b/(2*a)
    print(x)
else:
    print('delta mniejsza od 0')




