from faker import Faker
from re import U
from src.db_ops import create_database, get_user,get_group, disable_user, query_users, turn_enabled_user, delete_user, add_email_to_user, crear_grupo
from src.models import Base, Usuario
from src.db import engine, Session

fake = Faker(["es_ES", "en_US"])
def main():
    create_database()

    #add_email_to_user(username="ckent", email="ckent@umag.cl")

    # grupo_admins =get_group(name="admins")
    # print(grupo_admins)

    # with Session() as session:
    #     usuario = get_user(username="kkuch", session=session)
    #     if usuario is not None:
    #         print(usuario.emails)

    #         usuario.grupos = [grupo_admins]
    #         session.commit()
    #         print(usuario.grupos)

    with Session() as session:
        for _ in range(20):
            usuario = Usuario(nombre_usuario = fake.user_name(), nombre=fake.name())
            session.add(usuario)
        session.commit()


    

    
    #ckent_emails = get_user_emails(username="ckent")
    #print(ckent_emails)
    #print(usuario)
    #disable_user(usernames=["airlopez"])
    #turn_enabled_user(usernames=["arilopez", "dialvarezs"], enabled=True)

    #delete_user(usernames="dialvarezs")

    #users = query_users()    

    #for user in users:
        #print(f"nombre_usuario={user.nombre_usuario}, habilitado={user.habilitado}")

if __name__ == "__main__":
    main()