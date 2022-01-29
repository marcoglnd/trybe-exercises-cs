from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        return NotImplementedError

    @abstractmethod
    def perimeter(self):
        return NotImplementedError

class Square(GeometricFigure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Rectangle(GeometricFigure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)


class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 3.14 * self.radius * 2

sq = Circle(5)
print(sq.area())
print(sq.perimeter())