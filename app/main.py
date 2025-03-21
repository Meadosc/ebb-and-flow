import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .model_ai.model import AIModel
from .model_db.model import DBModel
from .model_gutenberg.model import GutenbergModel


if os.getenv("ENVIRONMENT") == "production":
    origins = ["https://pale-november-dew.fly.dev"]
else:
    origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/read/{item_id}")
def read_item(item_id: int):

    # check the cache first, and if it's empty, fetch the data from gutenberg
    data = DBModel.get_book(item_id)
    if not data:
        data = GutenbergModel.get_book(item_id)
        DBModel.add_book(data)

    response = {
        "status": 200,
        "data": data,
    }
    return response


class SummaryRequest(BaseModel):
    book_title: str

@app.post("/api/summary")
def get_summary(request: SummaryRequest):
    ai_response = AIModel.get_summary(request.book_title)
    response = {
        "status": 200,
        "data": ai_response,
    }
    
    return response


@app.get("/api/get_book_list")
def get_book_list():
    db_response = DBModel.get_book_list()
    response = {
        "status": 200,
        "data": db_response,
    }
    
    return response
