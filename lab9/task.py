from random import randint
import os


def zad1(first, second, third):
    if first == 0 or second == 0 or third == 0 or second <= first:
        raise Exception
    arr = [randint(first,second)for _ in range(third)]
    odd = [x for x in arr if x%2 == 1]
    even = [x for x in arr if x%2 == 0]
    return (len(even))/(len(odd))

try:
    x = zad1(1,20,321)
except:
    print('Zgłoszono wyjątek')


def zad2(file):
    average = []
    with open("srednia.dat", "w") as srd:
        with open(file, "r") as y:
            for line in y:
                columns = line.split()
                if len(columns) < 2:
                    raise Exception
                if columns[0].isdigit() is False or columns[1].isdigit() is False:
                    raise Exception
                average.append(int(columns[0]))
                average.append(int(columns[1]))
            kek = sum(average)/len(average)
            print(kek)
            srd.write(str(kek))
            srd.write('\n')



filelist = os.listdir()
for file in filelist:
    if file.endswith(".dat"):
        try:
            zad2(file)
        except:
            print('zlapano wyjatek')




def zad3(my_list, n):
    if len(my_list)%n != 0:
        raise Exception
    flag = False
    odd = 0
    even = 0
    for i in range(0,len(my_list),n):
        if my_list[i]*my_list[i] + my_list[i+1]*my_list[i+1] == my_list[i+2]*my_list[i+2]:
            flag = True
            for x in range(3):
                if my_list[i+x]%2 == 0:
                    even += 1
                else:
                    odd += 1
            print('parzyste {}, nieparzyste {}'.format(even, odd))
        odd = 0
        even = 0
    if flag is False:
        raise Exception


my_list = (3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
zad3(my_list,3)


def zad4(fun, a, b):
    x = a
    vala = eval(fun)
    x = b
    valb = eval(fun)
    if vala*valb > 0:
        raise Exception
    x = (a + b) / 2
    while abs(eval(fun)) > 10**-7:

        xtmp = x
        valx = eval(fun)
        x = a
        vala = eval(fun)
        x = b
        valb = eval(fun)
        if valx*vala < 0:
            b = xtmp
        if valx*valb < 0:
            a = xtmp
        x = (a + b) / 2
    return x


print(zad4('x-1', 0, 2))
