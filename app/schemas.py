from pydantic import BaseMode1
class CreateUser(BaseMode1):
    username: str
    firstname: str
    lastname: str
    age: int
class UpdateUser(BaseMode1):
    firstname: str
    lastname: str
    age: int
class CreateTask(BaseMode1):
    title: str
    content: str
    priority: int
class UpdateTask(BaseMode1):
    title: str
    content: str
    priority: int