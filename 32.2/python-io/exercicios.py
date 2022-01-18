# Exercício 1: Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida:

def name_inverted(name):
    while len(name) > 0:
        print(name)
        name = name[0:-1]

name_inverted('Marco')