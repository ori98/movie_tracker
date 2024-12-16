from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from datetime import datetime

from backend.database.db import get_session
from backend.database.models import Movie
from backend.response_models import MovieResponse

app = FastAPI()

@app.get("/")
def root_msg():
    return {"message": "Hello movie watcher"}

@app.post("/add-movie", response_model=MovieResponse)
def add_question(movie: Movie, session: Session = Depends(get_session)):
    # Since datetime object can't be passed
    if isinstance(movie.release_date, str):
        movie.release_date = datetime.fromisoformat(movie.release_date)

    session.add(movie)
    session.commit()
    session.refresh(movie)

    #TODO Return a can not add message with reason if not able to insert
    return movie

@app.get("/get-movie", response_model=list[MovieResponse])
def get_movies(search_term: str, session: Session = Depends(get_session)):
   statement = select(Movie).where(Movie.name.like(f"%{search_term}%"))
   movies = session.exec(statement=statement).all()

   return movies