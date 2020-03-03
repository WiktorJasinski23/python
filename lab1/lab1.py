#!/usr/bin/env python3.7

import copy

print("Hello world!")


c = 3.7
d = "string"
f = None
g = True
a, *b = 2, 3, 4, 5, 'a'

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(f))
print(type(g))
print(b)

a, b, c = 2, 3, 4
print()
print(a)
print(b)
print(c)

a, b, c = c, a, b
print()
print(a)
print(b)
print(c)
print()

print(1/2)
print(1//2)
print(4 % 2)
# print(dir(math))

print(pow(3, 2))

print()
k = (1, 3, 'a')
print(type(k))
print(len(k))

k = [1, 3, 'a']

print(type(k))
print(len(k))

k = ([1, 3, 'a'], 2, ('e',))

# k[0] = 3
k[0][0] = 3

print(k)

k = [[1, 3, 'a'], 2, ('e',)]

# k[0] = 3222 # it works
k[0][0] = 3

print(k)

k1 = k

k1[1] = 222

print(k)

print(id(k), id(k1))

k = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

print(len(k))

k1 = k[2:-1]
print(k1)
print(len(k1))


k1 = k[2:7:2]
print(k1)
print(len(k1))


k = [[1, 3, 'a'], 2, ('e',)]
k1 = k[:]
print(k1)
print(len(k1))

k1[0][0] = 322342


print(k)
print(k1)

k1 = copy.deepcopy(k)


# k1 = k[::-1]
print(k)
print(k1)

k1[0][0] = 1111
print('k:', k)
print('k1', k1)

print()

k = [0]*100

k[22] = 213

print(k)
k = [[]]*100
print(k)
k[7].append(7)
print(k)

# lista skladana
k = [[0 for x in range(2)] for y in range(100)]
k[7].append(7)
k[7].append(7)
print(k)
###########################

k = []
print(k)
k.append([1, 2, 3])
print(k)

k.extend([1, 2, 3])
print(k)

if 3 in k:
    print('in')
if 4 not in k:
    print('not in')

b = 3

a = 1 if 3 <= b < 44 else 0

print(a)

k = [1, 2, 3, 4, 5, 6, ]

for i in k:
    print(i)

for i in range(len(k)):
    print(i)
    if k[i] > 40:
        print('if')
        break
else:
    print('else do fora')

range(10)
range(2, 10)
range(2, 10, 2)
range(10, 2, -2)

k = [[1, 2], (3, 4), (5, 6)]
for i, j in k:
    print(i, j)


k = [1, 2, 3]
print(k)
k.reverse()
print(k)
k = (1, 2, 3)
k1 = k[::-1]
print(k1)

k = [1, 2, 3, 4, 5, 6, 7, 8]

k1 = k[7:1:-1]
print(k1)

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
zipped = zip(a, b)
print(zipped)

for i, j in zipped:
    print(i, j)
