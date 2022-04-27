# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Informe o valor em metros: '))

valoremcentimetros = valor * 100
valoremmilimetros = valor * 1000

print('{0}m equivale a {1:.0f}cm e a {2:.0f}mm'.format(valor, valoremcentimetros, valoremmilimetros))
