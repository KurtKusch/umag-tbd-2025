from enum import auto
from typing import Sequence
from litestar import Controller, get, post, patch, delete
from litestar.exceptions import HTTPException
from advanced_alchemy.exceptions import NotFoundError
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from advanced_alchemy.filters import ComparisonFilter
from sqlalchemy.orm import Session
from app.dtos import TodoItemReadDTO, TodoItemCreateDTO, TodoItemUpdateDTO, UserReadDTO, UserReadFullDTO, TodoItemFullReadDTO
from litestar.dto import DTOData
from litestar.di import Provide
from app.repositories import provide_todoitem_repo, TodoItemRepository, provide_users_repo, UserRepository
from app.models import TodoItem, User

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
    tags = ["Items"]
    return_dto=TodoItemReadDTO
    dependencies = {
        "todoitem_repo": Provide(provide_todoitem_repo)
    }
    
    @get("/")
    async def list_items(self, todoitem_repo: TodoItemRepository, done: bool | None = None) -> Sequence[TodoItem]:
        if done is None:
            return todoitem_repo.list()
        return todoitem_repo.list(ComparisonFilter("done", "eq". done))

    @post("/", dto=TodoItemCreateDTO)
    async def add_todo(self, todoitem_repo:TodoItemRepository, data: TodoItem) -> Sequence[TodoItem]:
        return todoitem_repo.add(data, auto_commit=True)
    
    @get("/{item_id:int}")
    async def get_item(self, todoitem_repo: TodoItemRepository, item_id: int) -> TodoItem:
        try:
            return todoitem_repo.get(item_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"Item con id ={item_id} no existe")
        
    @get("/{item_id:int}/full", return_dto=TodoItemFullReadDTO)
    async def get_item_full(self, todoitem_repo: TodoItemRepository, item_id: int) -> TodoItem:
        try:
            return todoitem_repo.get(item_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"Item con id ={item_id} no existe")
        
    @patch("/{item_id:int}", dto=TodoItemUpdateDTO)
    async def update_item(self, todoitem_repo: TodoItemRepository, item_id: int, data: DTOData[TodoItem]) -> TodoItem:
        item, _ = todoitem_repo.get_and_update(
            match_fields= "id", 
            id=item_id, 
            **data.as_builtins(),
            auto_commit=True
        )
        
        return item
    
    @delete("/{item_id:int}")
    async def delete_item(
        self, item_id: int, todoitem_repo: TodoItemRepository) -> None:
        todoitem_repo.delete(item_id, auto_commit=True)
        
        
class UserController(Controller):
    path = "/users"
    tags = ["Users"]
    dependencies = {
        "users_repo": Provide(provide_users_repo)
    }
    return_dto = UserReadDTO
    
    @get("/")
    async def list_users(self, users_repo: UserRepository) -> Sequence[User]:
        return users_repo.list()
    
    @get ("/{user_id:int}")
    async def get_user(self, users_repo: UserRepository, user_id: int) -> User:
        try:
            return users_repo.get(user_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"User con id ={user_id} no existe")
        
    @get ("/{user_id:int}/full", return_dto=UserReadFullDTO)
    async def get_user_full(self, users_repo: UserRepository, user_id: int) -> User:
        try:
            return users_repo.get(user_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"User con id ={user_id} no existe")
    
    



@get("/") 
async def hello_world() -> str:
    return "Hello, world!"
