from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel

class MovieResponse(BaseModel):
    name: str   
    description: str | None
    release_date: datetime


class MovieRead(BaseModel):
    id: UUID
    name: str   
    description: str | None
    release_date: datetime