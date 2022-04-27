# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
numero = float(input('informe um número:'))

numerotruncado = trunc(numero)

print('A porção inteira de {0} é {1}'.format(numero, numerotruncado))
print('A porção inteira de {0} é {1}'.format(numero, int(numero)))
