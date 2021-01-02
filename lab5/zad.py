from sys import version
from random import uniform
from math import sqrt
from time import time_ns
from functools import reduce


################################# 1 ############################

powt=1000
N=10000


def forStatement(n):
    x = []
    sum = 0
    for i in range(n):
        sum += sum +i


def listComprehension(n):
    x = [i*i for i in range(n)]

def mapFunction(n):
    x = map(lambda x: x*x, range(n))

def generatorExpression(n):
    x = (i*i for i in range(n))

def tester(fun):
    t = time_ns()
    for i in range(powt):
        fun(N)
    return time_ns() - t

print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:

    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

# dodawanie
# forStatement         => 781946300
# listComprehension    => 341110500
# mapFunction          => 973100
# generatorExpression  => 996600

# do kw
# forStatement         => 1219706900
# listComprehension    => 775958300
# mapFunction          => 965000
# generatorExpression  => 997500



# ################################# 2 ############################
#
# def solve_integral(fun, x_1, x_2, n):
#     d = (x_2 - x_1)/n
#     k = []
#     for i in range(n):
#         if i == 0:
#             k.append(0)
#         else:
#             k.append(round(k[i-1] + d, 2))
#     p = map(lambda x: eval(fun), k)
#     sum = 0
#     for el in p:
#         sum += round(el*d,2)
#
#     print(sum)
#
#
# solve_integral('x+1', 0, 4, 100)
#
# ######################### 3 #############################
#
#
# lis = []
# for i in range(10000):
#     f = lambda x, y: sqrt(x * x + y * y)
#     lis.append(f(uniform(-1, 1), uniform(-1, 1)))
#
#
# fil = filter(lambda x: x <= 1, lis)
# sets = set(fil)
# stos = len(sets)/10000
# pi = stos * 4
# print(pi)
#
# ############################# 4 ########################
#
# A = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# B = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# print(set(map(lambda x: max(x), A)))
# print(set(map(lambda x: max(x), zip(*A))))
# print([[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))])
#
#
# #################### 5 ######################################
#
#
# def fun(list_x, list_y):
#     li = zip(list_x, list_y)
#     avg_x = reduce(lambda x, y: x+y, list_x)/len(list_x)
#     avg_y = reduce(lambda x, y: x + y, list_y) / len(list_y)
#     D = reduce(lambda x, y: x + y, map(lambda x: (x-avg_x)**2, list_x))
#     a = reduce(lambda x,y: x+y, map(lambda x, y: y*(x-avg_x), list_x, list_y))/D
#     b = avg_y - a*avg_x
#     delta_y = sqrt(reduce(lambda x, y: x +y, map(lambda x, y: y -(a*x) + b, list_x, list_y)) / len(list_x))
#     delta_a = delta_y / sqrt(D)
#     delta_b = delta_y*sqrt(1/len(list_y) + avg_x**2/D)
#
#     return a, delta_a, b, delta_b
#
# fun([1,3,4],[2,5,7])