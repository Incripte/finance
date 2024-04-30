from pydantic import BaseModel


class Users(BaseModel):
    name: str
    birth: str
    email: str
    password: str
