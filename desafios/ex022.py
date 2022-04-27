# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Total de letras (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nomecompleto = input('Informe o nome completo: ')

nomecomletrasmaiusculas = nomecompleto.upper()
nomecomletrasminusculas = nomecompleto.lower()
split = nomecompleto.split()
totaldeletrassemespacos = len(''.join(split))
quantidadeletrasprimeironome = len(split[0])

print('Nome com todas letras maiúsculas: {}'.format(nomecomletrasmaiusculas))
print('Nome com todas letras minúsculas: {}'.format(nomecomletrasminusculas))
print('Total de letras (sem considerar espaço): {}'.format(totaldeletrassemespacos))
print('Quantidade de letras do primerio nome: {}'.format(quantidadeletrasprimeironome))
