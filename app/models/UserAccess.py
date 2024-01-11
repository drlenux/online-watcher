from pydantic import BaseModel


class UserAccess(BaseModel):
    login: str
    password: str
