from flask import Blueprint
from flask_restx import Api

from src.api.todo import api as todo_api

bl = Blueprint("api", __name__)
api = Api(
    version="0.0.1",
    title="API TITLE",
    description="API"
)

api.init_app(bl, doc="/")

api.namespaces.clear()
api.add_namespace(todo_api)

