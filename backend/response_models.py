from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel

#TODO Implement later
class MovieResponse(BaseModel):
    pass

class MovieRead(BaseModel):
    id: UUID
    name: str   
    description: str | None
    release_date: datetime