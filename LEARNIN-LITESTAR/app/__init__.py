from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin, SQLAlchemySyncConfig
from app.controllers import TodoController, hello_world, UserController
from app.models import Base

db_config = SQLAlchemySyncConfig(
    connection_string="sqlite:///db.sqlite3",create_all=True, metadata=Base.metadata
)

slqa_plugin = SQLAlchemyPlugin(config = db_config)

app = Litestar(
    route_handlers=[hello_world, TodoController, UserController],plugins = [slqa_plugin],debug=True
)