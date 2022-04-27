# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot

catetooposto = float(input('Informe o comprimento do cateto oposto: '))
catetoadjacente = float(input('Informe o comprimento do cateto adjacente: '))

hipotenusa = hypot(catetooposto, catetoadjacente)

print('A hipotenusa do triângulo retângulo é {:.2f}'.format(hipotenusa))
