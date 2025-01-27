palavra = 'FANTASTICO'

for espaco in palavra:
    print(espaco, end='  ')

# OU PODE FAZER DESSA FORMA:

palavra =  input("Escreva uma palavra: ")

for espaco in palavra:
    print(f'{espaco}', end=' ')
