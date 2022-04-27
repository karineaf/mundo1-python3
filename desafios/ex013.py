# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Informe o valor do salário do funcionário: '))

novosalario = salario * 1.15

print('O novo salário do funcionário é de R${:.2f}'.format(novosalario))

