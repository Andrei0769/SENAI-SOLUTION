import pytest
from unittest.mock import MagicMock
from models.usuario_models import Usuario
from repositories.usuario_repository import UsuarioRepository

@pytest.fixture
def mock_session():
    return MagicMock()

@pytest.fixture
def usuario_repository(mock_session):
    return UsuarioRepository(mock_session)

def test_salvar_usuario(usuario_repository, mock_session):
    usuario = Usuario(nome="Test User", email="test@example.com", senha="password")
    usuario_repository.salvar_usuario(usuario)
    mock_session.add.assert_called_once_with(usuario)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(usuario)

def test_pesquisar_usuario_por_email(usuario_repository, mock_session):
    usuario = Usuario(nome="Test User", email="test@example.com", senha="password")
    mock_session.query.return_value.filter_by.return_value.first.return_value = usuario

    result = usuario_repository.pesquisar_usuario_por_email("test@example.com")
    
    assert result == usuario
    mock_session.query.assert_called_once_with(Usuario)
    mock_session.query.return_value.filter_by.assert_called_once_with(email="test@example.com")

def test_excluir_usuario(usuario_repository, mock_session):
    usuario = Usuario(nome="Test User", email="test@example.com", senha="password")
    usuario_repository.excluir_usuario(usuario)
    
    mock_session.delete.assert_called_once_with(usuario)
    mock_session.commit.assert_called_once()