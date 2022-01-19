# Exercício 1: Escreva um programa que retorne uma lista com os valores numéricos de 1 a N, mas com as seguintes exceções :

# Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
# Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número';

def fizz_buzz(number):
    result = []
    i = 1
    while i <= number:
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 5 == 0:
            result.append('Buzz')
        elif i % 3 == 0:
            result.append('Fizz')
        else:
            result.append(i)
        i += 1
    return result

print(fizz_buzz(15))