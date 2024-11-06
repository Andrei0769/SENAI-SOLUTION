import pytest
from unittest.mock import MagicMock
from services.usuario_services import UsuarioService
from models.usuario_models import Usuario
from repositories.usuario_repository import UsuarioRepository

@pytest.fixture
def usuario_service():
    mock_repository = MagicMock(UsuarioRepository)
    return UsuarioService(repository=mock_repository)

# Teste para criar usuário
def test_criar_usuario(usuario_service):
    usuario_service.repository.pesquisar_usuario_por_email.return_value = None  # Não encontrado no DB
    usuario_service.criar_usuario("Lucas", "lucas@example.com", "senha123")
    
    # Verificar se o método salvar_usuario foi chamado
    usuario_service.repository.salvar_usuario.assert_called_once()

# Teste para tentar criar um usuário com email já cadastrado
def test_criar_usuario_com_email_existente(usuario_service):
    usuario_service.repository.pesquisar_usuario_por_email.return_value = Usuario(nome="Lucas", email="lucas@example.com", senha="senha123")
    
    usuario_service.criar_usuario("Lucas", "lucas@example.com", "nova_senha")
    
    # Verificar se a mensagem de erro foi impressa corretamente
    usuario_service.repository.salvar_usuario.assert_not_called()

# Teste para listar todos os usuários
def test_listar_todos_usuarios(usuario_service):
    usuario_service.repository.listar_usuario.return_value = [Usuario(nome="Lucas", email="lucas@example.com", senha="senha123")]
    
    usuarios = usuario_service.listar_todos_usuarios()
    assert len(usuarios) > 0
    assert usuarios[0].nome == "Lucas"

# Teste para excluir um usuário
def test_excluir_usuario(usuario_service):
    usuario = Usuario(nome="Ana", email="ana@example.com", senha="senha123")
    usuario_service.repository.pesquisar_usuario_por_email.return_value = usuario
    
    usuario_service.excluir_usuario(usuario)
    
    # Verificar se o método excluir_usuario foi chamado
    usuario_service.repository.excluir_usuario.assert_called_once()
