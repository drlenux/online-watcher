from fastapi import Depends, HTTPException
from starlette import status
from fastapi.security import HTTPBasicCredentials
import secrets
from typing import Annotated

from app.models import UserAccess
from app.get_user_access import get_user_access


