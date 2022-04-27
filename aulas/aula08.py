from math import sqrt, ceil
from random import randint
import emoji

numero = int(input('digite um número: '))

raiz = sqrt(numero)

print('A raiz de {0} é {1}'.format(numero, ceil(raiz)))
print('*' * 20)

print(randint(0, 85))
print('*' * 20)

print(emoji.emojize('Olá, mundo! :thumbs_up:'))
