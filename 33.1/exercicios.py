class Square:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return self.side1 * self.side2

    def calculate_perimeter(self):
        return self.side1 * 2 + self.side2 * 2


meu_retangulo = Square(4, 5)
print(meu_retangulo.calculate_area())
print(meu_retangulo.calculate_perimeter())

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius * self.radius)

    def calculate_circumference(self):
        return 3.14 * self.radius * 2


meu_circulo = Circle(4)
print(meu_circulo.calculate_circumference())
print(meu_circulo.calculate_area())