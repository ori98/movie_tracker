from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Column, String
from datetime import datetime

class Movie(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(sa_column=Column("name", String, unique=True, index=True))   
    description: str | None
    release_date: datetime = Field(index=True)