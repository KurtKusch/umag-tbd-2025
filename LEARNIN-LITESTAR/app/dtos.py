from litestar.plugins.sqlalchemy import SQLAlchemyDTO
from advanced_alchemy.extensions.litestar import SQLAlchemyDTOConfig
from app.models import TodoItem, User

class TodoItemReadDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude=["user_id", "user"])
    
class TodoItemFullReadDTO(SQLAlchemyDTO[TodoItem]):
    pass

class TodoItemCreateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude=["user", "id"])
    
class TodoItemUpdateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude=["id"], partial=True, )
    
class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude=["items"])

class UserReadFullDTO(SQLAlchemyDTO[User]):
    pass