# EXEMPLO 1

idade = 18
tem_carteira = True

if idade >= 18 and tem_carteira:
    print('Pode dirigir')
else:
    print('Não pode dirigir')

# EXEMPLO 2

nota = 5
frequencia = 75

if nota >= 6 and frequencia >= 75:
    print('Passou')
elif nota >= 5 and frequencia >= 75:
    print('Recuperação')
else:
    print('Reprovado')

# EXEMPLO 3

tem_cafe = False

if not tem_cafe:
    print("Precisamos fazer mais café!")
else:
    print("Já temos café suficiente.")

# EXEMPLO 4

numero = int(input("Digite um número: "))

if numero > 0 or numero % 2 == 0:
    print("O número é positivo ou par")
else:
    print("O número não é positivo nem par")