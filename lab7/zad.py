import numpy as np
import matplotlib.pyplot as plt
import collections

############################### 1 #################################
# def zad1(filename, n):
#     with open(filename) as pl:
#         line = pl.readlines()
#         print(line[0:n])
#         print(line[len(line)-n:len(line)])
#         print(line[::n])
#
#         print([x[::n] for x in line])
#
#
# zad1('test.txt', 3)

############################### 2 ######################################
# with open('plik0.in') as pl0, open('plik1.in') as pl1,open('plik2.in') as pl2,open('plik3.in') as pl3, \
#     open('plik4.in') as pl4, open('plik5.in') as pl5, open('result.txt', 'w') as result:
#     for line in pl0:
#         tmp = line.split()
#         x = tmp[0]
#         arr = np.array([float(tmp[1]), float(pl1.readline().split()[1]), float(pl2.readline().split()[1]),
#                         float(pl3.readline().split()[1]), float(pl4.readline().split()[1]),
#                         float(pl5.readline().split()[1])])
#         avg = np.average(arr)
#         std = np.std(arr)
#         result.write(f'{x} {avg} {std}\n')



################################# 3 #########################

################################# 4 #########################

with open('ZAD4A.in') as  pl1, open('ZAD4B.in') as pl2:
    counts = dict()
    for line in pl1:
        data = line.split()
    for line in pl2:
        data.extend(line.split())

    data = [x.lower() for x in data]

    for word in data:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


############################ 5 ##############################
# def zad5(filename, result):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#     letters = []
#     vowelscount = 0
#     notvowelscount = 0
#     list = []
#     sum = 0
#     with open(filename) as pl:
#         for line in pl:
#             for char in line:
#                 if char.isdigit():
#                     list.append(char)
#                 if char.isalpha() and char in vowels:
#                     vowelscount += 1
#                     letters.append(char)
#                 if char.isalpha() and char not in vowels:
#                     notvowelscount += 1
#                     letters.append(char)
#
#     with open(result, 'w') as pl:
#         for x in list:
#             pl.write(x)
#
#         pl.write(' -> ')
#         for x in list:
#             if list.index(x) != len(list) - 1:
#                 pl.write(f'{x}+')
#             sum = sum + int(x)
#         pl.write(f'= {sum}\n')
#         for x in letters:
#             pl.write(x)
#         pl.write(f'= {vowelscount}+{notvowelscount}')
#
#
# zad5('zad5.in', 'zad5.out')