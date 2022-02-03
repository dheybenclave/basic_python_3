from common.common_global import my_logger

from abc import *


class Vehicle(ABC):
    '''
    abstract method is to ensure the all inherited method from parent should have override method in subclass
    '''

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    color = None
    def set_color(self,color):
        my_logger(f'The Color of {self.__class__.__name__} is {color}')


class Car(Vehicle):

    def go(self):
        my_logger("You are using the car")

    def stop(self):
        my_logger("the car stop")


# Pass Object as Aguments
def change_color(_object, color):
    _object.color = color
    return my_logger(f'Change Color = The Color of {_object.__class__.__name__} is {color}')


class Motorcyle(Vehicle):

    def go(self):
        my_logger("You are using the motorcyle")

    def stop(self):
        my_logger("the motorcyle stop")

my_logger("=============================================================")
car = Car()
car.go()
car.stop()

car.set_color("pink")
change_color(car,"green")

my_logger("=============================================================")
motor = Motorcyle()
motor.go()
motor.stop()
change_color(motor,"Blue")
