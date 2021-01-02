from random import randint
from math import sqrt

class Automat:
    def __init__(self, N, reg, init):
        self.train = ''
        if init:
            for i in range(N):
                self.train += str(randint(0, 1))
        else:
            for i in range(N):
                if i == N//2:
                    self.train += '1'
                else:
                    self.train += '0'

        self.rule = {}
        x = '{0:b}'.format(reg).zfill(8)
        self.rule['111'] = x[0]
        self.rule['110'] = x[1]
        self.rule['101'] = x[2]
        self.rule['100'] = x[3]
        self.rule['011'] = x[4]
        self.rule['010'] = x[5]
        self.rule['001'] = x[6]
        self.rule['000'] = x[7]

    def evolution(self, count):
        self.show(self.train)
        for j in range(count):
            tmp = ''
            for i in range(len(self.train)):
                if i+1 == len(self.train):
                    value = self.train[i - 1] + self.train[i] + self.train[0]
                else:
                    value = self.train[i-1]+self.train[i]+self.train[i+1]
                add = self.rule[value]
                tmp += add
            self.train = tmp
            self.show(self.train)

    def show(self, figure):
        for i in figure:
            if i == '0':
                print(' ', end='')
            if i == '1':
                print('*', end='')
        print()


class Wektor:
    def __init__(self, *args):
        self.coordinates = list(args)

    def __add__(self, other):
        new = []
        for i in range(len(other.coordinates)):
            new.append(self.coordinates[i] + other.coordinates[i])
        return Wektor(*new)

    def __iadd__(self, other):
        for i in range(len(other.coordinates)):
            self.coordinates[i] += other.coordinates[i]
        return self

    def __sub__(self, other):
        new = []
        for i in range(len(other.coordinates)):
            new.append(self.coordinates[i] - other.coordinates[i])
        return Wektor(*new)

    def __isub__(self, other):
        for i in range(len(other.coordinates)):
            self.coordinates[i] -= other.coordinates[i]
        return self

    def __mul__(self, other):
        new = []
        for i in range(len(self.coordinates)):
            new.append(self.coordinates[i] * other)
        return Wektor(*new)

    __rmul__ = __mul__

    def __imul__(self, other):
        for i in range(len(self.coordinates)):
            self.coordinates[i] *= other
        return self

    def __getitem__(self, item):
        return self.coordinates[item]

    def __len__(self):
        return len(self.coordinates)

    def __str__(self):
        str = ''
        for i in self.coordinates:
            str += str(i) + ''
        return str

    def __eq__(self, other):
        for i in range(len(self.coordinates)):
            if self.coordinates[i] != other.coordinates[i]:
                return False
        return True

    def len(self):
        suma = 0
        for i in range(0, len(self.coordinates), 2):
            suma += self.coordinates[i]*self.coordinates[i]
        return sqrt(suma)


if __name__ == "__main__":
    test = Automat(19,30,False)
    test.evolution(3)
    a = Automat(31, 90, False)
    a.evolution(16)
    b = Automat(31, 94, False)
    b.evolution(16)
    c = Automat(31, 182, False)
    c.evolution(16)

    u = Wektor(1,2,3,4)
    print(u.len())
    v = Wektor(1,2,3,4)
    if u == v:
        print('da')
    else:
        print(u[1])
    print(v.coordinates)

