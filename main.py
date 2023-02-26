from fastapi import FastAPI,Depends
import models
from database import engine,Session_local
from schema import Book
from sqlalchemy.orm import Session




app = FastAPI()

models.base.metadata.create_all(engine)

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()





@app.post("/book")
def createBook(request:Book,db:Session=Depends(get_db)):
    new_book = models.BookDetails(author_name=request.author_name,isbn=request.isbn,description=request.description)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get("/books")
def getAllBooks(db: Session = Depends(get_db)):
    books = db.query(models.BookDetails).all()
    return books


@app.get("/book/{id}")
def getBookByID(db:Session=Depends(get_db),id:int = id):
    book = db.query(models.BookDetails).filter(models.BookDetails.id==id).first()
    return book


@app.get("/book/author/{author_name}")
def getBookByAuthor(author_name:str,db:Session=Depends(get_db)):
    book = db.query(models.BookDetails).filter(models.BookDetails.author_name==author_name).first()
    return book