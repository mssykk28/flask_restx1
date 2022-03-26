from src.model.todo import Todo


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        self.status = "active"

    def response(self):
        data = {
            "todo_id": self.todo_id,
            "task": self.task,
            "status": self.status,
        }
        return Todo(**data)
