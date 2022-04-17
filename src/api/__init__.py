from flask import Blueprint
from flask_restx import Api

from src.api.todo.methods import api as todo_api
from src.api.number.methods import api as number_api

bl = Blueprint("api", __name__)
api = Api(
    version="0.0.1",
    title="API TITLE",
    description="API"
)

api.init_app(bl, doc="/")

api.namespaces.clear()
api.add_namespace(todo_api)
api.add_namespace(number_api)

