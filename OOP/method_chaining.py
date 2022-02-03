from common.common_global import my_logger


class Car:
    '''
      Method Chaining is a continous calling of their function
    '''

    def engine_on(self):
        my_logger(f'The {self.__class__.__name__} is On')
        return self

    def drive(self):
        my_logger(f'The {self.__class__.__name__} is Driving')
        return self

    def brake(self):
        my_logger(f'The {self.__class__.__name__} is step the Break')
        return self

    def engine_off(self):
        my_logger(f'The {self.__class__.__name__} is Off')
        return self


car = Car()
car2 = Car()

car.engine_on().drive().brake().engine_off()
my_logger("=============================================================")
car.engine_on().drive().engine_off()