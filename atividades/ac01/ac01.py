gastos = float(input('Qual seus gastos:'))
ganhos = float(input('Qual seus ganhos:'))

saldo = ganhos - gastos
saldoNegativo = gastos - ganhos

if ganhos == gastos:
    print('Você está não está no vermelho, mas não pode gastar com mais nada. Pois você tem: ' + str(saldo) + ' real(reais)')
elif ganhos > gastos:
        print('Você está positivo, pode gastar até: ' + str(saldo) + ' real(reais)')
elif ganhos < gastos:
        print('Você está no negativo, você deve conseguir pelo menos ' + str(saldoNegativo) + ' para sair do vermelho')

while ganhos < gastos:
    print('Seu saldo está negativo adicione mais dinheiro na sua conta')
    ganhosExtras = float(input('Adicionar:'))
    ganhos += ganhosExtras
    print('Você saiu do vermelho, seu saldo atual é:' + str(ganhos - gastos))