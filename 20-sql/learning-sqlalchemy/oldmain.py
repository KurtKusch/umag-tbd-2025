from sqlalchemy import create_engine, not_, text, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from typing import Optional
from datetime import datetime


engine = create_engine("postgresql+psycopg:///test_db_2025", echo=False)
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_usuario: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    nombre: Mapped[str]
    apodo: Mapped[Optional[str]]
    ultimo_login: Mapped[Optional[datetime]]
    creado_en: Mapped[datetime] = mapped_column(default=datetime.now)
    habilitado: Mapped[bool] = mapped_column(default=True, server_default="1")

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, nombre_usuario='{self.nombre_usuario}')"

def main(): 
    #Base.metadata.create_all(engine)
    #add_users()
    #query_users()
    usuario = get_user(nombre_usuario="kkuch")
    print(usuario)

def query_users():
    with Session() as session:
        stmt = (
            select(Usuario)
            .where(Usuario.apodo.is_(None))
            .order_by(Usuario.nombre_usuario.desc())
            )
        results = session.execute(stmt).scalars()

        for row in results:
            print(row)

def get_user(nombre_usuario: str) -> Usuario | None:
    stmt = select(Usuario).where(Usuario.nombre_usuario == nombre_usuario)

    with Session() as session:
        return session.execute(stmt).scalar_one_or_none()



def add_users():
    u1 = Usuario(nombre_usuario="kkuch", nombre="Kurt Kusch")
    u2 = Usuario(nombre_usuario="ckent", nombre="Clark Kent", apodo="Superman")
    u3 = Usuario(nombre_usuario="jdoe", nombre="Jane Doe")

    with Session() as session:
        session.add_all([u1, u2, u3])
        print(u1.id)
        session.commit()
        print(u1.id)
    

if __name__ == "__main__":
    main()