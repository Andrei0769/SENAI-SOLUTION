from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        os.system("cls || clear")
        # Exibindo o menu
        print("\n=== SENAI SOLUTION ===")
        print("1 - Adicionar usuário")
        print("2 - Pesquisar um usuário")
        print("3 - Atualizar dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Exibir todos os usuários cadastrados")
        print("0 - Sair")
        
        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            # Adicionar usuário
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o e-mail do usuário: ")
            senha = input("Digite a senha do usuário: ")
            service.criar_usuario(nome=nome, email=email, senha=senha)

        elif opcao == "2":
            # Pesquisar um usuário
            email = input("Digite o e-mail do usuário para pesquisa: ")
            usuario = service.repository.pesquisar_usuario_por_email(email)
            if usuario:
                print(f"Usuário encontrado: Nome: {usuario.nome}, Email: {usuario.email}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "3":
            # Atualizar dados de um usuário
            email = input("Digite o e-mail do usuário para atualizar: ")
            usuario = service.repository.pesquisar_usuario_por_email(email)
            if usuario:
                novo_nome = input("Digite o novo nome do usuário: ")
                nova_senha = input("Digite a nova senha do usuário: ")
                usuario.nome = novo_nome
                usuario.senha = nova_senha
                service.repository.salvar_usuario(usuario)
                print("Dados do usuário atualizados com sucesso!")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            # Excluir um usuário
            email = input("Digite o e-mail do usuário para excluir: ")
            usuario = service.repository.pesquisar_usuario_por_email(email)
            if usuario:
                service.repository.excluir_usuario(usuario)
                print("Usuário excluído com sucesso!")
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":
            # Exibir todos os usuários cadastrados
            usuarios = service.repository.listar_todos_usuarios()
            if usuarios:
                print("\n--- Lista de Usuários Cadastrados ---")
                for usuario in usuarios:
                    print(f"Nome: {usuario.nome}, Email: {usuario.email}")
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "0":
            print("Saindo do programa... Obrigado por usar o Sistema SENAI SOLUTION")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
