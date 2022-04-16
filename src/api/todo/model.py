from flask_restx import fields


class TodoModel:
    def __init__(self, api):
        self.api = api

    todo_id = fields.String(title="todo_id", example="job todo")
    task = fields.String(title="task", example="mail")
    status = fields.String(title="status", example="inactive")

    def response_model(self):
        return self.api.model(
            "todoResponseModel",
            model={
                self.todo_id.title: self.todo_id,
                self.task.title: self.task,
                self.status.title: self.status,
            }
        )

    def request_model(self):
        return self.api.model(
            "todoRequestModel",
            model={
                self.todo_id.title: self.todo_id,
                self.task.title: self.task,
            }
        )
