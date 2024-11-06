import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.usuario_models import Usuario, Base
from repositories.usuario_repository import UsuarioRepository

# Configuração do banco de dados em memória para testes
@pytest.fixture(scope="module")
def setup_db():
    engine = create_engine('sqlite:///:memory:')  # Banco de dados em memória
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session  # Retorna a sessão para os testes
    
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def usuario_repository(setup_db):
    return UsuarioRepository(session=setup_db)

# Teste para salvar usuário
def test_salvar_usuario(usuario_repository):
    usuario = Usuario(nome="João", email="joao@example.com", senha="senha123")
    usuario_repository.salvar_usuario(usuario)
    
    # Verificar se o usuário foi salvo corretamente
    usuario_salvo = usuario_repository.pesquisar_usuario_por_email("joao@example.com")
    assert usuario_salvo is not None
    assert usuario_salvo.nome == "João"
    assert usuario_salvo.email == "joao@example.com"

# Teste para listar todos os usuários
def test_listar_todos_usuarios(usuario_repository):
    usuario = Usuario(nome="Maria", email="maria@example.com", senha="senha123")
    usuario_repository.salvar_usuario(usuario)
    
    usuarios = usuario_repository.listar_todos_usuarios()
    assert len(usuarios) > 0
    assert usuarios[0].nome == "Maria"

# Teste para excluir usuário
def test_excluir_usuario(usuario_repository):
    usuario = Usuario(nome="Pedro", email="pedro@example.com", senha="senha123")
    usuario_repository.salvar_usuario(usuario)
    
    # Excluir o usuário
    usuario_repository.excluir_usuario(usuario)
    usuario_excluido = usuario_repository.pesquisar_usuario_por_email("pedro@example.com")
    
    assert usuario_excluido is None
