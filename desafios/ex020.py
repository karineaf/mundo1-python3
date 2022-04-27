# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
from random import choice

lista = list()
lista.append(input('Informe o primeiro nome: '))
lista.append(input('Informe o segundo nome: '))
lista.append(input('Informe o terceiro nome: '))
lista.append(input('Informe o quarto nome: '))

while len(lista) > 0:
    alunoescolhido = choice(lista)
    print("Alunx escolhido: {}".format(alunoescolhido))
    lista.remove(alunoescolhido)

'''outra forma de fazer
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))'''
