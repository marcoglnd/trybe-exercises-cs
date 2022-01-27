# Exercício 4 Baseado no exercício anterior, escreva uma função que, dado uma lista de emails,
# deve retornar somente os emails válidos. Caso uma exceção ocorra, apenas a escreva na tela.

from exercicio3 import verify_email

def verify_email_list(list):
    result = []
    for email in list:
        if verify_email(email):
            result.append(email)
    return result