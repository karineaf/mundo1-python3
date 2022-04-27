# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

nomecompleto = input('Informe o nome completo: ').strip()

splitnome = nomecompleto.split()
primeironome = splitnome[0]
ultimonome = splitnome[len(nomecompleto.split())-1]

print('O primeiro nome de {0} é {1} e o último nome é {2}'.format(nomecompleto, primeironome, ultimonome))
