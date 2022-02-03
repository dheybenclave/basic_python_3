from common.common_global import my_logger


class Rectangle:
    '''
        Super Function is to reuse the properties that you set
    '''

    def __init__(self, length=0, width=0, height=0):
        self.length = length
        self.width = width
        self.height = height


class Square(Rectangle):

    def __init__(self, s_length, s_width):
        super().__init__(s_length, s_width)

    def area(self):
        return str(self.length * self.width)


class Cube(Rectangle):

    def __init__(self, c_length, c_width, c_height):
        super().__init__(c_length, c_width, c_height)

    def volume(self):
        return str(self.length * self.width * self.height)


square = Square(4, 2)
my_logger(f'AREA : {square.area()}')

cube = Cube(6, 2, 8)
my_logger(f'VOLUME : {cube.volume()}')
