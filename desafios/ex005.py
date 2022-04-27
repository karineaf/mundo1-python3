# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

numero = int(input('Informe um número inteiro: '))

antecessor = numero - 1
sucessor = numero + 1

print('{0} tem como {1} seu antecessor e {2} como seu sucessor'.format(numero, antecessor, sucessor))
