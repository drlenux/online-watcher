from fastapi import FastAPI, Response, Cookie
from typing import Optional
from uuid import uuid4

from app.get_user_access import get_user_access
from app.models.PingResponse import PingResponse
from app.models.UsersList import UsersList
from fastapi.security import HTTPBasic
from fastapi import Depends, HTTPException
from starlette import status
from fastapi.security import HTTPBasicCredentials
import secrets
from typing import Annotated

security = HTTPBasic()


def include_router(app: FastAPI, config, users: UsersList):

    def validate_credentials(
            credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    ) -> bool:
        for user in get_user_access(config):
            is_correct_username = secrets.compare_digest(
                credentials.username.encode("utf8"), user.login.encode("utf8")
            )
            is_correct_password = secrets.compare_digest(
                credentials.password.encode("utf8"), user.password.encode("utf8")
            )

            if is_correct_username and is_correct_password:
                return True

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Basic"},
        )

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

    @app.get("/count/user")
    async def count(isAllow: Annotated[bool, Depends(validate_credentials)]) -> int:
        if isAllow:
            return users.count()

    @app.get('/count/hits')
    async def countHits(isAllow: Annotated[bool, Depends(validate_credentials)]) -> int:
        if isAllow:
            return users.count_hits()