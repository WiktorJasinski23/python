#!/usr/bin/env python3.7

import random

###################################### 1 ###############################################


def fun1(x):
    d = {}
    for i in range(random.randrange(0, 20)):
        key = random.random()
        d.setdefault((round(key, 3)), str(round(eval('{}'.format(x).format(key)), 3)))

    return d

# print(fun1('5*{}+22'))


###################################### 2 ###############################################


def fun2(*args):
    my_list = []
    for i in args[0]:
        for j in args[1:]:
            if i not in j:
                break
        else:
            my_list.append(i)
    return my_list


print(fun2((1, 2,3,4), (2, 3,4), [1, 2,3,4,5]))


###################################### 3 ###############################################


def fun3(seq1, seq2, parameter=True):
    if parameter is True:
        my_list = [(seq1[i], seq2[i]) for i in range(len(seq1) if len(seq1) < len(seq2) else len(seq2))]
    else:
        my_list = [(seq1[i] if i<len(seq1) else None, seq2[i] if i < len(seq2) else None) for i in range(len(seq1) if len(seq1) > len(seq2) else len(seq2))]
    return my_list


print(fun3((1, 2, 2), (1, 3, 4, 5)))
print(fun3((1, 2, 2), (1, 3, 4, 5), False))


###################################### 4 ###############################################


def fun4(*args):
    my_min = args[0]
    my_max = args[0]
    for i in args:
        if i > my_max:
            my_max = i
        if i < my_min:
            my_min = i
    return(my_min, my_max)

# print(fun4(1, 23, 5465, 44, 33))


def fun5(fun, *args):
    return fun(*args[0])


# print(fun5(fun4, [1, 6, 7]))


###################################### 5 ###############################################


def fun6(kwota, nominaly=(10,5,2)):
    tab = []
    while kwota > 1:
        for i in range(len(nominaly)):
            x = kwota//nominaly[i]
            tab.append(x)
            kwota = kwota % nominaly[i]
    if kwota == 1:
        tab.append('r: 1')
    return tab


# print(fun6(12))

###################################### 6 ###############################################


def fun7(number, my_min, my_max, how='r'):
    if how == 'r':
        i = 0
        while True:
            i += 1
            x = random.randint(my_min, my_max)
            print(x)
            if x > number:
                my_max = x
            if x < number:
                my_min = x
            if x == number:
                break
        return x,i
    else:
        i = 0
        while True:
            i += 1
            x = my_max+my_min/2

            if x > number:
                my_max = x
                print(x)
            if x < number:
                my_min = x
                print(x)
            if x == number:
                break
        return x,i


print(fun7(2, 1, 453))

