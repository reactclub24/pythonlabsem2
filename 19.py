#Write a program to implement the hybrid inheritance


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


class D(B, C):

    def __init__(self, a, b, c, d):
        B.__init__(self, a, b)
        C.__init__(self, a, c)
        self.__d = d

    def set_d(self, d):
        self.__d = d

    def get_d(self):
        return self.__d
def main():
    obj = D(10, 20, 30, 40)


    print('A: a =', obj.get_a())
    print('B: b =', obj.get_b())
    print('C: c =', obj.get_c())
    print('D: d =', obj.get_d())
# Call the main function
main()