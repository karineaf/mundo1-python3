# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input('Informe um número de 0 a 9999: ')

quantidecasas = len(numero)

if quantidecasas == 3:
    numero = '0' + numero

if quantidecasas == 2:
    numero = '00' + numero

if quantidecasas == 1:
    numero = '000' + numero

print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))

# segunda opção:
# numero = int(input('Informe um número de 0 a 9999: '))
#
# unidade = numero // 1 % 10
# dezena = numero // 10 % 10
# centena = numero // 100 % 10
# milhar = numero // 1000 % 10
#
# print('Unidade: {}'.format(unidade))
# print('Dezena: {}'.format(dezena))
# print('Centena: {}'.format(centena))
# print('Milhar: {}'.format(milhar))
