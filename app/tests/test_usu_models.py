import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.usuario_models import Usuario, Base

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

# Teste para a criação de um novo usuário
def test_criar_usuario(setup_db):
    usuario = Usuario(nome="Carlos", email="carlos@example.com", senha="senha123")
    setup_db.add(usuario)
    setup_db.commit()
    
    # Verificar se o usuário foi inserido corretamente no banco de dados
    usuario_salvo = setup_db.query(Usuario).filter_by(email="carlos@example.com").first()
    
    assert usuario_salvo is not None
    assert usuario_salvo.nome == "Carlos"
    assert usuario_salvo.email == "carlos@example.com"
    assert usuario_salvo.senha == "senha123"

# Teste para validar que o campo `id` é gerado automaticamente
def test_id_automatico(setup_db):
    usuario = Usuario(nome="Julia", email="julia@example.com", senha="senha123")
    setup_db.add(usuario)
    setup_db.commit()
    
    # Verificar se o id foi gerado automaticamente
    usuario_salvo = setup_db.query(Usuario).filter_by(email="julia@example.com").first()
    
    assert usuario_salvo.id is not None  # O id deve ser gerado automaticamente
    assert isinstance(usuario_salvo.id, int)  # O id deve ser um inteiro

# Teste para verificar se o campo `email` é único (não permite duplicados)
def test_email_unico(setup_db):
    usuario1 = Usuario(nome="Lucas", email="lucas@example.com", senha="senha123")
    usuario2 = Usuario(nome="Rafael", email="lucas@example.com", senha="senha456")
    
    setup_db.add(usuario1)
    setup_db.commit()

    # Tentar adicionar um usuário com email duplicado
    with pytest.raises(Exception):  # Espera-se uma exceção ao tentar salvar o segundo usuário
        setup_db.add(usuario2)
        setup_db.commit()

# Teste para garantir que o nome não é vazio
def test_nome_nao_vazio(setup_db):
    usuario = Usuario(nome="", email="sem_nome@example.com", senha="senha123")
    
    # Tentar adicionar um usuário com nome vazio
    with pytest.raises(Exception):  # Espera-se uma exceção ao tentar salvar
        setup_db.add(usuario)
        setup_db.commit()
