#  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nomepessoa = input('Informe o nome da pessoa: ').strip()

silva = 'SILVA' in nomepessoa.upper()

if silva:
    print('{} possui o nome "SILVA"'.format(nomepessoa))
else:
    print('{} não possui o nome "SILVA"'.format(nomepessoa))

