# Exercício 2 Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras.
# Dessa maneira a expressão MY LOVE significa 69 5683.
# Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase
# e os dígitos 1 e 0 não estão associados a nenhuma letra.

# Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo.
# Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.

# Letras  ->  Número
# ABC     ->  2
# DEF     ->  3
# GHI     ->  4
# JKL     ->  5
# MNO     ->  6
# PQRS    ->  7
# TUV     ->  8
# WXYZ    ->  9

import re


def letters_to_phone_numbers(string):
    dictionary = {
      "ABC": 2,
      "DEF": 3,
      "GHI": 4,
      "JKL": 5,
      "MNO": 6,
      "PQRS": 7,
      "TUV": 8,
      "WXYZ": 9
    }
    result = ''
    regex = '/[a-zA-Z]/'
    dict_keys = list(dictionary.keys())
    for letter in string:
        if (re.search('[a-zA-Z]', letter)):
            for key in dict_keys:
                if letter.upper() in key:
                    result += str(dictionary[key])
        else:
            result += letter
    return result

print(letters_to_phone_numbers('oitudobem'))