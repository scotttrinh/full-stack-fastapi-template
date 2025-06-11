from pydantic import BaseModel

from app.models.data.default import User
from app.models.data.ext import auth as ext_auth


class UserCreate(BaseModel):
    email: str
    full_name: str
    identity: ext_auth.Identity
