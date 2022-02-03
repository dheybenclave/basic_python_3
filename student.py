import docx
from common.common_global import *


class Student:

    def __init__(self, name, major, gpa, is_probation, is_pass):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_probation = is_probation
        self.is_pass = is_pass

    def get_name(self):
        return self.name

    def get_major(self):
        return self.major

    def get_gpa(self):
        return self.gpa

    def get_is_probation(self):
        return self.is_probation

    def is_pass(self):
        return self.is_pass

    def on_dean_list(self):
        if int(self.gpa) >= 3:
            return True
        else:
            return False

    def first_year(self):
        my_logger(f'Student is in the first year level')

    def second_year(self):
        my_logger(f'Student is in the second year level')

    def third_year(self):
        my_logger(f'Student is in the third year level')

    def fourth_year(self):
        my_logger(f'Student is in the fourth year level')
