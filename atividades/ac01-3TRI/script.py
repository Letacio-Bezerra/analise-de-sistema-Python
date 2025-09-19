# Lista de usuários e senhas pré-cadastrados
usuarios_cadastrados = {
    "usuario1": "senha123",
    "usuario2": "senha456",
    "usuario3": "senha789"
}


# Função para tentar fazer login
def login():
    tentativas = 0
    while tentativas < 3:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        # Verifica se o usuário existe
        if usuario in usuarios_cadastrados:
            if usuarios_cadastrados[usuario] == senha:
                print("Login realizado com sucesso!")
                return usuario  # Retorna o nome de usuário logado
            else:
                print("Senha inválida.")
        else:
            print("Usuário não encontrado.")

        tentativas += 1
        print(f"Tentativa {tentativas}/3\n")

    print("Número máximo de tentativas excedido. Acesso bloqueado.")
    return None  # Retorna None caso o login falhe


# Função para mostrar o menu após o login bem-sucedido
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
            criar_usuario()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Função para criar um novo usuário
def criar_usuario():
    novo_usuario = input("Digite o nome do novo usuário: ")
    if novo_usuario in usuarios_cadastrados:
        print("Usuário já existe.")
    else:
        nova_senha = input("Digite a senha do novo usuário: ")
        usuarios_cadastrados[novo_usuario] = nova_senha
        print("Usuário criado com sucesso!")


# Função principal que controla o fluxo do programa
def main():
    usuario_logado = login()
    if usuario_logado:
        menu(usuario_logado)


# Executa o programa
if __name__ == "__main__":
    main()
