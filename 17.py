#zzWrite a program to implement the hierarchical inheritance


class A:

    def __init__(self, a):
        self.__a = a

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a


class B(A):

    def __init__(self, a, b):
        A.__init__(self, a)
        self.__b = b

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b


class C(A):

    def __init__(self, a, c):
        A.__init__(self, a)
        self.__c = c

    def set_c(self, c):
        self.__c = c

    def get_c(self):
        return self.__c


def main():
    obj1 = B(10, 20)
    print('A: a =', obj1.get_a())
    print('B: b =', obj1.get_b())
    obj2 = C(30, 40)
    print('A: a =', obj2.get_a())
    print('C: c =', obj2.get_c())


main()