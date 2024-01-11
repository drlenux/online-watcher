from typing import List

from app.models.UserAccess import UserAccess


def get_user_access(config) -> List[UserAccess]:
    res = []
    for usr in config["server"]["access"]:
        res.append(UserAccess(login=usr["login"], password=usr["password"]))

    return res
