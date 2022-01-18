# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.


def biggest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(biggest_number(30, 20))

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

list = [1, 2, 3]
print(sum(list) / len(list))

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n .


def square(n):
    for i in range(n):
        print(n * "*")


square(5)

# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres.


def biggest_name(name_list):
    big_name = ""
    for name in name_list:
        if len(name) > len(big_name):
            big_name = name
    return big_name


print(biggest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta
# a serem compradas e o preço total a partir do tamanho de uma parede(em m²).

import math


def paint_buckets(wall_size):
    number_of_buckets = math.ceil(wall_size / 54)
    return tuple([number_of_buckets, number_of_buckets * 80.00])


print(paint_buckets(150))

# Exercício 6: Crie uma função que receba os três lado de um triângulo
# e informe qual o tipo de triângulo formado ou "não é triangulo" , caso não seja possível formar um triângulo.


def triangle(side1, side2, side3):
    if side1 + side2 < side3 or side2 + side3 < side1 or side3 + side1 < side2:
        print("nao é um triangulo")
    elif side1 == side2 == side3:
        print("equilátero")
    elif side1 != side2 != side3:
        print("escaleno")
    else:
        print("isóceles")


triangle(3, 3, 10)
