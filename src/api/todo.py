from flask_restx import Resource, Namespace, fields

from src.dao.todo import TodoDao

api = Namespace("todo", description="TODOサンプル")

model = api.model('Model', {
    'task': fields.String,
    'uri': fields.Url('todo_ep')
})


@api.route("")
class Todo(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')
