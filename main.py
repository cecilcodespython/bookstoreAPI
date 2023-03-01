from fastapi import FastAPI,Depends
import models
from database import engine,Session_local
from schema import Book
from sqlalchemy.orm import Session
from random import randint




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
    new_book = models.BookDetails(author_name=request.author_name,isbn=request.isbn,description=request.description,genre=request.genre,title=request.title)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/book/random")
def getRandomBook(db:Session=Depends(get_db)):
    num_of_books = db.query(models.BookDetails).count()
    random_id = randint(1,num_of_books)
    random_book = db.query(models.BookDetails).filter(models.BookDetails.id == random_id).first()
    return random_book

   


@app.get("/books")
def getAllBooks(db: Session = Depends(get_db)):
    books = db.query(models.BookDetails).all()
    return books


@app.get("/book/{genre}")
def getAllBooksbyGenre(genre:str,db:Session=Depends(get_db)):
    books = db.query(models.BookDetails).filter(models.BookDetails.genre==genre).all()
    return books


@app.get("/book/{id}")
def getBookByID(db:Session=Depends(get_db),id:int = id):
    book = db.query(models.BookDetails).filter(models.BookDetails.id==id).first()
    return book


@app.get("/book/author/{author_name}")
def getBookByAuthor(author_name:str,db:Session=Depends(get_db)):
    book = db.query(models.BookDetails).filter(models.BookDetails.author_name==author_name).all()
    return book

@app.get("/book/isbn/{isbn}")
def getBookByIsbn(isbn:int,db:Session=Depends(get_db)):
    book = db.query(models.BookDetails).filter(models.BookDetails.isbn ==isbn).first()
    return book


@app.get("/book/random")
def getRandomBook(db:Session=Depends(get_db)):
    num_of_books = db.query(models.BookDetails).count()
    random_id = randint(1,num_of_books)
    random_book = db.query(models.BookDetails).filter(models.BookDetails.id == random_id).first()
    return random_book


@app.delete("/book/delete/{book_id}")
def deleteBook(book_id:int,db:Session=Depends(get_db)):
    book = db.query(models.BookDetails).filter(models.BookDetails.id==book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message":"book has beem deleted"}
    else:
        return {"message":"book does not exist"}
    

