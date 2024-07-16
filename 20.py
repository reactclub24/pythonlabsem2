#Write a program to implement the polymorphism
# Defining abstract class
class Car :
    def __init__(self, name) :
        self.name = name
# Defining abstract method
    def drive(self) :
        raise NotImplementedError
    def stop(self) :
        raise NotImplementedError

# Defining concrete class
class Sportscar(Car) :
    def drive(self) :
        return 'Sports car driving'
    def stop(self) :
        return 'Sports car stopping'
class Truckcar(Car) :
    def drive(self) :
        return 'Truck car driving'
    def stop(self) :
        return 'Truckc ar stopping'

cars = [Sportscar('x'), Truckcar('y'), Sportscar('z')]
for car in cars:
            print(car.name,':',car.drive())
            print(car.name,':',car.stop())