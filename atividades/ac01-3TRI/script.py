usuarios_cadastrados = {
    "usuario1": "senha123",
    "usuario2": "senha456",
    "usuario3": "senha789"
}

def login():
    tentativas = 0
    while tentativas < 3:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        if usuario in usuarios_cadastrados:
            if usuarios_cadastrados[usuario] == senha:
                print("Login realizado com sucesso!")
                return usuario
            else:
                print("Senha inválida.")
        else:
            print("Usuário não encontrado.")

        tentativas += 1
        print(f"Tentativa {tentativas}/3")

    print("Número máximo de tentativas excedido. Acesso bloqueado.")
    return None

def menu(usuario_logado):
    while True:
        print("\nMenu de opções:")
        print("1 - Ver Perfil")
        print("2 - Criar usuário")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Nome do usuário logado: {usuario_logado}")
        elif opcao == "2":
            print("Vamos criar seu usuario em algum momento")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

usuario_logado = login()

if usuario_logado:
    menu(usuario_logado)
else:
    print("Não foi possível realizar o login.")