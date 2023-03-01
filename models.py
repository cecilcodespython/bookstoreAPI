from sqlalchemy import Column,String,Integer
from database import base

class BookDetails(base):
    __tablename__ = "book_details"
    id = Column(Integer,primary_key=True,index=True)
    author_name = Column(String)
    title=Column(String)
    isbn =Column(String)
    description=Column(String)
    genre=Column(String)