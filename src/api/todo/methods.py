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

    @api.expect(_model.request_model())
    @api.marshal_with(_model.response_model())
    def post(self):
        return TodoDao(todo_id=_model.request_model().get("todo_id").title, task=_model.request_model().get("task").title)

