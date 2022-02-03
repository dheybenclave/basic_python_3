from common.common_global import my_logger


class Orgnanism:
    '''
         Multi level of Inheritance is absorbing all properties/method of diff parent class
    '''
    alive = True


class Animal(Orgnanism):

    def eat(self):
        my_logger(f'This Animal is eating')


class Prey:
    def flee(self):
        my_logger("This animal Flees")


class Predator:
    def hunt(self):
        my_logger("This animal is hunting")


class Tiger(Animal, Predator):
    pass


# my_logger("This animal is Predator")


class Rabbit(Animal, Prey):
    pass
    # my_logger("This animal is Prey ")


class Hawk(Animal, Prey, Predator):
    pass
    # my_logger("This animal may become Prey and or Predator ")


class Dog(Animal):

    def bark(self):
        my_logger("This dog is barking")


my_logger("=============================================================")

tiger = Tiger()
my_logger(f'The {tiger.__class__.__name__} is {"Alive" if tiger.alive else "Dead"}')
tiger.eat()
tiger.hunt()

my_logger("=============================================================")

rabbit = Rabbit()
my_logger(f'The {rabbit.__class__.__name__} is {"Alive" if rabbit.alive else "Dead"}')
rabbit.eat()
rabbit.flee()

my_logger("=============================================================")

hawk = Hawk()
my_logger(f'The {hawk.__class__.__name__} is {"Alive" if hawk.alive else "Dead"}')
hawk.eat()
hawk.flee()
hawk.hunt()

my_logger("=============================================================")

dog = Dog()
my_logger(f'The {dog.__class__.__name__} is {"Alive" if dog.alive else "Dead"}')
dog.eat()
dog.bark()
