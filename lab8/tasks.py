import my_module

if __name__ == '__main__':
    help(my_module)

    help(my_module.zad1)
    my_module.zad1(10**4)

    help(my_module.zad2)
    my_module.zad2(lambda x: x*x - 3, 0, 5, -4, 25, 10**-6)

    help(my_module.zad3)
    my_module.zad3(lambda x: x*x - 3, 0, 5, 10**-5)
