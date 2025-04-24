from typing import Sequence
from litestar import Controller, get, post, patch, delete
from litestar.exceptions import HTTPException
from advanced_alchemy.exceptions import NotFoundError
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from advanced_alchemy.filters import ComparisonFilter
from sqlalchemy.orm import Session
from app.dtos import TodoItemReadDTO, TodoItemCreateDTO, TodoItemUpdateDTO
from litestar.dto import DTOData
from litestar.di import Provide

from app.repositories import provide_todoitem_repo, TodoItemRepository
from app.models import TodoItem

# @dataclass
# class TodoItem:
#     id: int
#     title: str
#     done: bool

# @dataclass
# class TodoItemUpdate:
#     title: str | None = None
#     done: bool | None = None



# TODO_LIST: list[TodoItem] = [
#     TodoItem(id = 1, title= "Aprender python", done = True),
#     TodoItem(id = 2,title= "Aprender SQLAlchemy", done = True),
#     TodoItem(id = 3,title= "Aprender Litestar", done = False),
# ]

class TodoController(Controller):
    path = "/items"
    return_dto=TodoItemReadDTO
    dependencies = {
        "todoitem_repo": Provide(provide_todoitem_repo)
    }
    
    @get("/")
    async def list_items(self, todoitems_repo: TodoItemRepository, done: bool | None = None) -> Sequence[TodoItem]:
        return todoitems_repo.list(ComparisonFilter("done", "eq". done))

    @post("/", dto=TodoItemCreateDTO)
    async def add_todo(self, data: TodoItem, db_session:Session) -> Sequence[TodoItem]:
        with db_session.begin():
            db_session.add(data)
        return db_session.execute(select(TodoItem)).scalars().all()
    
    @get("/{item_id:int}")
    async def get_item(self, item_id: int, todo_item_repo: TodoItemRepository) -> TodoItem:
        try:
            return todo_item_repo.get(item_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"Item con id ={item_id} no existe")
        
    @patch("/{item_id:int}", dto=TodoItemUpdateDTO)
    async def update_item(self, item_id: int, data: DTOData[TodoItem], db_session: Session) -> TodoItem:
        data_dict = data.as_builtins()
        item = db_session.execute(select(TodoItem).where(TodoItem.id == item_id)).scalar_one()
        for field in ("title", "done"):
            if field in data_dict is not None:
                setattr(item, field, data_dict[field])
        db_session.commit()
        
        return item
    
    @delete("/{item_id:int}")
    async def delete_item(
        self, item_id: int, todoitem_repo: TodoItemRepository
    ) -> None: todoitem_repo.delete(item_id)
        
        
@get("/") 
async def hello_world() -> str:
    return "Hello, world!"
