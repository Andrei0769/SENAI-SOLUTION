import sys
sys.path.append('/caminho/para/a/pasta/services')
from models.usuario_models import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository
    
    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            novo_usuario = self.pesquisar_usuario_por_email(usuario.email)  # Alteração aqui
    
            if novo_usuario:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
    
    def listar_todos_usuarios(self):
        return self.repository.listar_usuario()

    def pesquisar_usuario_por_email(self, email: str):
        # Importação do próprio módulo dentro da função para evitar a importação circular
        from services.usuario_service import UsuarioService
        return self.repository.pesquisar_usuario_por_email(email)

    def atualizar_usuario(self, usuario: Usuario, novo_nome: str, nova_senha: str):
        usuario.nome = novo_nome
        usuario.senha = nova_senha
        self.repository.salvar_usuario(usuario)
        print("Dados do usuário atualizados com sucesso!")

    def excluir_usuario(self, usuario: Usuario):
        self.repository.excluir_usuario(usuario)
        print("Usuário excluído com sucesso!")
