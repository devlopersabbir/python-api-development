from pydantic import BaseModel, Field


class UserModel1(BaseModel):
    name: str | None


class UserModel2(BaseModel):
    name: str | None = Field(examples=["Sabbir Hossain Shuvo"])


class UserModel3(BaseModel):
    name: str | None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Fucker boy"
                }
            ]
        }
    }
