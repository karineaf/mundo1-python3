# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperaturaemcelsius = float(input('Informe a temperatura em Cº: '))
temperaturaemfahrenheit = ((9 * temperaturaemcelsius) / 5) + 32
print('A temperatura de {0}ºC corresponde a {1}ºF'.format(temperaturaemcelsius, temperaturaemfahrenheit))


