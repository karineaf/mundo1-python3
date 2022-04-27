# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Informe um número: '))
i = 1
while i <= 10:
    resultado = numero * i
    print('{0} x {1} = {2}'.format(numero, i, resultado))
    i += 1
