# Recebe o nome e o número do usuário
name = input("Escreva seu nome: ")
number = int(input("Digite um número: "))  # Converte a entrada do número para inteiro

# Loop que percorre cada letra do nome
for letter in name:
    # Loop que mostra os números de 1 até o número escolhido
    for n in range(1, number + 1):  
        # Imprime o nome e o número
        print(f'Seu nome é {name} e os números escolhidos foram {n}')