nome = input("Qual o nome do cidadão que irá votar? ")
idade = int(input('Informe a idade da pessoa: '))

if idade >= 16 and titulo:
    resultado = print('O cidadão está permitido para votar')
else:
    resultado = print('O cidadão não está permitido para votar')

print(resultado)
