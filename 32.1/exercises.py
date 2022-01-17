# coding=UTF-8

# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.

def biggest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(biggest_number(30, 20))

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

list = [1, 2, 3]
sum = 0
for number in list:
    sum += number
print(sum / len(list))

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n .

def square(n):
    for i in range(n):
        print(n * '*')

square(5)

# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres.

def biggest_name(list):
    big_name = ''
    for name in list:
        if len(name) > len(big_name):
            big_name = name
    return big_name

print(biggest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))