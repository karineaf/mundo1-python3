# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
from math import ceil

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
quantidadetinta = int(ceil(area / 2))

print('A quantidade de tinta necessário para pintar a parede, é de {} litros de tinta'.format(quantidadetinta))
