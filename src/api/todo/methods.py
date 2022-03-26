from flask_restx import Resource, Namespace

from src.api.todo.model import TodoModel
from src.dao.todo import TodoDao

api = Namespace("todo", description="TODO")

_model = TodoModel(api)


@api.route("")
class Todo(Resource):
    @api.marshal_with(_model.response_model())
    def get(self):
        return TodoDao(todo_id="my_todo", task="Remember the milk")
