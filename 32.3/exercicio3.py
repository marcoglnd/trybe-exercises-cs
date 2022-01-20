# Exercício 3 Faça uma função que valide um e-mail nos seguintes critérios abaixo,
# lançando uma exceção quando o valor for inválido. Endereços de email válidos devem seguir as seguintes regras:

# Devem seguir o formato nomeusuario@nomewebsite.extensao;
# O nome de usuário deve conter somente letras, dígitos, traços e underscores ;
# O nome de usuário deve iniciar com letra;
# O nome do website deve conter somente letras e dígitos;
# O tamanho máximo da extensão é três.

def contain_at_sign(string):
    if not '@' in string:
        return False
    return True

def verify_first_letter(string):
    if not string[0].isalpha():
        return False
    return True

def verify_extension(string):
    if len(string) > 3:
        return False
    return True

def verify_username(string):
    for letter in string:
        if not (letter.isdigit() or letter.isalpha() or letter == '_' or letter == '-'):
            return False
    return True

def verify_website(string):
    for letter in string:
        if not (letter.isdigit() or letter.isalpha()):
            return False
    return True

def verify_email(string):
    if not contain_at_sign(string): raise ValueError('Email deve possuir @')
    if not verify_first_letter(string.split('@')[0]): raise ValueError('Nome do usuário deve iniciar com letra')
    if not verify_username(string.split('@')[0]): raise ValueError('Nome do usuário deve conter somente letras, dígitos, traços e underscores')
    if not verify_website(string.split('@')[1].split('.')[0]): raise ValueError('Nome do website deve conter somente letras e dígitos')
    if not verify_extension(string.split('.')[1]): raise ValueError('Tamanho máximo da extensão é três')
    return 'O email é válido'

print(verify_email('omeusuar**io@nomewebsite.extensao'))