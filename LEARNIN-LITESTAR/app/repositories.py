
from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy.orm import Session

from app.models import TodoItem, User

class TodoItemRepository(SQLAlchemySyncRepository[TodoItem]):
    model_type = TodoItem
    
async def provide_todoitem_repo(db_session: Session) -> TodoItemRepository:
    return TodoItemRepository(session=db_session)

class UserRepository(SQLAlchemySyncRepository[User]):
    model_type = User
    
async def provide_users_repo(db_session: Session) -> UserRepository:
    return UserRepository(session=db_session)