from pydantic import BaseModel
from enum import Enum


class Relation(Enum):
    FATHER = "father"
    MOTHER = "mother"


class Parents(BaseModel):
    full_name: str | None
    relation: Relation | None = Relation.MOTHER


class UserModel(BaseModel):
    name: str
    username: str
    password: str
    # skills: set[str] = set()  # it will just give us a unique item
    reference: Parents
