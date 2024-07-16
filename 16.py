 #Write a program to implement the multilevel inheritance
class A :
# The _ _init_ _method initializes data
    def __init__(self, a) :
        self.__a = a
    def set_a(self, a) :
        self.__a = a
    def get_a(self) :
        return self.__a
class B(A) :
    def __init__(self, a, b):
        A.__init__(self, a)
        self.__b = b
    def set_b(self, b) :
        self.__b = b
    def get_b(self) :
        return self.__b
# Defining class C. It is a subclass of class B
class C(B) :
    def __init__(self, a, b, c):
      B.__init__(self, a, b)
      self.__c = c
    def set_c(self, c) :
     self.__c = c
    def get_c(self) :
        return self.__c
def main() :
    obj = C(10,20,30)
    print('A: a =',obj.get_a())
    print('B: b =',obj.get_b())
    print('C: c =',obj.get_c())
# Call the main function
main()