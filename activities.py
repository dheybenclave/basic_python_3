from common.common_global import *
from student import Student


class Activities(Student):

    def sport(self):
        my_logger(f'{self.get_name()} is doing sport')

    def literature(self):
        my_logger(f'{self.get_name()} is doing literature')

    def debating(self):
        my_logger(f'{self.get_name()} is doing debating')


class Course(Student):

    def set_major(self, major):
        self.major = major
        return self
