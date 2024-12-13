from sqlmodel import SQLModel, Session, create_engine

import backend.database.models

# Creating sqlite engine in SQLModel
sqlite_file_name = "backend/database/movie_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Engine
engine = create_engine(sqlite_url, echo=True)

# Conditionally create the table
SQLModel.metadata.create_all(bind=engine)

# Session object
def get_session():
    with Session(bind=engine) as session:
        yield session