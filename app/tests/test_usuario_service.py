import pytest
from unittest.mock import MagicMock
from services.usuario_service import UsuarioService
from models.usuario_models import Usuario

@pytest.fixture
def mock_repository():
    return MagicMock()

@pytest.fixture
def usuario_service(mock_repository):
    return UsuarioService(repository=mock_repository)

def test_criar_usuario_usuario_existente(usuario_service, mock_repository):
    mock_repository.pesquisar_usuario_por_email.return_value = Usuario(nome="Test User", email="test@example.com", senha="password")
    
    usuario_service.criar_usuario("Test User", "test@example.com", "password")
    
    mock_repository.pesquisar_usuario_por_email.assert_called_once_with("test@example.com")
    mock_repository.salvar_usuario.assert_not_called()  # Não deve salvar se o usuário já existe

def test_criar_usuario_novo(usuario_service, mock_repository):
    mock_repository.pesquisar_usuario_por_email.return_value = None
    
    usuario_service.criar_usuario("Test User", "test@example.com", "password")
    
    mock_repository.pesquisar_usuario_por_email.assert_called_once_with("test@example.com")
    mock_repository.salvar_usuario.assert_called_once()  # Deve salvar se o usuário não existe

def test_atualizar_usuario(usuario_service, mock_repository):
    usuario = Usuario(nome="Test User", email="test@example.com", senha="password")
    usuario_service.atualizar_usuario(usuario, "New Name", "new_password")
    
    assert usuario.nome == "New Name"
    assert usuario.senha == "new_password"
    mock_repository.salvar_usuario.assert_called_once_with(usuario)

def test_excluir_usuario(usuario_service, mock_repository):
    usuario = Usuario(nome="Test User", email="test@example.com", senha="password")
    usuario_service.excluir_usuario(usuario)
    
    mock_repository.excluir_usuario.assert_called_once_with(usuario)