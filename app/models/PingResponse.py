from pydantic import BaseModel


class PingResponse(BaseModel):
    status: int
    token: str
