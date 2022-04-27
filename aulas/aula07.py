nome = input('Qual é o seu nome? ')

print('Prazer em te conhecer, {}!'.format(nome))

# valor ocupa 10 posições (porém não quebra se tiver mais que isso)
print('Prazer em te conhecer, {:10}!'.format(nome))

# valor ocupa 10 posições e fica alinhado à direta
print('Prazer em te conhecer, {:>10}!'.format(nome))

# valor ocupa 10 posições e fica alinhado à esquerda
print('Prazer em te conhecer, {:<10}!'.format(nome))

# valor ocupa 10 posições e fica alinhado ao meio
print('Prazer em te conhecer, {:<10}!'.format(nome))

# valor ocupa 10 posições, fica alinhado ao meio e preenche vazios com #
print('Prazer em te conhecer, {:#^10}!'.format(nome))


print('_'*50)


numero1 = int(input('primeiro numero = '))
numero2 = int(input('segundo numero = '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
potencia = numero1 ** numero2
divisao = numero1 / numero2
divisaointeira = numero1 // numero2
modulo = numero1 % numero2

print('A soma entre {0} e {1} vale {2}'.format(numero1, numero2, soma))
print('A subtracao entre {0} e {1} vale {2}'.format(numero1, numero2, subtracao))
print('A multiplicacao entre {0} e {1} vale {2}'.format(numero1, numero2, multiplicacao))
print('A potencia entre {0} e {1} vale {2}'.format(numero1, numero2, potencia))
# :.3f define quantas casas após a vírgula
print('A divisao entre {0} e {1} vale {2:.3f}'.format(numero1, numero2, divisao))
print('A divisao inteira entre {0} e {1} vale {2}'.format(numero1, numero2, divisaointeira))
print('O modulo entre {0} e {1} vale {2}'.format(numero1, numero2, modulo))



