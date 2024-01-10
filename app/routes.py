from fastapi import FastAPI, Response, Cookie
from typing import Optional
from uuid import uuid4
from models.PingResponse import PingResponse
from models.UsersList import UsersList

users = UsersList(save_time=5)
users.start_cleanup()


def include_router(app: FastAPI, config):
    @app.get("/")
    async def root():
        return "Hola"

    @app.get("/ping")
    async def ping(res: Response, token: Optional[str] = Cookie(default=None)) -> PingResponse:
        if not token:
            token = str(uuid4())
            res.set_cookie(key='token', value=token)

        users.add(token)

        return PingResponse(status=200, token=token)

    @app.get("/count/{password}")
    async def count(password: str) -> int:
        if password != config['server']['passwd']:
            return -1

        return users.count()
