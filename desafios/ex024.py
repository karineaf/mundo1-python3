# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nomecidade = input('Informe o nome da cidade: ')

santo = 'SANTO' in nomecidade[:5]

if santo:
    print('{} começa com o nome "SANTO"'.format(nomecidade))
else:
    print('{} não começa com o nome "SANTO"'.format(nomecidade))

