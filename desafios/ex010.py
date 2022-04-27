# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1.00 = R$3,27

valor = float(input('Informe quanto você possui na carteira: '))

valoremdolares = valor * 3.27

print('Você pode comprar {:.2f} dólares.'.format(valoremdolares))
