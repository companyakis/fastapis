from pydantic import BaseModel

class Task(BaseModel):
    todo_title: str
    todo_description: str

# let's use a list to store data

todos = []
