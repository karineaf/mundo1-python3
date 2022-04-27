# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Informe o preço do produto: '))

precocomdesconto = preco * 0.95

print('Dado desconto de 5%, preço do produto foi atualizado para R${:.2f}'.format(precocomdesconto))
