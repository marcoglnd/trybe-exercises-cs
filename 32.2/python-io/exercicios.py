# Exercício 1: Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida:

def name_inverted(name):
    while len(name) > 0:
        print(name)
        name = name[0:-1]

# name_inverted('Marco')

# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha que adivinhar
# uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras
# e escolherá uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra.
# Ao final a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo.

import random

def scramble_word_game(list):
    word = random.choice(list)
    scrambled_word = "".join(random.sample(word, len(word)))
    times = 0
    answer = ''
    while times < 3 and answer != word:
        print(f'Consegue advinhar qual é a palavra: {scrambled_word}?')
        print(f'{3 - times} tentativas restantes')
        answer = input()
        times += 1
    if answer == word:
        print(f'Você acertou! A palavra era {word}!')
    else:
        print(f'Tentativas esgotadas, a palavra era {word}!')

# scramble_word_game(['banana', 'morango', 'acerola'])

# Exercício 3: Modifique o exercício anterior para que as palavras sejam lidas de um arquivo.
# Considere que o arquivo terá cada palavra em uma linha.

def scramble_word_game(file):
    with open(file, 'r') as content:
        list = content.read().split()
        word = random.choice(list)
        scrambled_word = "".join(random.sample(word, len(word)))
        times = 0
        answer = ''
        while times < 3 and answer != word:
            print(f'Consegue advinhar qual é a palavra: {scrambled_word}?')
            print(f'{3 - times} tentativas restantes')
            answer = input()
            times += 1
        if answer == word:
            print(f'Você acertou! A palavra era {word}!')
        else:
            print(f'Tentativas esgotadas, a palavra era {word}!')

# scramble_word_game('arquivo.txt')

# Exercício 4: Dado o seguinte arquivo no formato JSON , leia seu conteúdo e calcule
# a porcentagem de livros em cada categoria, em relação ao número total de livros.
# O resultado deve ser escrito em um arquivo no formato CSV como o exemplo abaixo.

# categoria,porcentagem
# Python,0.23201856148491878
# Java,0.23201856148491878
# PHP,0.23201856148491878

import json
import csv


def book_percentage(file):
    with open(file, 'r') as content:
        books = []
        category_count = dict()
        for line in content:
            books.append(json.loads(line))
        for book in books:
            for category in book['categories']:
                if category in category_count:
                    category_count[category] += 1
                else:
                    category_count[category] = 1
        with open("book_categories.csv", 'w') as book_categories:
            writer = csv.writer(book_categories)

            header = [
              'categoria',
              'porcentagem'
            ]
            writer.writerow(header)
            for categories in category_count.items():
                row = [categories[0], categories[1]/len(books) * 100]
                writer.writerow(row)

book_percentage('file.json')