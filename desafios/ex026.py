# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip().upper()

quantasvezesaparece = frase.count('A')
posicaoprimeiraletraa = frase.find('A') + 1
posicaoultimaletraa = frase.rfind('A') + 1

print('A letra A apareceu {} vezes na frase'.format(quantasvezesaparece))
print('A primeira letra A apareceu na posicão {}'.format(posicaoprimeiraletraa))
print('A ultima letra A apareceu na posicão {}'.format(posicaoultimaletraa))
