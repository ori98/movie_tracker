from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel
from datetime import datetime

class Movie(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)   
    description: str | None
    release_date: datetime = Field(index=True)