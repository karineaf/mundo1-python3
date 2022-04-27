# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

lista = list()
lista.append(input('Informe o primeiro nome: '))
lista.append(input('Informe o segundo nome: '))
lista.append(input('Informe o terceiro nome: '))
lista.append(input('Informe o quarto nome: '))

alunoescolhido = choice(lista)

print("Alunx escolhido: {}".format(alunoescolhido))

