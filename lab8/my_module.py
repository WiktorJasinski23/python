u"""łańcuch dokumentacyjny

    Przykłądowa wiadomość widoczna za pomocą help z całego modułu.
"""
import random
import matplotlib.pyplot as plt
import scipy.integrate as integrate


def zad1(n):
    u"""łańcuch dokumentacyjny

        Funkcja rysująca paproć.
    """
    x0 = random.uniform(0, 1)
    y0 = random.uniform(0, 1)
    list_x = [x0]
    list_y = [y0]


    for i in range(n):
        len_x = len(list_x)
        len_y = len(list_y)
        wsp = ((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6))
        my_wsp = random.choices(wsp, weights=[1, 7, 7, 85])
        x = my_wsp[0][0]*list_x[len_x-1] + my_wsp[0][1]*list_y[len_y-1]+my_wsp[0][2]
        y = my_wsp[0][3]*list_x[len_x-1] + my_wsp[0][4]*list_y[len_y-1]+my_wsp[0][5]
        list_x.append(x)
        list_y.append(y)

    plt.plot(list_x,list_y, 'rx')
    plt.show()

def zad2(fun, a, b, y_bottom, y_top, acc):
    u"""łańcuch dokumentacyjny

        Funkcja licząca ilość iteracji potrzebnych do wyznaczenia wartości całki za pomocą metody Monte Carlo.
    """
    n = 0
    t = 0
    true_value = integrate.quad(fun, a, b)
    value = 0
    while value + acc < true_value[0] or value - acc > true_value[0]:
        n += 1
        x = random.uniform(a, b)
        y = random.uniform(y_bottom, y_top)

        if 0 < y <= fun(x):
            t += 1
        if 0 > y >= fun(x):
            t -= 1
        value = (b - a) * (y_top - y_bottom) * t / n

    print(n)


def zad3(fun, a, b, acc):
    u"""łańcuch dokumentacyjny

        Funkcja licząca ilość iteracji potrzebnych do wyznaczenia wartości całki za pomocą innej metody. Przy dokładności
        10^-6 zwykle szuka baaaardzo długo (chociaż czasami znajduje prawie od razu), dlatego zaleca się ustawienie
        mniejszej dokładności. Ogólnie czasem liczy i się nie może doliczyć, a czasem wypluwa wynik od razu. Pewnie coś
        źle zrobiłem :(.
    """
    n = 0
    true_value = integrate.quad(fun, a, b)
    value = 0
    list_x = []
    while value + acc < true_value[0] or value - acc > true_value[0]:
        n += 1
        x = random.uniform(a, b)
        var = fun(x)
        list_x.append(var)
        value = (sum(list_x)/len(list_x)) * (b - a)

    print(n)


if __name__ == '__main__':
    pass
