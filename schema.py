from pydantic import BaseModel


class Book(BaseModel):
    title : str
    author_name:str
    isbn: str
    description:str
    genre:str
    