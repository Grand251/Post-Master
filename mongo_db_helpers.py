from fastapi.encoders import jsonable_encoder
from typing import Optional, Any
from bson import ObjectId
from enum import Enum, auto

from pydantic import BaseModel, Field


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class MongoDBModelMixin(BaseModel):
    id: Optional[ObjectIdStr] = Field(None, alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: lambda x: str(x)}