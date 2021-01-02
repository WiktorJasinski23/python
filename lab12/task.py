import abc
from math import sin, pi

################################## 1 ###############################################

class Calka(abc.ABC):
    def __init__(self, p, k, n, fun):
        self.p = p
        self.k = k
        self.n = n
        self.fun = fun

    @abc.abstractmethod
    def licz(self):
        pass


class Trapez(Calka):
    def licz(self):
        result = 0
        dx = (self.k - self.p) / self.n
        for i in range(self.n):
            xi = i * dx + self.p
            xii = xi + dx
            result += 0.5 * dx * (self.fun(xi) + self.fun(xii))
        return result


class Simpson(Calka):
    def licz(self):
        dx = (self.k-self.p)/(2*self.n)
        four = 0
        two = 0
        for i in range(1,2*self.n):
            if i % 2 == 1:
                xi = i*dx + self.p
                four += self.fun(xi)
            if i % 2 == 0:
                xi = i * dx + self.p
                two += self.fun(xi)
        result = dx/3 * (self.fun(self.p) + 4 * four + 2 * two+self.fun(2*self.n))
        return result


def my_func(x):
    return sin(x)


x = Trapez(1, pi, 100, my_func)
print(x.licz())
y = Simpson(1, pi, 100, my_func)
print(y.licz())

################################## 2 ###############################################


class Stack:
    def __init__(self, other_satck=None):
        self.items = []
        if other_satck:
            self.items.extend(other_satck.items)



    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def add(self, other_stack):
        self.items.extend(other_stack.items)

    def size(self):
        return len(self.items)

    def print(self):
        for x in self.items:
            print(x, end=' ')
        print()

class SortedStack(Stack):
    def __init__(self):
        super().__init__()

    def push(self,item):
        if len(self.items) == 0:
            self.items.append(item)
        elif item >= self.items[-1]:
            self.items.append(item)
        else:
            pass

    def add(self, other_stack):
        if isinstance(other_stack, SortedStack):
            if self.items[-1] < other_stack.items[0]:
                self.items.extend(other_stack.items)
        else:
            pass


p = Stack()
p.push(2)
p.push(3)
p.push(4)
p.print()
p.pop()
p.print()
p2 = Stack(p)
p2.print()
p2.add(p)
p2.print()


s1 = SortedStack()
s1.push(3)
s1.push(4)
s1.push(2)
s1.print()
s1.add(p)
s1.print()
s2 = SortedStack()
s2.push(12)
s2.push(33)
s1.add(s2)
s1.print()

################################## 3 ###############################################

class Counter:
    def __init__(self):
        self.chars = 0
        self.words = 0
        self.lines = 0

    def count(self, filename):
        file = open(filename, "r")
        for line in file:
            words = line.split()
            self.lines += 1
            self.words += len(words)
            self.chars += len(line)
        file.close()
        print('{} {} {} {}'.format(self.lines, self.words, self.chars, filename))
    #
    # @staticmethod
    # def count_static():



i = Counter()
i.count('test1.txt')