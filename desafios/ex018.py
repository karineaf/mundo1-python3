# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

angulo = float(input('Informe o ângulo: '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print('O ângulo {0} possui seno de {1:.2f}, cosseno de {2:.2f} e tangente de {3:.2f}'
      .format(angulo, seno, cosseno, tangente))
