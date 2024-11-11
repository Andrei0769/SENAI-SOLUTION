from sqlalchemy import Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = (UniqueConstraint('email', name='uix_1'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        if "@" not in email:
            raise ValueError("O email precisa conter '@'.")
        
        self.nome = nome
        self.email = email
        self.senha = senha
