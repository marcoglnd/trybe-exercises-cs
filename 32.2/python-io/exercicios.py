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

scramble_word_game(['banana', 'morango', 'acerola'])