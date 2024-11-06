from models.usuario_models import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session):
        self.session = session

    def listar_todos_usuarios(self):
        return self.session.query(Usuario).all()

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
    
    def pesquisar_usuario_por_email(self, email: str):
        return self.session.query(Usuario).filter_by(email=email).first()
    
    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()  # Remova a linha `self.session.refresh()`

    def listar_usuario(self):
        return self.session.query(Usuario).all()