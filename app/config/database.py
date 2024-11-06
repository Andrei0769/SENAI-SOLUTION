from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

## ENDEREÇO/CAMINHO PARA CONEXÃO COM BD MySQL
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

## CONECTANDO AO BANCO DE DADOS.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

## GERENCIANDO SESSÃO.
@contextmanager
def get_db():
    db = Session()
    try: 
        yield db
        db.commit() ## SE DER CERTO, FAZ COMMIT
    except Exception as erro: 
        db.rollback() ## SE DER ERRADO, DEFAZ A OPERAÇÃO
        raise erro ## LANÇA A EXCEÇÃO, INFORMANDO O ERRO
    finally:
        db.close() ## GARANTE O FECHAMENTO DE SESSÃO 