#!/usr/bin/env python3.7

from sys import argv
# from sys import exit
from math import sqrt

# print(type(argv))
# print(type(argv[0]))
# print(dir(argv))

if len(argv) == 4:
    a = float(argv[1])
    b = float(argv[2])
    c = float(argv[3])
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
else:
    print('nie spoko')
    exit()
