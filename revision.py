velocidadeMaxima = int(input("Qual a velocidade máxima permitida da via: "))
velocidadeDoVeiculo = int(input('Qual a velocidade do veículo: '))
multa = 200

if velocidadeDoVeiculo >= velocidadeMaxima:
    print("Cuidado, está acima da velocidade permitida!")
    print(f"o valor da sua multa é de: R$ {multa:.2f}")
else:
    print("Velocidade permitida!")
