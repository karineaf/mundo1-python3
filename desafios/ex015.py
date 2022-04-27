# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quilometrospercorridos = float(input('Informe a quantidade de Km percorridos: '))
diasalugados = int(input('Informe a quantidade de dias alugados: '))

precofinal = quilometrospercorridos * 0.15 + diasalugados * 60

print('Valor total a pagar: R${:.2f}'.format(precofinal))

