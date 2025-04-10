from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound
from typing import Sequence

from src.db import Session, engine
from src.models import Base, Usuario, Email, Grupo

def query_users():
    with Session() as session:
        #stmt = select(Usuario).where(Usuario.apodo.is_(None)).order_by(Usuario.nombre_usuario) # Statement = stmt
        stmt = select(Usuario) # Statement = stmt
        stmt.order_by(Usuario.nombre_usuario.desc()) # Statement = stmt

        results = session.execute(stmt).scalars().fetchall()
        
        return results



def crear_grupo(name: str) -> Grupo:
    with Session() as session:
        with session.begin():
            grupo = Grupo(nombre=name)
            session.add(grupo)

        return grupo
    
def get_group(name: str) -> Grupo:
    with Session() as session:
        grupo = session.execute(
            select(Grupo).where(Grupo.nombre == name)
        ).scalar_one()

        return grupo

def get_user(username: str, session) -> Usuario | None: 
    stmt = (select(Usuario)
            #.options(selectinload(Usuario.emails))
            .where(Usuario.nombre_usuario == username))

    user = session.execute(stmt).scalar_one_or_none()
    return user

def add_users():
    u1 = Usuario(nombre_usuario="arilopez",nombre="ariel lopez")
    u2 = Usuario(nombre_usuario="ckent",nombre="clark kent", apodo="Superman")
    u3 = Usuario(nombre_usuario="dialvarezs",nombre="Diego Alvarez S.", apodo="El Prime")

    with Session() as session:
        session.add_all([u1, u2, u3])

        print(u1.id)
        session.commit()
        print(u1.id)

def disable_user(username: str) -> None:
    
    with Session() as session:
        with session.begin():
            stmt = (
                update(Usuario)
                .where(Usuario.nombre_usuario.in_(username))
                .values(habilitado=False)
            )
            session.execute(stmt)

def turn_enabled_user(username: str, enabled: bool) -> None:
    
    with Session() as session:
        with session.begin():
            stmt = (
                update(Usuario)
                .where(Usuario.nombre_usuario.in_(username))
                .values(habilitado=enabled)
            )
            session.execute(stmt)

def delete_user(username: str) -> None:
    with Session() as session:
        with session.begin():
            user= session.execute(
                select(Usuario).where(Usuario.nombre_usuario == username)
            ).scalar_one()
            session.delete(user)
            session.commit()

def add_email_to_user(username: int, email: str) -> None:
    with Session() as session:
        with session.begin():
            user = session.execute(
                select(Usuario).where(Usuario.nombre_usuario == username)
            ).scalar_one()
            user.emails.append(Email(email=email))

def create_database():
    Base.metadata.create_all(engine)

