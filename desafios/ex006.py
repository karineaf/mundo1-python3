# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
import math

numero = int(input('Informe um número: '))

dobro = 2 * numero
triplo = 3 * numero
raizquadrada = math.sqrt(numero)

print('O dobro de {0} é {1}'.format(numero, dobro))
print('O triplo de {0} é {1}'.format(numero, triplo))
print('A raiz quadrada de {0} é {1}'.format(numero, raizquadrada))
