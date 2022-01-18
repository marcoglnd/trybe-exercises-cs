# Exercício 1: Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical. Exemplo:

# name = input("Digite seu nome: ")
# for letter in name:
#     print(f"{letter}")

# Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses valores.
# Caso algum valor da entrada seja inválido, por exemplo uma letra, uma mensagem deve ser exibida,
# na saída de erros, no seguinte formato: "Erro ao somar valores, {valor} é um valor inválido".
# Ao final, você deve imprimir a soma dos valores válidos.

# Receba os valores em um mesmo input , solicitando à pessoa usuária que separe-os com um espaço.
# Receba os valores no formato str e utilize o método split para pegar cada valor separado.
# O método isdigit , embutido no tipo str , pode ser utilizado para verificar se a string corresponde a um número natural.

# sum = 0
# numbers = input("Digite os números para a soma, separados por espaço: ").split()
# for value in numbers:
#     if value.isdigit():
#         sum += int(value)
#     else:
#         print(f"Erro ao somar valores, {value} é um valor inválido")
# print(sum)

# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que lê todas essas informações
# e filtre mantendo somente as pessoas que estão reprovadas, e escreva seus nomes em outro arquivo. A nota miníma para aprovação é 6.

file = open('arquivo.txt', 'r')
second_file = open('segundo_arquivo.txt', 'w')
for line in file:
    if int(line.split(' ')[1]) >= 6:
        name = line.split(' ')[0]
        second_file.write(f'{name}\n')
      