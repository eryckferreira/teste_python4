compraConfirmada = True
dadosDaCompra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compraConfirmada:
        print(dadosDaCompra)
        print('detalhes enviado para seu email')
        break
else:
    print('Falha na compra')
