# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informacoes possiveis sobre ele

entrada = input('Digite algo: ')

print(type(entrada))
print('É numérico? {}'.format(entrada.isnumeric()))
print('É alfanúmerico? {}'.format(entrada.isalnum()))
print('É alfa? {}'.format(entrada.isalpha()))
print('Está apenas em caixa baixa? {}'.format(entrada.islower()))
print('Está apenas em caixa alta? {}'.format(entrada.isupper()))
print('É um espaço? {}'.format(entrada.isspace()))

