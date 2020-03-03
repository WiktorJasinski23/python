#!/usr/bin/env python3.7

from sys import argv


if len(argv) > 1:
    myStr = ' '.join(argv[1:])
    print(myStr)
    upperLetters = [x for x in myStr if x.isupper()]
    lowerLetters = [x for x in myStr if x.islower()]
    numbers = [x for x in myStr if x.isnumeric()]
    notLetters = [x for x in myStr if not x.isalpha()]
    print(upperLetters)
    print(lowerLetters)
    print(numbers)
    print(notLetters)
    uniqueLowerLetters = []
    for x in lowerLetters:
        if x not in uniqueLowerLetters:
            uniqueLowerLetters.append(x)
    print(uniqueLowerLetters)
    numberOfLetters = [[x, lowerLetters.count(x)] for x in uniqueLowerLetters]
    print(numberOfLetters)
    numberOfLetters.sort(key=lambda x: x[1])
    print(numberOfLetters)
    # a e i o u y
    # vowels- samo consonants - spół
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    vowelsFromLower = sum(1 for x in myStr if x.lower() in vowels)
    consonantsFromLower = sum(1 for x in myStr if x.isalpha()) - vowelsFromLower
    print(vowelsFromLower)
    print(consonantsFromLower)
    squareEquation = [(int(x), int(vowelsFromLower)*int(x)+int(consonantsFromLower)) for x in numbers]
    print(squareEquation)
    xAvg = sum(x for x, _ in squareEquation)/len(squareEquation)
    yAvg = sum(y for _, y in squareEquation) / len(squareEquation)
    D = sum((x-xAvg)**2 for x, y in squareEquation)
    a = (1/D)*sum(y*(x-xAvg) for x, y in squareEquation)
    b = yAvg-a*xAvg
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'D = {D}')


else:
    print('Prosze podac argumrnty wywolania, na przyklad python zad2.py pies kot')

