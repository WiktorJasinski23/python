from math import sqrt

class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @x.getter
    def x(self):
        return self.__x

    @y.getter
    def y(self):
        return self.__y


def myRange(x1, x2, y1, y2):
    def fz(pf):
        def fw(p1, p2):
            if x1 < p1.x < x2 and x1 < p2.x < x2 and y1 < p1.y < y2 and y1 < p2.y < y2:
                return pf(p1, p2)
            else:
                raise Exception('Points out of range')
        return fw
    return fz

class Modulo2:
    i = 0
    def __init__(self, pf):
        self.__pf=pf

    def __call__(self, *p):
        Modulo2.i += 1
        return self.__pf(*p)

    @staticmethod
    def tellMe():
        return Modulo2.i


@Modulo2
@myRange(0, 10, 0, 10)
def add(p1, p2):
    tmp = Point()
    tmp.x = p1.x + p2.x
    tmp.y = p1.y + p2.y
    return tmp


@Modulo2
@myRange(0, 10, 0, 10)
def subtract(p1, p2):
    tmp = Point()
    tmp.x = p1.x - p2.x
    tmp.y = p1.y - p2.y
    return tmp


class Calculate:
    @staticmethod
    def heron(a, b, c):
        circuit = sqrt((b.x - a.x)**2 + (b.y - a.y)**2) + sqrt((c.x - b.x)**2 + (c.y - b.y)**2) + sqrt((a.x - c.x)**2 +
                                                                                                       (a.y - c.y)**2)
        p = circuit/2
        area = (p*(p - sqrt((b.x - a.x)**2 + (b.y - a.y)**2))*(p-sqrt((c.x - b.x)**2 + (c.y - b.y)**2)) *
                (p-sqrt((a.x - c.x)**2 + (a.y - c.y)**2)))**1/2
        return circuit, area

    @staticmethod
    def brahmagupta(a, b, c, d):
        circuit = sqrt((b.x - a.x)**2 + (b.y - a.y)**2) + sqrt((c.x - b.x)**2 + (c.y - b.y)**2)\
                  + sqrt((d.x - c.x) ** 2 + (d.y - c.y) ** 2) + sqrt((a.x - d.x) ** 2 + (a.y - d.y) ** 2)
        p = circuit/2
        area = (p*(p - sqrt((b.x - a.x)**2 + (b.y - a.y)**2))*(p-sqrt((c.x - b.x)**2 + (c.y - b.y)**2)) *
                (p-sqrt((d.x - c.x)**2 + (d.y - c.y)**2)) * (p-sqrt((a.x - d.x)**2 + (a.y - d.y)**2)))**1/2
        return circuit, area


if __name__ == "__main__":
    p1 = Point()
    p2 = Point()
    p3 = Point()
    p4 = Point()
    p1.x = 9
    p1.y = 5
    p2.x = 3
    p2.y = 5
    p3.x = 10
    p3.y = 12
    p4.x = 12
    p4.y = 12
    result = add(p1, p2)
    result = add(p1, p2)
    result = add(p1, p2)
    result2 = subtract(p1, p2)
    print(result.x, result.y)
    print(result2.x, result2.y)
    print(Calculate.heron(p1, p2, p3))
    print(Calculate.brahmagupta(p1, p2, p3, p4))
    print(Modulo2.tellMe())
