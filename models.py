from fastapi.encoders import jsonable_encoder
from typing import Optional, Any
from bson import ObjectId
from enum import Enum, auto

from pydantic import BaseModel, Field

from mongo_db_helpers import ObjectIdStr, MongoDBModelMixin


class GenderEnum(str, Enum):
    boy = 'boy'
    girl = 'girl'


class Letter(MongoDBModelMixin):
    #_id: ObjectIdStr = ObjectId()
    sender: str
    gender: GenderEnum = None
    title: str = 'To Santa'
    body: str
    response: str = None
