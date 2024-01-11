from pydantic import BaseModel


class User(BaseModel):
    id: str
    last_visit: int
    hit: int
