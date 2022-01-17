# fat = 1
# number = 1
# while number < 6:
#     fat *= number
#     number += 1

# print(fat)

# ratings = [6, 8, 5, 9, 10]

# new_rating = []
# for rating in ratings:
#     new_rating.append(rating * 10)

# print(new_rating)

# for rating in new_rating:
#     if (rating % 3 == 0):
#         print('Multiplo de 3')

PI = 3.14  # PI é uma "constante" em nosso módulo


def square(side):
    '''Calculate area of square.'''
    return side * side


def rectangle(length, width):
    '''Calculate area of rectangle.'''
    return length * width


def circle(radius):
    '''Calculate area of circle.'''
    return PI * radius * radius

print("Área do quadrado:", square(10))
print("Área do retângulo:", rectangle(2, 2))
print("Área do círculo:", circle(3))