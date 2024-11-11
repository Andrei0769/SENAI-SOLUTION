import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.usuario_models import Usuario, Base

@pytest.fixture
def session():
    # Configura o banco de dados em memória
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Cria as tabelas no banco de dados de teste
    Base.metadata.create_all(engine)

    yield session  # Retorna a sessão para uso nos testes

    # Teardown: encerra a sessão e descarta o banco de dados em memória
    session.close()
    engine.dispose()

def test_usuario_nome_vazio(session):
    with pytest.raises(ValueError):
        usuario = Usuario(nome="", email="email@exemplo.com", senha="senha123")
        session.add(usuario)
        session.commit()

def test_usuario_email_invalido(session):
    with pytest.raises(ValueError):
        usuario = Usuario(nome="João", email="emailsemarroba.com", senha="senha123")
        session.add(usuario)
        session.commit()
