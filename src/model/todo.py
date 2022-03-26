from typing import Optional

from pydantic import BaseModel


class Todo(BaseModel):
    todo_id: str
    task: str
    status: Optional[str] = None
