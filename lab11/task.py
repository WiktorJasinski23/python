from scipy import misc
from math import sin
from random import random

class PrimeNumbers:
    def __init__(self, mini, maxi):
        self.actualPrime = mini
        self.max = maxi

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.actualPrime += 1
            for x in range(2, self.actualPrime):
                if self.actualPrime % x == 0:
                    self.actualPrime += 1
                else:
                    break
            break

        if self.actualPrime > self.max:
            raise StopIteration
        return self.actualPrime


# primes = PrimeNumbers(2, 20)
# for i in primes:
#     print(i)
#
# for i in primes:
#     print(i)


class PrimeNumbers2:
    def __init__(self, mini, maxi):
        self.actualPrime = mini
        self.max = maxi

    def __iter__(self):
        return PrimeNumbers3(self.actualPrime, self.max)


class PrimeNumbers3:
    def __init__(self, mini, maxi):
        self.actualPrime = mini
        self.max = maxi

    def __next__(self):
        while True:
            self.actualPrime += 1
            for x in range(2, self.actualPrime):
                if self.actualPrime % x == 0:
                    self.actualPrime += 1
                else:
                    break
            break

        if self.actualPrime > self.max:
            raise StopIteration
        return self.actualPrime


# primes2 = PrimeNumbers2(2, 20)
# for i in primes2:
#     print(i)
#
# for i in primes2:
#     print(i)


class NewtonRaphson:
    def __init__(self, func, x, eps):
        self.function = func
        self.x = x
        self.eps = eps

    def __iter__(self):
        return self

    def __next__(self):
        self.x = self.x - (self.function(self.x)/misc.derivative(self.function, self.x))
        if abs(self.function(self.x)) < self.eps:
            raise StopIteration
        return self.x


def my_func(x):
    return sin(x)-(0.5*x)*(0.5*x)


# nr = NewtonRaphson(my_func, 1.5, 10**-5)
# for i in nr:
#     print(i)


class RandNumber:
    def __init__(self):
        self.x = 1
        self.m = (2**31)-1
        self.a = 7**5
        self.c = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x/self.m


rnd = RandNumber()
my_list = []
for i in range(10**5):
    my_list.append((next(rnd), next(rnd)))

percent = []
for i in range(1,11):
    pr = 0
    for x,y in my_list:
        if x <= 0.1*i and y <= 01.*i:
            pr += 1
    pr = pr / len(my_list)
    percent.append(pr)

for x in enumerate(percent):
    print(x)

my_list2 = []
for i in range(10**5):
    my_list2.append((random(), random()))

percent2 = []
for i in range(1,11):
    pr = 0
    for x,y in my_list2:
        if x <= 0.1*i and y <= 01.*i:
            pr += 1
    pr = pr / len(my_list2)
    percent2.append(pr)

for x in enumerate(percent2):
    print(x)
