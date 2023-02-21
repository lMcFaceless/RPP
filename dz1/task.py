import math


class Furniture:
    def _size_count(self):
        pass

    def print_size(self):
        pass


class Table(Furniture):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def _size_count(self, length, width):
        return length * width

    def print_size(self):
        print(self._size_count(self.length, self.width))


class Chair(Furniture):
    def __init__(self, radius):
        self.radius = radius

    def _size_count(self, radius):
        return math.pi * math.pow(radius, 2)

    def print_size(self):
        print(self._size_count(self.radius))


table = Table(2, 3)
table.print_size()
chair = Chair(3)
chair.print_size()
