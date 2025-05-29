def calcular_saldo(ganhos, gastos):
    return ganhos - gastos

def adicionar_dinheiro(ganhos):
    adicionar = float(input('Adicionar: '))
    if adicionar >= 0:
        ganhos += adicionar
        print('Você adicionou dinheiro na sua conta, seu saldo atual é: R$' + str(calcular_saldo(ganhos, gastos)))
    else:
        print('Valor inválido! Você não pode adicionar valores negativos.')
    return ganhos

def remover_dinheiro(gastos):
    remover = float(input('Remover: '))
    if remover > 0:
        gastos += remover
        print('Você removeu dinheiro da sua conta, seu saldo atual é: R$' + str(calcular_saldo(ganhos, gastos)))
    else:
        print('Valor inválido! Você deve inserir um valor positivo para remover.')
    return gastos

gastos = float(input('Qual seus gastos: '))
ganhos = float(input('Qual seus ganhos: '))

saldo = calcular_saldo(ganhos, gastos)

if ganhos == gastos:
    print('Você não está no vermelho, mas não pode gastar com mais nada. Seu saldo: R$' + str(saldo))
elif ganhos > gastos:
    print('Você está positivo, pode gastar até: R$' + str(saldo))
else:
    print('Você está no negativo, precisa de pelo menos R$' + str(abs(saldo)) + ' para sair do vermelho')

while ganhos < gastos:
    print('Seu saldo está negativo, adicione mais dinheiro.')
    ganhosExtras = float(input('Adicionar: '))

    if ganhosExtras > 0:
        ganhos += ganhosExtras
        print('Você saiu do vermelho, seu saldo atual é: R$' + str(calcular_saldo(ganhos, gastos)))
    else:
        print('Você não pode tirar mais dinheiro da sua conta')

while True:
    print('Gostaria de adicionar mais dinheiro?')
    respostaGanhos = input('Sim ou Não? ').upper()

    if respostaGanhos == 'SIM':
        ganhos = adicionar_dinheiro(ganhos)
    elif respostaGanhos == 'NÃO':
        print('Gostaria de remover dinheiro da sua conta?')
        respostaGastos = input('Sim ou Não? ').upper()

        if respostaGastos == 'SIM':
            gastos = remover_dinheiro(gastos)
        elif respostaGastos == 'NÃO':
            print('TOP! d(✪ ω ✪)b')
            print('        d b')
            break
