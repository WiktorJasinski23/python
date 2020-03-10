#!/usr/bin/env python3.7

import random
from sys import argv


def isPalindrome(x):
    palindrome = str(x)
    return palindrome == palindrome[::-1]


s = {}

while len(s) < 100:
    y = random.randint(100, 10000)
    s.setdefault(y, isPalindrome(y))
# print(s)

myList = [random.randrange(0, 20) for x in range(100)]
# print(myList)
even = {}
odd = {}

for i, item in enumerate(myList):
    if item % 2:
        odd.setdefault(item, []).append(i)
    else:
        even.setdefault(item, []).append(i)

# print(even)

newDictionary = {key: [x for x in listForKey if not x % 3] if [x for x in listForKey if not x % 3] else (listForKey[0], listForKey[-1]) for key, listForKey in even.items()}

# print(newDictionary)

anotherDictionary = {}

if len(argv) == 2:
    for i in range(int(argv[1])):
        anotherDictionary.setdefault(i, random.randrange(2, 15))

anotherList = [(key, value) for key, value in anotherDictionary.items()]

# print(anotherDictionary)

yetAnotherDictionary = {value: key for key, value in anotherList}

# print(yetAnotherDictionary)

yetAnotherList = [random.randrange(0, 11) for x in range(100)]

anotherOne = {}
for value in yetAnotherList:
    anotherOne.setdefault(value, []).append(yetAnotherList.index(value, anotherOne[value][-1] + 1) if anotherOne[value] else yetAnotherList.index(value))

#print(anotherOne)

Dictionary10 = {x: random.randrange(1, 100) for x in range(10)}
Dictionary11 = {x: random.randrange(1, 100) for x in range(10)}


Dictionary10 = {value: key for key, value in Dictionary10.items()}
Dictionary11 = {value: key for key, value in Dictionary11.items()}


finalDictionary = {key: (Dictionary10[key], Dictionary11[key]) for key in Dictionary10 if key in Dictionary11}

print(finalDictionary)
