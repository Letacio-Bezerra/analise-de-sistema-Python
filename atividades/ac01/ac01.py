gastos = float(input('Qual seus gastos:'))
ganhos = float(input('Qual seus ganhos:'))

saldo = ganhos - gastos
saldoNegativo = gastos - ganhos

if ganhos == gastos:
    print('Você está não está no vermelho, mas não pode gastar com mais nada. Pois você tem: R$' + str(saldo))
elif ganhos > gastos:
        print('Você está positivo, pode gastar até: R$' + str(saldo))
elif ganhos < gastos:
        print('Você está no negativo, você deve conseguir pelo menos R$' + str(saldoNegativo) + ' para sair do vermelho')

while ganhos < gastos:
    print('Seu saldo está negativo adicione mais dinheiro na sua conta')
    ganhosExtras = float(input('Adicionar:'))

    if ganhosExtras > 0:
        ganhos += ganhosExtras
        print('Você saiu do vermelho, seu saldo atual é: R$' + str(ganhos - gastos))
    else:
        print('Você não pode tirar mais dinheiro da sua conta')

while ganhos > gastos:
    print('Seu saldo está positivo, gostaria de adicionar mais dinheiro?')
    respostaGanhos = input('Sim ou Não?').upper()

    if respostaGanhos == 'SIM':
        adicionar = float(input('Adicionar:'))
        if adicionar > 0:
            ganhos += adicionar
            print('Você adicionou dinheiro na sua conta, seu saldo atual é: R$' + str(ganhos))
        else:
            print('Você tirou dinheiro da sua conta, seu saldo atual é: R$' + str(ganhos - adicionar))
    else:
        print('Ok')